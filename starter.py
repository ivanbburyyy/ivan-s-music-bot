from scr.main import bot
import os
from dotenv import load_dotenv
load_dotenv()
SECRET_TOKEN = os.getenv("SECRET_TOKEN")
bot.run(SECRET_TOKEN)