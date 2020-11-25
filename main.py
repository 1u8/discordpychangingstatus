async def status():
    while True:
        await client.wait_until_ready()
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='irc@swat.移动')) #status 1
        await sleep(3)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='skid@cia.移动')) #status 2
        await sleep(3)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='god@fucksw.at')) #status 3
        await sleep(3)
@client.event
async def on_ready():
    print(f'{client.user} has started succesfully!')
client.loop.create_task(status())
