import discord

client = discord.Client()

@client.event
async def on_ready():
    print('다음으로 로그인합니다 : {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('FROM YNOKIM 2020.05.12 TUESDAY')

client.run('NTQ5MjIzNjI3Njc0MDkxNTQx.XrrPsw.waVFdtU1VcSlF229K6XPp5sSpSg')