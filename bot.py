import discord
from datetime import date
from discord.ext import commands
from random import randint
from random import choice
import os

a_file = open("script.txt")
lines = a_file.readlines()
today = date.today()
 
client = commands.Bot(command_prefix = ">")

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Cat Videos"))
  print('We have logged in as {0.user}'.format(client))

@client.command()
async def test(ctx):
  await ctx.scend("123")

@client.event
async def on_message(message):

  if message.content.startswith('shrug'):
    await message.channel.send('¯\_(ツ)_/¯')

  if message.content.startswith('client'):
    await message.channel.send('How can I help you today?')

  if message.content.startswith('today'):
    await message.channel.send(today)

  if message.content.startswith('beemovie'):
    for line in lines:
      await message.channel.send(line)
      a_file. close()           

  if message.content.startswith('!randomnum'):
    await message.channel.send(randint(0, 1000))

  if message.content.startswith('hello'):
    await message.channel.send('https://cataas.com/cat/says/hello%20world!')

    await client.process_commands(message)

client.run(os.getenv('TOKEN'))

