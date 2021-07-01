# Ejemplo básico de una API con FastAPI

Este proyecto es una muestra de lo facil que es crear APIs con el framework FastAPI.

La velocidad y limpieza durante el desarrollo es lo que lo distingue como la mejor opcion contra Flask o Django.

![CRUD Sencillo](/img/crud.png)

# Instalación

Descarga el repositorio en algun lugar de tu computadora, entra a la carpeta y crea un entrono virtual con el siguiente comando:

- python3 -m venv venv

Ahora ejecuta el entorno virtual de la siguiente manera:

- source venv/bin/activate

Estaras en tu ambiente virtual cuando veas esto en tu terminal "(venv)".

Ahora ubica el archivo requirements.txt y ejecuta el siguiente comando para instalar todas las dependencias necesarias para correr la aplicación:

- pip3 install -r requirements.txt


# Ejecución de la App

Ubicate en la misma posición donde se encuentre el archivo "main.py" y ejecuta el siguiente comando:

- uvicorn main:app --reload

Una vez hecho esto, entra a la siguiente URL dentro de tu navegador web:

- http://127.0.0.1:8000/