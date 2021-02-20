import pandas
from sqlalchemy import create_engine
import psycopg2
from sql_config import db_password

#build conn with function
def build_engine(db_password=db_password, database_name="group_project"):
    #create a db_string to connect to the database and conn -- connection variable
    db_string = f"postgres://postgres:{db_password}@127.0.0.1:5432/{database_name}"
    engine = create_engine(db_string)    
    return engine





