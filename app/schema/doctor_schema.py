from pydantic import BaseModel
from datetime import date

""""Esto funciona para definir las variables de la base de datos de PGADMING"""
#Se crea la clase Doctor se definen tipos de variables
class DoctorSchema(BaseModel):
    id_doctor: int
    nombre: str
    apellidos: str
    sexo: str
    fecha_nacimiento: date
    especialidad: str
    numero_colegiado: int
    cargo: str