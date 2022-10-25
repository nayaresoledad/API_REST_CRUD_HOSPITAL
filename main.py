# De la libreria fastapi importamos FastAPI para poder hacer nuestra api
from fastapi import FastAPI
# Del archivo router en la carpeta router importamos user que es el nombre que tienen nuestras funciones
from router.router import user

# Declaramos la variable que va a ser una instancia de FastAPI
app= FastAPI(
    title= "Hopital F5",
    description= "API para la gestión de la base de datos de Hospital F5",
    openapi_tags=[
        {"name": "Pacientes","description":"Pacientes del hospital F5"},
        {"name": "Doctores","description":"Doctores del hospital F5"}
    ]
)


# 
app.include_router(user)