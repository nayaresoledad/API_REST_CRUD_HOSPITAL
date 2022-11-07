# De la libreria fastapi importamos FastAPI para poder hacer nuestra api
from fastapi import FastAPI
# Del archivo router en la carpeta router importamos user que es el nombre que tienen nuestras funciones
from router.router import user

# Declaramos la variable que va a ser una instancia de FastAPI
app = FastAPI(
       title= "Hospital F5 API",                                         #Título de la API
       description="API para CRUD de la base de datos del Hospital F5",  #Descripción de la API
       openapi_tags= [{                                                  #Aquí añadiremos descripción de los grupos de tags que hemos hecho en router
                 "name" : "Pacientes",
                 "description" : "Rutas de pacientes",

        }, {
            "name" : "Doctores",
            "description" : "Rutas de doctores"
        }, {
            "name" : "Contactos",
            "description" : "Rutas de contactos de pacientes"
        }, {
            "name" : "Citas",
            "description" : "Rutas de citas"
        }]
)


# 
app.include_router(user)