from pydantic import BaseModel
from typing import Optional

class PacienteSchema(BaseModel):
    id: Optional[str]
    sepal_lenght: float
    sepal_width: float
    petal_length: float
    petal_width: float
    species: str
