import discord
import datetime
import time
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} ich bin online {datetime.date}')
    await bot.change_presence(activity=discord.Game('Ich mag Kekse'))

@bot.command(pass_context=True)
async def ping(ctx):
    rdd = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - rdd) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")
    print(f'Ping {int(ping)}ms')

bot.run("TOKEN")
