from sqlalchemy import  Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float
from config.db import engine, meta_data

iris = Table("iris", meta_data,
               Column("id", Integer, primary_key=True),
               Column("sepal_lenght", Float, nullable=False),
               Column("sepal_width", Float, nullable=False),
               Column("petal_length", Float, nullable=False),
               Column("petal_width", Float, nullable=False),
               Column("species", String, nullable=False))

meta_data.create_all(engine)
