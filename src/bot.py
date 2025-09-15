import requests
import discord
from discord import app_commands
import json

with open("config1.json", "r") as f:
    config = json.load(f)

DISCORD_TOKEN = config["DISCORD_TOKEN"]
WEATHER_API_KEY = config["WEATHER_API_KEY"]

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

def get_weather(city):
    url= f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
            main = data["main"]
            weather = data["weather"][0]
            return (
                f" {city.title()}\n"
                f" Temp: {main['temp']}°C\n"
                f" Humidity: {main['humidity']}%\n"
                f" Condition: {weather['description'].title()}"
            )
    else:
        return "City not found!"
    
@tree.command(name="weather",description="uwu")

async def weather(interaction: discord.Interaction, city: str):
    report = get_weather(city)
    await interaction.response.send_message(report)

@client.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {client.user}")

client.run(DISCORD_TOKEN)
