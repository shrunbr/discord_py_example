#Import required modules
import asyncio
import discord
import os
import yaml
from discord.ext import commands

#Intent setup
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Parse config.yaml
config = yaml.safe_load(open('config.yaml'))

#Set bot prefix
activity = discord.Game(name="with myself | !help")
bot = commands.Bot(command_prefix='!', intents=intents, activity=activity)
bot_token = config['config']['token']

#Important Variables
cwd = os.getcwd()

#Load cog command
@bot.command(hidden=True)
@commands.is_owner()
async def load(ctx, extension):
    await bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been loaded')

#Unload cog command
@bot.command(hidden=True)
@commands.is_owner()
async def unload(ctx, extension):
    await bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been unloaded')

#Reload cog command
@bot.command(hidden=True)
@commands.is_owner()
async def reload(ctx, extension):
    await bot.unload_extension(f'cogs.{extension}')
    await bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been reloaded')

#Find cogs in OS
async def load_extensions():
    for filename in os.listdir(f'{cwd}/cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

#Set activity status on Discord
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

#Start bot
async def main():
    async with bot:
        await load_extensions()
        await bot.start(bot_token)
asyncio.run(main())