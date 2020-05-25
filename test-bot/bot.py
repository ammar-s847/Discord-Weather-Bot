#Token: NzE0MjI1MzIwMDg1MTYwMDM5.XsrkxQ.t7hbt963JiFYWwcWeEt29GDHle8

import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

'''
@client.event
async def on_ready() :
    await self.client.change_presence(status=discord.Status.online, activity=discord.Game('Hello There!'))
    print("Bot is Ready")

@client.event
async def on_member_join(member) :
    print(f"{member} has joined the server")

@client.event
async def on_member_remove(member) :
    print(f"{member} has left the server")

@client.command(aliases = ['showPing'])
async def ping(ctx) :
    await ctx.send(f"Ping: {round(1000 * client.latency)}ms")
    print(f"{str(ctx.message.author)} asked for the Ping")
    # print(str(ctx.message.author))
    # print(str(ctx.message.channel))
    # print(str(ctx.message.content))
'''

@client.command()
async def load(ctx, extension) :
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension) :
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs') :
    if filename.endswith('.py') :
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NzE0MjI1MzIwMDg1MTYwMDM5.XsrkxQ.t7hbt963JiFYWwcWeEt29GDHle8')