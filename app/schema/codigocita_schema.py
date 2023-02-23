from pydantic import BaseModel
from datetime import date

""""Esto funciona para definir las variables de la base de datos de PGADMING"""
# se crea clase citas se definen tipos de variables
class CodigocitaSchema(BaseModel):
    fecha: date
    direccion: str
    id_paciente: int
    id_doctor: int