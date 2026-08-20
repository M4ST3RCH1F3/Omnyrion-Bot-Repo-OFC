import discord
from src.main import PREFIXOS
from discord import app_commands
from discord.ext import commands

class Ajuda(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	@app_commands.command(name='ajuda', description= 'Comando para listar todoos os prefixos e comandos, sejam eles prefixos ou slashs.')
	async def ajuda_slash(self, interaction: discord.Interaction):

		slash_cmds = self.bot.tree.get_commands()
		slash_list = "\n".join([f"***{cmd.name}*** | {cmd.description}" for cmd in slash_cmds])

		prefix_cmds = self.bot.commands
		prefixos_str = ", ".join(PREFIXOS)
		prefix_list = "\n".join([f"***{PREFIXOS[0]}{cmd.name}***" for cmd in prefix_cmds])

		desc = (
			f"\n**Prefixos disponíveis:** {prefixos_str}\n\n"
			f"**Comandos (Slash):**\n{slash_list}\n\n"
			f"**Comandos (Prefixo):**\n{prefix_list}"
		)

		embed = discord.Embed(
			title = "Ajuda | Lista de Comandos & Prefixos",
			description = desc if desc else "Nenhum comando encontrado.\nCertifique-se de que existe algum comando na pasta cmds/. do bot.",
			color = 0xad00ff
		)
		await interaction.response.send_message(embed=embed)

	@commands.command(name='ajuda')
	async def ajuda_prefix(self, ctx):

		slash_cmds = self.bot.tree.get_commands()
		slash_list = "\n".join([f"***{cmd.name}*** | {cmd.description}" for cmd in slash_cmds])

		prefix_cmds = self.bot.commands
		prefixos_str = ", ".join(PREFIXOS)
		prefix_list = "\n".join([f"***{PREFIXOS[0]}{cmd.name}***" for cmd in prefix_cmds])

		desc = (
			f"\n**Prefixos disponíveis:** {prefixos_str}\n\n"
			f"**Comandos (Slash):**\n{slash_list}\n\n"
			f"**Comandos (Prefixo):**\n{prefix_list}"
		)

		embed = discord.Embed(
			title = "Ajuda | Lista de Comandos & Prefixos",
			description = desc if desc else "Nenhum comando encontrado.\nCertifique-se de que existe algum comando na pasta cmds/. do bot.",
			color = 0xad00ff
		)
		await ctx.send(embed=embed)

async def setup(bot):
	await bot.add_cog(Ajuda(bot))