from datetime import date
from urllib import response
from fastapi import APIRouter, Response
from schema.paciente_schema import PacienteSchema
from schema.doctor_schema import DoctorSchema
from schema.contactopaciente_schema import ContactopacienteSchema
from schema.codigocita_schema import CodigocitaSchema
from config.db import engine
from model.user import doctor, paciente, contacto_paciente, codigo_cita
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



@user.get("/doctores", response_model=List[DoctorSchema])
def get_doctores():
 with engine.connect() as conn:
    result = conn.execute(doctor.select()).fetchall()
    return result

@user.get("/doctores/{doctor_id}", response_model=DoctorSchema)
def get_doctor(doctor_id: int):
    with engine.connect() as conn:
        result = conn.execute(doctor.select().where(doctor.c.id_doctor == doctor_id)).first()
        return result    

@user.post("/doctores", status_code=HTTP_201_CREATED)
def crear_doctor(data_doctor: DoctorSchema):
    with engine.connect() as conn:
        nuevo_doctor = data_doctor.dict()
        conn.execute(doctor.insert().values(nuevo_doctor))
        return Response(status_code=HTTP_201_CREATED)

@user.put("/doctores/{doctor_id}")
def actualizar_doctor(data_update: DoctorSchema, doctor_id: int):
    with engine.connect() as conn:
        result = conn.execute(doctor.update().where(doctor.c.id_doctor == doctor_id).values(id_doctor=data_update.id_doctor, nombre=data_update.nombre, apellidos=data_update.apellidos, sexo=data_update.sexo, fecha_nacimiento=data_update.fecha_nacimiento, especialidad=data_update.especialidad, numero_colegiado=data_update.numero_colegiado, cargo=data_update.cargo))
        result = conn.execute(doctor.select().where(doctor.c.id_doctor == doctor_id)).first()
        return result

@user.delete("/doctores/{doctor_id}", status_code=HTTP_204_NO_CONTENT)
def borrar_doctor(doctor_id: int):
    with engine.connect() as conn:
        conn.execute(doctor.delete().where(doctor.c.id_doctor == doctor_id))
        return Response(status_code=HTTP_204_NO_CONTENT)
        
#####

@user.get("/contacto_pacientes", response_model=List[ContactopacienteSchema])
def get_contacto_pacientes():
 with engine.connect() as conn:
    result = conn.execute(contacto_paciente.select()).fetchall()
    return result

@user.get("/contacto_pacientes/{paciente_id}", response_model=ContactopacienteSchema)
def get_contacto_paciente(paciente_id: int):
    with engine.connect() as conn:
        result = conn.execute(contacto_paciente.select().where(contacto_paciente.c.id_paciente == paciente_id)).first()
        return result    

@user.post("/contacto_pacientes", status_code=HTTP_201_CREATED)
def crear_contacto_paciente(data_contacto: ContactopacienteSchema):
    with engine.connect() as conn:
        nuevo_contacto = data_contacto.dict()
        conn.execute(contacto_paciente.insert().values(nuevo_contacto))
        return Response(status_code=HTTP_201_CREATED)

@user.put("/contacto_pacientes/{paciente_id}")
def actualizar_contacto_paciente(data_update: ContactopacienteSchema, paciente_id: int):
    with engine.connect() as conn:
        result = conn.execute(contacto_paciente.update().where(contacto_paciente.c.id_paciente == paciente_id).values(id_paciente=data_update.id_paciente, domicilio=data_update.domicilio, poblacion=data_update.poblacion, provincia=data_update.provincia, codigo_postal=data_update.codigo_postal, telefono=data_update.telefono))
        result = conn.execute(contacto_paciente.select().where(contacto_paciente.c.id_paciente == paciente_id)).first()
        return result

@user.delete("/contacto_pacientes/{paciente_id}", status_code=HTTP_204_NO_CONTENT)
def borrar_contacto_paciente(paciente_id: int):
    with engine.connect() as conn:
        conn.execute(contacto_paciente.delete().where(contacto_paciente.c.id_paciente == paciente_id))
        return Response(status_code=HTTP_204_NO_CONTENT)


#####

@user.get("/codigo_cita", response_model=List[CodigocitaSchema])
def get_codigo_citas():
 with engine.connect() as conn:
    result = conn.execute(codigo_cita.select()).fetchall()
    return result

@user.get("/codigo_cita/{fechaThora}", response_model=CodigocitaSchema)
def get_codigo_cita(fechaThora: date):
    with engine.connect() as conn:
        result = conn.execute(codigo_cita.select().where(codigo_cita.c.fecha_hora == fechaThora)).first()
        return result

@user.post("/codigo_cita", status_code=HTTP_201_CREATED)
def crear_codigo_cita(data_contacto: CodigocitaSchema):
    with engine.connect() as conn:
        nuevo_contacto = data_contacto.dict()
        conn.execute(codigo_cita.insert().values(nuevo_contacto))
        return Response(status_code=HTTP_201_CREATED)

@user.put("/codigo_cita/{fechaThora}")
def actualizar_codigo_cita(data_update: CodigocitaSchema, fechaThora: date):
    with engine.connect() as conn:
        result = conn.execute(codigo_cita.update().where(codigo_cita.c.fecha_hora == fechaThora).values(id_paciente=data_update.id_paciente, id_doctor=data_update.id_doctor, fecha_hora=data_update.fecha_hora, direccion=data_update.direccion))
        result = conn.execute(codigo_cita.select().where(codigo_cita.c.fecha_hora == fechaThora)).first()
        return result

@user.delete("/codigo_cita/{fechaThora}", status_code=HTTP_204_NO_CONTENT)
def borrar_codigo_cita(fechaThora: date):
    with engine.connect() as conn:
        conn.execute(codigo_cita.delete().where(codigo_cita.c.fecha_hora == fechaThora))
        return Response(status_code=HTTP_204_NO_CONTENT)
