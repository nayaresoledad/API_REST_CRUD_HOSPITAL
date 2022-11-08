# Hospital F5 API

## ***¿Cómo se instala la API?***
1. Crea un entorno específicamente para este proyecto. Por ejemplo con conda 
```
conda create -n nombreEntorno
```
2. Dentro de este entorno será necesario instalar SQLAlchemy , FastAPI y psycopg2:
```
pip install sqlalchemy
pip install fastapi
pip install psycopg2
```
3. Descarga el contenido del repositorio https://github.com/Factoria-F5-AI-Bootcamp-1-Edicion/hospital-base.git
4. Solicite los datos de acceso a la base de datos del propietario e introdúzcaos en un archivo **.env** y ponga este archivo en la misma carpeta que el resto de archivos de la API. ![datos sensibles](img/basedatos.png)
5. Desde la terminal, diríjase a la cArpeta que contiene los archivos de la API y desde allí ejecute
```
uvicorn main:app
```
   esta terminal debe permanecer abierta para el correcto funcionamiento de la API.

6. En la terminal le aparecerá un mensaje que dirá **Uvicorn running on direcciónServidor** ![Uvicorn running on direcciónServidor](img/uvicorn.png)
7. Diríjse a la dirección del servidor dada, se abrirá en su navegador predeterminado.\n 8. A la ruta raíz en la que se encuentra añada /docs, **ejemplo: http://127.0.0.1:8000/docs**
7. En este momento se encuentra en la documentación Swagger de la API, allí encontrará las peticiones que puede hacer al servidor, con su explicación.
8. Comience a consultar, crear, modificar y eliminar los datos de pacientes, doctores, contactos de pacientes y citas.

## ***¿Para qué puedo utilizar esta API?***

Esta API le permite al usuario crear, consultar, actualizar y eliminar datos de los pacientes, así como sus datos de contacto y sus citas, y los doctores del Hospital F5.

## ***Créditos***

Desarrollado por Vaneza, Pablo, Christian y Nayare como ejercicio para el bootcamp de Inteligencia Artifical en Factoría F5.
Contacto: hospitalf5@factoriaf5.org 