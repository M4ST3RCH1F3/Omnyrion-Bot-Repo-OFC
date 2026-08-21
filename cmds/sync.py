import os
import discord
from discord import app_commands
from discord.ext import commands

class SysAdm(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@app_commands.command(name='sync', description='Sincroniza todos os comandos do bot.')
	async def sync(self, interaction: discord.Interaction):
		if interaction.user.id != interaction.guild.owner_id and not interaction.user.guild_permissions.administrator:
			await interaction.response.send_message("Você não é dono, muito menos não tem permissões o suficiente para isso.", ephemeral = True)
			return

		await interaction.response.defer(ephemeral=True)

		try:
			cmds_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "cmds")
			recarregadas = []
			for filename in os.listdir(cmds_path):
				if filename.endswith('.py') and filename != '__init__.py':
					cog_name = f"cmds.{filename[:-3]}"
					await self.bot.reload_extension(cog_name)
					recarregadas.append(filename)
			mensagem_sync_prefix = f"{len(recarregadas)} Comandos Recarregados. | Commandos: {', '.join(recarregadas)}"
		except Exception as e:
			mensagem_sync_prefix = f"[PREFIXO] | Erro ao Sincronizar comando. | {e}"

		try:
			await self.bot.tree.sync()
			mensagem_sync_slash = "**Comandos Slash Sincronizados com sucesso.**"
		except Exception as e:
			mensagem_sync_slash = f"[SLASH] | Erro ao Sincronizar comando. | {e}"

		await interaction.followup.send(f"{mensagem_sync_prefix}\n{mensagem_sync_slash}")

async def setup(bot):
	await bot.add_cog(SysAdm(bot))