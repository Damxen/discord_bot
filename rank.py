import requests
from vars import api_key, pseudo

import discord
from discord.ext import commands
from vars import language

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents = intents)

@client.command()
async def rank_pseudo(ctx, pseudo):
    global language
    
    get_sumID_url = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
    api_sumID_url = get_sumID_url + pseudo +"?api_key=" + api_key

    responseSumID = requests.get(api_sumID_url)

    if responseSumID.status_code == 200:
        responseSumID_data = responseSumID.json()

        if responseSumID_data:
            encrypted_summoner_id = responseSumID_data["id"]
    else:
        print(f"Erreur de requête : {responseSumID.status_code}")


        #----------------------------
    rank_url = "https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/"
    api_rank_url = rank_url + encrypted_summoner_id+"?api_key=" + api_key

    responseRank = requests.get(api_rank_url)

    if responseRank.status_code == 200:
        responseRank_data = responseRank.json()

        if responseRank_data :

            tier = responseRank_data[0]["tier"]
            rank = responseRank_data[0]["rank"]
            wins = responseRank_data[0]["wins"]
            losses = responseRank_data[0]["losses"]

            totGames = wins + losses
            WR = wins/totGames*100
            realWR = str(WR).replace('.','')[:2]

            await ctx.send(f"{pseudo} : {tier} {rank}, {realWR}% WR - {totGames} played.")
        else:
            await ctx.send("**NONE**")
    else:
        await ctx.send("**DATA ERROR, PLEASE TRY LATER**")


@client.command()
async def rank_solo(ctx):
    url = "https://euw1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I?page=1"
    api_url = url + "&api_key=" + api_key

    response = requests.get(api_url)

    if response.status_code == 200:
        response_data = response.json()

        if response_data:
            first_entry = response_data[0]
            summoner_name = first_entry["summonerName"]
            league_points = first_entry["leaguePoints"]
            wins = first_entry["wins"]
            losses = first_entry["losses"]
            totGames = wins + losses
            WR = wins / totGames * 100
            aVirgule = str(WR)
            realWR = aVirgule.replace('.', '')[:2]

            await ctx.send(f"Rank 1 Solo: {summoner_name}, {league_points} LPs. {realWR}% , {totGames} played.")
        else:
            await ctx.send("**NONE**")
    else:
        await ctx.send("**DATA ERROR, PLEASE TRY LATER**")

@client.command()
async def rank_flex(ctx):
    url = "https://euw1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_FLEX_SR/CHALLENGER/I?page=1"
    api_url = url + "&api_key=" + api_key

    response = requests.get(api_url)

    if response.status_code == 200:

        response_data = response.json()

        if response_data:

            first_entry = response_data[0]
            summoner_name = first_entry["summonerName"]
            league_points = first_entry["leaguePoints"]
            wins = first_entry["wins"]
            losses = first_entry["losses"]
            totGames = wins + losses
            WR = wins/totGames*100
            aVirgule = str(WR)
            realWR = aVirgule.replace('.','')[:2]

            await ctx.send(f"Rank 1 Flex: {summoner_name}, {league_points} LPs. {realWR}% , {totGames} played.")
        else:
            await ctx.send("**NONE**")
    else:
        await ctx.send("**DATA ERROR, PLEASE TRY LATER**")

