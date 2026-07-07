import requests
import time
import os
#Cargando las credenciales del bot desde el .env
from dotenv import load_dotenv
#Estos son los tokens y el chat id para que te llegue al telegram
load_dotenv()
token = os.getenv("TOKEN")
chat_id = os.getenv("CHAT_ID")

#Aqui es donde te va a llegar el mensaje con su función
def enviar(mensaje):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.get(url, params={"chat_id": chat_id, "text": mensaje})

#De aqui sacamos la pagina donde cogemos las coins  
respuesta = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd")
datos = respuesta.json()

#Bucle de pregunta para la moneda
while True:
    moneda = input("Que moneda quieres ver: ")
    if moneda in datos:
        break
    else:
        print("Esa moneda no existe prueba con otra")

#Bucle de pregunta para el precio que quieres aviso        
while True:
    try:
        limite = int(input("En que precio quieres el aviso: "))
        break
    except:
        print("Pon un numero")

#Aqui da el aviso cuando este en el precio que le indicaste     
while True:
    respuesta = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd")
    datos = respuesta.json() 
    precio = datos[moneda]["usd"]
    if precio < limite:
        enviar (f"{moneda} bajo a {precio}")
    print(moneda, precio)
    #El tiempo de espera    
    time.sleep(60)
    