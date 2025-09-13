import discord
import os
import dotenv
from minecraft_cog import MinecraftServerCog
from config import load_config

dotenv.load_dotenv()
config = load_config()

bot = discord.Bot()
mc_cog = MinecraftServerCog(bot, config)

bot.add_cog(mc_cog)


@bot.event
async def on_ready():
    print(f"{bot.user} is running")


bot.run(os.environ["TOKEN"])
