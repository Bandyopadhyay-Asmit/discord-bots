from http import client
from pydoc import cli
from urllib import response
import discord
import random

TOKEN = 'OTk1MzI1MzU0OTg0MDgzNTI3.GIh74p.RnMIVKjBwh-oNyLUveYvncuoW6QLEVsbbrt2TI'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    if message.channel.name == 'bakchodi-zone':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == "!random":
            response = f'This is your random number: {random.randrange(1000000)}'
            await message.channel.send(response)
            return
        elif user_message.lower() == '!facebook':
            await message.channel.send(f'https://www.facebook.com/profile.php?id=100009224708988')
            return
        elif user_message.lower() == '!instagram':
            await message.channel.send(f'https://www.instagram.com/devsatyamr')
            return
        elif user_message.lower() == '!twitter':
            await message.channel.send(f'https://twitter.com/DevsatyamR')
            return
        elif user_message.lower() == '!commands':
            myList = ("hello,  bye,  !random,  !facebook,  !instagram,  !twitter")
            await message.channel.send(myList)
            return                            

//great

                                            
                                            
            
    
client.run(TOKEN)

