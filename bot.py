import discord

# Replace with your actual bot token
TOKEN = '<DISCORD BOT TOKEN>'

# Message to send when "thoughts" is detected
RESPONSE_MESSAGE = f"<@274748598233858048>, thoughts? <ROONEYDOG GIF LINK OR WHATEVER LINK>"

# Set up the bot's intents
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Bot is now online as {client.user}')

@client.event
async def on_message(message):
    # Print every message the bot sees (for debugging)
    print(f"Message from {message.author.id}: {message.content}")

    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Trigger if message contains the word "thoughts" (case-insensitive)
    if "thoughts" in message.content.lower():
        await message.channel.send(RESPONSE_MESSAGE)

client.run(TOKEN)
