import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  #await client.change_presence(activity=discord.Game(name="살육머신 가동 중"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="몬가 하는 중"))
  
  print("클쟝머신:",client.user.name,"클쟝머신#2273:",client.user.id,"1.0.0:",discord.__version__)


client.run(os.environ['Nzg0MzUxMDg4ODQ0MzQxMjQ4.X8oB4A.Mc6oxUUlFfYN6lcFB2UL4nw7kFI'])
