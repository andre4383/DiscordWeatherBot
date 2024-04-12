import discord
import requests

WEATHER_API_KEY = ''

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Logado!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ola'):
        await message.channel.send(f'Olá {message.author.mention}!')

    if message.content.startswith('$clima'):
        await message.channel.send(await on_message1(message))  # Corrected function call


async def on_message1(message):
    if message.content.startswith('$clima'):
        cidade = message.content.split('$clima ')[1]
        clima = get_weather(cidade)
        return clima

def get_weather(cidade):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = { 
        'q': cidade,
        'appid': WEATHER_API_KEY,
        'units': 'metric',
        'lang': 'pt'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        clima = f"Clima em {cidade}: {data['weather'][0]['description']}, Temperatura: {data['main']['temp']}°C"
        return clima
    else:
        return "Não foi possível obter informações sobre o clima da cidade especificada."

client.run('')
