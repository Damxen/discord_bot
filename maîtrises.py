import json
import requests, discord
from discord.ext import commands

from vars import api_key, pseudo, tagLine,language

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def masteries(ctx, pseudo, tagLine):
    global language
    get_uuid_url = "https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/"
    api_uuid_url = get_uuid_url + pseudo +"/"+tagLine +"?api_key=" + api_key

    responseUUID = requests.get(api_uuid_url)

    if responseUUID.status_code == 200:
        responseUUID_data = responseUUID.json()

        if responseUUID_data:
            PUUID = responseUUID_data["puuid"]
        
    else:
        print(f"Erreur de requête : {responseUUID.status_code}")

    #----------------------------
    mastery_url = "https://euw1.api.riotgames.com/lol/champion-mastery/v4/scores/by-puuid/"
    api_mastery_url = mastery_url + PUUID+"?api_key=" + api_key
    
    responseMastery = requests.get(api_mastery_url)

    if responseMastery.status_code == 200:
        responseMastery_data = responseMastery.json()

        if responseMastery_data:
            if language == "FR":
                await ctx.send(f"{pseudo} #{tagLine} possède {json.dumps(responseMastery_data, indent=2)} maîtrises !")
            elif language == "EN":
                await ctx.send(f"{pseudo} #{tagLine} has {json.dumps(responseMastery_data, indent=2)} masteries !")
            elif language == "ES":
                await ctx.send(f"{pseudo} #{tagLine} posee {json.dumps(responseMastery_data, indent=2)} maestrías !")
            elif language == "GER":
                await ctx.send(f"{pseudo} #{tagLine} besitzt {json.dumps(responseMastery_data, indent=2)} master-abschlüsse !")
            elif language == "IT":
                await ctx.send(f"{pseudo} #{tagLine} possiede {json.dumps(responseMastery_data, indent=2)} master !")
            elif language == "JP":
                await ctx.send(f"{pseudo} #{tagLine} 持っている {json.dumps(responseMastery_data, indent=2)} 修士号 !")
            elif language == "KR":
                await ctx.send(f"{pseudo} #{tagLine} 소유하고 있다 {json.dumps(responseMastery_data, indent=2)} 석사 학위 !")
        else:
            await ctx.send("**NONE**")
    else:
        await ctx.send("**DATA ERROR, PLEASE TRY LATER**")