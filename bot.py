import asyncio
import datetime
import json
import os
import random
from random import randint

from discord_slash import SlashContext, SlashCommandOptionType
import discord
from discord import Embed
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
from dotenv import load_dotenv

from AuditData import AuditData

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=".", description="TESTING", intents=intents)

slash = SlashCommand(bot, sync_commands=True) # Declares slash commands through the␣






guild_ids=[844733913011060779]#, 843302697486647316, 839567563544461372]


@slash.slash(name="Ping", description="Finds the bot latency. In Ping Pong! 🏓", guild_ids=guild_ids)
async def _ping(ctx):  # Defines a new "context" (ctx) command called "ping."
    await ctx.send(f"Pong! ({bot.latency * 1000}ms)")


@slash.slash(name="say", description="Says what you want the bot to say", guild_ids=guild_ids)
async def _say(ctx, message):
    await ctx.send(message)

@slash.slash(name="pfp", description="Displays your pfp", guild_ids=guild_ids)
async def pfp(ctx):

    embed = discord.Embed(
        title=f"Avatar of {ctx.author.display_name}",
        color=discord.Color.teal()
    ).set_image(url=ctx.author.avatar_url)

    await ctx.send(embed=embed)


@slash.slash(name="pick",
             description="choose randomly between 2 options",
             options=[
               create_option(
                 name="choice1",
                 description="This is the first option we have.",
                 option_type=3,
                 required=False
               ),
               create_option(
                 name="choice2",
                 description="This is the second option we have.",
                 option_type=3,
                 required=False
               )
             ])
async def _pick(ctx, choice1="head", choice2="tail"): # Command with 1 or more args.
    ch = random.choice([choice1, choice2])
    ch_str = str(ch)
    await ctx.send(content=ch_str)


@slash.slash(name="Help", description="This is just a link to the list of command for the bot.", guild_ids=guild_ids)
async def help(ctx):
  await ctx.send(content="https://bit.ly/3uVdQqK")




log = []
with open('logs.txt', 'a+', encoding='utf-8') as a:
  try:
    # log.append(AuditData("a", "b", "c", "d", "e"))
    for line in a:
       (msg_id, user_name, user_id, activity, timestamp) = line.split()
       log.append(AuditData(msg_id, user_name, user_id, activity, timestamp))
  except Exception as e:
    print(e)


def add_audit_event(msg_id:str, user_name:str, user_id:str, activity:str, timestamp:str):
    with open('logs.txt', 'a+', encoding='utf-8') as a:
        try:
            a.write(str(msg_id) + ","
                    + str(user_name) + ","
                    + str(user_id) + ","
                    + str(activity) + ","
                    + str(timestamp) + "\n")

        except Exception as e:
            print(e)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    add_audit_event(message.author.display_name,
                    message.author.roles,
                    "Member has used a on_message event.",
                    message.author.avatar_url,
                    datetime.datetime.utcnow())

    if message.content == 'o!random number':
        await message.channel.send(f'This is your random number {random.randrange(100000)}')

    if message.content.startswith(".say"):
                mes = message.content.split()
                output = ""
                for word in mes[1:]:
                    output += word
                    output += " "
                await message.channel.purge(limit=1)
                await message.channel.send(output)

    if message.content.startswith('o!mute'):

        message_array2 = message.content[29:]

        # guild = bot.get_guild(839567563544461372)
        mbr = await message.guild.fetch_member(message.raw_mentions[0])

        guild = message.guild
        mutedRole = discord.utils.get(mbr.roles, name='Muted')

        if not mutedRole:
            try:
                mutedRole = await guild.create_role(name="Muted")
            except Exception as e:
                print(e)

        for channel in guild.channels:
            # await message.channel.send("No muted role has been found. Creating role...")
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True,
                                          read_messages=False)
        # await bot.fetch_user(message.raw_mentions[0]).add_role(mutedRole)
        # mbr = await message.guild.fetch_member(message.raw_mentions[0])
        await mbr.add_roles(mutedRole)
        # await member.add_roles(mutedRole)
        await message.channel.send(f"Muted {mbr.mention} for reason {message_array2}")
        await mbr.send(f"You were muted in the server {guild.name} for {message_array2}")
        await asyncio.sleep(600)
        await mbr.remove_roles(mutedRole)
        await message.channel.send(f"You were unmuted by the system! {mbr.mention}. ")
        await mbr.send(f"You were unmuted in the server {guild.name}")


    if message.content.startswith('Annoy'):
        # message_array6 = message.content[29:]
        #     await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Cocomelon!"))

        # guild = bot.get_guild(839567563544461372)
        sure = await message.guild.fetch_member(message.raw_mentions[0])
        for userRole in message.author.roles:
            if userRole.name == 'Omie':
                await sure.send(f"I was told to annoy you! {sure.mention}")
                await sure.send(f"I was told to annoy you! {sure.mention}")
                await sure.send(f"I was told to annoy you! {sure.mention}")
                await sure.send(f"I was told to annoy you! {sure.mention}")
                await sure.send(f"I was told to annoy you! {sure.mention}")
                await sure.send(f"I was told to annoy you! {sure.mention}")
                await sure.send(f"I was told to annoy you! {sure.mention}")
                await sure.send(f"I was told to annoy you! {sure.mention}")
                await sure.send(f"I was told to annoy you! {sure.mention}")


    if message.content.startswith('o!Nick'):
        message_array5 = message.content[29:]
        oka = await message.guild.fetch_member(message.raw_mentions[0])
        guild = message.guild
        for userRole in message.author.roles:
            if userRole.name == 'Omie':
                await oka.edit(member=oka, nick=message_array5)
                await message.channel.send(f"Changed {oka.mention}  Nickname.")
                await oka.send(f"Your nickname was changed in a server: {guild.name} for {message_array5}")

    if message.content.startswith('o!slowmode'):
        message_array6 = message.content[13:]
        # huh = await message.guild.fetch_channel(message.raw_channel_mentions[0])
        huh = discord.utils.get(message.raw_channel_mentions[0])
        guild = message.guild
        seconds : message_array6
        for userRole in message.author.roles:
            if userRole.name == 'Admin':
                await huh.edit(slowmode_delay=seconds)
                await message.channel.send('Slow mode has been enabled!')


    if message.content.startswith('o!unmute'):

        message_array3 = message.content[31:]

        # guild = bot.get_guild(839567563544461372)
        mrb = await message.guild.fetch_member(message.raw_mentions[0])

        guild = message.guild
        mutedRole = discord.utils.get(mrb.roles, name='Muted')

        if not mutedRole:
            try:
                mutedRole = await guild.create_role(name="Muted")
            except Exception as e:
                print(e)

        for channel in guild.channels:
            # await message.channel.send("No muted role has been found. Creating role...")
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True,
                                          read_messages=False)

        # await bot.fetch_user(message.raw_mentions[0]).add_role(mutedRole)
        # mbr = await message.guild.fetch_member(message.raw_mentions[0])
        await mrb.remove_roles(mutedRole)
        # await member.add_roles(mutedRole)
        await message.channel.send(f"unmuted {mrb.mention} for reason {message_array3}")
        await mrb.send(f"You were unmuted in the server {guild.name} for {message_array3}")

    if message.content.startswith('Purge:'):
        for userRole in message.author.roles:
            if userRole.name == 'Admin':
                amount = 10
                await message.channel.purge(limit=amount)
                await message.channel.send('I have purged the channel!')
                await asyncio.sleep(5)
                await message.channel.purge(limit=1)


    if message.content == 'Who am I':
        embed = discord.Embed(title="Hello!", description="You name is...")
        embed.add_field(name="Name:", value='You are' + " " + message.author.display_name)
        embed.set_footer(text="Asked by:" + " " + message.author.display_name)

        await message.channel.send(content=None, embed=embed)

        if message.content.startswith('o!add'):
            variables = message.content.strip().split(' ')
            num1 = int(variables[1])
            num2 = int(variables[2])
            await message.channel.send(num1 + num2)

        if message.content.startswith('o!multiply'):
            variables = message.content.strip().split(' ')
            num1 = int(variables[1])
            num2 = int(variables[2])
            await message.channel.send(num1 * num2)

        if message.content.startswith('o!divide'):
            variables = message.content.strip().split(' ')
            num1 = int(variables[1])
            num2 = int(variables[2])
            await message.channel.send(num1 / num2)

        if message.content.startswith('o!sub'):
            variables = message.content.strip().split(' ')
            num1 = int(variables[1])
            num2 = int(variables[2])
            await message.channel.send(num1 - num2)

    if message.content.startswith('ping'):
        await message.channel.send(f"Pong! {round(bot.latency * 1000)}ms")

    if message.content.startswith('.kick'):
        for userRole in message.author.roles:
            if userRole.name == 'Omie':
                message_array = message.content[28:]
                await message.guild.kick(await bot.fetch_user(message.raw_mentions[0]), reason=message_array[2])
                # txt = message.content
                #
                # x = txt.split()
                # x[2]
                # print(x)
                await message.channel.send(f'A member has been kicked for {message_array}')

    if message.content.startswith('o!warn'):
        message_array3 = message.content[29:]

        guild = bot.get_guild(839567563544461372)
        mhm = await message.guild.fetch_member(message.raw_mentions[0])

        # await bot.fetch_user(message.raw_mentions[0])
        await message.channel.send(f"Warned {mhm.mention} for reason {message_array3}")
        await mhm.send(f"You were warned in a server: {guild.name} for {message_array3}")



    if message.content.startswith('say'):

        for userRole in message.author.roles:
            if userRole.name == 'Omie':

                message_array4 = message.content[26:]
                oki = await message.guild.fetch_member(message.raw_mentions[0])
                webhook = await message.channel.create_webhook(name=oki.display_name)
                await message.channel.purge(limit=1)
                await webhook.send(
                    str(message_array4), username=oki.display_name, avatar_url=oki.avatar_url)

                webhooks = await message.channel.webhooks()
                for webhook in webhooks:
                        await webhook.delete()

    empty_array = []
    modmail_channel = discord.utils.get(bot.get_all_channels(), name="modmail")


    if str(message.channel.type) == "private":
        for guild in bot.guilds:
            for channel in guild.channels:
                if channel.name == 'modmail':
                    embed = discord.Embed(title="Question reported!", description=f"Message ID: {message.id}.")
                    embed.add_field(name="Question content:", value=message.content)
                    embed.set_thumbnail(url=message.author.avatar_url)
                    embed.set_footer(text="Question request by: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
                    await channel.send(content=None, embed=embed)

    elif str(message.channel) == "modmail" and message.content.startswith("<"):
        if len(message.mentions) > 0:
            member_object = message.mentions[0]
            if message.attachments != empty_array:
                files = message.attachments
                await member_object.send("•" + message.author.display_name + "•")
                for file in files:
                    await member_object.send(file.url)
            else:
                index = message.content.index(" ")
                string = message.content
                mod_message = string[index:]

            embed = discord.Embed(title="Question Answered!:", description="Question Answered. Member Please Check")
            embed.add_field(name="Question Answer:", value=message.content)
            embed.set_footer(text="Answered by:" + " " + message.author.display_name)
            embed.set_thumbnail(url=message.author.avatar_url)
            embed.set_footer(text="Answered by:" + " " + message.author.display_name, icon_url=message.author.avatar_url)
            await member_object.send(content=None, embed=embed)





#
# with open('reports.json', 'a+', encoding='utf-8') as f:
#   try:
#     report = json.load(f)
#   except ValueError:
#     report = {}
#     report['users'] = []
#
#
# @bot.command(pass_context = True)
# # @has_permissions(manage_roles=True, ban_members=True)
# async def warn(self, ctx, user = discord.Member, reason = None):
#     print("I am in warn")
#
#     if not reason:
#         await ctx.send("Please provide a reason")
#         return
#
#     reason = ' '.join(reason)
#     for current_user in report['users']:
#         if current_user['name'] == user.name:
#             current_user['reasons'].append(reason)
#             break
#         else:
#             report['users'].append({
#             'name':user.name,
#             'reasons': [reason,]
#             })
#
#     with open('reports.json', 'w+') as f:
#         json.dump(report, f)
#
#
# @bot.command(pass_context=True)
# async def warnings(ctx, user = discord.Member):
#     print("I am in warnings")
#     for current_user in report['users']:
#         if user.name == current_user['name']:
#             await ctx.send(
#                 f"{user.name} has been reported {len(current_user['reasons'])} times : {','.join(current_user['reasons'])}")
#             break
#     else:
#         await ctx.send(f"{user.name} has never been reported")

# @bot.event
# async def on_ready():
#     await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Cocomelon!"))
    #
    # await bot.change_presence(activity=discord.Game(name="mhm.."))
    #
    # await bot.change_presence(activity=discord.Game(name="idk"))
    #
    # await bot.change_presence(activity=discord.Game(name="ok"))
    #
    # await bot.change_presence(activity=discord.Game(name="so what?"))


async def ch_pr():
    await bot.wait_until_ready()

    statuses = ["Cocomelon", "Moderation| o!help", f" The bot is on {len(bot.guilds)}servers", "Trying to devise a way to cure.... Sleep"]

    while not bot.is_closed():

        status = random.choice(statuses)

        await bot.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(2)

bot.loop.create_task(ch_pr())


@bot.event
async def on_member_join(member):
     role = discord.utils.get(member.guild.roles, name='Member')
     await member.add_roles(role)





#
# @bot.command(aliases=['8ball', 'test'])
# async def _8ball(ctx, *, question):
#     responses = ['It is certain.',
#                  'It is decidedly so',
#                  'Without a doubt',
#                  'Yes - definetely',]
#     await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    # if message.content.startswith('.kick'):
    #     # await message.channel.send(f"Pong! {round(bot.latency *1000)}ms")
    #     # user_id = message.raw_mentions[0]
    #     # message.
    #     # await user =
    #     # reason=None
    #     message_array = message.content.split()
    #     await message.guild.kick(await bot.fetch_user(message.raw_mentions[0]), reason=message_array[2])
    #     # txt = message.content
    #     #
    #     # x = txt.split()
    #     # x[2]
    #     # print(x)
    #     await message.channel.send(f'A member has been kicked for {message_array[2]}')


    # if message.content.startswith('8ball'):
    #
    #
    #      message_array1 = message.content.split()
    #      question = message.content.split()
    # responses = ['It is certain.',
    #                   'It is decidedly so',
    #                   'Without a doubt',
    #                   'Yes - definetely',]
    # await message.channel.send(f'Question: {question[0]}. \n Answer: {random.choice(responses)}')

    #await message.channel.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#
# @bot.command(description="Mutes the specified user.")
# @commands.has_permissions(manage_messages=True)
# async def mute(ctx, member: discord.member, *, reason=None):
#     guild = ctx.guild
#     mutedRole = discord.utils.get(guild.roles, name="muted")
#
#     if not mutedRole:
#         mutedRole = await guild.create_role(name="Muted")
#
#         for channel in guild.channels:
#             await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
#
#     await member.add_roles(mutedRole, reason=reason)
#     await ctx.send(f"Muted {member.mention} for reason {reason}")
#     await member.send(f"You were muted in the server {guild.name} for {reason}")





@bot.event
async def on_member_join(member):
    add_audit_event(member.id,
                    member.display_name,
                    f"{member} has joined the server!",
                    "Member Joined",
                    datetime.datetime.utcnow())

    a = [f"Everyone welcome {member}", f"{member} is here", f"Lets welcome {member}. Enjoy your stay :)", f"OMG {member} is here. Its a honor to have you here!"]
    welcome_message = a[randint(0, 1 )]
    channel = discord.utils.get(member.guild.channels, name='welcome-and-leave')
    await channel.send(welcome_message)
    print(f"{member} has joined the server")

@bot.event
async def on_member_remove(member):
    add_audit_event(member.id,
                    member.display_name,
                    f" {member} has left the server",
                    "Member removed",
                    datetime.datetime.utcnow())
    b = [f"{member} has just left the server :(", f"{member} just left we hope you had a good time.", f"Oh no {member} has left the server.", f"{member} has just left. Come back soon! :')"]
    leave_message = b[randint(0, 1)]
    channel = discord.utils.get(member.guild.channels, name='welcome-and-leave')
    await channel.send(leave_message)
    print(f"{member} has just left the server")


@bot.event
async def on_member_update(before, after):
    if not before.bot:
        if before.display_name != after.display_name:
            add_audit_event(before.id,
                            before.author.display_name,
                            before.author.id,
                            "Member Updated",
                            datetime.datetime.utcnow())
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
                    if channel.name == 'audit-log':
                        await channel.send(embed=embed)


log = []
with open('logs.txt', 'a+', encoding='utf-8') as a:
  try:
    # log.append(AuditData("a", "b", "c", "d", "e"))
    for line in a:
       (msg_id, user_name, user_id, activity, timestamp) = line.split()
       log.append(AuditData(msg_id, user_name, user_id, activity, timestamp))
  except Exception as e:
    print(e)


def add_audit_event(msg_id:str, user_name:str, user_id:str, activity:str, timestamp:str):
    with open('logs.txt', 'a+', encoding='utf-8') as a:
        try:
            a.write(str(msg_id) + ","
                    + str(user_name) + ","
                    + str(user_id) + ","
                    + str(activity) + ","
                    + str(timestamp) + "\n")

        except Exception as e:
            print(e)


@bot.event
async def on_message_edit(before, after):
    if not before.author.bot:
        if before.content != after.content:
            add_audit_event(before.id,
                            before.author.display_name,
                            before.author.id,
                            "Message edited",
                            datetime.datetime.utcnow())

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
                    if channel.name == 'audit-log':
                        await channel.send(embed=embed)

@bot.event
async def on_guild_channel_create(channel):
    add_audit_event(channel.id,
                    "Channel",
                    "A channel has been created:",
                    channel.name,
                    datetime.datetime.utcnow())
    embed = Embed(title="Channel created.",
                      description=f"Channel created by",
                       #colour=message.author.color,
                      timestamp=datetime.datetime.utcnow())

    fields = [("Channel" , channel.id)]

    for name, value in fields:
        embed.add_field(name=name, value=str(value))

        for guild in bot.guilds:
            for channel in guild.channels:
                if channel.name == 'audit-log':
                    await channel.send(embed=embed)


@bot.event
async def on_guild_channel_delete(channel):
    add_audit_event(channel.id,
                    "Channel",
                    f"A channel has been deleted: {channel.name}",
                    channel.name,
                    datetime.datetime.utcnow())
    embed = Embed(title="Channel deleted.",
                      description=f"Channel deleted {channel.name}",
                       #colour=message.author.color,
                      timestamp=datetime.datetime.utcnow())

    fields = [("Channel" , channel.id)]

    for name, value in fields:
        embed.add_field(name=name, value=str(value))

        for guild in bot.guilds:
            for channel in guild.channels:
                if channel.name == 'audit-log':
                    await channel.send(embed=embed)



@bot.event
async def on_guild_channel_pins_update(channel, last_pin):
    add_audit_event(channel.id,
                    "Channel",
                    "A channel pin has been created:",
                    channel.name,
                    datetime.datetime.utcnow())
    embed = Embed(title="Channel pin updated.",
                      description=f"Channel pins made {channel.name}",
                       #colour=message.author.color,
                      timestamp=datetime.datetime.utcnow())

    fields = [("Channel" , channel.id)]

    for name, value in fields:
        embed.add_field(name=name, value=str(value))

        for guild in bot.guilds:
            for channel in guild.channels:
                if channel.name == 'audit-log':
                    await channel.send(embed=embed)


@bot.event
async def on_guild_integrations_update(channel, guild):
    add_audit_event(guild.channels,
                    "Integration",
                    "A integration has been updated:",
                    channel.name,
                    datetime.datetime.utcnow())
    embed = Embed(title="Integration updated.",
                      description=f"Intergration UPDATED",
                       #colour=message.author.color,
                      timestamp=datetime.datetime.utcnow())

    fields = [("Intergration" , channel.id)]

    for name, value in fields:
        embed.add_field(name=name, value=str(value))

        for guild in bot.guilds:
            for channel in guild.channels:
                if channel.name == 'audit-log':
                    await channel.send(embed=embed)

@bot.event
async def on_webhooks_update(channel):
    add_audit_event(channel.id,
                    "Webhook",
                    "A Webhook has been updated:",
                    channel.name,
                    datetime.datetime.utcnow())
    embed = Embed(title="Webhook Updated.",
                      description=f"Webhook UPDATED",
                       #colour=message.author.color,
                      timestamp=datetime.datetime.utcnow())

    fields = [("Webhook" , channel.id)]

    for name, value in fields:
        embed.add_field(name=name, value=str(value))

        for guild in bot.guilds:
            for channel in guild.channels:
                if channel.name == 'audit-log':
                    await channel.send(embed=embed)


#
# @bot.event
# async def on_typing(channel, user, when):
#     if not user.bot:
#         add_audit_event(channel.id,
#                         "Type",
#                         "A user is typing:",
#                         channel.name,
#                         datetime.datetime.utcnow())
#
#         embed = Embed(title="A user is typing!",
#                       description=f"User is typing: {user.display_name}.",
#                       colour=user.colour,
#                       timestamp=datetime.datetime.utcnow())
#
#         fields = [("Typing", True)]  # ,
#         # ("After", after.content, False)]
#
#         for name, value in fields:
#             embed.add_field(name=name, value=value)
#
#         for guild in bot.guilds:
#             for channel in guild.channels:
#                 if channel.name == 'audit-log':
#                     await channel.send(embed=embed)


@bot.event
async def on_member_ban(before, after):
    if not before.author.bot:
        if before.content:# != after.content:
            embed = Embed(title="A member has been banned!",
                          description=f"Banned user: {before.author.display_name}.",
                          colour=after.author.colour,
                          timestamp=datetime.datetime.utcnow())

            fields = [("Banned", before.content, False)]#,
                      #("After", after.content, False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            for guild in bot.guilds:
                for channel in guild.channels:
                    if channel.name == 'audit-log':
                        await channel.send(embed=embed)


@bot.event
async def on_invite_create(invite):
    invite_user = invite.inviter
    if not invite_user.bot:
        add_audit_event(invite.inviter.id,
                        invite.inviter.display_name,
                        invite.inviter.id,
                        "Invite created",
                        datetime.datetime.utcnow())

        embed = Embed(title="Invite created.",
                      description=f"Invite created by {invite_user.display_name} {invite.url}.",
                      colour=invite_user.colour,
                      timestamp=datetime.datetime.utcnow())

        fields = [("Invite", invite.url, False)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        for guild in bot.guilds:
            for channel in guild.channels:
                if channel.name == 'audit-log':
                    await channel.send(embed=embed)


@bot.event
async def on_message_delete(before):
    if not before.author.bot:
        if before.content:
            add_audit_event(before.id,
                            before.author.display_name,
                            before.author.id,
                            "Message deleted",
                            datetime.datetime.utcnow())

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
                    if channel.name == 'audit-log':
                        await channel.send(embed=embed)


@bot.event
async def on_guild_role_create(role):
#    if not before.author.bot:
        if role.name:
            add_audit_event(role.id,
                            role.name,
                            role.id,
                            "Role created",
                            datetime.datetime.utcnow())

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
                    if channel.name == 'audit-log':
                        await channel.send(embed=embed)

@bot.event
async def on_guild_role_delete(role):
#    if not before.author.bot:
        if role.name:
            add_audit_event(role.id,
                            role.name,
                            role.id,
                            "Role deleted",
                            datetime.datetime.utcnow())

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
                    if channel.name == 'audit-log':
                        await channel.send(embed=embed)

@bot.event
async def on_guild_role_update(before, after):
        if after.name:
            add_audit_event(after.id,
                            after.name,
                            after.id,
                            "Role updated",
                            datetime.datetime.utcnow())

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
                    if channel.name == 'audit-log':
                        await channel.send(embed=embed)

# @bot.command(pass_context=True)
# async def chnick(ctx, member: discord.Member, nick):
#     await member.edit(nick=nick)
#     await ctx.send(f'Nickname was changed for {member.mention} ')

bot.run(TOKEN)
