#idiotbotv1
import chalk
import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot
bot = commands.Bot(command_prefix='$')

@bot.command(pass_context=True)
async def idiot(ctx, user: discord.Member):
    await bot.say((user.name)+" you idiot")

@bot.command(pass_context=True)
async def idiotm(ctx):
    await bot.say("Michael you idiot")

bot.run("Mzg1OTY0Njk3MTI5NTgyNTky.DQJBKQ.UEICEHQXmqOQ4CAYgMW4pkBbepA")
