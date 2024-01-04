import requests, discord
from discord.ext import commands

from vars import api_key, pseudo, tagLine,language

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def challenges(ctx, pseudo, tagLine):
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
    challenge_url = "https://euw1.api.riotgames.com/lol/challenges/v1/player-data/"
    api_challenge_url = challenge_url + PUUID+"?api_key=" + api_key
    responseChallenge = requests.get(api_challenge_url)

    if responseChallenge.status_code == 200:
        responseChallenge_data = responseChallenge.json()

        if responseChallenge_data:

            elo_challenge = responseChallenge_data["totalPoints"]["level"]
            if language == "FR":
                await ctx.send("Ton rank de challenge est : "+elo_challenge)
            elif language == "EN":
                await ctx.send("Your challenge rank is : "+elo_challenge)
            elif language == "ES":
                await ctx.send("Tu rango de desafío es : "+elo_challenge)
            elif language == "GER":
                await ctx.send("Ihr Challenge-Rang ist : "+elo_challenge)
            elif language == "IT":
                await ctx.send("Il tuo grado di sfida è : "+elo_challenge)
            elif language == "JP":
                await ctx.send("あなたのチャレンジランクは次のとおりです。 "+elo_challenge)
            elif language == "KR":
                await ctx.send("귀하의 도전 순위는 다음과 같습니다: "+elo_challenge)
        
    else:
        await ctx.send("**DATA ERROR, PLEASE TRY LATER**")
