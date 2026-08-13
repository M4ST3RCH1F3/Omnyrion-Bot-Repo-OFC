import discord
import os
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv('token.env')
TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
  async def on_ready(self):
    print(f'Sucesso, Logado como {self.user}.')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

if __name__ == "__main__":
    if TOKEN:
        client.run(TOKEN)
    else:
        print("Erro: Bot Token não encontrado no arquivo .env")
