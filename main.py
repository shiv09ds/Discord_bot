import sys
sys.dont_write_bytecode = True
import os
import discord
from discord.ext.commands import Bot
from keepAlive import keep_alive
keep_alive()
bot = Bot(command_prefix="!", intents= discord.Intents.all())


@bot.event
async def on_ready():
	os.system('clear')
	synced = await bot.tree.sync()
	print(f"Synced {len(synced)} command(s)")

@bot.tree.command(name="ping",description="Pings the bot")
async def remove_channel(interaction : discord.Interaction):
	await interaction.response.send_message("Pong")

@bot.event
async def on_message(ctx):
	author_Id= ctx.author.id
	if author_Id == bot.user.id : pass

	elif ctx.content.lower() == "hi" : await ctx.channel.send("Hello <:emoji_48:1115693431256272917> <:emoji_18:1115652337382465627> ")

bot.run(os.getenv("token"))