import discord

TOKEN = 'NDYzMDM0NTcxOTE1NjU3MjI2.Dvq7ow.M2lFt2IQWcfS9NtvV16CVnOsE90'

client = discord.Client()


@client.event
async def on_message(message):
    print(message.author,":",message.content)











@client.event
async def on_ready():
    print('Logged in as: '+client.user.name)

client.run(TOKEN,bot=False)
