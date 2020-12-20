import discord
from discord.ext import commands
from random import randint
import os

illegal_words = ["bitch", "ass", "fuck"]

client = discord.Client()


@client.event
async def on_ready():
  await client.change_presense(status=discord.Status.online, activity = discord.Activity(type = discord.ActivityType.watching, name ="Cat Vidoes"))
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

  if message.author == client.user:
    return

  if message.content.startswith('shrug'):
    await message.channel.send('¯\_(ツ)_/¯')

  if message.content.startswith('ping'):
    await message.channel.send('pong')

  if message.content.startswith('!randomnum'):
    await message.channel.send(randint(0, 1000))

  if any(word in message.content for word in illegal_words):
     await message.delete()

  if message.content.startswith('hello'):
    await message.channel.send('https://cataas.com/cat/says/hello%20world!')

client.run(os.getenv('TOKEN'))

