import discord
from discord.enums import SpeakingState
from discord.ext import commands
from discord.ext.commands import bot
from core.classes import cog_Extension

class ping(cog_Extension):

 @commands.command()
 async def test(self, ctx):
  channel = bot.get_channel(896414728178516031)
  await channel.send("傻逼呆蛙们明天武统")

def setup(bot):
 bot.add_cog(speak(bot))