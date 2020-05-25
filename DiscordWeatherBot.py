import discord
from discord.ext import commands
import os
import pyowm

owm = pyowm.OWM('c215dad8b6c6f9603d49028b5fbcda3e')
obv = owm.weather_at_place('los angeles, ca')
print(obv)

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready() :
    print("WeatherBot is Ready")

@client.command()
async def test(ctx, city, state) :
    print(f"{str(ctx.message.author)} asked for the weather of {city}, {state}")
    # url = f"api.openweathermap.org/data/2.5/weather?q={city},{state}&appid=c215dad8b6c6f9603d49028b5fbcda3e"
    # response = requests.request("GET", url)
    # await ctx.send(response.text)

client.run('NzE0MjI1MzIwMDg1MTYwMDM5.XsrkxQ.t7hbt963JiFYWwcWeEt29GDHle8')