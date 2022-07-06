                                #░█████╗░██████╗░███╗░░░███╗██╗███╗░░██╗  ████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
                                #██╔══██╗██╔══██╗████╗░████║██║████╗░██║  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
                                #███████║██║░░██║██╔████╔██║██║██╔██╗██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
                                #██╔══██║██║░░██║██║╚██╔╝██║██║██║╚████║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
                                #██║░░██║██████╔╝██║░╚═╝░██║██║██║░╚███║  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
                                #╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░

##kick

@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    if (not ctx.author.guild_permissions.administrator):
        await ctx.send(f"{ctx.author.mention} You do not have permission to use this command!")
        return
    await member.kick(reason=reason)
    await ctx.send(f"{member.name} has been kicked from the server!")
    channel5 = client.get_channel(mylogchannelid)
    embed2 = discord.Embed(title=f"Member kicked",
                           description=f"{ctx.author.mention} kicked {member.mention} from the server",
                           color=discord.Colour.random())
    embed2.add_field(name="Reason", value=reason, inline=False)
    now = datetime.datetime.now().strftime("%H:%M")
    embed2.set_footer(icon_url=ctx.author.avatar_url,
                      text=f"Kicked by {ctx.author.name}#" + ctx.author.discriminator + f'' + f" Today at | {now}")
    await channel5.send(embed=embed2)

#EXAMPLE: kick @user Stop Spamming 

##mute

@client.command()
@commands.has_permissions(manage_roles=True)
async def rmute(ctx, member: discord.Member, time, *, reason=None):
    guild = ctx.guild
    if (not ctx.author.guild_permissions.administrator):
        await ctx.send(f"{ctx.author.mention} You don't have permission to use this command!")

    for role in guild.roles:
        if role.name == f"Your mute role name":
            await member.add_roles(role)
    for role in guild.roles:
        if role.name == f"Members role":
            await member.remove_roles(role)
            await ctx.send(f"{member.mention} has been muted for {time} for: {reason}")
            await ctx.message.delete()
            channel = client.get_channel(mylogchannelid)
            embed2 = discord.Embed(title=f"Member Muted", description=f"The muted user: {member.mention}",
                                   color=discord.Colour.random())
            embed2.add_field(name="Time", value=time, inline=False)
            embed2.add_field(name="Reason", value=reason, inline=False)
            now = datetime.datetime.now().strftime("%H:%M")
            embed2.set_footer(icon_url=ctx.author.avatar_url,
                              text=f"Muted by {ctx.author.name}#" + ctx.author.discriminator + f'' + f" Today at | {now}")
            await channel.send(embed=embed2)
            d = time[-1]

            num = int(time[:-1])

            if d == "s":
                await asyncio.sleep(num)

            if d == "m":
                await asyncio.sleep(num * 60)

            if d == "h":
                await asyncio.sleep(num * 60 * 60)

            if d == "d":
                await asyncio.sleep(num * 60 * 60 * 24)
            await member.add_roles(role)
        for role in guild.roles:
            if role.name == f"Your mute role":
                await member.remove_roles(role)
                channel2 = client.get_channel(mylogchannelid)
                embed = discord.Embed(title="Member Unmuted", description=f"Unmuted {member.mention}",
                                      color=discord.Colour.random())
                await channel2.send(embed=embed)

#EXAMPLE: mute @user 24h Spamming (Mutes user for 24 Hours)

##unmute

@client.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.mute_members:
        guild = ctx.guild

        for role in guild.roles:
            if role.name == f"Your mute role name":
                await member.remove_roles(role)
        for role in guild.roles:
            if role.name == f"Members role":
                await member.add_roles(role)
                await ctx.send(f"{member.mention} was unmuted")
                await ctx.message.delete()
                channel = client.get_channel(mylogchannelid)
                embed2 = discord.Embed(title=f"Member Unmuted", description=f"{member.mention} was unmuted",
                                       color=discord.Colour.random())
                embed2.add_field(name="Reason", value=reason, inline=False)
                now = datetime.datetime.now().strftime("%H:%M")
                embed2.set_footer(icon_url=ctx.author.avatar_url,
                                  text=f"Unmuted by {ctx.author.name}#" + ctx.author.discriminator + f'' + f" Today at | {now}")
                await channel.send(embed=embed2)


#EXAMPLE: unmute @user

##Ban (Specific time)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, time, *, reason=None):
    if ctx.author.guild_permissions.ban_members:
        guild = ctx.guild
        await guild.ban(member)
        await ctx.send(f"{member.mention} has been banned from the server!")
        await ctx.message.delete()
        channel = client.get_channel(mylogchannelid)
        embed2 = discord.Embed(title=f"Member Banned", description=f"The banned user: {member.name}",
                               color=discord.Colour.random())
        embed2.add_field(name="Time", value=time, inline=False)
        embed2.add_field(name="Reason", value=reason, inline=False)
        now = datetime.datetime.now().strftime("%H:%M")
        embed2.set_footer(icon_url=ctx.author.avatar_url,
                          text=f"Banned by {ctx.author.name}#" + ctx.author.discriminator + f'' + f" Today at | {now}")
        await channel.send(embed=embed2)
        d = time[-1]

        num = int(time[:-1])

        if d == "s":
            await asyncio.sleep(num)

        if d == "m":
            await asyncio.sleep(num * 60)

        if d == "h":
            await asyncio.sleep(num * 60 * 60)

        if d == "d":
            await asyncio.sleep(num * 60 * 60 * 24)
        await member.unban()
        channel2 = client.get_channel(mylogchannelid)
        embed = discord.Embed(title="Member Unbanned", description=f"{member.mention} was unbanned",
                              color=discord.Colour.random())
        embed.set_footer(text=f" Today at | {now}")
        await channel2.send(embed=embed)

#Example: ban @user 24h Spamming (Bans user and Unbans him after 24h, also known as 'softban')


##unban

@client.command()
async def unban(ctx, member: discord.Member):
    await member.unban()
    channel2 = client.get_channel(mylogchannelid)
    embed2 = discord.Embed(title="Member Unbanned", description=f"{member.mention} was unbanned",
                           color=discord.Colour.random())
    now = datetime.datetime.now().strftime("%H:%M")
    embed2.set_footer(text=f" Today at | {now}")
    await channel2.send(embed=embed2)

#EXAMPLE: unban @user 

##Announce

@client.command()
@commands.has_permissions(administrator=True)
async def announce(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(f"{msg}")
    channel = client.get_channel(mylogchannelid)
    embed = discord.Embed(title=f"`Say` command was used",
                          description=f"Announcement by {ctx.author.mention}: **{msg}**",
                          color=discord.Colour.random())
    now = datetime.datetime.now().strftime("%H:%M")
    embed.set_footer(text=f"Today at | {now}")
    await channel.send(embed=embed)

#EXAMPLE: announce I like cake
#Output: Announcement by @user: I like cake



