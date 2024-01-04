import asyncio
import discord

class ConversationTree:
    def __init__(self, client):
        self.client = client
    
    async def reset_conversation(self, message):
        await message.channel.send("**Conversation reset.**")
        await self.start_conversation(message)

    async def stop_conversation(self, message):
        await message.channel.send("**See you later !**")
        return


    async def start_conversation(self, message):
        await message.channel.send("**Welcome to the League of Legends bot. Type 'reset' to restart the conversation, or 'stop' to stop the conversation. Answer with 'yes' or 'no'.**\n\n Do you like League of Legends ?")
        response = await self.get_user_response(message)
        
        if response.lower() == "yes" or response.lower() == "y":
            await self.playLoL(message)
            response = await self.get_user_response(message)
            if response.lower() == "yes" or response.lower() == "y":
                await self.guess(message)
                response = await self.get_user_response(message)
                if response.lower() == "yes" or response.lower() == "y":
                    await self.found(message)
                elif response.lower() == "no" or response.lower() == "n":
                    await self.noFound(message)
                elif response.lower() == "reset":
                    await self.reset_conversation(message)
                    return
                elif response.lower() == "stop":
                    await self.stop_conversation(message)
                elif response.lower().startswith("speak about"):
                    topic = response[12:].strip()
                    await self.speak_about(message, topic)

            elif response.lower() == "no" or response.lower() == "n":
                await self.casual(message)
                response = await self.get_user_response(message)
                if response.lower() == "yes" or response.lower() == "y":
                    await self.fun(message)
                elif response.lower() == "no" or response.lower() == "n":
                    await self.noFun(message)
                elif response.lower() == "reset":
                    await self.reset_conversation(message)
                    return
                elif response.lower() == "stop":
                    await self.stop_conversation(message)
                elif response.lower().startswith("speak about"):
                    topic = response[12:].strip()
                    await self.speak_about(message, topic)

            elif response.lower() == "reset":
                await self.reset_conversation(message)
                return
            elif response.lower() == "stop":
                await self.stop_conversation(message)
            elif response.lower().startswith("speak about"):
                topic = response[12:].strip()
                await self.speak_about(message, topic)
#---------
        elif response.lower() == "no" or response.lower() == "n":
            await self.noPlayLoL(message)
            response = await self.get_user_response(message)
            if response.lower() == "yes" or response.lower() == "y":
                await self.frustrated(message)
            elif response.lower() == "no" or response.lower() == "n":
                await self.moba(message)
                response = await self.get_user_response(message)
                if response.lower() == "yes" or response.lower() == "y":
                    await self.otherGame(message)
                elif response.lower() == "no" or response.lower() == "n":
                    await self.noOtherGame(message)
                elif response.lower() == "reset":
                    await self.reset_conversation(message)
                    return
                elif response.lower() == "stop":
                    await self.stop_conversation(message)
                elif response.lower().startswith("speak about"):
                    topic = response[12:].strip()
                    await self.speak_about(message, topic)
            elif response.lower() == "reset":
                await self.reset_conversation(message)
                return
            elif response.lower() == "stop":
                await self.stop_conversation(message)
            elif response.lower().startswith("speak about"):
                topic = response[12:].strip()
                await self.speak_about(message, topic)
        elif response.lower() == "reset":
            await self.reset_conversation(message)
            return
        elif response.lower() == "stop":
            await self.stop_conversation(message)
        elif response.lower().startswith("speak about"):
            topic = response[12:].strip()
            await self.speak_about(message, topic)

        else:
            await message.channel.send("Invalid response.")
            await self.start_conversation(message)

#First Yes
    async def playLoL(self, message):
        await message.channel.send("Do you play LoL regularly ?")

    async def guess(self, message):
        await message.channel.send("Ok ok, let me guess your role, I think you're a supp !")

    async def casual(self, message):
        await message.channel.send("Oh ok, you're just having fun, isn't it ?")

    async def found(self, message):
        await message.channel.send("Yeaaaaaaaaaaah gotya !")

    async def noFound(self, message):
        await message.channel.send("Oh unluckyyyy")

    async def fun(self, message):
        await message.channel.send("Sometimes it's just so cool to chill on that kind of game without tryharding, u're right")
    
    async def noFun(self, message):
        await message.channel.send("Ye i'm with you on this, we can't have fun in every game, sadly...")

#First No
    async def noPlayLoL(self, message):
        await message.channel.send("Oh you don't like LoL... Is this because of the community ?")

    async def frustrated(self, message):
        await message.channel.send("I see... Sometimes, players are very frustrated during the game, it's not realy cool to play with them.")

    async def moba(self, message):
        await message.channel.send("Huh, you prefer other kind of games ?")

    async def otherGame(self, message):
        await message.channel.send("I guess you play FPS.")

    async def noOtherGame(self, message):
        await message.channel.send("Daaaaamn you like to suffer tho...")
    
    async def speak_about(self, message, topic):
        valid_topics = ["lol", "champion", "champions", "elo", "rank", "league of legends", "league"]

        if topic.lower() in valid_topics:
            await message.channel.send(f"**Yes, we are speaking about {topic.capitalize()}, that's so cool.**")
        else:
            await message.channel.send("**Sorry, I can't help you on this subject... I'm not Einstein**")

    async def get_user_response(self, message):
        try:
            response = await asyncio.wait_for(self.client.wait_for("message", check=lambda m: m.author == message.author and m.channel == message.channel), timeout=60)
            return response.content
        except asyncio.TimeoutError:
            await message.channel.send("Time's up. Conversation ended.")
            return "timeout"
        

