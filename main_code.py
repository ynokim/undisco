import discord

client = discord.Client()

@client.event
async def on_ready():
    print('다음으로 로그인합니다 : {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='냉탕에 연어가 살거라고 믿었지'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('FROM YNOKIM 2020.05.13 THURSDAY')

client.run('token_here')