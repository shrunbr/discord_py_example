#Import required modules
import discord
from discord.ext import commands

#Command Category
class General(commands.Cog):

    #Must INIT!
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def testcommand(self, ctx):
        """ The command to prove ultimate power. """
        await ctx.send(f"Power has been achieved.")
    
    @commands.command()
    async def ambertest(self, ctx):
        """This is to test this command"""
        await ctx.send(f"See told you amber.")

#Add cog to bot
async def setup(bot):
    await bot.add_cog(General(bot))