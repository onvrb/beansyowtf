import os
import discord
from discord.ext import commands

DISCORD_API_TOKEN = os.getenv('DISCORD_API_TOKEN')

client = discord.Client()

emojiB = "🅱"
emojiE = "🇪"
emojiA = "🅰"
emojiN = "🇳"
emojiS = "🇸"
emojiCan = "🥫"
emojiY = "🇾"
emojiO = "🅾"
emojiEgg = "🥚"
emojiW = "🇼"
emojiT = "🇹"
emojiF = "🇫"
emojiFire = "🔥"

async def react(message):
    await message.add_reaction(emojiB)
    await message.add_reaction(emojiE)
    await message.add_reaction(emojiA)
    await message.add_reaction(emojiN)
    await message.add_reaction(emojiS)
    await message.add_reaction(emojiEgg)
    await message.add_reaction(emojiY)
    await message.add_reaction(emojiO)
    await message.add_reaction(emojiCan)
    await message.add_reaction(emojiW)
    await message.add_reaction(emojiT)
    await message.add_reaction(emojiF)
    await message.add_reaction(emojiFire)

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
