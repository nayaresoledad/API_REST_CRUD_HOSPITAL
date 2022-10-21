from sqlalchemy import  Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float
from config.db import engine, meta_data

paciente = Table("paciente", meta_data,
               Column("id_paciente", Integer, primary_key=True),
               Column("nombre_paciente", String, nullable=True),
               Column("apellidos_paciente", String, nullable=True),
               Column("numero_historial_clinico", Integer, nullable=False),
               Column("observaciones", String, nullable=True))

meta_data.create_all(engine)