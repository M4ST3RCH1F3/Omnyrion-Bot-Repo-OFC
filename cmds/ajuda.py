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
		mention = self.bot.user.mention
		prefixos_str = ", ".join(PREFIXOS)
		prefix_list = "\n".join([f"***{PREFIXOS[0]}{cmd.name}***" for cmd in prefix_cmds])

		desc = (
			f"══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n"
			f"** **\n"
			f"# Ajuda\n"
			f"## Lista de Comandos & Prefixos\n"
			f"** **\n"
			f"══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n"
			f"** **\n"
			f"**Prefixos disponíveis:** {prefixos_str}, {mention}\n\n"
			f"══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n\n"
			f"**Comandos (Slash):**\n{slash_list}\n\n"
			f"══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n\n"
			f"**Comandos (Prefixo):**\n{prefix_list}\n\n"
			f"══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n"
			f"** **"
		)

		embed = discord.Embed(
			description = desc if desc else "Nenhum comando encontrado.\nCertifique-se de que existe algum comando na pasta cmds/. do bot.",
			color = 0xad00ff
		)
		embed.set_image(url="https://cdn.discordapp.com/attachments/1436920976758669465/1524131540483969114/ChatGPT_Image_7_de_jul._de_2026_11_56_34.png?ex=6a88a39c&is=6a87521c&hm=1fad4e3464938af92e30aad63cd18a7f49210e24b57f29d932a0e8e0cd9b7035&")
		await interaction.response.send_message(embed=embed)

	@commands.command(name='ajuda')
	async def ajuda_prefix(self, ctx):

		slash_cmds = self.bot.tree.get_commands()
		slash_list = "\n".join([f"***{cmd.name}*** | {cmd.description}" for cmd in slash_cmds])

		prefix_cmds = self.bot.commands
		mention = self.bot.user.mention
		prefixos_str = ", ".join(PREFIXOS)
		prefix_list = "\n".join([f"***{PREFIXOS[0]}{cmd.name}***" for cmd in prefix_cmds])

		desc = (
			f"══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n"
			f"** **\n"
			f"# Ajuda\n"
			f"## Lista de Comandos & Prefixos\n"
			f"** **\n"
			f"══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n"
			f"** **\n"
			f"**Prefixos disponíveis:** {prefixos_str}, {mention}\n\n"
			f"══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n\n"
			f"**Comandos (Slash):**\n{slash_list}\n\n"
			f"══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n\n"
			f"**Comandos (Prefixo):**\n{prefix_list}\n\n"
			f"══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n"
			f"** **"
		)

		embed = discord.Embed(
			description = desc if desc else "Nenhum comando encontrado.\nCertifique-se de que existe algum comando na pasta cmds/. do bot.",
			color = 0xad00ff
		)
		embed.set_image(url="https://cdn.discordapp.com/attachments/1436920976758669465/1524131540483969114/ChatGPT_Image_7_de_jul._de_2026_11_56_34.png?ex=6a88a39c&is=6a87521c&hm=1fad4e3464938af92e30aad63cd18a7f49210e24b57f29d932a0e8e0cd9b7035&")
		await ctx.send(embed=embed)

async def setup(bot):
	await bot.add_cog(Ajuda(bot))