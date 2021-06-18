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


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="$",description='A Simple, Yet Complex Bot!')

@bot.event
async def on_member_update(before, after):
  if not before.bot:
      if before.display_name != after.display_name:

          embed = Embed(title="Member update",
                        description=f"N {before.display_name}.",
                        colour=after.colour,
                        timestamp=datetime.datetime.utcnow())

          fields = [("Previous Nickname:", before.display_name, False),
                    ("Current Nickname", after.display_name, False)]

          for name, value, inline in fields:
              embed.add_field(name=name, value=value, inline=inline)


          for guild in bot.guilds:
              for channel in guild.channels:
                  if channel.name == 'modlog':
                      await channel.send(embed=embed)



@bot.event
async def on_message_edit(before, after):
  if not before.author.bot:
      if before.content != after.content:


          embed = Embed(title="Message edit",
                        description=f"Edit by {before.author.display_name}.",
                        colour=after.author.colour,
                        timestamp=datetime.datetime.utcnow())

          fields = [("Before", before.content, False),
                    ("After", after.content, False)]

          for name, value, inline in fields:
              embed.add_field(name=name, value=value, inline=inline)

          for guild in bot.guilds:
              for channel in guild.channels:
                  if channel.name == 'modlog':
                      await channel.send(embed=embed)

@bot.event
async def on_guild_channel_create(channel):

  embed = Embed(title="Channel created.",
                    description=f"Channel created by",
                      #colour=message.author.color,
                    timestamp=datetime.datetime.utcnow())

  fields = [("Channel" , channel.id)]

  for name, value in fields:
      embed.add_field(name=name, value=str(value))

      for guild in bot.guilds:
          for channel in guild.channels:
              if channel.name == 'modlog':
                  await channel.send(embed=embed)


@bot.event
async def on_guild_channel_delete(channel):

  embed = Embed(title="Channel deleted.",
                    description=f"Channel deleted {channel.name}",
                      #colour=message.author.color,
                    timestamp=datetime.datetime.utcnow())

  fields = [("Channel" , channel.id)]

  for name, value in fields:
      embed.add_field(name=name, value=str(value))

      for guild in bot.guilds:
          for channel in guild.channels:
              if channel.name == 'modlog':
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

      for guild in bot.guilds:
          for channel in guild.channels:
              if channel.name == 'modlog':
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
      for guild in bot.guilds:
          for channel in guild.channels:
              if channel.name == 'modlog':
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

      for guild in bot.guilds:
          for channel in guild.channels:
              if channel.name == 'modlog':
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

      for guild in bot.guilds:
          for channel in guild.channels:
              if channel.name == 'modlog':
                  await channel.send(embed=embed)


@bot.event
async def on_message_delete(before):
  if not before.author.bot:
      if before.content:


          embed = Embed(title="Message deleted",
                        description=f"Deleted by {before.author.display_name}.",
                        colour=before.author.colour,
                        timestamp=datetime.datetime.utcnow())

          fields = [("Deleted message:", before.content, False)]#,
                    #("After", after.content, False)]

          for name, value, inline in fields:
              embed.add_field(name=name, value=value, inline=inline)

          for guild in bot.guilds:
              for channel in guild.channels:
                  if channel.name == 'modlog':
                      await channel.send(embed=embed)


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

          for guild in bot.guilds:
              for channel in guild.channels:
                  if channel.name == 'modlog':
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

          for guild in bot.guilds:
              for channel in guild.channels:
                  if channel.name == 'modlog':
                      await channel.send(embed=embed)

@bot.event
async def on_guild_role_update(before, after):
      if after.name:

          embed = Embed(title="Role updated",
                        description=f"Name = {after.name}.",
                        colour=after.colour,
                        timestamp=datetime.datetime.utcnow())

          fields = [("Role:", True)]#,
                    #("After", after.content, False)]

          for name, value in fields:

              embed.add_field(name=name, value=value)

          for guild in bot.guilds:
              for channel in guild.channels:
                  if channel.name == 'modlog':
                      await channel.send(embed=embed)

bot.run("ODQ0NzQ2NDExNDI5OTg2MzE0.YKW5Zw.lJ2OLEiDa80egfSUvrktTMWA7zA")

