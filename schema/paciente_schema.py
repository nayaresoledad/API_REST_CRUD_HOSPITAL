from pydantic import BaseModel
from typing import Optional

""""Esto funciona para definir las variables de la base de datos de PGADMING"""

# Se crea la clase Paciente y se definen tipos de variables
class PacienteSchema(BaseModel):
    id_paciente: int
    nombre_paciente: str
    apellidos_paciente: str
    numero_historial_clinico: int
    domicilio: str
    poblacion_provincia: str
    telefono: str