import discord
from discord.ext import tasks

client = discord.Client()

@client.event
async def on_ready():
  print("Ready!")
  auto.start()
  
@client.event
async def on_message(message):
  print(message)
  
@tasks.loop(hours=1.0)
async def auto():
  print("I'm doing something every 1 hour!")
 

client.run('TOKEN')
