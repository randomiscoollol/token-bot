import discord
from discord.ext import commands
import base64

TOKEN = 'BOT-TOKEN'  # REPLACE ME

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

# When the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Respond to direct messages
@bot.event
async def on_message(message):
    # Ensure the bot does not respond to itself
    if message.author == bot.user:
        return

    # Check if the message is a direct message
    if isinstance(message.channel, discord.DMChannel):
        # Encode the sender's ID in base64
        user_id = str(message.author.id)
        encoded_id = base64.b64encode(user_id.encode()).decode()

        # Prepare the response message
        response = (
            f"I have your token! Now I got access. "
            f"I am the most annoying user. First part of your token: {encoded_id}. "
            f"For proof, go to https://github.com/Discord-Oxygen/Discord-Console-hacks"
        )
        
        # Send the response message
        await message.channel.send(response)

# Run the bot
bot.run(TOKEN)
