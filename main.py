import discord
from discord.ext import commands
import configparser
import os
import asyncio

# Define paths
current_directory = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(current_directory, 'config.ini')

# Create a config file if it doesn't exist
def create_config_file():
    config = configparser.ConfigParser()
    config['BOT'] = {
        'discord_secret': 'YOUR_DISCORD_SECRET_TOKEN_HERE'
    }
    with open(config_file, 'w') as f:
        config.write(f)

# Load configuration
def load_config():
    config = configparser.ConfigParser()
    if not os.path.exists(config_file):
        create_config_file()
    config.read(config_file)
    return config['BOT']['discord_secret']

# Get Discord secret from config file
discord_secret = load_config()

# Intents (required for some features)
intents = discord.Intents.default()
intents.members = True  # Required for on_member_join to work
intents.message_content = True  # Ensure message content is enabled if needed
intents.reactions = True        # Enable reaction intents

# Bot setup
bot = commands.Bot(command_prefix='!', intents=intents)

# Load cogs
async def load_cogs():
    cogs_directory = os.path.join(current_directory, 'cogs')
    for filename in os.listdir(cogs_directory):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

# On ready event
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash commands.")
    except Exception as e:
        print(f"Error syncing commands: {e}")

# Run the bot
async def main():
    await load_cogs()  # Load cogs before starting the bot
    try:
        await bot.start(discord_secret)
    except discord.errors.LoginFailure:
        print("Failed to login. Please check your Discord token in the config file and try again.")

# Start the bot
asyncio.run(main())
