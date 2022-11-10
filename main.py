# De la libreria fastapi importamos FastAPI para poder hacer nuestra api
from fastapi import FastAPI
# Del archivo router en la carpeta router importamos user que es el nombre que tienen nuestras funciones
from router.router import user

from doc import docu

# Declaramos la variable que va a ser una instancia de FastAPI
app = FastAPI(
       title = "Hospital F5 API",                                         #Título de la API
       description = docu,                                                #Documentación de la API
       openapi_tags= [{                                                   #Aquí añadiremos descripción de los grupos de tags que hemos hecho en router
                 "name" : "Pacientes",
                 "description" : "Rutas de pacientes",

        }, {
            "name" : "Doctores",
            "description" : "Rutas de doctores"
        }, {
            "name" : "Citas",
            "description" : "Rutas de citas"
        }]
)


# 
app.include_router(user)