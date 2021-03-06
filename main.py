import os

my_secret = os.environ['token']
import asyncio
import datetime
import json
import os
import random
import urllib
from random import randint
import functools
import itertools
import math
import youtube_dl
from async_timeout import timeout

import youtube_dl
import requests
from datetime import date
from discord.ext import tasks
from io import BytesIO
from PIL import Image
from discord import Spotify, reaction
import discord
from discord import Embed, message
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
from dotenv import load_dotenv
from replit import db
from keep_alive import keep_alive
import time

youtube_dl.utils.bug_reports_message = lambda: ''
start_time = time.time()
startdate = datetime.datetime.now()


# @bot.event
# async def on_ready():
#     startdate = datetime.datetime.now()

user = discord.User
member = discord.Member



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="$",description='A Simple, Yet Complex Bot!')

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

async def add_blacklist(message):


  if message.content.startswith('Block List'):
      sureee = await message.guild.fetch_member(message.raw_mentions[0])


      with open("blacklist.txt", "r") as i:
          lines = i.read().splitlines()

          if (str(sureee.id) not in lines):
              with open('blacklist.txt', 'a+', encoding='utf-8') as i:
                  i.write(str(sureee.id) + "\n")
                  await message.channel.send('User Block Listed - ' + str(sureee.display_name))
          else:
              await message.channel.send('User already Block Listed - ' + str(sureee.display_name))

  if message.content.startswith('Allow'):
      sureeee = await message.guild.fetch_member(message.raw_mentions[0])
      lines = []
      with open("blacklist.txt", "r") as f:
          lines = f.read().splitlines()

      with open("blacklist.txt", "w") as f:
          for line in lines:
              if line.strip("\n") != f"{sureeee.id}":
                  f.write(line)
                  await message.channel.send(f'{sureeee.mention} has been enabled via bot commands')


async def update_levels_txt(message):
    levels = []
    # Open levels.txt in read-only mode and Read all lines
    with open('Levels.txt', 'r', encoding='utf-8') as q:
        levels = q.read().splitlines()

    # declare a boolean variable named something like user_id_found = False
    user_id_is_here = False
    # Open levels.txt in write mode
    with open('Levels.txt', 'w', encoding='utf-8') as q:
        # Iterate over the lines read from file
        for line in levels:
            # If a line starts with message author id
            if line.startswith(str(message.author.id)):
                # set the value of user_id_found = True
                user_id_is_here = True
                # split the line seperated by comma in to author id and message count
                (user_id, msg_count) = line.split(',')
                # write user id and message count + 1 to levels.txt with a comma between them
                q.write(user_id + "," + str(int(msg_count)+1) + "\n")

            else:
              # write line in to levels.txt
              q.write(line + "\n")

        # if user_id_found = False
        if user_id_is_here is False:
            # write user id and message count of 1 to levels.txt with a comma between them
            q.write(str(message.author.id) + ",1" + "\n")




@bot.event
async def on_message(message):
  await add_blacklist(message)
  with open("blacklist.txt", "r") as f:
    lines = f.read().splitlines()

  await update_levels_txt(message)

  msg_count = 1
  with open('Levels.txt', 'r', encoding='utf-8') as q:
      try:
          for line in q:
              if line.startswith(str(message.author.id)):
                  (user_id, msg_count) = line.split(',')
      except Exception as e:
          print(e)

  msg_count = int(msg_count)
  if (msg_count == 10):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 2!')
  elif (msg_count == 20):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 3!')
  elif (msg_count == 40):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 4!')
  elif (msg_count == 60):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 5!')
  elif (msg_count == 80):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 6!')
  elif (msg_count == 100):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 7!')
  elif (msg_count == 200):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 8!')
  elif (msg_count == 300):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 9!')
  elif (msg_count == 350):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 10!')
  elif (msg_count == 400):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 11!')
  elif (msg_count == 500):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 12!')
  elif (msg_count == 750):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 13!')
  elif (msg_count == 1000):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 14!')
  elif (msg_count == 2000):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 15!')
  elif (msg_count == 2150):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 16!')
  elif (msg_count == 2300):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 17!')
  elif (msg_count == 2350):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 18!')
  elif (msg_count == 2500):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 19!')
  elif (msg_count == 2750):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 20!')
  elif (msg_count == 3000):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 21!')
  elif (msg_count == 3500):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 22!')  
  elif (msg_count == 4000):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 23!')
  elif (msg_count == 5000):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 24!')
  elif (msg_count == 6000):
      await message.channel.send(f'{message.author.mention} has leveled up to Level 25!')         


  if message.content == '$uptime':
    now = datetime.datetime.now()
    uptime = now - startdate 
    # uptime = uptime.strftime('%d/%h/%M')
    await message.channel.send(f'Uptime: {uptime}')




  if message.content.startswith('$add'):
      variables = message.content.strip().split(' ')
      num1 = int(variables[1])
      num2 = int(variables[2])
      await message.channel.send(num1 + num2)

  if message.content.startswith('$multiply'):
      variables = message.content.strip().split(' ')
      num1 = int(variables[1])
      num2 = int(variables[2])
      await message.channel.send(num1 * num2)

  if message.content.startswith('$divide'):
      variables = message.content.strip().split(' ')
      num1 = int(variables[1])
      num2 = int(variables[2])
      await message.channel.send(num1 / num2)

  if message.content.startswith('$sub'):
      variables = message.content.strip().split(' ')
      num1 = int(variables[1])
      num2 = int(variables[2])
      await message.channel.send(num1 - num2)


  if message.content.startswith('$ban'):
      for userRole in message.author.roles:
          if userRole.name == 'Admin':
              whyyyyy = await message.guild.fetch_member(message.raw_mentions[0])
              message_array101010011111 = message.content[28:]
              guild = message.guild
              await message.guild.ban(await bot.fetch_user(message.raw_mentions[0]),
                                      reason=message_array101010011111[2])
              await message.channel.send(f'A member has been banned for {message_array101010011111}')
              await whyyyyy.send(f'{whyyyyy.mention} You have been banned from {guild} for the reason: {message_array101010011111}')


  if message.content.startswith('$Poll'):

      hasPollRole = False
      for userRole in message.author.roles:
          if userRole.name == 'Owner':
              hasPollRole = True

      if (hasPollRole):

          message_array10 = message.content[27:]
          HAHAHA = message.guild.get_channel(message.raw_channel_mentions[0])

          embed = discord.Embed(title="A Poll Has Been Created!", description="Please react with the reaction of your choice")
          embed.add_field(name="Poll:", value=f'```{message_array10}```')
          embed.colour=discord.embeds.Colour.random()
          embed.set_footer(
          text="Poll created by: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
          icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
          await message.channel.purge(limit=1)
          await HAHAHA.send(content=None, embed=embed, )
      else:
          embed = discord.Embed(title="Error", description="Error")
          embed.add_field(name="You lack the required permissions:", value=f'Missing permissions')
          embed.colour=discord.embeds.Colour.dark_red()
          embed.set_footer(
          text="Error: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
          icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
          await message.channel.send(content=None, embed=embed, )


  if message.content == '$random number':
      await message.channel.send(f'This is your random number {random.randrange(100000)}')

  if message.content == '$Support':
      await message.channel.send(f'Click here to join the support server: https://discord.gg/avknX8v7X7')

  if message.content.startswith('$mute'):

      message_array2 = message.content[28:]

      # guild = bot.get_guild(839567563544461372)
      mbr = await message.guild.fetch_member(message.raw_mentions[0])

      guild = message.guild
      mutedRole = discord.utils.get(mbr.roles, name='Muted')


      hasPnerRole = False
      for userRole in message.author.roles:
          if userRole.name == 'Admin':
              hasPnerRole = True
      if (hasPnerRole):

          if not mutedRole:
              try:
                  mutedRole = await guild.create_role(name="Muted")
              except Exception as e:
                  print(e)

          for channel in guild.channels:
              # await message.channel.send("No muted role has been found. Creating role...")
              await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True,
                                            read_messages=False)
          await mbr.add_roles(mutedRole)
          await message.channel.send(f"Muted {mbr.mention} for reason {message_array2}")
          await mbr.send(f"You were muted in the server {guild.name} for {message_array2}")
          await asyncio.sleep(600)
          await mbr.remove_roles(mutedRole)
          await message.channel.send(f"You were unmuted by the system! {mbr.mention}. ")
          await mbr.send(f"You were unmuted in the server {guild.name}")
      else:
          embed = discord.Embed(title="You lack the permissions to do this command", description="Error")
          embed.add_field(name="Error:", value=f'Missing permissions')
          embed.colour=discord.embeds.Colour.red()
          embed.set_footer(
          text="Error: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
          icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
          await message.channel.send(content=None, embed=embed, )

  if message.content.startswith('$Nick'):
      message_array5 = message.content[28:]
      oka = await message.guild.fetch_member(message.raw_mentions[0])
      guild = message.guild
      hasAnerRole = False
      for userRole in message.author.roles:
          if userRole.name == 'Admin':
              hasAerRole = True

      if (hasAnerRole):
          await oka.edit(member=oka, nick=message_array5)
          await message.channel.send(f"Changed {oka.mention}  Nickname.")
          await oka.send(f"Your nickname was changed in a server: {guild.name} for {message_array5}")
      else:
          embed = discord.Embed(title="You lack the permissions to do this command", description="Error")
          embed.add_field(name="Error:", value=f'Missing permissions')
          embed.colour=discord.embeds.Colour.red()
          embed.set_footer(
          text="Error: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
          icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
          await message.channel.send(content=None, embed=embed, )

  if message.content.startswith('$slowmode'):
      # message_array6 = message.content[12:]
      huh = message.guild.get_channel(message.raw_channel_mentions[0])
      time = message.content[32:]
      # huh = discord.utils.get(message.raw_channel_mentions[0])
      guild = message.guild
      # seconds = 5
      haNickRole = False
      for userRole in message.author.roles:
          if userRole.name == 'Admin':
              haNickRole = True

      if (haNickRole):

          await huh.edit(slowmode_delay=time)
          await message.channel.send(f'Slow mode has been enabled! Channel: {huh} for {time} seconds.')
      else:
          embed = discord.Embed(title="You lack the permissions to do this command", description="Error")
          embed.add_field(name="Error:", value=f'Missing permissions')
          embed.colour=discord.embeds.Colour.red()
          embed.set_footer(
          text="Error: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
          icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
          await message.channel.send(content=None, embed=embed, )


  if message.content == '$Delete channel':
      for userRole in message.author.roles:
          if userRole.name == 'Moderator':
              await message.channel.delete()



  if message.content.startswith('$unmute'):

      message_array3 = message.content[30:]

      # guild = bot.get_guild(839567563544461372)
      mrb = await message.guild.fetch_member(message.raw_mentions[0])

      guild = message.guild
      mutedRole = discord.utils.get(mrb.roles, name='Muted')
      haUickRole = False
      for userRole in message.author.roles:
          if userRole.name == 'Admin':
              haUickRole = True


      if (haNickRole):

          await mrb.remove_roles(mutedRole)
          # await member.add_roles(mutedRole)
          await message.channel.send(f"unmuted {mrb.mention} for reason {message_array3}")
          await mrb.send(f"You were unmuted in the server {guild.name} for {message_array3}")
      else:
          embed = discord.Embed(title="You lack the permissions to do this command", description="Error")
          embed.add_field(name="Error:", value=f'Missing permissions')
          embed.colour = discord.embeds.Colour.red()
          embed.set_footer(
              text="Error: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
              icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
          await message.channel.send(content=None, embed=embed, )





  if message.content.startswith('$Purge'):
      hasidkROle = False
      for userRole in message.author.roles:
          if userRole.name == 'Admin':
              hasidkROle = True


      if (hasidkROle):
          amount = int(message.content[7:])
          await message.channel.purge(limit=amount)
          await message.channel.send(f'I have deleted {amount} messages')
          await asyncio.sleep(5)
          await message.channel.purge(limit=1)
      else:
          embed = discord.Embed(title="You lack the permissions to do this command", description="Error")
          embed.add_field(name="Error:", value=f'Missing permissions')
          embed.colour = discord.embeds.Colour.red()
          embed.set_footer(
              text="Error: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
              icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
          await message.channel.send(content=None, embed=embed, )


  msg = message.content
  badwords = ["hell", "stupid", "jerk", "gang", "idiot", "frick"]
  if any(word in msg for word in badwords):
      msg_array2 = message.content[29:]
      guild = message.guild
      bob = message.author

      mutedRole = discord.utils.get(message.author.roles, name='Muted')
      embed = discord.Embed(title=f"{message.author} (ID {message.author.id})")
      embed.set_image(url=message.author.avatar_url)
      embed.add_field(name="**Muted**", value=f':mute: Muted **{message.author.display_name}** (ID {message.author.id})')
      embed.add_field(name="**Reason**", value=f":page_facing_up: **Reason**: AutoModerator: A bad word trigger was fired. This word is banned!")
      embed.add_field(name="**Message**", value=f"{message.content}")
      # msg1 = msg.split("hell", "stupid", "jerk", "gang", "idiot", "frick"
      embed.colour = discord.embeds.Colour.light_grey()
      embed.set_footer(text="Duration: 10 minutes")
      await message.channel.send(content=None, embed=embed)








  if message.content.startswith('$Remind'):
      guild = message.guild
      message_array11 = int(message.content[8:])
      await message.channel.send(f"Hello {message.author.name} you will be reminded in {message_array11} seconds.")
      await asyncio.sleep(message_array11)
      await message.channel.send(f'You are being reminded {message.author.mention}')

  if message.content.startswith('$Server info'):
      owner = str(message.guild.owner)
      id = str(message.guild.id)
      region = str(message.guild.region)
      memberCount = str(message.guild.member_count)
#Type Server info to see the info
      icon = str(message.guild.icon_url)
      rules = str(message.guild.rules_channel)
      verification_level = message.guild.verification_level

      embed = discord.Embed(title=f"Guild info", description=f"{message.guild.name}, {id}")
      embed.add_field(name=f"{message.guild.name} was created at:", value=f'{message.guild.created_at}')
      embed.add_field(name=f"{message.guild.name} verification level:", value=f'{verification_level}')
      embed.add_field(name=f"{message.guild.name} rules channel:", value=f'{rules}')
      embed.add_field(name=f"{message.guild.name} was created at:", value=f'{message.guild.created_at}')
      embed.add_field(name=f"{message.guild.name}'s owner is:", value=f'{owner}')
      embed.add_field(name=f"{message.guild.name} has this many members", value=f'{memberCount}')
      embed.add_field(name=f"{message.guild.name} is residented in", value=f'{region}')
      embed.set_footer(
          text="Asked by: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
          icon_url=icon)  # + " " + datetime.datetime.utcnow())
      await message.channel.send(content=None, embed=embed)


  if message.content == '$Hack':
      mes12 = await message.channel.send("The hacking process has beginning in 5")
      await asyncio.sleep(1)
      await mes12.edit(content="The hacking process has beginning in 4")
      await asyncio.sleep(1)
      await mes12.edit(content="The hacking process has beginning in 3")
      await asyncio.sleep(1)
      await asyncio.sleep(1)
      await mes12.edit(content="The hacking process has beginning in 2")
      await asyncio.sleep(1)
      await mes12.edit(content="The hacking process has beginning in 1")
      await asyncio.sleep(1)
      await mes12.edit(content="Going through history. How to protect against hackers found.")
      await asyncio.sleep(2)
      await mes12.edit(content="Installing Core Operating System.VIRUS")
      await asyncio.sleep(2)
      await mes12.edit(content="Deleting anti hacking internal systems")
      await asyncio.sleep(2)
      await mes12.edit(content="Email comprimised")
      await asyncio.sleep(2)
      await mes12.edit(content="Locating IP Address.")
      await asyncio.sleep(1)
      await mes12.edit(content="Locating IP Address..")
      await asyncio.sleep(1)
      await mes12.edit(content="Locating IP Address...")
      await asyncio.sleep(1)
      await mes12.edit(content="IP Address located. 169.173.207.1")
      await asyncio.sleep(1)
      await mes12.edit(content="Sending military unit 1 to 169.173.207.1.")
      await asyncio.sleep(1)
      await mes12.edit(content="Extraction at 24%")
      await asyncio.sleep(2)
      await mes12.edit(content="Extraction at 52%")
      await asyncio.sleep(2)
      await mes12.edit(content="Extraction at 77%")
      await asyncio.sleep(2)
      await mes12.edit(content="Extraction at 91%")
      await asyncio.sleep(2)
      await mes12.edit(content="Extraction at 100%")
      await asyncio.sleep(3)
      await mes12.edit(content="Hack complete.")
      await asyncio.sleep(5)
      await mes12.edit(content="https://tenor.com/view/traffic-fbi-open-up-raid-gif-13450966")


  if message.content.startswith('$Give'):
      AP = await message.guild.fetch_member(message.raw_mentions[0])
      BP = message.guild.get_role(message.raw_role_mentions[0])
      guild = message.guild

      ModRole = False
      for userRole in message.author.roles:
          if userRole.name == 'Moderator':
              ModRole = True

              if (ModRole):
                  await AP.add_roles(BP)
                  await message.channel.send(f'Role given to {AP.mention} Added role: {BP.name}')
              else:
                  embed = discord.Embed(title="You lack the permissions to do this command", description="Error")
                  embed.add_field(name="Error:", value=f'Missing permissions')
                  embed.colour = discord.embeds.Colour.red()
                  embed.set_footer(
                      text="Error: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
                      icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
                  await message.channel.send(content=None, embed=embed, )

  if message.content.startswith('$Remove'):
      CP = await message.guild.fetch_member(message.raw_mentions[0])
      DP = message.guild.get_role(message.raw_role_mentions[0])
      guild = message.guild

      # memberRole = discord.utils.get(guild.roles, name='Member')

      for userRole in message.author.roles:
          if userRole.name == 'Moderator':
              await CP.remove_roles(DP)
              # await message.channel.send(f'Role given to {AP.display_name}')
              await message.channel.send(f'Role removed from {CP.mention} Removed Role: {DP.name}')





  valid_users = ["Cosmic Dorito ????#4930"]

  if str(message.author) in valid_users:
      if message.content.startswith('$Stream'):
          # userRole1 = discord.utils.get(message.author.roles, name='Owner')
              message_array14 = message.content[7:]
              mes13 = await message.channel.send("Changing bot status")
              await mes13.edit(content="Changing bot status.")
              await asyncio.sleep(1.5)
              await mes13.edit(content="Changing bot status..")
              await asyncio.sleep(1.5)
              await mes13.edit(content="Changing bot status...")
              await asyncio.sleep(1.5)
              await mes13.edit(content="Process completed!")
              await bot.change_presence(activity=discord.Streaming(name=f'{message_array14}', url='https://www.twitch.tv/cosmic_tostilla_101'))


  if str(message.author) not in valid_users:
      if message.content.startswith('$Stream'):
              embed = discord.Embed(title="You lack the permissions to do this command", description="Error")
              embed.add_field(name="Error:", value=f'Missing permissions')
              embed.colour = discord.embeds.Colour.dark_red()
              embed.set_footer(
                  text="Error: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
                  icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
              await message.channel.send(content=None, embed=embed, )


  if str(message.author) in valid_users:
      if message.content.startswith('$Status'):
          # userRole1 = discord.utils.get(message.author.roles, name='Owner')
              message_array18 = message.content[8:]
              mes16 = await message.channel.send("Changing bot status")
              await mes16.edit(content="Changing bot status.")
              await asyncio.sleep(1.5)
              await mes16.edit(content="Changing bot status..")
              await asyncio.sleep(1.5)
              await mes16.edit(content="Changing bot status...")
              await asyncio.sleep(1.5)
              await mes16.edit(content="Process completed!")
              await bot.change_presence(activity=discord.Game(f'{message_array18}'))

  if str(message.author) not in valid_users:
      if message.content.startswith('$Status'):
              embed = discord.Embed(title="You lack the permissions to do this command", description="Error")
              embed.add_field(name="Error:", value=f'Missing permissions')
              embed.colour = discord.embeds.Colour.dark_red()
              embed.set_footer(
                  text="Error: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
                  icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
              await message.channel.send(content=None, embed=embed, )


  if str(message.author) in valid_users:
      if message.content.startswith('$Status Watching'):
          # userRole1 = discord.utils.get(message.author.roles, name='Owner')
              message_array19 = message.content[17:]
              mes15 = await message.channel.send("Changing bot status")
              await mes15.edit(content="Changing bot status.")
              await asyncio.sleep(1.5)
              await mes15.edit(content="Changing bot status..")
              await asyncio.sleep(1.5)
              await mes15.edit(content="Changing bot status...")
              await asyncio.sleep(1.5)
              await mes15.edit(content="Process completed!")
              await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{message_array19}'))

  if str(message.author) not in valid_users:
      if message.content.startswith('$Status Watching'):
              embed = discord.Embed(title="You lack the permissions to do this command", description="Error")
              embed.add_field(name="Error:", value=f'Missing permissions')
              embed.colour = discord.embeds.Colour.dark_red()
              embed.set_footer(
                  text="Error: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
                  icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
              await message.channel.send(content=None, embed=embed, )



  if str(message.author) in valid_users:
      if message.content.startswith('$Status listening'):
          # userRole1 = discord.utils.get(message.author.roles, name='Owner')
              message_array20 = message.content[18:]
              mes14 = await message.channel.send("Changing bot status")
              await mes14.edit(content="Changing bot status.")
              await asyncio.sleep(1.5)
              await mes14.edit(content="Changing bot status..")
              await asyncio.sleep(1.5)
              await mes14.edit(content="Changing bot status...")
              await asyncio.sleep(1.5)
              await mes14.edit(content="Process completed!")
              await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{message_array20}'))

  if str(message.author) not in valid_users:
      if message.content.startswith('$Status listening'):
              embed = discord.Embed(title="You lack the permissions to do this command", description="Error")
              embed.add_field(name="Error:", value=f'Missing permissions')
              embed.colour = discord.embeds.Colour.dark_red()
              embed.set_footer(
                  text="Error: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
                  icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
              await message.channel.send(content=None, embed=embed, )

  if str(message.author) in valid_users:
      if message.content.startswith('$Status competing'):
          # userRole1 = discord.utils.get(message.author.roles, name='Owner')
              message_array20 = message.content[18:]
              mes17 = await message.channel.send("Changing bot status")
              await mes17.edit(content="Changing bot status.")
              await asyncio.sleep(1.5)
              await mes17.edit(content="Changing bot status..")
              await asyncio.sleep(1.5)
              await mes17.edit(content="Changing bot status...")
              await asyncio.sleep(1.5)
              await mes17.edit(content="Process completed!")
              await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{message_array20}'))

  if str(message.author) not in valid_users:
      if message.content.startswith('$Status listening'):
              embed = discord.Embed(title="You lack the permissions to do this command", description="Error")
              embed.add_field(name="Error:", value=f'Missing permissions')
              embed.colour = discord.embeds.Colour.dark_red()
              embed.set_footer(
                  text="Error: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
                  icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
              await message.channel.send(content=None, embed=embed, )


  if message.content == '$help':

      embed = discord.Embed(title="Spirit Help Command!", description="Help Command")
      embed.add_field(name="Moderation", value='Type ```$help moderation``` to trigger the help command')
      embed.add_field(name="Audit-Log", value='Type ```$help audit``` to trigger the help command')
      embed.add_field(name="Fun", value='Type ```$help fun``` to trigger the help command')
      embed.add_field(name="Modmail", value='Type ```$help modmail``` to trigger the help command')
      embed.add_field(name="Slash commands", value='Type ```/``` to view the bots slash command!')
      embed.add_field(name="General", value='Type ```$help general``` to trigger the help command!')
      embed.add_field(name="Giveaways", value='Type ```$help giveaways``` to trigger the giveaway help command!')
      embed.colour = discord.embeds.Colour.random()

      embed.set_footer(
          text="Help requested by: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
          icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
      await message.channel.send(content=None, embed=embed)

  if message.content == '$info':


      embed = discord.Embed(title="Shard stuff", description="Idk")
      embed.add_field(name="Shard_count", value=f'{str(bot.shard_count)}')
      embed.add_field(name="Shard id", value=f'{bot.shard_id}')
      # embed.add_field(name="Shard id", value=f'{bot.activity.name}')
      embed.add_field(name="Shard id", value=f'{bot.owner_id}')
      embed.add_field(name="Shard id", value=f'{bot.application_info()}')
      embed.add_field(name="Is bot ratelimited", value=f'{bot.is_ws_ratelimited()}')
      # embed.add_field(name="Modmail", value='Type ```$help modmail``` to trigger the help command')
      # embed.add_field(name="Slash commands", value='Type ```/``` to view the bots slash command!')
      # embed.add_field(name="General", value='Type ```$help general``` to trigger the help command!')
      embed.colour = discord.embeds.Colour.random()

      embed.set_footer(
          text="Help requested by: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
          icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
      await message.channel.send(content=None, embed=embed)

  if message.content == '$help moderation':


      embed = discord.Embed(title="Spirit Help Admin/moderator Commands!", description="Moderation")
      embed.add_field(name="$mute", value='```$mute [user] [reason].``` If you do not unmute the user with [$unmute [user] [reason], Then it will auto unmute after 10 minutes.')
      embed.add_field(name="$Nick", value='```$Nick [user] [new-nickname]```  This gives a user a new server nickname')
      embed.add_field(name="$Purge", value='```$Purge```, To delete 10 messages at a time in txt channel. ')
      embed.add_field(name="$slowmode", value='```Type `$slowmode [#channel-name]```  This is a command to enable only 5 seconds slow mode onto a channel.')
      embed.add_field(name="$kick", value='```$kick [@user] [reason]```  Use this command to kick members. ')
      embed.add_field(name="$warn", value='```$warn [user] [reason]``` to trigger warn a user.')
      embed.colour = discord.embeds.Colour.random()

      embed.add_field(name="Requirements", value='Must have ```Administrator``` Permissions. ')
      embed.set_footer(
          text="Help requested by: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
          icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
      await message.channel.send(content=None, embed=embed)

  if message.content == '$help general':


      embed = discord.Embed(title="Spirit Help General Commands!", description="General commands")
      embed.add_field(name="$Remind", value='```$Remind [Amount (In seconds)].``` A General reminder command.')
      embed.add_field(name="$Poll", value='```$Poll [question]``` This will help collect data in your server ')
      embed.add_field(name="$User info", value='```$User info [@mention]```, Gets information about a user ')
      embed.add_field(name="$Server info", value='```Type $Server info``` Gets some kinda- helpful server info')
      embed.add_field(name="$Invite", value='```$Invite``` Sends a Dm containing the link to invite')
      # embed.add_field(name="$Support", value='```$Support``` This is to get support for the bot')
      embed.add_field(name="$new", value='```$new``` this is ONLY if you have a question.')
      embed.add_field(name="$Close", value='```$Close``` Use this basic command to Close a ticket')
      # embed.add_field(name="$Invite", value='```$Invite``` do this to invite the bot')
      embed.add_field(name="$Support", value='```$Support``` to get the invite link to the support server')
      embed.colour = discord.embeds.Colour.random()

      embed.add_field(name="$new", value='```$reply``` This is the reply to a users $new command.')
      embed.set_footer(
          text="Help requested by: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
          icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
      await message.channel.send(content=None, embed=embed)


  if message.content == '$help audit':


      embed = discord.Embed(title="Spirit Help Audit Command!", description="Audit Commands")
      embed.add_field(name="On_message_events", value='Type ```$Audit-log``` to trigger the list of events it responds to')
      embed.colour = discord.embeds.Colour.random()
      embed.add_field(name="Requirements", value='Must have a channel called ```audit-log``` ')
      embed.set_footer(
          text="Help requested by: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
          icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
      await message.channel.send(content=None, embed=embed)

  if message.content == '$help modmail':


      embed = discord.Embed(title="Spirit Help Modmail Command!", description="Modmail Commands")
      embed.add_field(name="Modmail", value='DM the bot with your question.')
      embed.add_field(name="Requirements", value='Must have a channel called ```Modmail``` ')
      embed.colour = discord.embeds.Colour.random()
      embed.set_footer(
          text="Help requested by: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
          icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
      await message.channel.send(content=None, embed=embed)

  if message.content == '$Audit-log':

      embed = discord.Embed(title="Audit-events", description="List of events bot audit-log responds to.")
      embed.add_field(name="Events:", value='```On_message_events``` ```On_member_join``` ```on_member_remove``` ```on_message_edit``` ```on_message_delete``` ```on_guild_channel_create``` ```on_guild_channel_delete``` ```on_guild_channels_pins_update``` ```on_webhook_update``` ```on_invite_create``` ```on_role_create``` ```on_role_delete``` ```on_role_update``` ')
      embed.colour = discord.embeds.Colour.random()

      embed.set_footer(
          text="Help requested by: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
          icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
      await message.channel.send(content=None, embed=embed)

  if message.content == '$help fun':


      embed = discord.Embed(title="Spirit Help Fun Command!", description="Fun")
      embed.add_field(name="$random number", value='```$random number``` to pick a number with in a range of 100,000')
      embed.add_field(name="$Math", value='```$add [num1] [num2]```, ```$sub [num1] [num2]```, ```multiply [num1] [num2]```, ```divide [num1] [num2]```')
      embed.add_field(name="Who am I", value='```Who am I```, Well it says who you are! ')
      embed.add_field(name="$ping", value='```$ping```  Finds the bots latency')
      embed.colour = discord.embeds.Colour.random()
      embed.set_footer(
          text="Help requested by: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
          icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
      await message.channel.send(content=None, embed=embed)

  if message.content.startswith("$say"):
      owner101 = str(message.author)
      message_array16 = message.content[5:]
      await message.channel.send(f'{message_array16} \n \n -{owner101}')

  if message.content.startswith('$Imagine'):
      ownerte = str(message.author)
      message_array17 = message.content[9:]
      await message.channel.send(f'Imagine a {message_array17} \n \n {ownerte} is trying really hard to imagine a {message_array17}')


  if message.content == '$Typing':
      typing = message.channel.trigger_typing()
      await typing
      await message.channel.send('I WAS TYPING')



  if message.content.startswith('$help giveaways'):
      embed = discord.Embed(title="Giveaways help command", description="Help On Command Giveaway")
      embed.add_field(name="Command:", value=f'```$Gstart [seconds] [Giveaway Prize]```')
      embed.add_field(name="Warning!:", value=f'The Giveaway Mechanism Is Complex, If you have a giveaway lasting less that 10 seconds: ```$Gstart 5     [Giveaway Prize]```. \n If you have a giveaway lasting 10-99 seconds: ```$Gstart 50    [Giveaway Prize]``` \n If you have a giveaway lasting 100-999 seconds: ```$Gstart 500   [Giveaway Prize]``` \n If you have a giveaway lasting 1000-9999 seconds: ```$Gstart 5000  [Giveaway Prize]``` \n If you have a giveaway lasting 10000-99999 seconds: ```$Gstart 50000 [Giveaway Prize]``` \n')
      embed.add_field(name="Please note:", value=f'The Lines Above The 5, 50, 500, 5000, 50000. Can be customized to any number which has the same amount of digits.')
      embed.add_field(name="Requirements:", value=f'Must have a role named Giveaways. Assigned to giveaway creator')

      embed.colour = discord.embeds.Colour.red()
      embed.set_footer(
          text="Giveaway HELP: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
          icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
      await message.channel.send(content=None, embed=embed, )

  if message.content.startswith('$Gstart'):

      giveaway = False
      for userRole in message.author.roles:
          if userRole.name == 'Giveaways':
              giveaway = True
      if (giveaway):
          channel99 = discord.utils.get(message.author.guild.channels, name='giveaways')
          time10101 = int(message.content[8:13])

          message_array21 = message.content[14:]
          embed = discord.Embed(title=f"Giveaway", description=f"A Giveaway Has Been Created")
          embed.add_field(name=f"{message_array21}", value=f'Giveaway Duration: {time10101} Seconds.')
          embed.set_footer(
              text="Giveaway Creator " + message.author.display_name + " at " + str(datetime.datetime.utcnow()), icon_url=message.author.avatar_url)
          # await channel99.send(content=None, embed=embed)
          message10101010 = await channel99.send(content=None, embed=embed)
          await message10101010.add_reaction(":Giveaway: 847253991284146238")
          await asyncio.sleep(time10101)
          guild = message.guild
          memberList = guild.members
          Giveaway_Pick = random.choice(memberList)
          message_array21 = message.content[14:]
          embed = discord.Embed(title=f"The Giveaway for {message_array21} is over!", description=f"GIVEAWAY ENDED")
          embed.add_field(name=f"{message_array21}", value=f'The winner is {Giveaway_Pick}   :tada:')
          embed.set_footer(text="Giveaway Ended " + " at " + str(datetime.datetime.utcnow()))
          await message10101010.edit(content=None, embed=embed)
          # mehhh = await message.guild.fetch_member(message.raw_mentions[0])
          webhook = await message.channel.create_webhook(name="Giveaway Winner Bot")
          await webhook.send(str(f" {Giveaway_Pick} HAS WON {message_array21}!  :tada: "), username="Giveaway Winner Bot", avatar_url="https://cdn2.iconfinder.com/data/icons/bots-monochrome/280/9-512.png")

          webhooks = await message.channel.webhooks()
          for webhook in webhooks:
              await webhook.delete()


      else:
          embed = discord.Embed(title="You lack the permissions to do this command", description="Error. Must Have Role Called 'Giveaway'")
          embed.add_field(name="Error:", value=f'Missing permissions')
          embed.colour = discord.embeds.Colour.red()
          embed.set_footer(
              text="Error: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
              icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
          await message.channel.send(content=None, embed=embed, )









  if message.content.startswith('$User info'):

      IDC = await message.guild.fetch_member(message.raw_mentions[0])
      guild = message.guild

      embed = discord.Embed(title=f"User info {IDC.mention}", description=f"{IDC.display_name}")
      embed.add_field(name=f"{IDC.display_name} was created at:", value=f'{IDC.created_at}')
      embed.add_field(name=f"Is {IDC.display_name} a bot?:", value=f'{IDC.bot}')
      # embed.add_field(name=f"{IDC.display_name} status:", value=f'{IDC.desktop_status}')
      embed.add_field(name=f"{IDC.display_name} permissions:", value=f'{IDC.guild_permissions}')
      embed.add_field(name=f"When {IDC.display_name} joined:", value=f'{IDC.joined_at}')
      embed.add_field(name=f"{IDC.display_name} has had nitro since:", value=f'{IDC.premium_since}')
      embed.add_field(name=f"{IDC.display_name}'s best role:", value=f'{IDC.top_role}')
      embed.add_field(name=f"{IDC.display_name}'s activity:", value=f'{IDC.activity}')
      embed.add_field(name=f"{IDC.display_name}'s color:", value=f'{IDC.color}')
      # embed.add_field(name=f"{IDC.display_name} is in these same guilds as me:", value=f'{IDC.mutual_guilds}')
      embed.set_footer(
          text="Asked by: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
          icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
      await message.channel.send(content=None, embed=embed)

  if message.content.startswith('$Server info'):
      owner = str(message.guild.owner)
      id = str(message.guild.id)
      region = str(message.guild.region)
      memberCount = str(message.guild.member_count)
      icon = str(message.guild.icon_url)
      rules = str(message.guild.rules_channel)
      verification_level = message.guild.verification_level

      embed = discord.Embed(title=f"Guild info", description=f"{message.guild.name}, {id}")
      embed.add_field(name=f"{message.guild.name} was created at:", value=f'{message.guild.created_at}')
      embed.add_field(name=f"{message.guild.name} verification level:", value=f'{verification_level}')
      embed.add_field(name=f"{message.guild.name} rules channel:", value=f'{rules}')
      embed.add_field(name=f"{message.guild.name} was created at:", value=f'{message.guild.created_at}')
      embed.add_field(name=f"{message.guild.name}'s owner is:", value=f'{owner}')
      embed.add_field(name=f"{message.guild.name} has this many members", value=f'{memberCount}')
      embed.add_field(name=f"{message.guild.name} is residented in", value=f'{region}')
      embed.set_footer(
          text="Asked by: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
          icon_url=icon)  # + " " + datetime.datetime.utcnow())
      await message.channel.send(content=None, embed=embed)

  if message.content == '$info':


      embed = discord.Embed(title="Shard stuff", description="Idk")
      embed.add_field(name="Shard_count", value=f'{str(bot.shard_count)}')
      embed.add_field(name="Shard id", value=f'{bot.shard_id}')
      # embed.add_field(name="Shard id", value=f'{bot.activity.name}')
      embed.add_field(name="Shard id", value=f'{bot.owner_id}')
      embed.add_field(name="Shard id", value=f'{bot.application_info()}')
      embed.add_field(name="Is bot ratelimited", value=f'{bot.is_ws_ratelimited()}')
      # embed.add_field(name="Modmail", value='Type ```$help modmail``` to trigger the help command')
      # embed.add_field(name="Slash commands", value='Type ```/``` to view the bots slash command!')
      # embed.add_field(name="General", value='Type ```$help general``` to trigger the help command!')
      embed.colour = discord.embeds.Colour.random()

      embed.set_footer(
          text="Help requested by: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
          icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
      await message.channel.send(content=None, embed=embed)

  if message.content.startswith('Ping'):
      Guild = message.guild

      ping = Image.open("ping.png")

      asset010101 = Guild.icon_url_as(size = 128)
      data10101 = BytesIO(await asset010101.read())
      pfp10101 = Image.open(data10101)

      pfp10101 = pfp10101.resize((708,708))

      ping.paste(pfp10101, (354,354))

      ping.save("Ping.png")

      await message.channel.send(file = discord.File("Ping.png"))



  if message.content.startswith('Spank'):
      okokokokk = await message.guild.fetch_member(message.raw_mentions[0])

      spank = Image.open("spank.jpg")

      asset2 = message.author.avatar_url_as(size = 128)
      asset1 = okokokokk.avatar_url_as(size = 128)
      data1 = BytesIO(await asset1.read())
      data2 = BytesIO(await asset2.read())
      pfp1 = Image.open(data1)
      pfp2 = Image.open(data2)
      pfp1 = pfp1.resize((100,100))
      pfp2 = pfp2.resize((100,100))
      spank.paste(pfp1, (150, 200))
      spank.paste(pfp2, (145, 50))

      spank.save("Spank.jpg")

      await message.channel.send(file = discord.File("Spank.jpg"))

  if message.content.startswith('$Poll'):

      hasPollRole = False
      for userRole in message.author.roles:
          if userRole.name == 'Owner':
              hasPollRole = True

      if (hasPollRole):

          message_array10 = message.content[27:]
          HAHAHA = message.guild.get_channel(message.raw_channel_mentions[0])

          embed = discord.Embed(title="A Poll Has Been Created!", description="Please react with the reaction of your choice")
          embed.add_field(name="Poll:", value=f'```{message_array10}```')
          embed.colour=discord.embeds.Colour.random()
          embed.set_footer(
          text="Poll created by: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
          icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
          await message.channel.purge(limit=1)
          await HAHAHA.send(content=None, embed=embed, )
      else:
          embed = discord.Embed(title="Error", description="Error")
          embed.add_field(name="You lack the required permissions:", value=f'Missing permissions')
          embed.colour=discord.embeds.Colour.dark_red()
          embed.set_footer(
          text="Error: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
          icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
          await message.channel.send(content=None, embed=embed, )


  if message.content == '$random number':
      await message.channel.send(f'This is your random number {random.randrange(100000)}')

  if message.content == '$Support':
      await message.channel.send(f'Click here to join the support server: https://discord.gg/avknX8v7X7')


  if message.content.startswith('$ping'):
      await message.channel.send(f"Pong! {round(bot.latency * 1000)}ms")


  if message.content.startswith('$kick'):
      haha = False
      for userRole in message.author.roles:
          if userRole.name == 'Admin':
              haha = True


      if (haha):
          message_array = message.content[28:]
          await message.guild.kick(await bot.fetch_user(message.raw_mentions[0]), reason=message_array[2])
          # txt = message.content
          #
          # x = txt.split()
          # x[2]
          # print(x)
          await message.channel.send(f'A member has been kicked for {message_array}')
      else:
          embed = discord.Embed(title="You lack the permissions to do this command", description="Error")
          embed.add_field(name="Error:", value=f'Missing permissions')
          embed.colour = discord.embeds.Colour.red()
          embed.set_footer(
              text="Error: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
              icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
          await message.channel.send(content=None, embed=embed, )


  if message.content.startswith('$warn'):
      message_array3 = message.content[28:]

      guild = message.guild
      mhm = await message.guild.fetch_member(message.raw_mentions[0])

      OKA = False
      for userRole in message.author.roles:
          if userRole.name == 'Jr. Moderator':
              OKA = True


              if (OKA):
                  # await bot.fetch_user(message.raw_mentions[0])
                  await message.channel.send(f"Warned {mhm.mention} for reason {message_array3}")
                  await mhm.send(f"You were warned in a server: {guild.name} for {message_array3}")
              else:
                  embed = discord.Embed(title="You lack the permissions to do this command", description="Error")
                  embed.add_field(name="Error:", value=f'Missing permissions')
                  embed.colour = discord.embeds.Colour.red()
                  embed.set_footer(
                      text="Error: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
                      icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
                  await message.channel.send(content=None, embed=embed, )


  if message.content == '$new':
      await message.channel.send(f'Success! Please answer these questions: In the channel questions')
      channel1 = bot.get_channel(845456242587729931)
      await message.channel.send('Please provide your questions here in the format: ```Question: [question]```')

  if message.content.startswith('Question:'):
      Cool = await message.guild.create_category(name=f"{message.author.name}'s ticket", overwrites=None, reason=None,
                                                  position=None)
      message_array13 = message.content[10:]
      Cool_channel = await Cool.create_text_channel(name=f"{message.author.display_name}", overwrites=None, reason=None)
      embed = discord.Embed(title=f"{message.author.display_name} has asked a question", description=f"Sender ID {message.author.id}")
      embed.add_field(name=f"Question Content:", value=f'{message_array13}')
      embed.set_footer(text="Question request by: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
      await Cool_channel.send(content=None, embed=embed)
      # await Cool_channel.send

  if message.content.startswith('$Close'):
      #
      for userRole in message.author.roles:
          if userRole.name == 'Support':
              await message.channel.category.delete()
              await message.channel.delete()



  if message.content.startswith('$reply'):
      message_array14 = message.content[25:]
      cook = await message.guild.fetch_member(message.raw_mentions[0])
      reply = False
      for userRole in message.author.roles:
          if userRole.name == 'Admin':
              reply = True


              if (reply):
                  embed = discord.Embed(title="Question Answered!:", description="Question Answered. User Please Check")
                  embed.add_field(name="Question Answer:", value=message_array14)
                  embed.set_footer(text="Answered by:" + " " + message.author.display_name)
                  embed.set_thumbnail(url=message.author.avatar_url)
                  embed.set_footer(text="Answered by: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
                  await cook.create_dm()
                  await cook.dm_channel.send(content=None, embed=embed)
              else:
                  embed = discord.Embed(title="You lack the permissions to do this command", description="Error")
                  embed.add_field(name="Error:", value=f'Missing permissions')
                  embed.colour = discord.embeds.Colour.red()
                  embed.set_footer(
                      text="Error: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
                      icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
                  await message.channel.send(content=None, embed=embed, )

  if message.content.startswith('say'):

      for userRole in message.author.roles:
          if userRole.name == 'Admin':

              message_array4 = message.content[26:]
              oki = await message.guild.fetch_member(message.raw_mentions[0])
              webhook = await message.channel.create_webhook(name=oki.display_name)
              await message.channel.purge(limit=1)
              await webhook.send(
                  str(message_array4), username=oki.display_name, avatar_url=oki.avatar_url)

              webhooks = await message.channel.webhooks()
              for webhook in webhooks:
                      await webhook.delete()

  if message.content.startswith('Ann'):

      for userRole in message.author.roles:
          if userRole.name == 'Admin':

              message_array9 = message.content[26:]
              mehhh = await message.guild.fetch_member(message.raw_mentions[0])
              webhook = await message.channel.create_webhook(name="Annoucement Bot")
              await message.channel.purge(limit=1)
              await webhook.send(
                  str(message_array9), username="Annoucement Bot", avatar_url=mehhh.avatar_url)

              webhooks = await message.channel.webhooks()
              for webhook in webhooks:
                      await webhook.delete()

@bot.event
async def on_guild_channel_create(channel):

  embed = Embed(title="Channel created.",
                    description=f"Channel created by",
                      #colour=message.author.color,
                    timestamp=datetime.datetime.utcnow())

  fields = [("Channel" , channel.id)]

  for name, value in fields:
      embed.add_field(name=name, value=str(value))

      guild = channel.guild
      channel = discord.utils.get(guild.channels, name="modlog")
      await channel.send(embed=embed)

@bot.event
async def on_message_edit(after, message):
    if not message.author.bot:
      embed = Embed(title="Message edit",
                    description=f"Edited by {message.author.display_name}.",
                    colour=message.author.colour,
                    timestamp=datetime.datetime.utcnow())

      fields = [("Message", after.content, False)]

      for name, value, inline in fields:
          embed.add_field(name=name, value=value, inline=inline)

          guild = message.guild
          channel = discord.utils.get(guild.channels, name="modlog")
          await channel.send(embed=embed)

@bot.event
async def on_message_delete(message):
    if not message.author.bot:
      embed = Embed(title="Message delete",
                    description=f"Delete by {message.author.display_name}.",
                    colour=message.author.colour,
                    timestamp=datetime.datetime.utcnow())

      fields = [("Message", message.content, False)]

      for name, value, inline in fields:
          embed.add_field(name=name, value=value, inline=inline)

          guild = message.guild
          channel = discord.utils.get(guild.channels, name="modlog")
          await channel.send(embed=embed)


@bot.event
async def on_guild_channel_delete(channel):
  # channel_id = bot.get_channel
  embed = Embed(title="Channel deleted.",
                    description=f"Channel deleted {channel.name}",
                      #colour=message.author.color,
                    timestamp=datetime.datetime.utcnow())

  fields = [("Channel" , channel.id)]

  for name, value in fields:
      embed.add_field(name=name, value=str(value))
      guild = channel.guild
      channel = discord.utils.get(guild.channels, name="modlog")
      await channel.send(embed=embed)


@bot.event
async def on_guild_channel_pins_update(channel, last_pin):
  embed = Embed(title="Channel pin updated.",
                    description=f"Channel pins made {channel.name}",
                      #colour=message.author.color,
                    timestamp=datetime.datetime.utcnow())

  fields = [("Channel" , channel.id)]

  for name, value in fields:
      embed.add_field(name=name, value=str(value))

      guild = channel.guild
      channel = discord.utils.get(guild.channels, name="modlog")
      await channel.send(embed=embed)


@bot.event
async def on_guild_integrations_update(channel, guild):

  embed = Embed(title="Integration updated.",
                    description=f"Intergration UPDATED",
                      #colour=message.author.color,
                    timestamp=datetime.datetime.utcnow())

  fields = [("Intergration" , channel.id)]

  for name, value in fields:
      embed.add_field(name=name, value=str(value))
      # s
      guild = channel.guild
      channel = discord.utils.get(guild.channels, name="modlog")
      await channel.send(embed=embed)

@bot.event
async def on_webhooks_update(channel):

  embed = Embed(title="Webhook Updated.",
                    description=f"Webhook UPDATED",
                      #colour=message.author.color,
                    timestamp=datetime.datetime.utcnow())

  fields = [("Webhook" , channel.id)]

  for name, value in fields:
      embed.add_field(name=name, value=str(value))
      guild = channel.guild
      channel = discord.utils.get(guild.channels, name="modlog")
      await channel.send(embed=embed)



@bot.event
async def on_invite_create(invite):
  invite_user = invite.inviter
  if not invite_user.bot:


      embed = Embed(title="Invite created.",
                    description=f"Invite created by {invite_user.display_name} {invite.url}.",
                    colour=invite_user.colour,
                    timestamp=datetime.datetime.utcnow())

      fields = [("Invite", invite.url, False)]

      for name, value, inline in fields:
          embed.add_field(name=name, value=value, inline=inline)
      guild = invite.guild
      channel = discord.utils.get(guild.channels, name="modlog")
      await channel.send(embed=embed)


# @bot.event
# async def on_message_delete(before, guild):
#   if not before.author.bot:
#       if before.content:


#           embed = Embed(title="Message deleted",
#                         description=f"Deleted by {before.author.display_name}.",
#                         colour=before.author.colour,
#                         timestamp=datetime.datetime.utcnow())

#           fields = [("Deleted message:", before.content, False)]#,
#                     #("After", after.content, False)]

#           for name, value, inline in fields:
#               embed.add_field(name=name, value=value, inline=inline)

#       guild = guild
#       channel = discord.utils.get(guild.channels, name="modlog")
#       await channel.send(embed=embed)


@bot.event
async def on_guild_role_create(role):
#    if not before.author.bot:
      if role.name:


          embed = Embed(title="Role created",
                        description=f"Name = {role.name}.",
                        colour=role.colour,
                        timestamp=datetime.datetime.utcnow())

          fields = [("Role:", True)]#,
                    #("After", after.content, False)]

          for name, value in fields:
              embed.add_field(name=name, value=value)

      guild = role.guild
      channel = discord.utils.get(guild.channels, name="modlog")
      await channel.send(embed=embed)

@bot.event
async def on_guild_role_delete(role):
#    if not before.author.bot:
      if role.name:


          embed = Embed(title="Role deleted",
                        description=f"Name = {role.name}.",
                        colour=role.colour,
                        timestamp=datetime.datetime.utcnow())

          fields = [("Role:", True)]#,
                    #("After", after.content, False)]

          for name, value in fields:
              embed.add_field(name=name, value=value)

      guild = role.guild
      channel = discord.utils.get(guild.channels, name="modlog")
      await channel.send(embed=embed)

@bot.event
async def on_guild_role_update(before, after, guild):
      if after.name:

          embed = Embed(title="Role updated",
                        description=f"Name = {after.name}.",
                        colour=after.colour,
                        timestamp=datetime.datetime.utcnow())

          fields = [("Role:", True)]#,
                    #("After", after.content, False)]

          for name, value in fields:

              embed.add_field(name=name, value=value)

      guild = guild
      channel = discord.utils.get(guild.channels, name="modlog")
      await channel.send(embed=embed)



@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
          emoji23 = discord.utils.get(bot.emojis, name='SpiritJoinServer')
          # await channel.send('Hi there' + str(emoji23) + "\n" + "You now have added me to your amazing server. Feel ")
          em = discord.Embed(title=f"Hello my name is Spirit",color=discord.Color.blue())
          em.add_field(name="To get started:", value=f'Type: ```$help``` this is your way to access all our commands. To initiate audit-logging type: ```$Init audit```')
          em.add_field(name="**Important Links**", value=f'**Support**: https://discord.gg/fHpgwz6sE6 \n **Invite**: https://discord.com/api/oauth2/authorize?client_id=844746411429986314&permissions=8&scope=bot%20applications.commands \n **Website**: https://leonf4331.wixsite.com/spirit-bot')
          await channel.send(embed = em)          
        break



keep_alive()
bot.run(my_secret)
