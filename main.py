from fastapi import FastAPI
import json

app = FastAPI()
datos = {
    "1": "Python",
    "2": "Java",
    "3": "PHP",
    "4": "JavaScript",
    "5": "C++"
}

@app.get("/")
def raiz():
    sin_codificar = json.dumps(datos)
    return json.loads(sin_codificar)