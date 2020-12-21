import discord
from datetime import date
from discord.ext import commands
from random import randint
from random import choice
import os

a_file = open("script.txt")
lines = a_file.readlines()
today = date.today()
 
bot = commands.Bot(command_prefix = ">")

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Cat Videos"))
  print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def foo(ctx, arg):
  await ctx.send("HI")

@bot.event
async def on_message(message):

  if message.content.startswith('shrug'):
    await message.channel.send('¯\_(ツ)_/¯')

  if message.content.startswith('bot'):
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

    await bot.process_commands(message)

bot.run(os.getenv('TOKEN'))

