@client.command()
async def poll(ctx,*,message):
   emb=discord.Embed(tile="POLL",description=f"(message}")
   msg=await ctx.channel.send(embed=emb)
   await msg.add_reaction('👆')
   await msg.add_reaction('👇')