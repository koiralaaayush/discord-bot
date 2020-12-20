import discord
from discord.ext import commands
from random import randint
import os

illegal_words = ["bitch", "ass", "fuck"]

PREFIX = ("$")
bot = commands.Bot(command_prefix=PREFIX, description='BeepBoop')


@bot.event
async def on_ready():
  activity = discord.Game(name="Just")
  await bot.change_presence(status=discord.Status.idle, activity=activity)

@bot.event
async def on_message(message):

  if message.author == bot.user:
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

bot.run(os.getenv('TOKEN'))

