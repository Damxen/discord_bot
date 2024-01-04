import asyncio
import os
import discord

from discord.ext import commands

from histo import CommandHistory
from save import load_data
from vars import api_key,pseudo,tagLine,command,wanted, language
from challenges import challenges
from data_champs import champions
from maîtrises import masteries
from rank import rank_flex, rank_pseudo, rank_solo
from rotationFree import rotation
from tree import ConversationTree

language = "EN"

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)
histo_commands = CommandHistory()
conversation_tree = ConversationTree(client)

command_history, conversation_progress = load_data()

histo_commands.command_history = command_history
histo_commands.conversation_progress = conversation_progress

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="!Commands"))
    print(f'Connected as {client.user.name}')

@client.event
async def on_message(message):
    global language
    pseudo, tagLine, command, wanted = "","","",""   

    if message.author == client.user:
        return    
#-----------------------------------
    elif message.content.startswith("!TopSolo") or message.content.startswith("!topsolo") or message.content.startswith("!topSolo") or message.content.startswith("!Topsolo"):
        try:
            context = await client.get_context(message)
            await rank_solo(context)
        except Exception as e:
            print(f"An error occurred: {e}")
            await message.channel.send("**ERROR, PLEASE TRY LATER**")
#-----------------------------------

    elif message.content.startswith("!TopFlex") or message.content.startswith("!topflex") or message.content.startswith("!topFlex") or message.content.startswith("!Topflex"):
        try:
            context = await client.get_context(message)
            await rank_flex(context)
        except Exception as e:
            print(f"An error occurred: {e}")
            await message.channel.send("**ERROR, PLEASE TRY LATER**")
#-----------------------------------

    elif message.content.startswith("!Rank") or message.content.startswith("!rank"):
        def check(response):
            return response.author == message.author and response.channel == message.channel
        if language == "FR":
            try:
                await message.channel.send("Quel est ton pseudo ? (sans le #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                pseudo = response.content
                context = await client.get_context(message)
                await rank_pseudo(context, pseudo)
            except asyncio.TimeoutError:
                await message.channel.send("Temps écoulé !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("Je ne retrouve pas ce joueur...")
        elif language == "EN":
            try:
                await message.channel.send("What is your nickname ? (without the #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                pseudo = response.content
                context = await client.get_context(message)
                await rank_pseudo(context, pseudo)
            except asyncio.TimeoutError:
                await message.channel.send("Time's up ! Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("I don't find this player...")
        elif language == "ES":
            try:
                await message.channel.send("Cual es su apodo ? (sin el #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                pseudo = response.content
                context = await client.get_context(message)
                await rank_pseudo(context, pseudo)
            except asyncio.TimeoutError:
                await message.channel.send("Tiempo pasado !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("No encuentro este reproductor...")
        elif language == "GER":
            try:
                await message.channel.send("Was ist dein Username ? (ohne das #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                pseudo = response.content
                context = await client.get_context(message)
                await rank_pseudo(context, pseudo)
            except asyncio.TimeoutError:
                await message.channel.send("Verstrichene Zeit !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("Ich kann diesen Player nicht finden...")
        elif language == "IT":
            try:
                await message.channel.send("Qual'è il tuo soprannome ? (senza il #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                pseudo = response.content
                context = await client.get_context(message)
                await rank_pseudo(context, pseudo)
            except asyncio.TimeoutError:
                await message.channel.send("Tempo trascorso !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("Non riesco a trovare questo lettore...")
        elif language == "JP":
            try:
                await message.channel.send("あなたのニックネームは何ですか ？ (#なし)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                pseudo = response.content
                context = await client.get_context(message)
                await rank_pseudo(context, pseudo)
            except asyncio.TimeoutError:
                await message.channel.send("時間が経過した ！")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("このプレイヤーが見つからない...")
        elif language == "KR":
            try:
                await message.channel.send("당신의 별명은 무엇입니까? (# 제외)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                pseudo = response.content
                context = await client.get_context(message)
                await rank_pseudo(context, pseudo)
            except asyncio.TimeoutError:
                await message.channel.send("시간이 경과되었습니다!")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("이 선수를 못찾겠어요...")
        #histo_commands.add_command(message.author.id, message.content)
#-----------------------------------

    elif message.content.startswith("!Description") or message.content.startswith("!description"):
        def check(response):
            return response.author == message.author and response.channel == message.channel
        if language == "FR":
            try:
                wanted = "title"
                await message.channel.send("De quel champion veux-tu voir la description ?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("Temps écoulé !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("Je ne retrouve pas ce champion...")
        elif language == "EN":
            try:
                wanted = "title"
                await message.channel.send("Which champion do you want to see the description of ?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("Time's up ! Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("I don't find this champion...")
        elif language == "ES":
            try:
                wanted = "title"
                await message.channel.send("¿De qué campeón quieres ver la descripción?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("Tiempo pasado !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("No encuentro este campeón...")
        elif language == "GER":
            try:
                wanted = "title"
                await message.channel.send("Von welchem ​​Champion möchtest du die Beschreibung sehen?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("Verstrichene Zeit !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("Ich kann diesen Champion nicht finden ...")
        elif language == "IT":
            try:
                wanted = "title"
                await message.channel.send("Di quale campione vuoi vedere la descrizione?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("Tempo trascorso !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("Non riesco a trovare questo campione...")
        elif language == "JP":
            try:
                wanted = "title"
                await message.channel.send("どのチャンピオンの説明を見たいですか?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("時間が経過した ！")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("このチャンピオンが見つからない...")
        elif language == "KR":
            try:
                wanted = "title"
                await message.channel.send("어떤 챔피언에 대한 설명을 보고 싶으신가요?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("시간이 경과되었습니다!")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("챔피언을 못찾겠어요...")
#-----------------------------------

    elif message.content.startswith("!Version") or message.content.startswith("!version"):
        try:
            command = "Version"
            context = await client.get_context(message)
            await champions(context,command, wanted)
        except Exception as e:
            print(f"An error occurred: {e}")
            await message.channel.send("**ERROR, PLEASE TRY LATER**")
#-----------------------------------

    elif message.content.startswith("!Commands") or message.content.startswith("!commands"):
        try:
            await message.channel.send("```Commands : \n\n !Commands\n !Help\n !Language\n !Version\n !Description\n !Image\n !Tags\n !Stats\n !Counter \n !Rotation\n !TopSolo\n !TopFlex\n !Rank\n !Challenge\n !Masteries```")
        except Exception as e:
            print(f"An error occurred: {e}")
            await message.channel.send("**ERROR, PLEASE TRY LATER**")
#-----------------------------------

    elif message.content.startswith("!Counter") or message.content.startswith("!counter"):
        def check(response):
            return response.author == message.author and response.channel == message.channel
        try:
            command = "Counter"
            await message.channel.send("De quel champion veux-tu voir les counters ?")
            response = await client.wait_for('message', check=check, timeout=30.0)
            wanted = response.content
            context = await client.get_context(message)
            await champions(context, command, wanted)
        except asyncio.TimeoutError:
            await message.channel.send("Temps écoulé !")
        except Exception as e:
            print(f"An error occurred: {e}")
            await message.channel.send("Ah, j'ai un problème dans mes données... Je règle ça vite !")
#-----------------------------------
    
    elif message.content.startswith("!Image") or message.content.startswith("!image"):
        def check(response):
            return response.author == message.author and response.channel == message.channel
        if language == "FR":
            try:
                wanted = "image"
                await message.channel.send("De quel champion veux-tu voir l'image ?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("Temps écoulé !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("Je ne retrouve pas ce champion...")
        elif language == "EN":
            try:
                wanted = "image"
                await message.channel.send("Which champion do you want to see the image of ?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("Time's up ! Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("I don't find this champion...")
        elif language == "ES":
            try:
                wanted = "image"
                await message.channel.send("¿De qué campeón quieres ver la imagen?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("Tiempo pasado !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("No encuentro este campeón...")
        elif language == "GER":
            try:
                wanted = "image"
                await message.channel.send("Von welchem ​​Champion möchtest du das Bild sehen?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("Verstrichene Zeit !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("Ich kann diesen Champion nicht finden ...")
        elif language == "IT":
            try:
                wanted = "image"
                await message.channel.send("Di quale campione vuoi vedere l'immagine ?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("Tempo trascorso !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("Non riesco a trovare questo campione...")
        elif language == "JP":
            try:
                wanted = "image"
                await message.channel.send("どのチャンピオンの画像を見たいですか?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("時間が経過した ！")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("このチャンピオンが見つからない...")
        elif language == "KR":
            try:
                wanted = "image"
                await message.channel.send("어떤 챔피언의 이미지를 보고 싶으신가요?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("시간이 경과되었습니다!")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("챔피언을 못찾겠어요...")
#-----------------------------------
   
    elif message.content.startswith("!Tags") or message.content.startswith("!tags"):
        def check(response):
            return response.author == message.author and response.channel == message.channel
        if language == "FR":
            try:
                wanted = "tags"
                await message.channel.send("De quel champion veux-tu voir les tags ?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("Temps écoulé !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("Je ne retrouve pas ce champion...")
        elif language == "EN":
            try:
                wanted = "tags"
                await message.channel.send("Which champion do you want to see the tags of ?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("Time's up ! Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("I don't find this champion...")
        elif language == "ES":
            try:
                wanted = "tags"
                await message.channel.send("¿De qué campeón quieres ver las etiquetas?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("Tiempo pasado !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("No encuentro este campeón...")
        elif language == "GER":
            try:
                wanted = "tags"
                await message.channel.send("Von welchem ​​Champion möchtest du die Tags sehen?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("Verstrichene Zeit !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("Ich kann diesen Champion nicht finden ...")
        elif language == "IT":
            try:
                wanted = "tags"
                await message.channel.send("Di quale campione vuoi vedere i tag?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("Tempo trascorso !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("Non riesco a trovare questo campione...")
        elif language == "JP":
            try:
                wanted = "tags"
                await message.channel.send("どのチャンピオンのタグを見たいですか?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("時間が経過した ！")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("このチャンピオンが見つからない...")
        elif language == "KR":
            try:
                wanted = "tags"
                await message.channel.send("어떤 챔피언의 태그를 보고 싶으신가요?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("시간이 경과되었습니다!")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("챔피언을 못찾겠어요...")
#-----------------------------------
    
    elif message.content.startswith("!Stats") or message.content.startswith("!stats"):
        def check(response):
            return response.author == message.author and response.channel == message.channel
        if language == "FR":
            try:
                wanted = "stats"
                await message.channel.send("De quel champion veux-tu voir les stats ?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("Temps écoulé !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("Je ne retrouve pas ce champion...")
        elif language == "EN":
            try:
                wanted = "stats"
                await message.channel.send("Which champion do you want to see the stats of ?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("Time's up ! Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("I don't find this player...")
        elif language == "ES":
            try:
                wanted = "stats"
                await message.channel.send("¿De qué campeón quieres ver las estadísticas?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("Tiempo pasado !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("No encuentro este reproductor...")
        elif language == "GER":
            try:
                wanted = "stats"
                await message.channel.send("Von welchem ​​Champion möchtest du die Statistiken sehen ?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("Verstrichene Zeit !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("Ich kann diesen Player nicht finden...")
        elif language == "IT":
            try:
                wanted = "stats"
                await message.channel.send("Di quale campione vuoi vedere le statistiche ?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("Tempo trascorso !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("Non riesco a trovare questo lettore...")
        elif language == "JP":
            try:
                wanted = "stats"
                await message.channel.send("どのチャンピオンの統計を見たいですか?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("時間が経過した ！")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("このプレイヤーが見つからない...")
        elif language == "KR":
            try:
                wanted = "stats"
                await message.channel.send("어떤 챔피언의 통계를 보고 싶으신가요?")
                response = await client.wait_for('message', check=check, timeout=30.0)
                command = response.content
                context = await client.get_context(message)
                await champions(context,command,wanted)
            except asyncio.TimeoutError:
                await message.channel.send("시간이 경과되었습니다!")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("이 선수를 못찾겠어요...")
#-----------------------------------
    
    elif message.content.startswith("!Rotation") or message.content.startswith("!rotation"):
        try:
            context = await client.get_context(message)
            await rotation(context)
        except Exception as e:
            print(f"An error occurred: {e}")
            await message.channel.send("**ERROR, PLEASE TRY LATER**")
#-----------------------------------

    elif message.content.startswith("!Challenge") or message.content.startswith("!challenge"):
        def check(response):
            return response.author == message.author and response.channel == message.channel
        if language =="FR":
            try:
                await message.channel.send("Quel est ton pseudo ? (sans le #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                pseudo = response.content
                await message.channel.send("Ok super, et ton ID ? (le #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                tagLine = response.content
                context = await client.get_context(message)
                await challenges(context, pseudo, tagLine)
            except asyncio.TimeoutError:
                await message.channel.send("Time's up! Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("Je ne retrouve pas ce joueur...")
        elif language == "EN":
            try:
                await message.channel.send("What's your gameName ? (without #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                pseudo = response.content
                await message.channel.send("Ok good, now your ID ? (#)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                tagLine = response.content
                context = await client.get_context(message)
                await challenges(context, pseudo, tagLine)
            except asyncio.TimeoutError:
                await message.channel.send("Time's up ! Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("I don't find this player...")
        elif language == "ES":
            try:
                await message.channel.send("Cual es su apodo ? (sin el #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                pseudo = response.content
                await message.channel.send("Ok, genial, ¿y tu identificación? (el #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                tagLine = response.content
                context = await client.get_context(message)
                await challenges(context, pseudo, tagLine)
            except asyncio.TimeoutError:
                await message.channel.send("Tiempo pasado !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("No encuentro este reproductor...")
        elif language == "GER":
            try:
                await message.channel.send("Was ist dein Username ? (ohne das #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                pseudo = response.content
                await message.channel.send("Ok, großartig, und dein Ausweis? (der #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                tagLine = response.content
                context = await client.get_context(message)
                await challenges(context, pseudo, tagLine)
            except asyncio.TimeoutError:
                await message.channel.send("Verstrichene Zeit !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("Ich kann diesen Player nicht finden...")
        elif language == "IT":
            try:
                await message.channel.send("Qual'è il tuo soprannome ? (senza il #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                pseudo = response.content
                await message.channel.send("Ok fantastico, e il tuo documento d'identità? (IL #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                tagLine = response.content
                context = await client.get_context(message)
                await challenges(context, pseudo, tagLine)
            except asyncio.TimeoutError:
                await message.channel.send("Tempo trascorso !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("Non riesco a trovare questo lettore...")
        elif language == "JP":
            try:
                await message.channel.send("あなたのニックネームは何ですか ？ (#なし)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                pseudo = response.content
                await message.channel.send("わかりました。それであなたの ID は? (#)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                tagLine = response.content
                context = await client.get_context(message)
                await challenges(context, pseudo, tagLine)
            except asyncio.TimeoutError:
                await message.channel.send("時間が経過した ！")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("このプレイヤーが見つからない...")
        elif language == "KR":
            try:
                await message.channel.send("당신의 별명은 무엇입니까? (# 제외)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                pseudo = response.content
                await message.channel.send("좋습니다. 신분증은요? (그 #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                tagLine = response.content
                context = await client.get_context(message)
                await challenges(context, pseudo, tagLine)
            except asyncio.TimeoutError:
                await message.channel.send("시간이 경과되었습니다!")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("이 선수를 못찾겠어요...")
#-----------------------------------
    
    elif message.content.startswith("!Masteries") or message.content.startswith("!masteries"):
        def check(response):
            return response.author == message.author and response.channel == message.channel
        if language == "FR":
            try:
                await message.channel.send("Quel est ton pseudo ? (sans le #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                pseudo = response.content
                await message.channel.send("Ok super, et ton ID ? (le #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                tagLine = response.content
                context = await client.get_context(message)
                await masteries(context, pseudo, tagLine)
            except asyncio.TimeoutError:
                await message.channel.send("Temps écoulé !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("Je ne retrouve pas ce joueur...")
        elif language == "EN":
            try:
                await message.channel.send("What's your gameName ? (without #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                pseudo = response.content
                await message.channel.send("Ok good, now your ID ? (#)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                tagLine = response.content
                context = await client.get_context(message)
                await masteries(context, pseudo, tagLine)
            except asyncio.TimeoutError:
                await message.channel.send("Time's up ! Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("I don't find this player...")
        elif language == "ES":
            try:
                await message.channel.send("Cual es su apodo ? (sin el #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                pseudo = response.content
                await message.channel.send("Ok, genial, ¿y tu identificación? (el #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                tagLine = response.content
                context = await client.get_context(message)
                await masteries(context, pseudo, tagLine)
            except asyncio.TimeoutError:
                await message.channel.send("Tiempo pasado !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("No encuentro este reproductor...")
        elif language == "GER":
            try:
                await message.channel.send("Was ist dein Username ? (ohne das #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                pseudo = response.content
                await message.channel.send("Ok, großartig, und dein Ausweis? (der #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                tagLine = response.content
                context = await client.get_context(message)
                await masteries(context, pseudo, tagLine)
            except asyncio.TimeoutError:
                await message.channel.send("Verstrichene Zeit !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("Ich kann diesen Player nicht finden...")
        elif language == "IT":
            try:
                await message.channel.send("Qual'è il tuo soprannome ? (senza il #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                pseudo = response.content
                await message.channel.send("Ok fantastico, e il tuo documento d'identità? (IL #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                tagLine = response.content
                context = await client.get_context(message)
                await masteries(context, pseudo, tagLine)
            except asyncio.TimeoutError:
                await message.channel.send("Tempo trascorso !")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("Non riesco a trovare questo lettore...")
        elif language == "JP":
            try:
                await message.channel.send("あなたのニックネームは何ですか ？ (#なし)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                pseudo = response.content
                await message.channel.send("わかりました。それであなたの ID は? (#)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                tagLine = response.content
                context = await client.get_context(message)
                await masteries(context, pseudo, tagLine)
            except asyncio.TimeoutError:
                await message.channel.send("時間が経過した ！")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("このプレイヤーが見つからない...")
        elif language == "KR":
            try:
                await message.channel.send("당신의 별명은 무엇입니까? (# 제외)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                pseudo = response.content
                await message.channel.send("좋습니다. 신분증은요? (그 #)")
                response = await client.wait_for('message', check=check, timeout=30.0)
                tagLine = response.content
                context = await client.get_context(message)
                await masteries(context, pseudo, tagLine)
            except asyncio.TimeoutError:
                await message.channel.send("시간이 경과되었습니다!")
            except Exception as e:
                print(f"An error occurred: {e}")
                await message.channel.send("이 선수를 못찾겠어요...")
#-----------------------------------    
            
    elif message.content.startswith("!Language") or message.content.startswith("!language"):
        def check(response):
            return response.author == message.author and response.channel == message.channel
        try: 
            await message.channel.send("```Which language do you prefer to speak with me ?\n\n FR - Français\n IT - Italian\n ES - Spanich\n JP - Japanese\n EN - English\n KR - Korean\n GER - German```")
            response = await client.wait_for('message', check=check, timeout=30.0)
            language = response.content
            if language == "EN":
                await message.channel.send("Bot is now speaking English")
            elif language == "FR":
                await message.channel.send("Le bot parle maintenant Français")
            elif language == "IT":
                await message.channel.send("Il bot ora parla italiano")
            elif language == "ES":
                await message.channel.send("El bot ahora habla español")
            elif language == "JP":
                await message.channel.send("ボットが日本語を話すようになりました")
            elif language == "KR":
                await message.channel.send("봇이 이제 한국어로 말해요")
            elif language == "GER":
                await message.channel.send("Der Bot spricht jetzt Deutsch")
        except asyncio.TimeoutError:
            await message.channel.send("Time's up! Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
            await message.channel.send("**ERROR**")

    elif message.content.startswith("!AdminCommands") or message.content.startswith("!adminCommands") or message.content.startswith("!admincommands") or message.content.startswith("!Admincommands"):
        def check(response):
            return response.author == message.author and response.channel == message.channel
        
        await message.channel.send("```Admin Commands\n\n !LCommand\n !AllCommands\n !Del```")

    elif message.content.startswith("!LCommand") or message.content.startswith("!lcommand") or message.content.startswith("!Lcommand") or message.content.startswith("!lCommand"):
        def check(response):
            return response.author == message.author and response.channel == message.channel
        try:
            last_command = await histo_commands.get_last_command(message.author.id)
            await message.channel.send(f'```{last_command}```')
        except Exception as e:
            print(f"An error occurred: {e}")
            await message.channel.send("**ERROR**")

    elif message.content.startswith("!AllCommands") or message.content.startswith("!allCommands") or message.content.startswith("!Allcommands") or message.content.startswith("!allcommands"):
        def check(response):
            return response.author == message.author and response.channel == message.channel
        try:
            user_commands = await histo_commands.get_user_commands(message.author.id)
            await message.channel.send(f'```{message.author.name} :\n\n {user_commands}```')
        except Exception as e:
            print(f"An error occurred: {e}")
            await message.channel.send("**ERROR**")

    elif message.content.startswith("!Del") or message.content.startswith("!del"):
        def check(response):
            return response.author == message.author and response.channel == message.channel
        try:
            await histo_commands.clear_history(message.author.id)
            await message.channel.send('**Cleared**')
        except Exception as e:
            print(f"An error occurred: {e}")
            await message.channel.send("**Cleared**")

    elif message.content.startswith("!Help") or message.content.startswith("!help"):
        def check(response):
            return response.author == message.author and response.channel == message.channel
        try:
            await conversation_tree.start_conversation(message)
        except Exception as e:
            print(f"An error occurred: {e}")
            await message.channel.send("**ERROR**")


    if message.content.startswith("!"): 
        await histo_commands.add_command(str(message.author.id), message.content) 
        await client.process_commands(message)  
    

client.run("MTE2NzM5NzI4MjcyODEyODU2Mg.Gt-mip.qiIJclU8UHrGWNn4zqxI7zFsr95Fc3JW5CR1VY")
