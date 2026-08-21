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

		desc = (
			f"══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n"
			f"** **\n"
			f"# InfoBot\n"
			f"## Painel de Informações do {self.bot.user.name}\n"
			f"** **\n"
			f"══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n"
			f"\n__***Criador:***__ zShelbyTheOne\n"
			f"__***Versão:***__ {self._get_version()}\n"
			f"__***Licença de Uso:***__ Apache 2.0\n"
			f"__***Tempo Ativo:***__ {self._get_uptime()}\n"
			f"__***Tempo de Resposta:***__ {round(self.bot.latency * 1000, 2)} ms\n"
			f"__***Quantidade de comandos:***__ Total: {total_count} ({slash_count} comandos slash. | {prefix_count} comandos de prefixo.)\n\n"
			f"══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n"
			f"** **"
		)

		embed = discord.Embed(
			description = desc,
			color = 0xad00ff
		)
		embed.set_image(url="https://cdn.discordapp.com/attachments/1436920976758669465/1524131540483969114/ChatGPT_Image_7_de_jul._de_2026_11_56_34.png?ex=6a88a39c&is=6a87521c&hm=1fad4e3464938af92e30aad63cd18a7f49210e24b57f29d932a0e8e0cd9b7035&")
		await interaction.response.send_message(embed=embed)

	@commands.command(name = 'infobot')
	async def infobot_prefix(self, ctx):
		slash_count = len(self.bot.tree.get_commands())
		prefix_count = len(self.bot.commands)
		total_count = slash_count + prefix_count

		desc = (
			f"══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n"
			f"** **\n"
			f"# InfoBot\n"
			f"## Painel de Informações do {self.bot.user.name}\n"
			f"** **\n"
			f"══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n"
			f"\n__***Criador:***__ zShelbyTheOne\n"
			f"__***Versão:***__ {self._get_version()}\n"
			f"__***Licença de Uso:***__ Apache 2.0\n"
			f"__***Tempo Ativo:***__ {self._get_uptime()}\n"
			f"__***Tempo de Resposta:***__ {round(self.bot.latency * 1000, 2)} ms\n"
			f"__***Quantidade de comandos:***__ Total: {total_count} ({slash_count} comandos slash. | {prefix_count} comandos de prefixo.)\n\n"
			f"══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n"
			f"** **"
		)

		embed = discord.Embed(
			description = desc,
			color = 0xad00ff
		)
		embed.set_image(url="https://cdn.discordapp.com/attachments/1436920976758669465/1524131540483969114/ChatGPT_Image_7_de_jul._de_2026_11_56_34.png?ex=6a88a39c&is=6a87521c&hm=1fad4e3464938af92e30aad63cd18a7f49210e24b57f29d932a0e8e0cd9b7035&")
		await ctx.send(embed=embed)

async def setup(bot):
	await bot.add_cog(Info(bot))