import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import pyttsx3 
engine=pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices['''VOICE ID'''].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 120)
volume = engine.getProperty('volume')
engine.setProperty('volume',1.4)
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='.', intents=intents, fetch_offline_members =True)
kanal=[] # your own text channels ID should be here
t_chanel=0


@client.event
async def on_ready():
    r=False
    print("Ok working bot")
    global kanal
    global voices
    global engine
    global t_chanel
    i=0
    server = client.get_guild('''GUILD id''')
    while True:
        server = client.get_guild('''GUILD id''')
        mess=input("|| ME: ")
        if mess.startswith('!'):
            if mess=='!channel_text':
                t_chanel= server.get_channel(kanal[0])
                print('Вы на "channel_text"')
            elif mess=='!channel_voice':
                v_channel= server.get_channel('''YOUR CHANNEL ID''')
                if r==True:
                    print('Выхожу из "channel_voice"')
                    r=False
                    await vc.disconnect()
                else:
                    print('Захожу в "channel_voice"')
                    vc=await v_channel.connect(timeout=9999.0)
                    r=True
                    
        '''===You can add even more(if and elses) or remove if you don't have so much channels'''
        
        if (mess.startswith('?')) and (r==True):
            engine.save_to_file(mess, f'war{i}.mp3')
            engine.runAndWait()
            engine.stop()
            audio=discord.FFmpegPCMAudio(executable="path/ffmpeg.exe",source=f'path/war{i}.mp3')
            vc.play(audio)
            i+=1
        elif (mess.startswith('?')) and (r== False):
            print('Зайдите в голосовой канал')
        else:
            await t_chanel.send(mess)


@client.listen('on_message')
async def message(message):
    channel= message.channel
    if message.author.id!='''bot id''':
        print(f'||{message.author}: {message.content}   |{channel}')


            
    

client.run('token')

'''COMMANDS: !text- to get in channel(text and voice both)
             ?text- bot says "text" in  voice channel
    "vc is not defined"-error is ok, code will work fine, there should be another one, but without channels ID in kanal it will not raise.'''
