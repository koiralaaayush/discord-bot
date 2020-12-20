import discord
from discord.ext import commands
from random import randint
import os

illegal_words = ["bitch", "ass", "fuck"]

bot = commands.Bot(command_prefix="$", description='BeepBoop')

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Cat Videos"))
  print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):

  if message.author == bot.user:
    return

  if message.content.startswith('shrug'):
    await message.channel.send('¯\_(ツ)_/¯')

  if message.content.startswith('LOL'):
    await message.channel.send('Stop it!')

  if message.content.startswith('l0l'):
    await message.channel.send('Stop it!')

  if message.content.startswith('GG'):
    await message.channel.send('Stop it!')

  if message.content.startswith('WTF'):
    await message.channel.send('Stop it!')

  if message.content.startswith('op'):
    await message.channel.send('Stop it!')

  if message.content.startswith('OP'):
    await message.channel.send('Stop it!')            

  if message.content.startswith('!randomnum'):
    await message.channel.send(randint(0, 1000))

  if any(word in message.content for word in illegal_words):
     await message.delete()

  if message.content.startswith('hello'):
    await message.channel.send('https://cataas.com/cat/says/hello%20world!')

bot.run(os.getenv('TOKEN'))

