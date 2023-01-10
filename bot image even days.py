import discord
from discord import Webhook, AsyncWebhookAdapter
import requests
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready.")

def is_tuesday_thursday_saturday():
    now = datetime.datetime.now()
    return now.weekday() == 1 or now.weekday() == 3 or now.weekday() == 6

async def send_dall_e_image():
    channel = client.get_channel(<CHANNEL ID>)
    while True:
        if is_tuesday_thursday_saturday():
            if datetime.datetime.now().hour == 9:
                url = "https://api.openai.com/v1/images/generations"
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer <API KEY>"
                }
                params = {
                    "model": "image-alpha-001",
                    "prompt": "A beautiful image to inspire poetry."
                }
                response = requests.post(url, json=params, headers=headers)
                data = response.json()
                image_url = data['data']['url']
                description = data['data']['description']
                webhook = Webhook.from_url(<WEBHOOK URL>, adapter=AsyncWebhookAdapter(client))
                await webhook.send(f"Here is an image to inspire your poetry today: {description}", username="Poetry Inspiration Bot", avatar_url=image_url)
        await asyncio.sleep(3600) # check every hour

client.loop.create_task(send_dall_e_image())
client.run(<BOT TOKEN>)
