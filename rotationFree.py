import requests, discord
from discord.ext import commands

from vars import api_key,language

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents = intents)

@client.command()
async def rotation(ctx):
    global language
    url_rota = "https://euw1.api.riotgames.com/lol/platform/v3/champion-rotations"
    api_rota_url = url_rota + "?api_key=" + api_key

    response_rota = requests.get(api_rota_url)

    names_champions_weekly = set()

    if response_rota.status_code == 200:
        response_rota_data = response_rota.json()

        if response_rota_data:
            ids_rota = response_rota_data["freeChampionIds"]

            url_Name = "https://ddragon.leagueoflegends.com/cdn/13.22.1/data/en_US/champion.json"
            responseName = requests.get(url_Name)

            if responseName.status_code == 200:
                response_champion_name = responseName.json()

                for champ_names, champion_data in response_champion_name["data"].items():
                    id_champ = int(champion_data["key"])

                    if id_champ in ids_rota:
                        names_champions_weekly.add(champ_names)

                champions_string = ", ".join(names_champions_weekly)
                if language == "FR":
                    await ctx.send(f"Voici les champions gratuits de la semaine : {champions_string}")
                elif language == "EN":
                    await ctx.send(f"Here are the free champions :  {champions_string}")
                elif language == "GER":
                    await ctx.send(f"Hier sind die kostenlosen Champions der Woche :  {champions_string}")
                elif language == "IT":
                    await ctx.send(f"Ecco i campioni gratuiti della settimana : {champions_string}")
                elif language == "ES":
                    await ctx.send(f"Aquí están los campeones gratuitos de la semana : {champions_string}")
                elif language == "JP":
                    await ctx.send(f"今週の無料チャンピオンは次のとおりです。{champions_string}")
                elif language == "KR":
                    await ctx.send(f"금주의 무료 챔피언은 다음과 같습니다.{champions_string}")
    else:
        await ctx.send("**DATA ERROR**")
