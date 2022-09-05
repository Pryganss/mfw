import discord
import random

f = open("token.txt", "r")
TOKEN = f.read()
f.close()

intents = discord.Intents(messages=True, message_content=True)
client = discord.Client(intents=intents)

choices = ["my face when", "my face when", "my face when", "my", "he", "she", "they",  "when", "I", "when the", "when the", "when the", "it"]

@client.event
async def on_ready():
    print('Logged on as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = message.content
    print(f'{username}: {user_message}')
    
    if message.author == client.user:
        return
    
    if user_message.lower() == 'mfw!':
        string = ""
        for i in range (0, 10):
            string += random.choice(choices) + " "
        await message.channel.send(string)
        return
    
client.run(TOKEN)
