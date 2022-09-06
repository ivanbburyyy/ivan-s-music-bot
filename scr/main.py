import discord
from discord.ext import commands
import sys
sys.path.append("..")
bot = discord.Bot(intents=discord.Intents.all())
@bot.event
async def on_ready():
    activity = discord.Game(name="/help", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f"bot started {bot.user}")
from .commands import *
