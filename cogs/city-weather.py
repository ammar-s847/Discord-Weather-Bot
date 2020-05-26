import discord
from discord.ext import commands
from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit
from keys import APP_ID, API_KEY, API_SECRET

data = YahooWeather(APP_ID=APP_ID, api_key=API_KEY, api_secret=API_SECRET)

class City_Weather(commands.Cog) :
    def __init__(self, client) :
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self) :
        # await self.client.change_presence(status=discord.Status.online, activity=discord.Game('Hello There!'))
        print("City-Weather Cog is working")
    
    @commands.command(aliases = ['city'])
    async def temp(self, ctx, city) :
        data.get_yahoo_weather_by_city(f"{city.lower()}", Unit.celsius)
        print(f"{str(ctx.message.author)} asked for the weather in {city}")
        reply = f"Weather in {city}: \n Temp: {data.condition.temperature} degrees C \n Condition: {data.condition.text}" 
        await ctx.send(reply)

def setup(client) :
    client.add_cog(City_Weather(client))