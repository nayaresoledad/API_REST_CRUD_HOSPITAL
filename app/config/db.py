from sqlalchemy import MetaData
import sqlalchemy
from dotenv import dotenv_values

config = dotenv_values('.env')

engine = sqlalchemy.create_engine(config.get('DATABASE_URL'))

meta_data = MetaData()