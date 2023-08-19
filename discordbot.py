import discord

from sentieval.roberta import Roberta
from sentieval.deberta import DebertaV2



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        print("Incoming message", message.content)
        rsafetext = roberta.predicte(message.content)
        print("roberta sentimental analysis ")
        dsafetext = deberta.predicte(message.content)

        if rsafetext != "positive" and dsafetext != "positive":
            await message.delete()
            await message.channel.send('Banned message')




intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
roberta: Roberta = Roberta()
deberta: DebertaV2 = DebertaV2()

client.run('MTEzOTc2MzgxMzg3MzM1Njg5MA.G_ZmRy.X0sc_HPHGDIMRh01glZQIo60kAC0BskQunZERY')