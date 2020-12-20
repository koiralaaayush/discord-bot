import discord
import os

illegal_words = ["bitch", "ass", "fuck"]

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('shrug'):
    await message.channel.send('¯\_(ツ)_/¯')

  if message.content.startswith('ping'):
    await message.channel.send('pong')

  if any(word in message.content for word in illegal_words):
     await message.delete()

  if message.content.startswith('hello'):
    await message.channel.send('https://cataas.com/cat/says/hello%20world!')

client.run(os.getenv('TOKEN'))

