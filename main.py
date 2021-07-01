from fastapi import FastAPI, Request

import json
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")
datos = {
    "1": "Python",
    "2": "Java",
    "3": "PHP",
    "4": "JavaScript",
    "5": "C++"
}


@app.get("/")
def raiz(request:Request):
    sin_codificar = json.dumps(datos)
    json_datos = json.loads(sin_codificar)
    return templates.TemplateResponse("inicio.html", {"request":request,"listado":json_datos})
    

@app.post("/agregar")
async def agregar(request:Request):
    nuevos_datos = {}
    formdata = await request.form()
    i = 1
    for id in datos:
        nuevos_datos[str(id)] = datos[id]
        i+=1
    nuevos_datos[str(i)] = formdata["nuevolenguaje"]
    sin_codificar = json.dumps(nuevos_datos)
    return json.loads(sin_codificar)