import discord
from discord.ext import tasks

client = discord.Client()

@client.event
async def on_ready():
  print("Ready!")
  auto.start()

@tasks.loop(hours=1.0)
async def auto():
  print("I'm doing somthing every 1 hour!")

client.run('TOKEN')
