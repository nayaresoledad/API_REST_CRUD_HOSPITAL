from fastapi import APIRouter, Response
from schema.paciente_schema import PacienteSchema
from config.db import engine
from model.user import iris
from starlette.status import HTTP_201_CREATED
from typing import List

user = APIRouter()

@user.get("/")
def root():
    return "Ey, soy FastApio"

@user.get("/iris/pacientes", response_model=List[PacienteSchema])
def get_pacientes():
 with engine.connect() as conn:
    result = conn.execute(iris.select()).fetchall()
    return result

@user.get("/iris/pacientes/{paciente_id}", response_model=PacienteSchema)
def get_paciente(paciente_id: str):
 with engine.connect() as conn:
    result = conn.execute(iris.select().where(iris.c.id == paciente_id)).first()
    return result    

@user.post("/iris/pacientes", status_code=HTTP_201_CREATED)
def crear_paciente(data_paciente: PacienteSchema):
    with engine.connect() as conn:
     nuevo_paciente = data_paciente.dict()
     conn.execute(iris.insert().values(nuevo_paciente))
     return Response(status_code=HTTP_201_CREATED)

@user.put("/iris/pacientes")
def actualizar_paciente():
    pass


#1:02:40