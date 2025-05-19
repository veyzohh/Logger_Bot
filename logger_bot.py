import discord
import logging

# === CONFIG ===
TOKEN = "YOUR_BOT_TOKEN"
LOG_FILE = "discord_logs.txt"

# === SET UP LOGGER ===
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='[%(asctime)s] %(message)s')

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'🟢 Logged in as {client.user}')
    logging.info(f'Bot started: {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    log_entry = f"[MESSAGE] {message.author} in #{message.channel}: {message.content}"
    logging.info(log_entry)

@client.event
async def on_message_edit(before, after):
    if before.author.bot:
        return
    log_entry = f"[EDIT] {before.author} in #{before.channel}: '{before.content}' ➜ '{after.content}'"
    logging.info(log_entry)

@client.event
async def on_message_delete(message):
    if message.author.bot:
        return
    log_entry = f"[DELETE] {message.author} in #{message.channel}: {message.content}"
    logging.info(log_entry)

client.run(TOKEN)
