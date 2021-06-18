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
import dblpy
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

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="$",description='A Simple, Yet Complex Bot!')

@bot.event
async def on_message(message):
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





bot.run("ODQ0NzQ2NDExNDI5OTg2MzE0.YKW5Zw.lJ2OLEiDa80egfSUvrktTMWA7zA")
