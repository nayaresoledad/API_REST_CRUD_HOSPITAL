from datetime import date
from urllib import response
from fastapi import APIRouter, Response, HTTPException
from schema.paciente_schema import PacienteSchema
from schema.doctor_schema import DoctorSchema
from schema.contactopaciente_schema import ContactopacienteSchema
from schema.codigocita_schema import CodigocitaSchema
from config.db import engine
from model.user import doctor, paciente, codigo_cita
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from typing import List
import sqlalchemy as db
import logging

#Configuramos un logger para trackear las acciones en el CRUD
logging.basicConfig(
    level=logging.DEBUG, #if os.environ.get("DEBUG_MODE") == "1" else logging.INFO, 
    filename="logging_record.log", 
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s")

#Guardamos la función router en una variable para usarla después.
user = APIRouter()

#Página principal, la bienvenida a nuestro hospital
@user.get("/", tags=["pagina principal"])  #Indicamos aqui la ruta en la que se hará la consulta (get), y el tag apropiado para esa ruta
async def root():
    return "Esto es Hospital F5"


###Tabla Pacientes

#Buscar todos los pacientes
@user.get("/pacientes", response_model=List[PacienteSchema], tags=["Pacientes"])
async def get_pacientes():
 with engine.connect() as conn:                           #Usamos el entorno with para abrir la conexión con la DB sólo cuando es necesaria (buenas prácticas). Tras usarse, la conexión se cierra.
    result = conn.execute(paciente.select()).fetchall()
    logging.info("Se ha consultado los pacientes que hay")
    return result

#Buscar paciente por id
@user.get("/pacientes/{paciente_id}", response_model=PacienteSchema, tags=["Pacientes"]) #En este caso a la direccion paciente le añadiremos un id
async def get_paciente(paciente_id: int):
    with engine.connect() as conn:
        result = conn.execute(paciente.select().where(paciente.c.id_paciente == paciente_id)).first() #La función first hace que nos devuelva el primer elemento de la lista, ya que solo buscamos un paciente
        logging.debug(result)
        if result == None:
            raise HTTPException(status_code=404, detail="Paciente no encontrado")
        
        logging.info(f"Se ha consultado el pacientes con el id {paciente_id}")
        return result    #Devuelve la información del paciente buscado en forma de diccionario 

#Añadir nuevos pacientes a la base de datos
@user.post("/pacientes", status_code=HTTP_201_CREATED, tags=["Pacientes"])
async def crear_paciente(data_paciente: PacienteSchema):                      #Basamos los nuevos datos en el esquema de Paciente, creado en la carpeta schema
    with engine.connect() as conn:
        nuevo_paciente = data_paciente.dict()                           #Creamos un diccionario con los datos del nuevo paciente
        conn.execute(paciente.insert().values(nuevo_paciente))          #Conectamos a la DB e insertamos el nuevo paciente
        logging.info(f"Se ha creado un paciente con {nuevo_paciente}")
        return Response(status_code=HTTP_201_CREATED)                   #Hacemos que cuando sea exitoso devuelva un código 200 CREADO

#Actualizar información de un paciente ya existente
@user.put("/pacientes/{paciente_id}", tags=["Pacientes"])
async def actualizar_paciente(data_update: PacienteSchema, paciente_id: int):
    with engine.connect() as conn:
        result = conn.execute(paciente.update().where(paciente.c.id_paciente == paciente_id).values(id_paciente=data_update.id_paciente, nombre_paciente=data_update.nombre_paciente, apellidos_paciente=data_update.apellidos_paciente, numero_historial_clinico=data_update.numero_historial_clinico, domicilio=data_update.domicilio, poblacion_provincia=data_update.poblacion_provincia, telefono=data_update.telefono))
        result = conn.execute(paciente.select().where(paciente.c.id_paciente == paciente_id)).first()
        return result

#Borrar un paciente
@user.delete("/pacientes/{paciente_id}", status_code=HTTP_204_NO_CONTENT, tags=["Pacientes"])
async def borrar_paciente(paciente_id: int):
    with engine.connect() as conn:
        conn.execute(paciente.delete().where(paciente.c.id_paciente == paciente_id))           #Borra el paciente en el que la columna (c) id paciente es la introducida
        return Response(status_code=HTTP_204_NO_CONTENT)



####Tabla doctores

#Buscar todos los doctores
@user.get("/doctores", response_model=List[DoctorSchema], tags=["Doctores"])
async def get_doctores():
 with engine.connect() as conn:
    result = conn.execute(doctor.select()).fetchall()
    return result

#Buscar doctores por id
@user.get("/doctores/{doctor_id}", response_model=DoctorSchema, tags=["Doctores"])
async def get_doctor(doctor_id: int):
    with engine.connect() as conn:
        result = conn.execute(doctor.select().where(doctor.c.id_doctor == doctor_id)).first()
        return result    

#Añadir nuevos doctores a la base de datos
@user.post("/doctores", status_code=HTTP_201_CREATED, tags=["Doctores"])
async def crear_doctor(data_doctor: DoctorSchema):
    with engine.connect() as conn:
        nuevo_doctor = data_doctor.dict()
        conn.execute(doctor.insert().values(nuevo_doctor))
        return Response(status_code=HTTP_201_CREATED)

#Actualizar información de un doctor ya existente
@user.put("/doctores/{doctor_id}", tags=["Doctores"])
async def actualizar_doctor(data_update: DoctorSchema, doctor_id: int):
    with engine.connect() as conn:
        result = conn.execute(doctor.update().where(doctor.c.id_doctor == doctor_id).values(id_doctor=data_update.id_doctor, nombre=data_update.nombre, apellidos=data_update.apellidos, sexo=data_update.sexo, fecha_nacimiento=data_update.fecha_nacimiento, especialidad=data_update.especialidad, numero_colegiado=data_update.numero_colegiado, cargo=data_update.cargo))
        result = conn.execute(doctor.select().where(doctor.c.id_doctor == doctor_id)).first()
        return result

#Borrar un doctor
@user.delete("/doctores/{doctor_id}", status_code=HTTP_204_NO_CONTENT, tags=["Doctores"])
async def borrar_doctor(doctor_id: int):
    with engine.connect() as conn:
        conn.execute(doctor.delete().where(doctor.c.id_doctor == doctor_id))
        return Response(status_code=HTTP_204_NO_CONTENT)
        


#####Tabla citas

#Buscar todas las citas
@user.get("/codigo_cita", response_model=List[CodigocitaSchema], tags=["Citas"])
async def get_codigo_citas():
 with engine.connect() as conn:
    result = conn.execute(codigo_cita.select()).fetchall()
    return result

#Buscar citas por fecha
@user.get("/codigo_cita/{paciente_id}", response_model=CodigocitaSchema, tags=["Citas"])
async def get_codigo_cita( paciente_id: int):
    with engine.connect() as conn:
        result = conn.execute(codigo_cita.select().where(codigo_cita.c.id_paciente == paciente_id)).first()
        return result

#Añadir nuevas citas a la base de datos
@user.post("/codigo_cita", status_code=HTTP_201_CREATED, tags=["Citas"])
async def crear_codigo_cita(data_contacto: CodigocitaSchema):
    with engine.connect() as conn:
        nuevo_contacto = data_contacto.dict()
        conn.execute(codigo_cita.insert().values(nuevo_contacto))
        return Response(status_code=HTTP_201_CREATED)

#Actualizar información de una cita ya existente
@user.put("/codigo_cita/{paciente_id}", tags=["Citas"])
async def actualizar_codigo_cita(data_update: CodigocitaSchema, paciente_id: int):
    with engine.connect() as conn:
        result = conn.execute(codigo_cita.update().where(codigo_cita.c.id_paciente == paciente_id).values(id_paciente=data_update.id_paciente, id_doctor=data_update.id_doctor, fecha=data_update.fecha, direccion=data_update.direccion))
        result = conn.execute(codigo_cita.select().where(codigo_cita.c.id_paciente == paciente_id)).first()
        return result

#Borrar una cita
@user.delete("/codigo_cita/{paciente_id}", status_code=HTTP_204_NO_CONTENT, tags=["Citas"])
async def borrar_codigo_cita(paciente_id: int):
    with engine.connect() as conn:
        conn.execute(codigo_cita.delete().where(codigo_cita.c.id_paciente == paciente_id))
        return Response(status_code=HTTP_204_NO_CONTENT)