import discord

TOKEN = 'NDYzMDM0NTcxOTE1NjU3MjI2.Dvq7ow.M2lFt2IQWcfS9NtvV16CVnOsE90'

client = discord.Client()
klista = []

@client.event
async def on_message(message):
    print(message.author,":",message.content)
    with open('readme.neko','a') as hex:
        hex.write(str(message.author))
        hex.write(": ")
        hex.write(str(message.content))
        hex.write('\n')
        hex.close()










@client.event
async def on_ready():
    print('Logged in as: '+client.user.name)

client.run(TOKEN,bot=False)
