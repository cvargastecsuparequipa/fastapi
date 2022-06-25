from fastapi import FastAPI
import requests

app =FastAPI()

@app.get("/")
def inicio():
    return "Hola mundo"

@app.get("/prueba/{mensaje}")
def inicioMensaje(mensaje:str):
    return f"el mensaje mostrado es : {mensaje}"

@app.post("/pruebaPost")
def pruebaPost(nombre:str , edad:int):
    return f"{nombre} tiene {edad} anios"

@app.post("/enviarmensajeAPI")
def enviarMensajeAPI(celular:str , mensaje:str):
    cel = '51'+celular
    cadenajson ={
  "app": {
    "id": "51961498695",
    "time": "1656120356",
    "data": {
      "recipient": {
        "id": cel
      },
      "message": [
        {
          "time": "1656120356",
          "type": "text",
          "value": mensaje
        }
      ]
    }
  }
}
    res = requests.post('https://whapi.io/api/send',json=cadenajson)
    return res.text

