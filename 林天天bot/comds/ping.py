import discord
from discord.ext import commands
from core.classes import cog_Extension

class ping(cog_Extension):

 @commands.command()
 async def ping(self,ctx):
  await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

def setup(bot):
 bot.add_cog(ping(bot))