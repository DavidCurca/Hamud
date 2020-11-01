import discord
import asyncio
import requests,os,random
from gtts import gTTS
from discord.ext import commands

file = open('C:/Users/david/Documents/Hamud/jokes.txt', encoding="utf8") 
lines = file.readlines()
ones,twos,index = [],[],0
for line in lines:
    index += 1
    if(index%3 == 1):
        ones.append(line)
    elif(index%3 == 2):
        twos.append(line)

for i in range(len(ones)):
    ones[i] = ones[i][:-1]
    twos[i] = twos[i][:-1]

bot = commands.Bot(command_prefix='hamud ')

@bot.command()
async def ping(ctx):
    await ctx.send('bitch im up')

@bot.command()
async def piramid(ctx, n):
    str = ""
    totalStr = ctx.author.name + "'s piramid\n"
    for i in range(1, int(n)):
        str += "a"
        totalStr += str
        totalStr += "\n"
    for i in range(1, int(n)):
        str = str[:-1]
        totalStr += str
        totalStr += "\n"
    try:
        await ctx.send(totalStr)
    except:
        await ctx.send("piramid too big")

@bot.command()
async def peepeepoopoo(ctx, member: discord.Member):
    with requests.get(member.avatar_url_as(format='png')) as r:
        img_data = r.content
    with open(f'{member.name}.png', 'wb') as f:
        f.write(img_data)

    username = f"{member.name}'s info"
    desc = f"User Id:  {member.id}\n"
    desc += "He/She is " + str(random.randint(0,100)) + "% gay\n"
    desc += "Penis size: \n"
    penis = "8"
    for i in range(random.randint(0,12)):
        penis += "="
    penis += "D\n"
    desc += penis
    embed = discord.Embed(title=username, description=desc, color=discord.Colour.from_rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255))) #creates embed
    file = discord.File(f"{member.name}.png", filename="image.png")
    embed.set_image(url="attachment://image.png")
    await ctx.send(file=file, embed=embed)

@bot.command()
async def haha(ctx):
    position = random.randint(1,len(ones))
    embed = discord.Embed(title=ones[position], description=twos[position], color=discord.Colour.from_rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    await ctx.send(embed=embed)

@bot.command(name="say")
async def say(ctx, *args):
    str = ""
    for argv in args:
        str += argv + " "
    print(str)
    tts = gTTS(str)
    tts.save('C:/Users/david/Documents/Hamud/say.mp3')
    voice = await ctx.author.voice.channel.connect()
    voice.play(discord.FFmpegPCMAudio('C:/Users/david/Documents/Hamud/say.mp3'))
    while voice.is_playing():
        await asyncio.sleep(1)
    await voice.disconnect()

@bot.command(name="join")
async def join(ctx):
    voice = await ctx.author.voice.channel.connect()
    voice.play(discord.FFmpegPCMAudio('C:/Users/david/Documents/Hamud/audio.mp3'))
    counter = 0
    duration = 18
    while not counter >= duration:
        await asyncio.sleep(1)
        counter = counter + 1
    await voice.disconnect()


bot.run('NzY5NjY1MjQ5NDcyNDEzNzA2.X5SUnw.aA01C3gI3qG1aJOX-b_KF3vE9DA')