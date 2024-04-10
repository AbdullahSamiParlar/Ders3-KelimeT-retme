import discord
from kelimetüretme import kelimetüret

users = {
  "O": "999999"
}

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author != client.user and message.author in users==False:
        users.update({message.author: 0})
    

    if message.content.startswith('/')==False:
        await message.channel.send(kelimetüret(message.author,message.content))
        
        print(message.content)



        


client.run("TOKEN")
