import time
import discord
from discord import app_commands
from discord.ext import commands

class Ping(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.start_time = time.time()

  @commands.command(name='ping')
  async def ping(self, ctx):
    await ctx.send("Pong.")

  @app_commands.command(name = 'ping', description = 'Esse comando mostra o tempo de atividade e/ou resposta do bot.')
  async def ping_slash(self, interaction:discord.Interaction):
    await interaction.response.send_message("Pong.")
  
async def setup(bot):
  await bot.add_cog(Ping(bot))
