import discord
import os

illegal_words = ["apple", "pear", "banana"]

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

  if any(word in message.content for word in illegal_words):
     await message.delete()

  if message.content.startswith('hello'):
    await message.channel.send('https://cataas.com/cat/says/hello%20world!')

client.run(NzkwMTEyOTI0MzI4NTI1ODQ0.X974AA.2-B_-D2dO7vejmw4CsNIShfwdz4)

