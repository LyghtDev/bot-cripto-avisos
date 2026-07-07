# Bot de Alertas de Criptomonedas

Bot que vigila el precio de criptomonedas en tiempo real y te avisa por Telegram cuando bajan de un precio que tú decides.

## Características

- Consulta precios en tiempo real desde la API de CoinGecko
- Te pregunta qué moneda vigilar y a qué precio avisarte
- Envía notificaciones a tu Telegram
- Valida los datos que introduces (moneda y precio)

## Tecnologías

- Python
- API de CoinGecko
- API de Telegram
- python-dotenv (para las credenciales)

## Cómo usarlo

## Cómo usarlo

1. Instala las librerías necesarias:

```
pip3 install requests python-dotenv
```

2. Crea un archivo `.env` en la carpeta del proyecto con tus credenciales de Telegram:

```
TOKEN=tu_token_de_telegram
CHAT_ID=tu_chat_id
```

3. Ejecuta el bot:

```
python3 bot.py
```

4. El bot te preguntará qué moneda vigilar y a qué precio quieres recibir el aviso.
