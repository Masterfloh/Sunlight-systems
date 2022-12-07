import discord
import datetime
import time
import random
from discord.ext import commands
import asyncio
import json

## Settings ## 

bot = commands.Bot(intents=discord.Intents.all() , command_prefix= "!" , description='The Best Bot For the Best User!')

CONFIG_LOG = 1048969300767158272

PRESENCES = [ ## Words for the constantly changing presence
    "Playing games",
    "Listening to music",
    "Watching TV",
    "Working on code",
    "Hanging out with friends",
] 

############

bot.remove_command('help')

with open("banned_words.json") as f:
    banned_words = json.load(f)

with open("warns.json", "r") as f:
    warns_data = json.load(f)   

@bot.event
async def on_ready():

    while True:
        presence = random.choice(PRESENCES)
        await bot.change_presence(activity=discord.Game(name=presence))
        await asyncio.sleep(30)


@bot.command(name="help")
async def _help(ctx):
  
    embed = discord.Embed(title="Help", color=0x00ff00)
    embed.add_field(name="!ping", value="Displays the bot's ping", inline=False)
    embed.add_field(name="!poll", value="Creates a poll with the specified options", inline=False)
    embed.add_field(name="!mute", value="Mutes the specified user", inline=False)
    embed.add_field(name="!unmute", value="Unmutes the specified user", inline=False)
    embed.add_field(name="!kick", value="Kicks the specified user", inline=False)
    embed.add_field(name="!ban", value="Bans the specified user", inline=False)
    embed.add_field(name="!purge", value="Clears the specified number of messages", inline=False)
    embed.add_field(name="!warn", value="Warns the specified user", inline=False)
    embed.add_field(name="!getwarn", value="Gets warns from the specified user", inline=False)
    embed.add_field(name="!lockdown", value="Lockdowns a channel", inline=False)
    embed.add_field(name="!tempban", value="Tempbans a specified user", inline=False)
    embed.add_field(name="!tempmute", value="Tempmute a specified user", inline=False)
    embed.add_field(name="!unban", value="Unbans the specified user", inline=False)
    embed.add_field(name="!say", value="Repeats your sentence in a cleaner way", inline=False)
    embed.add_field(name="!announce", value="Announces something to a channel", inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    # create an Embed object with the bot's info
    embed = discord.Embed(title="Bot Info", color=0x00ff00)
    embed.add_field(name="Ping", value=f"{bot.latency * 1000:.2f} ms", inline=False)
    embed.add_field(name="User Count", value=len(bot.users), inline=False)
    embed.add_field(name="Server Count", value=len(bot.guilds), inline=False)

    # send the embedded message to the channel
    await ctx.send(embed=embed)

@bot.command()
async def poll(ctx, question: str, *options: str):

    embed = discord.Embed(title=question, color=0x00ff00)
    for i, option in enumerate(options, start=1):
        embed.add_field(name=option, value=f"{i}: {option}", inline=False)
    poll_message = await ctx.send(embed=embed)


    for i in range(1, len(options) + 1):
        await poll_message.add_reaction(str(i))


    await ctx.send("Poll ended")


    for i, option in enumerate(options, start=1):
     
        num_votes = sum(1 for reaction in poll_message.reactions if reaction.emoji == str(i))
        embed.set_field_at(i-1, name=option, value=f"{num_votes} votes", inline=False)
    await poll_message.edit(embed=embed)


@bot.event
async def on_member_join(member):

    general_channel = bot.get_channel(CONFIG_LOG) # Your join log channel
    await general_channel.send(f"Welcome {member.mention} to the server!")


    join_message = await general_channel.history(limit=1).get(author__id=member.id)
    await join_message.add_reaction("👋")

@bot.event
async def on_member_remove(member):

    general_channel = bot.get_channel(CONFIG_LOG) # Your leave log channel
    await general_channel.send(f"Goodbye {member.name}, we will miss you!")

    leave_message = await general_channel.history(limit=1).get(author__id=bot.user.id)
    await leave_message.add_reaction("😢")

@bot.command()
async def mute(ctx, user: discord.Member, *, reason: str):

    if ctx.author.guild_permissions.mute_members:

        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await user.add_roles(role)


        embed = discord.Embed(title="User Muted", color=0x00ff00)
        embed.add_field(name="User", value=user, inline=False)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.add_field(name="Moderator", value=ctx.author, inline=False)

        log_channel = bot.get_channel(CONFIG_LOG) # Your log channel id
        await log_channel.send(embed=embed)
    else:
        await ctx.send('You do not have permission to mute members')

@bot.command()
async def unmute(ctx, user: discord.Member):

    if ctx.author.guild_permissions.mute_members:
  
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await user.remove_roles(role)


        embed = discord.Embed(title="User Unmuted", color=0x00ff00)
        embed.add_field(name="User", value=user, inline=False)
        embed.add_field(name="Moderator", value=ctx.author, inline=False)

    
        log_channel = bot.get_channel(CONFIG_LOG) # Your log channel id
        await log_channel.send(embed=embed)
    else:
        await ctx.send('You do not have permission to unmute members')


@bot.command()
async def ban(ctx, user: discord.User):

    if ctx.author.guild_permissions.ban_members:

        await ctx.guild.ban(user)


        embed = discord.Embed(title="User Banned", color=0x00ff00)
        embed.add_field(name="User", value=user, inline=False)
        embed.add_field(name="Moderator", value=ctx.author, inline=False)

        general_channel = bot.get_channel(CONFIG_LOG) # Your log channel id
        await general_channel.send(embed=embed)
    else:
        await ctx.send('You do not have permission to ban users')

@bot.command()
async def kick(ctx, user: discord.User):

    if ctx.author.guild_permissions.kick_members:

        await ctx.guild.kick(user)


        embed = discord.Embed(title="User Kicked", color=0x00ff00)
        embed.add_field(name="User", value=user, inline=False)
        embed.add_field(name="Moderator", value=ctx.author, inline=False)

  
        general_channel = bot.get_channel(CONFIG_LOG)# Your log channel id
        await general_channel.send(embed=embed)
    else:
        await ctx.send('You do not have permission to kick users')

@bot.command()
async def tempban(ctx, user: discord.User, duration: int):

    if ctx.author.guild_permissions.ban_members:

        await ctx.guild.ban(user)


        embed = discord.Embed(title="User Temporarily Banned", color=0x00ff00)
        embed.add_field(name="User", value=user, inline=False)
        embed.add_field(name="Moderator", value=ctx.author, inline=False)
        embed.add_field(name="Duration", value=duration, inline=False)

        general_channel = bot.get_channel(CONFIG_LOG) # Your log channel id
        await general_channel.send(embed=embed)

        await asyncio.sleep(duration)
        await ctx.guild.unban(user)
    else:
        await ctx.send('You do not have permission to tempban users')

@bot.command()
async def unban(ctx, user_id: int):

    banned_users = await ctx.guild.bans()
    user = discord.Object(id=user_id)
    await ctx.guild.unban(user)


    general_channel = bot.get_channel(CONFIG_LOG)  # Your log channel id
    await general_channel.send(f"{user.mention} has been unbanned")

@bot.command()
async def announce(ctx, *, message: str):

    embed = discord.Embed(title="Announcement", description=message, color=0x00ff00)


    general_channel = bot.get_channel(HEREID)  # Your Announcement channel id
    await general_channel.send(embed=embed)

@bot.command()
async def say(ctx, *, message: str):

    embed = discord.Embed(description=message, color=0x00ff00)


    await ctx.send(embed=embed)


@bot.command()
async def purge(ctx, num_messages: int):

    if ctx.author.guild_permissions.manage_messages:

        deleted_messages = await ctx.channel.purge(limit=num_messages)


        embed = discord.Embed(title="Deleted Messages", color=0x00ff00)
        for message in deleted_messages:
            embed.add_field(name=message.author, value=message.content, inline=False)


        await ctx.send(embed=embed)
    else:
        await ctx.send('You do not have permission to delete messages')


@bot.command()
async def nuke(ctx, user: discord.Member):

    if ctx.author.guild_permissions.ban_members:

        deleted_messages = await ctx.channel.purge(limit=100, check=lambda m: m.author == user)
        while len(deleted_messages) == 100:
            deleted_messages = await ctx.channel.purge(limit=100, check=lambda m: m.author == user)


        embed = discord.Embed(title="Deleted Messages", color=0xff0000)
        for message in deleted_messages:
            embed.add_field(name=message.author, value=message.content, inline=False)

        await ctx.send(embed=embed)
    else:
        await ctx.send('You do not have permission to delete messages')

@bot.command()
async def tempmute(ctx, member: discord.Member, duration: int, *, reason: str):

    if ctx.author.guild_permissions.manage_roles:

        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not mute_role:
            mute_role = await ctx.guild.create_role(name="Muted")


        current_roles = member.roles
        await member.add_roles(mute_role)
        member.roles = current_roles


        embed = discord.Embed(title="Temporary Mute", color=0xff0000)
        embed.add_field(name="Member", value=member, inline=False)
        embed.add_field(name="Duration", value=duration, inline=False)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.set_footer(text=f"Muted by {ctx.author}")

        logs_channel = bot.get_channel(CONFIG_LOG) # Your log channel id
        await logs_channel.send(embed=embed)


        await asyncio.sleep(duration)
        await member.remove_roles(mute_role)
    else:
        await ctx.send('You do not have permission to mute members')

@bot.command()
async def lockdown(ctx, duration: int):

    if ctx.author.guild_permissions.manage_channels:

        channel = ctx.message.channel

    
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

        embed = discord.Embed(title="Lockdown", color=0xff0000)
        embed.add_field(name="Channel", value=channel, inline=False)
        embed.add_field(name="Duration", value=duration, inline=False)
        embed.set_footer(text=f"Locked down by {ctx.author}")

 
        logs_channel = bot.get_channel(CONFIG_LOG) # Your log channel id
        await logs_channel.send(embed=embed)


        await asyncio.sleep(duration)

@bot.event
async def on_message(message):

    if any(word in message.content.lower() for word in banned_words):

        await message.delete()
        await message.author.send("Please do not use swear words in this server")
    else:
        await bot.process_commands(message)

@bot.command()
async def warn(ctx, user: discord.Member, *, reason: str):

    if ctx.author.guild_permissions.kick_members:

        if user.id in warns_data:
            warns_data[user.id]["warns"] += 1
        else:
            warns_data[user.id] = {"warns": 1}


        with open("warns.json", "w") as f:
            json.dump(warns_data, f, indent=4)

        await ctx.send(f"{user.mention} has been warned for: {reason}")
    else:
        await ctx.send("You do not have permission to warn users")


@bot.command()
async def getwarn(ctx, user: discord.Member):

    if user.id in warns_data:
        await ctx.send(f"{user.mention} has {warns_data[user.id]['warns']} warns")
    else:
        await ctx.send(f"{user.mention} does not have any warns")

bot.run("YOURBOTTOKEM")
