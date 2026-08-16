import os
import sys
import discord
from dotenv import load_dotenv
from discord.ext import commands

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

load_dotenv(os.path.join(ROOT_DIR, 'token.env'))
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

PREFIXOS = ['Om!' , 'oM!' , 'OM!' , 'Om!' , '€', 'om!']

def get_prefix(bot, message):
  return commands.when_mentioned_or(*PREFIXOS)(bot, message)

bot = commands.Bot(
  command_prefix = get_prefix, 
  intents = intents, 
  case_insensitive = 'True',
  help_command = None
)

async def load_cmds():
  cmds_path = os.path.join(ROOT_DIR, 'cmds')

  for filename in os.listdir(cmds_path):
    if filename.endswith('.py') and filename != '__init__.py':
      try:
        await bot.load_extension(f"cmds.{filename[ : -3]}")
        print(f"✅ Comando carregado com sucesso. | {filename}")
        print(f"===================")
      except Exception as e:
        print(f"❎ Falha ao carregar o comando: | {filename} | {e}")
        print(f"===================")

@bot.event
async def on_ready():
  BOT_ID = bot.user.id
  print(f"===================")
  print(f"✅ Sucesso, bot ativo como {bot.user} | ID: {BOT_ID}")
  print(f"===================")
  print(f"Para desativar, use Ctrl + C.")
  print(f"===================")

  await load_cmds()

  try:
    synced = await bot.tree.sync()
    print(f"✅ Comandos Slash sincronizados com Sucesso.")
    print(f"===================")
  except Exception as e:
    print(f"❎ Erro ao carregar o comando: {e}")
    print(f"===================")
  
if TOKEN:
    bot.run(TOKEN)
else:
    print("Erro: Bot Token não encontrado no arquivo token.env")
