import discord
from discord.ext import commands
import os
from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit
from keys import CLIENT # APP_ID, API_KEY, API_SECRET

# data = YahooWeather(APP_ID=APP_ID, api_key=API_KEY, api_secret=API_SECRET)

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready() :
    print("WeatherBot is Ready")

@commands.command()
async def ping(ctx) :
    await ctx.send(f"Ping: {round(1000 * client.latency)}ms")
    print(f"{str(ctx.message.author)} asked for the Ping")

for filename in os.listdir('./cogs') :
    if filename.endswith('.py') and filename != 'keys.py':
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(CLIENT)