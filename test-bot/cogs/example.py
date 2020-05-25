import discord
from discord.ext import commands

class Example(commands.Cog) :
    def __init__(self, client) :
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self) :
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game('Hello There!'))
        print("Example Cog is working")
    
    @commands.command()
    async def ping(self, ctx) :
        await ctx.send(f"Ping: {round(1000 * self.client.latency)}ms")
        print(f"{str(ctx.message.author)} asked for the Ping")

def setup(client) :
    client.add_cog(Example(client))