import time
import discord
from discord import app_commands
from discord.ext import commands

class Ping(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.start_time = time.time()
  def _get_uptime(self):
    segundos_gerais = int(time.time() - self.start_time)
    dias, resto = divmod(segundos_gerais, 86400)
    horas, resto = divmod(resto, 3600)
    minutos, segundos = divmod(resto, 60)
    return f"{dias}d, {horas}h, {minutos}m, {segundos}s"
    
  def _get_anstime(self):
    return round(self.bot.latency * 1000, 2)

  @commands.command(name='ping')
  async def ping(self, ctx):
    mensagem = (
      f"\n**Pong.**\n"
      f"**Tempo de resposta:** {self._get_anstime()}ms\n"
      f"**Ativo há:** {self._get_uptime()}"
    )
    embed = discord.Embed(
      title = "Tempo de Resposta & Atividade",
      description = f"{mensagem}",
      color = 0xad00ff
    )
    await ctx.send(embed=embed)

  @app_commands.command(name = 'ping', description = 'Esse comando mostra o tempo de atividade e/ou resposta do bot.')
  async def ping_slash(self, interaction:discord.Interaction):
    mensagem = (
      f"\n**Pong.**\n"
      f"**Tempo de resposta:** {self._get_anstime()}ms\n"
      f"**Ativo há:** {self._get_uptime()}"
    )
    embed = discord.Embed(
      title = "Tempo de Resposta & Atividade",
      description = f"{mensagem}",
      color = 0xad00ff
    )
    await interaction.response.send_message(embed=embed)
  
async def setup(bot):
  await bot.add_cog(Ping(bot))
