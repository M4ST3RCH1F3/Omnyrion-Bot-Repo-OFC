import time
import discord
import subprocess
from discord import app_commands
from discord.ext import commands

class Info(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.start_time = time.time()

	def _get_version(self):
		try:
			tag = subprocess.check_output(
				["git", "tag", "--sort=creatordate"],
				text = True,
				stderr = subprocess.DEVNULL,
			).strip().splitlines()[-1]
			return tag
		except Exception:
			return "v0.0.0 (Sem Tags)."

	def _get_uptime(self):
		segundos = int(time.time() - self.start_time)
		dias, resto = divmod(segundos, 86400)
		horas, resto = divmod(resto, 3600)
		minutos, segundos = divmod(resto, 60)
		return f"{dias}d {horas}h {minutos}m {segundos}s"

	@app_commands.command(name ='infobot', description = 'Comando de informações do bot.' )
	async def infobot_slash(self, interaction: discord.Interaction):
		slash_count = len(self.bot.tree.get_commands())
		prefix_count = len(self.bot.commands)
		total_count = slash_count + prefix_count
		embed = discord.Embed(
			title = f"Painel de Informações do {self.bot.user.name}",
			description = (
				f"\n**Criador:** zShelbyTheOne\n"
				f"**Versão:** {self._get_version()}\n"
				f"**Licença de Uso:** Apache 2.0\n"
				f"**Tempo Ativo:** {self._get_uptime()}\n"
				f"**Tempo de Resposta:** {round(self.bot.latency * 1000, 2)} ms\n"
				f"**Quantidade de comandos:** Total: {total_count} ({slash_count} comandos slash. | {prefix_count} comandos de prefixo.)"
			),
			color = 0xad00ff
		)
		await interaction.response.send_message(embed=embed)

	@commands.command(name = 'infobot')
	async def infobot_prefix(self, ctx):
		slash_count = len(self.bot.tree.get_commands())
		prefix_count = len(self.bot.commands)
		total_count = slash_count + prefix_count
		embed = discord.Embed(
			title = f"Painel de Informações do {self.bot.user.name}",
			description = (
				f"\n**Criador:** zShelbyTheOne\n"
				f"**Versão:** {self._get_version()}\n"
				f"**Licença de Uso:** Apache 2.0\n"
				f"**Tempo Ativo:** {self._get_uptime()}\n"
				f"**Tempo de Resposta:** {round(self.bot.latency * 1000, 2)} ms\n"
				f"**Quantidade de comandos:** Total: {total_count} ({slash_count} comandos slash. | {prefix_count} comandos de prefixo.)"
			),
			color = 0xad00ff
		)
		await ctx.send(embed=embed)

async def setup(bot):
	await bot.add_cog(Info(bot))