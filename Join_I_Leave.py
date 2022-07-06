
                                #░░░░░██╗░█████╗░██╗███╗░░██╗  ░░░░██╗  ██╗░░░░░███████╗░█████╗░██╗░░░██╗███████╗
                                #░░░░░██║██╔══██╗██║████╗░██║  ░░░██╔╝  ██║░░░░░██╔════╝██╔══██╗██║░░░██║██╔════╝
                                #░░░░░██║██║░░██║██║██╔██╗██║  ░░██╔╝░  ██║░░░░░█████╗░░███████║╚██╗░██╔╝█████╗░░
                                #██╗░░██║██║░░██║██║██║╚████║  ░██╔╝░░  ██║░░░░░██╔══╝░░██╔══██║░╚████╔╝░██╔══╝░░
                                #╚█████╔╝╚█████╔╝██║██║░╚███║  ██╔╝░░░  ███████╗███████╗██║░░██║░░╚██╔╝░░███████╗
                                #░╚════╝░░╚════╝░╚═╝╚═╝░░╚══╝  ╚═╝░░░░  ╚══════╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝


@client.event
async def on_member_join(member):
    guild = client.get_guild() #YOUR INTEGER GUILD ID HERE
    welcome_channel = guild.get_channel() #YOUR INTEGER CHANNEL ID HERE
    await welcome_channel.send(f'Welcome to {guild.name} {member.mention} ! Enjoy your stay :partying_face:') #sends welcome message in channel
    await member.send(f'We are glad to have you in the {guild.name} Discord Server, {member.name} !  :partying_face:') #sends a message to the user via dm's. 



@client.event
async def on_member_leave(member):
    guild = client.get_guild() #YOUR INTEGER GUILD ID HERE
    leave_channel = guild.get_channel() #YOUR INTEGER CHANNEL ID HERE
    await leave_channel.send(f'So sad to see you go {member.mention} ! :cry:') #sends leave message in channel
    await member.send(f'You have left {guild.name} Discord Server. Join back any time with this link: Discord.gg/INVITELINK') #sends a message to the user via dm's. 

