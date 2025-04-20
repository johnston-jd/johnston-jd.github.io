#Jaymie Johnston
#Enhancement 1 - Software Engineering & Design
#Uses database to store users
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#MySQL database URL - username, password, host, port, and database name
URL_DATABASE = "mysql+pymysql://root:L3w!sZ03Sally:@localhost:3306/usersdatabase"

engine = create_engine(URL_DATABASE)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
