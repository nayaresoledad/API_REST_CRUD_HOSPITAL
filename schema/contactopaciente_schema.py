from pydantic import BaseModel
from typing import Optional

""""Esto funciona para definir las variables de la base de datos de PGADMING"""

# Se crea la clase contacto, esta contiene los datos del paciente y se definen tipos de variables
class ContactopacienteSchema(BaseModel):
    id_paciente: Optional[int]
    domicilio: str
    poblacion: str
    provincia: str
    codigo_postal: str
    telefono: str