import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import pyttsx3 
engine=pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[4].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 120)
volume = engine.getProperty('volume')
engine.setProperty('volume',1.4)
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='.', intents=intents, fetch_offline_members =True)
kanal=[502490265517293570, 753446436544446515,762570000610623498,762670861597147156]
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
    server = client.get_guild(502490265517293568)
    while True:
        server = client.get_guild(502490265517293568)
        mess=input("|| ME: ")
        if mess.startswith('!'):
            if mess=='!osnova':
                t_chanel= server.get_channel(kanal[0])
                print('Вы на основе')
            elif mess=='!bio':
                t_chanel= server.get_channel(kanal[1])
                print('Вы на био-хим')
            elif mess=='!code':
                t_chanel= server.get_channel(kanal[2])
                print('Вы на коды')
            elif mess=='!fiz':
                t_chanel= server.get_channel(kanal[3])
                print('Вы на физе')
            elif mess=='!durka':
                v_channel= server.get_channel(765403207810678785)
                if r==True:
                    print('Выхожу из "Дурка"')
                    r=False
                    await vc.disconnect()
                else:
                    print('Захожу в "Дурка"')
                    vc=await v_channel.connect(timeout=9999.0)
                    r=True
            elif mess=='!apex':
                v_channel= server.get_channel(764861667791863868)
                if r==True:
                    print('Выхожу из "Apex"')
                    r=False
                    await vc.disconnect()
                else:
                    print('Захожу в "Apex"')
                    vc= await v_channel.connect(timeout=9999.0)
                    r=True
            elif mess=='!cs':
                v_channel= server.get_channel(750898887425917038)
                if r==True:
                    print('Выхожу из "Контер-Стрике"')
                    r=False
                    await vc.disconnect()
                else:
                    print('Захожу в "Контер-Стрике"')
                    vc= await v_channel.connect(timeout=9999.0)
                    r=True
            elif mess=='!budlo':
                v_channel= server.get_channel(705292314997686312)
                if r==True:
                    print('Выхожу из "Быдлокодеры"')
                    r=False
                    await vc.disconnect()
                else:
                    print('Захожу в "Быдлокодеры"')
                    vc=await v_channel.connect(timeout=9999.0)
                    r=True
        elif (mess.startswith('?')) and (r==True):
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
    if message.author.id== 771755859428376626:
        print("||Бот че-то писанул")
    if message.author.id!=774134169953108010:
        print(f'||{message.author}: {message.content}   |{channel}')


            
    

client.run('Nzc0MTM0MTY5OTUzMTA4MDEw.X6TWoA.Hd3iqXqZSYVIcT7VFqe0CSkY6n0')