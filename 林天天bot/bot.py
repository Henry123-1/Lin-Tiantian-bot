import discord
from discord.ext import commands
import json
import os
bot = commands.Bot(command_prefix='!')

with open('setting.json', 'r',encoding='utf8') as jfile:
    jdate = json.load(jfile)

@bot.event
async def on_ready():
 print(">>Bot is online<<")

@bot.command()
async def load(ctx, extensign):
 bot.load_extension(f'cmds.{extensign}')
 await ctx.send(f'loaded {extensign} done.')

@bot.command()
async def unload(ctx, extensign):
 bot.unload_extension(f'cmds.{extensign}')
 await ctx.send(f'on-loaded {extensign} done.')

@bot.command()
async def reload(ctx, extensign):
 bot.reload_extension(f'cmds.{extensign}')
 await ctx.send(f're-loaded {extensign} done.')

for filename in os.listdir('./comds'):
    if filename.endswith('.py'):
        bot.load_extension(f'comds.{filename[:-3]}')

if __name__ == "__main__":
 bot.run(jdate['TOKEN'])