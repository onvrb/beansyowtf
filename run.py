import os
import discord
from discord.ext import commands
import counter_io as cio

DISCORD_API_TOKEN = os.getenv('DISCORD_API_TOKEN')
prefix = os.getenv('PREFIX')
counter_key_word = os.getenv('COUNTER_KEY_WORD')
bean_this = "bean this"
bot = commands.Bot(command_prefix=prefix)

lifetime_counter = cio.get_lifetime_counter()
session_counter = lifetime_counter - lifetime_counter # 😂👌

emojimsg = "🅱 🇪 🅰 🇳 🇸 🥚 🇾 🅾 🥫 🇼 🇹 🇫 🔥"  # space separeted, because covid

def increment_to_counter():
    global session_counter
    session_counter += 1
    global lifetime_counter
    lifetime_counter += 1
    cio.set_lifetime_counter(lifetime_counter)

async def react_ok(message):
    await message.add_reaction('👌')

async def react_beans(message):
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
    # if message is bean_that

    # if message has "bean that" and is not a bot
    if bean_this in message.content.lower() and not message.author.bot:
        # if message is a reply
        if message.reference:
            ref_id = message.reference.message_id
            ref_ch = message.reference.channel_id
            replied_message = await bot.get_channel(ref_ch).fetch_message(ref_id)
            await react_ok(message)
            await react_beans(replied_message)
        else:
            await message.reply("Which message? Reply \"bean this\" to it!")
    # if message contains the word beans
    if counter_key_word in message.content.lower():
        await send_counter_message(message)
    # if message is a link
    if message.content.startswith("https://"):
        await react_beans(message)
    # if message is an image
    if message.attachments:
        await react_beans(message)

@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(DISCORD_API_TOKEN)
