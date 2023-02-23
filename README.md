# Hospital F5 API

# Link a la Documentación en Notion https://www.notion.so/Documentaci-n-API-Hospital-F5-cf7d033453bb4e26a2b5c3476f202033

## ***¿Cómo se instala la API?***
1. Crea un entorno específicamente para este proyecto. Por ejemplo con conda 
```
conda create -n nombreEntorno
```
2. Dentro de este entorno será necesario instalar SQLAlchemy , FastAPI, psycopg2 y dotenv:
```
pip install sqlalchemy
pip install fastapi
pip install psycopg2
pip install dotenv
```
3. Descarga el contenido del repositorio https://github.com/Factoria-F5-AI-Bootcamp-1-Edicion/hospital-base.git
4. Solicite los datos de acceso a la base de datos del propietario e introdúzcaos en un archivo **.env** y ponga este archivo en la carpeta raíz. ![datos sensibles](img/basedatos.png)
5. Desde la terminal, diríjase a la cArpeta que contiene los archivos de la API y desde allí ejecute
```
uvicorn app.main:app
```
   Esta terminal debe permanecer abierta para el correcto funcionamiento de la API.

6. En la terminal le aparecerá un mensaje que dirá **Uvicorn running on direcciónDelServidor** ![Uvicorn running on direcciónServidor](img/uvicorn.png)
7. Diríjse a la dirección del servidor dada, se abrirá en su navegador predeterminado.\n 8. A la ruta raíz en la que se encuentra añada /docs, **ejemplo: http://127.0.0.1:8000/docs**
7. En este momento se encuentra en la documentación Swagger de la API, allí encontrará las peticiones que puede hacer al servidor, con su explicación.
8. Comience a consultar, crear, modificar y eliminar los datos de pacientes, doctores y citas.

## ***Otras rutas de interés en la API***

Añadiendo al final de la **direcciónDelServidor** (ejemplo: http://127.0.0.1:8000) estas rutas accederá a diferentes consultas:
```
/pacientes              En esta página podrá consultar los datos de los pacientes disponibles.
/doctores               En esta página podrá consultar los datos de los doctores disponibles.
/codigo_cita            En esta página podrá consultar los datos de las citas disponibles.
```

## ***Ejecutar el test de la API***

Para comprobar que todo funciona correctamente antes de empezar a realizar consultas a la base de datos con esta API, se recomienda ejecutar el test. Para ello, con la terminal y desde la carpeta raíz donde descargó el contenido del repositorio (por defecto: .../hospital-base) ejecute lo siguiente:
```
python tests/test_api
```
Tras ejecutar ese comando debería aparecer una salida mostrando los test completados como la siguiente:
![test](img/test.png)

Si alguno de los 15 tests fallaran habría que revisar el error y arreglar el problema antes de empezar a utilizar la API.

## ***¿Cómo levantar el Docker?***

1. Descargue e instale [docker](https://docs.docker.com/engine/install/ubuntu/) (dependerá de su S.O.).
2. Cree un archivo .env con los datos de autenticación. Estos datos serán los que indique en el archivo **docker-compose.yaml** (en environment). En este caso la direccion es:
![direccion](img/basedatos.png)
3. En el directorio raíz del proyecto ejecute
```
docker build -t hospital4 .
```
Esto creará una imagen con nombre **hospital4**. Usaremos esta imagen para levantar la API más adelante.
4. Descargue una imagen de postgresql, le recomendamos la más sencilla, llamada postgres. Ejecute en su terminal:
```
docker pull postgres
```
Esto descargará la imagen de postgres, para crear una base de datos dentro del contenedor, que se conectará a nuestra APP.
5. Ya teniendo las dos imágenes que necesita es el momentor de levantar el docker-compose. En el directorio raíz ejecute:
```
docker-compose up
```
Con esto quedará levantada la API conectada a un servidor postgres, ambos en contenedores. Para cerrar el servicio pulse **CTRL+C**.

## ***¿Para qué puedo utilizar esta API?***

Esta API le permite al usuario crear, consultar, actualizar y eliminar datos de los pacientes, así como sus datos de contacto y sus citas, y los doctores del Hospital F5.

## ***Esquema UML de las tablas creadas por esta API***

Al ejecutar el programa por primera vez, se crearan en el servidor 3 tablas: paciente, doctor y codigo_cita. Estas tablas están relacionadas de la siguiente manera:
![esquemauml](img/esquema.png)

## ***Tecnología utilizada***

- Organización: Metodología SCRUM y Trello.com
- Lenguajes utilizados: Python y PostgreSQL.
- Librerías utilizadas: SQLAlchemy, FastAPI, dotenv.
- Documentación: MarkDown y Swagger.

## ***Créditos***

Desarrollado por: 

- Vaneza Flores: Scrum Máster
- Pablo Ruano
- Christian Cabrera: Product Owner
- Nayare Montes

Ejercicio para el bootcamp de Inteligencia Artifical en **Factoría F5**.
> Contacto: hospitalf5@factoriaf5.org 
