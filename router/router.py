from urllib import response
from fastapi import APIRouter, Response
from schema.paciente_schema import PacienteSchema
from config.db import engine
from model.user import paciente
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from typing import List

user = APIRouter()

@user.get("/")
def root():
    return "Esto es Hospital F5"

@user.get("/pacientes", response_model=List[PacienteSchema])
def get_pacientes():
 with engine.connect() as conn:
    result = conn.execute(paciente.select()).fetchall()
    return result

@user.get("/pacientes/{paciente_id}", response_model=PacienteSchema)
def get_paciente(paciente_id: int):
    with engine.connect() as conn:
        result = conn.execute(paciente.select().where(paciente.c.id_paciente == paciente_id)).first()
        return result    

@user.post("/pacientes", status_code=HTTP_201_CREATED)
def crear_paciente(data_paciente: PacienteSchema):
    with engine.connect() as conn:
        nuevo_paciente = data_paciente.dict()
        conn.execute(paciente.insert().values(nuevo_paciente))
        return Response(status_code=HTTP_201_CREATED)

@user.put("/pacientes/{paciente_id}")
def actualizar_paciente(data_update: PacienteSchema, paciente_id: int):
    with engine.connect() as conn:
        result = conn.execute(paciente.update().where(paciente.c.id_paciente == paciente_id).values(id_paciente=data_update.id_paciente, nombre_paciente=data_update.nombre_paciente, apellidos_paciente=data_update.apellidos_paciente, numero_historial_clinico=data_update.numero_historial_clinico, observaciones=data_update.observaciones))
        result = conn.execute(paciente.select().where(paciente.c.id_paciente == paciente_id)).first()
        return result

@user.delete("/pacientes/{paciente_id}", status_code=HTTP_204_NO_CONTENT)
def borrar_paciente(paciente_id: int):
    with engine.connect() as conn:
        conn.execute(paciente.delete().where(paciente.c.id_paciente == paciente_id))
        return Response(status_code=HTTP_204_NO_CONTENT)