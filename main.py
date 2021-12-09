import discord
import datetime
import time
import random

from discord.ext import commands

bot = commands.Bot(command_prefix=['!'])


@bot.event
async def on_ready():
    print(f'{bot.user} ich bin online {datetime.date}')
    await bot.change_presence(activity=discord.Game('nicolas ist hot'))


@bot.command()
async def test(ctx):
    await ctx.send("test")


@bot.command(pass_context=True)
async def ping(ctx):
    rdd = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - rdd) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")
    print(f'Ping {int(ping)}ms')


begrüssung = ["Hey", "Hey wie gehts?", "Hallo", "Oha du redest echt mit mir?", "Servus", "Hi wolltest du echt zu mir sagen?"]


@bot.event
async def on_message(message):
    if message.content == 'hello','hi':
        await message.channel.send(random.choice(begrüssung))
    await bot.process_commands(message)

bot.run("OTE4MTU3MDYwODA0MzI1Mzc3.YbDKZQ.lDX9inxEvHyBEUoDuTLDb1VgmAk")
