from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CodigocitaSchema(BaseModel):
    id_paciente: Optional[int]
    id_doctor: Optional[int]
    fecha_hora: datetime
    direccion: str