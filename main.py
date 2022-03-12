import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  #if message.content != '225200':
    #await message.delete()
  if message.content != 'lmao':
    if message.content != 'LMAO':
      if message.content != 'Lmao':
        await message.delete()
keep_alive()
client.run(os.getenv('TOKEN'))
