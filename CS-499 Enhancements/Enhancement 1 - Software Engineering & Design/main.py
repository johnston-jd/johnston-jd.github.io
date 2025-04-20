#Jaymie Johnston
#CS499 Capstone
#Enhancement 1 - Software Engineering and Design
#Enhancement 1 - FastAPI
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from starlette import status
import auth
import models
from usersdb import engine, Sessionlocal
from sqlalchemy.orm import Session

#FastAPI
app = FastAPI()
app.include_router(auth.router)

models.Base.metadata.create_all(bind=engine)

#userbase class - has username as a string
class UserBase(BaseModel):
    username: str

#get user database
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[Session, Depends(auth.get_current_user)]

#post user
@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.model.dump())
    db.add(db_user)
    db.commit()

#get user
@app.get("/", status_code=status.HTTP_200_OK)
async def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    return {"User": user}