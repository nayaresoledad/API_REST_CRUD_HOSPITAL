from pydantic import BaseModel
from typing import Optional
from datetime import date

class DoctorSchema(BaseModel):
    id_doctor: Optional[int]
    nombre: str
    apellidos: str
    sexo: str
    fecha_nacimiento: date
    especialidad: str
    numero_colegiado: int
    cargo: str