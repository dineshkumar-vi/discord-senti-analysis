import discord

from sentieval.twitter_roberta import TwitterRoberta


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        print("Incoming message", message.content)
        twitterR.predicte(message.content)

        #await message.channel.send('Bot listing your message: '+ message.content)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
twitterR: TwitterRoberta = TwitterRoberta()

client.run('MTEzOTc2MzgxMzg3MzM1Njg5MA.G_ZmRy.X0sc_HPHGDIMRh01glZQIo60kAC0BskQunZERY')