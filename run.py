import os
import discord
from discord.ext import commands
import counter_io as cio

DISCORD_API_TOKEN = os.getenv('DISCORD_API_TOKEN')
prefix = os.getenv('PREFIX')
key_word = os.getenv('KEY_WORD')
bot = commands.Bot(command_prefix=prefix)

session_counter = 0
lifetime_counter = cio.get_lifetime_counter()

emojimsg = "🅱 🇪 🅰 🇳 🇸 🥚 🇾 🅾 🥫 🇼 🇹 🇫 🔥"  # space separeted, covid

def increment_to_counter():
    global session_counter
    session_counter += 1
    global lifetime_counter
    lifetime_counter += 1
    cio.set_lifetime_counter(lifetime_counter)

async def react(message):
    increment_to_counter()
    for emoji in emojimsg.split():
        await message.add_reaction(emoji)

async def send_counter_message(message):
    lifetime_counter = cio.get_lifetime_counter()
    counter_message =   "**Session**: " + cio.get_digits_as_emojis(session_counter) + " :flushed:" + "\n" + \
                        "**Lifetime**: " + cio.get_digits_as_emojis(lifetime_counter) + " :sunglasses:"
    await message.channel.send(counter_message)

@bot.event
async def on_message(message):
    # if message contains the word beans
    if key_word in message.content.lower():
        await send_counter_message(message)
    # if message is a link
    if message.content.startswith("https://"):
        await react(message)
    # if message is an image
    if message.attachments:
        await react(message)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(DISCORD_API_TOKEN)
