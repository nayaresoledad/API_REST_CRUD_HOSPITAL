from datetime import datetime
from sqlalchemy import  Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Date, DateTime
from config.db import engine, meta_data

paciente = Table("paciente", meta_data,
    Column("id_paciente", Integer, primary_key=True),
    Column("nombre_paciente", String(40), nullable=True),
    Column("apellidos_paciente", String(40), nullable=True),
    Column("numero_historial_clinico", Integer, nullable=False),
    Column("observaciones", String(200), nullable=True))

doctor = Table("doctor", meta_data,
    Column("id_doctor", Integer, primary_key=True),
    Column("nombre", String(40), nullable=True),
    Column("apellidos", String(40), nullable=True),
    Column("sexo", String(10), nullable=True),
    Column("fecha_nacimiento", Date, nullable=True),
    Column("especialidad", String(40), nullable=True),
    Column("numero_colegiado", Integer, nullable=False),
    Column("cargo", String(30), nullable=True))

contacto_paciente = Table("contacto_paciente", meta_data,
    Column("id_paciente", Integer, primary_key=True),
    Column("domicilio", String(50), nullable=True),
    Column("poblacion", String(20), nullable=True),
    Column("provincia", String(20), nullable=True),
    Column("codigo_postal", String(6), nullable=True),
    Column("telefono", String(9), nullable=True))

codigo_cita = Table("codigo_cita", meta_data,
    Column("id_paciente", Integer, nullable=True),
    Column("id_doctor", Integer, nullable=True),
    Column("fecha_hora", DateTime, primary_key=True),
    Column("direccion", String(50), nullable=True))

meta_data.create_all(engine)