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
async def on_message(message):
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

bot.run("ODQ0NzQ2NDExNDI5OTg2MzE0.YKW5Zw.lJ2OLEiDa80egfSUvrktTMWA7zA")

