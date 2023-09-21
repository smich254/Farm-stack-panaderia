# README.md para FastAPI en Python

## Configuración del entorno para FastAPI (Windows)

1. Instala Python si aún no lo tienes. Puedes descargarlo desde python.org.

2. Abre la línea de comandos y crea un entorno virtual utilizando virtualenv:

   ```
   python -m venv venv
   ```

3. Activa el entorno virtual:

   En Windows:

   ```
   venv\Scripts\activate
   ```

4. Clona o descarga este repositorio y navega a la carpeta del proyecto:

   ```
   git clone <url_del_repositorio>
   ```

   ```
   cd <nombre_del_proyecto>
   ```

5. Instala las dependencias del proyecto desde el archivo requirements.txt:

   ```
   pip install -r requirements.txt
   ```

6. Inicia la aplicación FastAPI:

   ```
   uvicorn main:app --reload
   ```

   Abre tu navegador y ve a http://localhost:8000 para ver la aplicación en funcionamiento.

## Configuración del entorno para FastAPI (Linux)

Los pasos para Linux son similares a los de Windows, pero no es necesario agregar \ en las rutas de los comandos.
