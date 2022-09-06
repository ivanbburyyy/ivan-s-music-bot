import sys
sys.path.append("..")
from .main import bot
command_list = "/help help command,"
@bot.command(description="ivan music bot help")
async def help(ctx):
    await ctx.respond(command_list)