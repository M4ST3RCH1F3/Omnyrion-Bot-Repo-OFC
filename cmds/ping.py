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
			f"══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n"
			f"** **\n"
			f"# Ping\n"
			f"## Tempo de Resposta & Atividade\n"
			f"** **\n"
			f"══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n"
			f"\n**Pong.**\n"
			f"**Tempo de resposta:** {self._get_anstime()}ms\n"
			f"**Ativo há:** {self._get_uptime()}\n"
			f"\n══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n"
			f"** **"
		)
		embed = discord.Embed(
			description = f"{mensagem}",
			color = 0xad00ff
		)
		embed.set_image(url="https://cdn.discordapp.com/attachments/1436920976758669465/1524131540483969114/ChatGPT_Image_7_de_jul._de_2026_11_56_34.png?ex=6a88a39c&is=6a87521c&hm=1fad4e3464938af92e30aad63cd18a7f49210e24b57f29d932a0e8e0cd9b7035&")
		await ctx.send(embed=embed)

	@app_commands.command(name = 'ping', description = 'Esse comando mostra o tempo de atividade e/ou resposta do bot.')
	async def ping_slash(self, interaction:discord.Interaction):

		mensagem = (
			f"══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n"
			f"** **\n"
			f"# Ping\n"
			f"## Tempo de Resposta & Atividade\n"
			f"** **\n"
			f"══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n"
			f"\n**Pong.**\n"
			f"**Tempo de resposta:** {self._get_anstime()}ms\n"
			f"**Ativo há:** {self._get_uptime()}\n"
			f"\n══════❖꙰✡︎ღ 「:wheel_of_dharma:」 ღ✡︎꙰❖══════\n"
			f"** **"
		)
		embed = discord.Embed(
			description = f"{mensagem}",
			color = 0xad00ff
		)
		embed.set_image(url="https://cdn.discordapp.com/attachments/1436920976758669465/1524131540483969114/ChatGPT_Image_7_de_jul._de_2026_11_56_34.png?ex=6a88a39c&is=6a87521c&hm=1fad4e3464938af92e30aad63cd18a7f49210e24b57f29d932a0e8e0cd9b7035&")
		await interaction.response.send_message(embed=embed)

async def setup(bot):
	await bot.add_cog(Ping(bot))
