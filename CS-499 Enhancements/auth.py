#Jaymie Johnston
#Enhancement 1 - Software Engineering & Design
#Authentication with FastAPI & JWT
from datetime import datetime, timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from usersdb import Sessionlocal
from models import User
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError

#Router
router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)
#Secret key and algorithm
SECRET_KEY = "1be3c23dfb31c7cb1b0d8fab54b151a6eb55a1795e7d75001248dbe6a378012d"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

#create user class
class CreateUser(BaseModel):
    username: str
    password: str

#create token class
class Token(BaseModel):
    access_token: str
    token_type: str

#get database
def get_bd():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_bd)]

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUser):
    create_user_model = User(username=create_user_request.username, hashed_password=bcrypt_context.hash(create_user_request.password),
                             )
    db.add(create_user_model)
    db.commit()

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                    db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=401, detail="Could not validate user")
    token = create_access_token(user.username, user.id, timedelta(minutes=60))

    return {"access_token": token, "token_type": "bearer"}

def authenticate_user(username: str, password: str, db):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id}
    expires = datetime.now(datetime.UTC) + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise HTTPException(status_code=401, detail="Could not verify user")
        return {'username': username, 'id': user_id}
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not verify user")

