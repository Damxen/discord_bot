import os
import requests, discord

from discord.ext import commands
from vars import command, wanted,language

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents = intents)

@client.command()
async def champions(ctx, command, wanted):
    global language

    if language == "FR":
        url = "https://ddragon.leagueoflegends.com/cdn/13.22.1/data/fr_FR/champion.json"
    elif language == "EN":
        url = "https://ddragon.leagueoflegends.com/cdn/13.22.1/data/en_US/champion.json"
    elif language == "IT":
        url = "https://ddragon.leagueoflegends.com/cdn/13.22.1/data/it_IT/champion.json"
    elif language == "ES":
        url = "https://ddragon.leagueoflegends.com/cdn/13.22.1/data/de_DE/champion.json"
    elif language == "GER":
        url = "https://ddragon.leagueoflegends.com/cdn/13.22.1/data/en_US/champion.json"
    elif language == "JP":
        url = "https://ddragon.leagueoflegends.com/cdn/13.22.1/data/ja_JP/champion.json"
    elif language == "KR":
        url = "https://ddragon.leagueoflegends.com/cdn/13.22.1/data/ko_KR/champion.json"
    

    response = requests.get(url)

    counters = {
        "aatrox": ["Fiora", "Tryndamere", "Teemo"],
        "ahri": ["LeBlanc", "Fizz", "Kassadin"],
        "akali": ["Diana", "Malzahar", "Lissandra"],
        "akshan":["Aurelion Sol", "Irelia", "Veigar"],
        "alistar":["Soraka", "Vel'Koz", "Janna"],
        "amumu":["Rengar", "Ivern", "Zac"],
        "anivia":["Diana", "Viktor", "Akali"],
        "annie":["Galio", "Tristana", "Talon"],
        "aphelios":["Twitch", "Seraphine", "Samira"],
        "ashe":["Seraphine", "Ziggs","Twitch"],
        "aurelion sol":["Fizz","Qiyana","Kassadin"],
        "azir":["Taliyah","Naafiri","Xerath"],
        "bard":["Senna","Brand","Renata Glasc"],
        "bel'veth":["Gragas","Rek'Sai","Master Yi"],
        "blitzcrank":["Taric","Leona","Rakan"],
        "brand":["Sona","Zyra","Maokai"],
        "braum":["Morgana","Neeko","Vel'Koz"],
        "briar":["Rammus","Jax","Master Yi"],
        "caitlyn":["Seraphine","Ziggs","Yasuo"],
        "camille":["Teemo","Poppy","Jax"],
        "cassiopeia":["Zoe","Talon","Ekko"],
        "cho'gath":["Vayne","Gwen","Dr. Mundo"],
        "corki":["Annie","Kassadin","Xerath"],
        "darius":["Quinn","Vayne","Dr. Mundo"],
        "diana":["Ivern","Rammus","Briar"],
        "dr.mundo":["Tryndamere","Riven","Aatrox"],
        "draven":["Ziggs","Yasuo","Twitch"],
        "ekko":["Kindred","Evelynn","Rek'Sai"],
        "elise":["Karthus","Rammus","Udyr"],
        "evelynn":["Ivern","Rek'Sai","Briar"],
        "ezreal":["Seraphine","Vayne","Kog'Maw"],
        "fiddlesticks":["Zac","Briar","Karthus"],
        "fiora":["Poppy","Vayne","Riven"],
        "fizz":["Kassadin","Galio","Sylas"],
        "galio":["Swain","Ryze","Qiyana"],
        "gangplank":["Rengar","Quinn","Kayle"],
        "garen":["Camille","Kayle","Vayne"],
        "gnar":["Vayne","Poppy","Yasuo"],
        "gragas":["Rammus","Nocturne","Taliyah"],
        "graves":["Rammus","Evelynn","Fiddlesticks"],
        "gwen":["Singed","Warwick","Riven"],
        "hecarim":["Rek'Sai","Ivern","Kindred"],
        "heimerdinger":["Maokai","Xerath","Neeko"],
        "illaoi":["Varus","Kayle","Vayne"],
        "irelia":["Taliyah","Malphite","Vladimir"],
        "ivern":["Rek'Sai","Fiddlesticks","Rammus"],
        "janna":["Sona","Soraka","Senna"],
        "jarvan iv":["Karthus","Kindred","Master Yi"],
        "jax":["Dr.Mundo","Rengar","Singed"],
        "jayce":["Rengar","Poppy","Malphite"],
        "jhin":["Seraphine","Vayne","Yasuo"],
        "jinx":["Seraphine","Twitch","Ziggs"],
        "k'sante":["Poppy","Fiora","Tryndamere"],
        "kai'sa":["Kog'Maw","Nilah","Ashe"],
        "kalista":["Kog'Maw","Ziggs","Miss Fortune"],
        "karma":["Maokai","Pyke","Blitzcrank"],
        "karthus":["Evelynn","Sejuani","Ivern"],
        "kassadin":["Swain","Pantheon","Akshan"],
        "katarina":["Vladimir","Galio","Zoe"],
        "kayle":["Poppy","Nasus","Tryndamere"],
        "kayn":["Fiddlesticks","Poppy","Master Yi"],
        "kennen":["Ornn","Rengar","Urgot"],
        "kha'zix":["Rengar","Rek'Sai","Nidalee"],
        "kindred":["Ivern","Rammus","Master Yi"],
        "kled":["Vayne","Singed","Quinn"],
        "kog'maw":["Seraphine","Yasuo","Twitch"],
        "leblanc":["Naafiri","Akshan","Kassadin"],
        "lee sin":["Ivern","Rek'Sai","Brand"],
        "leona":["Vel'Koz","Taric","Janna"],
        "lillia":["Rek'Sai","Talon","Briar"],
        "lissandra":["Annie","Galio","Xerath"],
        "lucian":["Kog'Maw","Ziggs","Ashe"],
        "lulu":["Sona","Senna","Bard"],
        "lux":["Shaco","Blitzcrank","Xerath"],
        "maître yi":["Rammus","Zac","Warwick"],
        "malphite":["Sylas","Ornn","Tahm Kench"],
        "malzahar":["Galio","Akshan","Talon"],
        "maokai":["Karthus","Xin Zhao","Rammus"],
        "milio":["Blitzcrank","Taric","Braum"],
        "miss fortune":["Kog'Maw","Seraphine","Ziggs"],
        "mordekaiser":["Vayne","Olaf","Poppy"],
        "morgana":["Zyra","Janna","Milio"],
        "naafiri":["Neeko","Talon","Vex"],
        "nami":["Blitz","Zilean","Bard"],
        "nasus":["Shen","Sylas","Illaoi"],
        "nautilus":["Renata Glasc","Rell","Rakan"],
        "neeko":["Vel'Koz","Zilean","Sona"],
        "nidalee":["Briar","Rammus","Bel'Veth"],
        "nilah":["Vayne","Xayah","Miss Fortune"],
        "nocturne":["Ivern","Rammus","Evelynn"],
        "nunu & willump":["Gragas","Briar","Ivern"],
        "olaf":["Kled","Trundle","Vayne"],
        "orianna":["Taliyah","Talon","Annie"],
        "ornn":["Singed","K'Sante","Fiora"],
        "pantheon":["Yorick","Tahm Kench","Singed"],
        "poppy":["Nocturne","Ivern","Taliyah"],
        "pyke":["Rakan","Maokai","Blitzcrank"],
        "qiyana":["Malphite","Anivia","Pantheon"],
        "quinn":["Dr.Mundo","Nasus","Malphite"],
        "rakan":["Sona","Soraka","Renata Glasc"],
        "rammus":["Shaco","Udyr","Lillia"],
        "rek'sai":["Karthus","Amumu","Nunu & Willump"],
        "rell":["Vel'Koz","Sona","Alistar"],
        "renata glasc":["Xerath","Zilean","Shaco"],
        "renekton":["Singed","Illaoi","Warwick"],
        "rengar":["Master Yi","Bel'Veth","Warwick"],
        "riven":["Quinn","Vayne","Kennen"],
        "rumble":["Olaf","Warwick","Ornn"],
        "ryze":["Naafiri","Taliyah","Anivia"],
        "samira":["Nilah","Xayah","Jinx"],
        "sejuani":["Ivern","Trundle","Brand"],
        "senna":["Blitzcrank","Xerath","Zyra"],
        "séraphine":["Maokai","Shaco","Zilean"],
        "sett":["Warwick","Vayne","Singed"],
        "shaco":["Briar","Talon","Graves"],
        "shen":["Singed","Vayne","Gwen"],
        "shyvana":["Ivern","Evelynn","Udyr"],
        "singed":["Gangplank","Dr. Mundo","Camille"],
        "sion":["Gwen","Riven","Tryndamere"],
        "sivir":["Twitch","Vayne","Draven"],
        "skarner":["Elise","Amumu","Taliyah"],
        "sona":["Taric","Seraphine","Zilean"],
        "soraka":["Blitzcrank","Maokai","Taric"],
        "swain":["Neeko","Zilean","Milio"],
        "sylas":["Taliayh","Akshan","Vex"],
        "syndra":["Xerath","Fizz","Katarina"],
        "tahm kench":["Riven","Vayne","Urgot"],
        "taliyah":["Ivern","Udyr","Nunu & Willump"],
        "talon":["Neeko","Akshan","Malphite"],
        "taric":["Janna","Morgana","Bard"],
        "teemo":["Vladimir","Ryze","Ornn"],
        "tresh":["Taric","Maokai","Rakan"],
        "tristana":["Kog'Maw","Nilah","Vayne"],
        "trundle":["Quinn","Vayne","Jax"],
        "tryndamere":["Malphite","Quinn","Poppy"],
        "twisted fate":["Diana","Pantheon","Kassadin"],
        "twitch":["Seraphine","Nilah","Vayne"],
        "udyr":["Ivern","Vi","Rek'Sai"],
        "urgot":["Ornn","Malphite","Kayle"],
        "varus":["Seraphine","Ziggs","Yasuo"],
        "vayne":["Seraphine","Draven","Miss Fortune"],
        "veigar":["Taliyah","Swain","Qiyana"],
        "vel'koz":["Maokai","Zyra","Xerath"],
        "vex":["Swain","Taliyah","Kassadin"],
        "vi":["Jax","Rek'Sai","Ivern"],
        "viego":["Rammus","Ivern","Karthus"],
        "viktor":["Akshan","Galio","Talon"],
        "vladimir":["Galio","Malzahar","Kassadin"],
        "volibear":["Quinn","Kayle","Rumble"],
        "warwick":["Ivern","Evelynn","Karthus"],
        "wukong":["Ivern","Talon","Taliyah"],
        "xayah":["Ashe","Ziggs","Draven"],
        "xerath":["Sylas","Janna","Sona"],
        "xin zhao":["Rek'Sai","Zac","Elise"],
        "yasuo":["Taliyah","Aurelion Sol","Renekton"],
        "yone":["Vex","Neeko","Taliyah"],
        "yorick":["Warwick","Irelia","Riven"],
        "yuumi":["Taric","Rell","Braum"],
        "zac":["Udyr","Trundle","Talon"],
        "zed":["Akshan","Zoe","Anivia"],
        "zeri":["Kog'Maw","Seraphine","Vayne"],
        "ziggs":["Vayne","Yasuo","Tristana"],
        "zilean":["Sylas","Janna","Soraka"],
        "zoe":["Naafiri","Tristana","Annie"],
        "zyra":["Taric","Sona","Bard"],
    }

    if response.status_code == 200:

        data = response.json()

        wanted_formatted = wanted.lower()    
        command_formatted = command#.capitalize()

        if wanted_formatted == "title" and command_formatted in data["data"]:
            title = data["data"][command_formatted][wanted_formatted] + " " + data["data"][command_formatted]["blurb"]
            await ctx.send(f"```{command_formatted}: {title}```")
            print(language)

        elif command_formatted == "Version" or command_formatted == "version" :
            version = data["version"]
            await ctx.send(f"Patch : {version}")
        
        elif wanted_formatted == "image":
            images_folder = "./img_splash_champs/"
            image_path = os.path.join(images_folder, f"{command}_0.jpg")
            if os.path.exists(image_path):
                await ctx.send(file=discord.File(image_path))
            else:
                await ctx.send(f"```{command_formatted}: {wanted_formatted} information not available```")

        elif wanted_formatted == "tags" and command_formatted in data["data"]:
            tags = data["data"][command_formatted][wanted_formatted]
            await ctx.send(f"{command_formatted}'s tags : {', '.join(tags)}")

        elif wanted_formatted == "stats" and command_formatted in data["data"]:
            stats = data["data"][command_formatted][wanted_formatted]
            await ctx.send(f"```{command_formatted}'s stats : {stats}```" )

        elif command_formatted == "Counter" and wanted_formatted in counters:
            champion_counters = counters[wanted_formatted]
            await ctx.send(f"Counters de **{wanted_formatted}** : {', '.join(champion_counters)}")

        else:
            await ctx.send("**RESPONSE ERROR**")
    else:
        await ctx.send("**ERROR COMMAND**")
