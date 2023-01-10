import discord
from discord import Webhook, AsyncWebhookAdapter
import requests
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!poemtopic'):
        url = "https://api.openai.com/v1/chatgpt/topics"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer <API KEY>"
        }
        params = {
            "model": "text-davinci-002",
            "prompt": "Give me a random poem topic."
        }
        response = requests.post(url, json=params, headers=headers)
        data = response.json()
        topic = data['data']['topics'][0]
        await message.channel.send(f"Here is a random poem topic: {topic}")

def is_monday_wednesday_friday():
    now = datetime.datetime.now()
    return now.weekday() == 0 or now.weekday() == 2 or now.weekday() == 4

async def send_random_poem_topic():
    channel = client.get_channel(<CHANNEL ID>)
    while True:
        if is_monday_wednesday_friday():
            if datetime.datetime.now().hour == 9:
                url = "https://api.openai.com/v1/chatgpt/topics"
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer <API KEY>"
                }
                params = {
                    "model": "text-davinci-002",
                    "prompt": "Give me a random poem topic."
                }
                response = requests.post(url, json=params, headers=headers)
                data = response.json()
                topic = data['data']['topics'][0]
                webhook = Webhook.from_url('<WEBHOOK URL>', adapter=AsyncWebhookAdapter(client))
                await webhook.send(f"Here is a random poem topic for today: {topic}", username="Poem Bot")
        await asyncio.sleep(3600) # check every hour

client.loop.create_task(send_random_poem_topic())
client.run(<BOT TOKEN>)
