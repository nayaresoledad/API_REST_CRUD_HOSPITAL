from pydantic import BaseModel
from typing import Optional

class PacienteSchema(BaseModel):
    id_paciente: Optional[int]
    nombre_paciente: str
    apellidos_paciente: str
    numero_historial_clinico: int
    observaciones: str