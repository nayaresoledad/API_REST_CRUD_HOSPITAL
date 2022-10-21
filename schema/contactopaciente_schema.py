from pydantic import BaseModel
from typing import Optional

class ContactopacienteSchema(BaseModel):
    id_paciente: Optional[int]
    domicilio: str
    poblacion: str
    provincia: str
    codigo_postal: str
    telefono: str