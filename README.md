##Hospital Base API
***¿Cómo se instala la API?***\n 
1. Crea un entorno específicamente para este proyecto. Por ejemplo con conda **conda create -n nombreEntorno**.\n 
2. Dentro de este entorno será necesario instalar SQLAlchemy (**pip install sqlalchemy**), FastAPI (**pip install fastapi**) y psycopg2 (**pip install psycopg2**).\n 
3. Descarga el contenido del repositorio **https://github.com/Factoria-F5-AI-Bootcamp-1-Edicion/hospital-base.git**\n 
4. Solicite los datos de acceso a la base de datos del propietario e introdúzcaos en un archivo **.env** y ponga este archivo en la misma carpeta que el resto de archivos de la API.\n 
5. Desde la terminal, diríjase a la crpeta que contiene los archivos de la API y desde allí ejecute **uvicorn main:app**. 
6. En la terminal le aparecerá un mensaje que dirá **Uvicorn running on direcciónServidor**.\n 7. Diríjse a la dirección del servidor dada, se abrirá en su navegador predeterminado.\n 8. A la ruta raíz en la que se encuentra añada /docs, **ejemplo: http://127.0.0.1:8000/docs**