from pydantic import BaseModel
from typing import Optional
from datetime import date

""""Esto funciona para definir las variables de la base de datos de PGADMING"""

# se crea clase citas se definen tipos de variables
class CodigocitaSchema(BaseModel):
    id_paciente: Optional[int]
    id_doctor: Optional[int]
    fecha: date
    direccion: str