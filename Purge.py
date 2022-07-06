@client.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx, *, amount=200000000000):
    guild = ctx.guild
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(title=f"Nuked Successfully!", description=f" Cleard {amount}",
                          color=discord.Color((0xe74c3c)))
    embed.set_image(url="Image")
    now = datetime.datetime.now().strftime("%H:%M")
    embed.set_footer(text=f"Today at | {now}")
    await ctx.send(embed=embed)
    channel = client.get_channel(mylogchannelid)
    embed2 = discord.Embed(title=f"Channel nuked", description=f"{ctx.author.mention} Cleard messages",
                           color=discord.Colour.random())
    embed2.add_field(name="Cleard messages", value=amount, inline=False)
    embed2.add_field(name="Channel", value=channel.mention, inline=False)
    await channel.send(embed=embed2)
