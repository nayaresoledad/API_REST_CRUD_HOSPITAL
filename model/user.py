from sqlalchemy import  Table, Column, String, Integer, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Date
from config.db import engine, meta_data

""""Modelos de datos, como voy a guaradar los datos"""

paciente = Table("paciente", meta_data,  #meta sirve para tener mas datos sobre la tabla
    Column("id_paciente", Integer, primary_key=True),
    Column("nombre_paciente", String(40), nullable=True),
    Column("apellidos_paciente", String(40), nullable=True),
    Column("numero_historial_clinico", Integer, nullable=False),
    Column("domicilio", String(50), nullable=True),
    Column("poblacion_provincia", String(40), nullable=True),
    Column("telefono", String(9), nullable=True))
    
doctor = Table("doctor", meta_data,
    Column("id_doctor", Integer, primary_key=True),
    Column("nombre", String(40), nullable=True),
    Column("apellidos", String(40), nullable=True),
    Column("sexo", String(10), nullable=True),
    Column("fecha_nacimiento", Date, nullable=True),
    Column("especialidad", String(40), nullable=True),
    Column("numero_colegiado", Integer, nullable=False),
    Column("cargo", String(30), nullable=True))

codigo_cita = Table("codigo_cita", meta_data,
    Column("id_paciente", Integer, ForeignKey("paciente.id_paciente")),
    Column("id_doctor", Integer, ForeignKey("doctor.id_doctor")),
    Column("fecha", Date, primary_key=True),
    Column("direccion", String(50), nullable=True))

meta_data.create_all(engine) #Para crear la tabla en la base de datos de pgadming