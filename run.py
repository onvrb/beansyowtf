import os
import discord
from discord.ext import commands

DISCORD_API_TOKEN = os.getenv('DISCORD_API_TOKEN')

client = discord.Client()

emojimsg = "🅱 🇪 🅰 🇳 🇸 🥚 🇾 🅾 🥫 🇼 🇹 🇫 🔥"  # space separeted, covid

async def react(message):
    for emoji in emojimsg.split():
        await message.add_reaction(emoji)

@client.event
async def on_message(message):
    # if message is a link
    if message.content.startswith("https://"):
        await react(message)
    # if message is an image
    if message.attachments:
        await react(message)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(DISCORD_API_TOKEN)
