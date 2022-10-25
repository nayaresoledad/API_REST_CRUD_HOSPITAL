from pydantic import BaseModel
from typing import Optional
from datetime import date

class CodigocitaSchema(BaseModel):
    id_paciente: Optional[int]
    id_doctor: Optional[int]
    fecha: date
    direccion: str