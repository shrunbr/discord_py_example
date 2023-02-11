#Import required modules
import discord
from discord.ext import commands

#Command Category
class Admin(commands.Cog):

    #Must INIT!
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def amiadmin(self, ctx):
        """ Are you admin? """
        if ctx.message.author.id == 200968736008699916:
            return await ctx.send(f"Well kinda **{ctx.author.name}**.. you own the source code")

        if ctx.message.author.guild_permissions.administrator:
            return await ctx.send(f"Yes **{ctx.author.name}** you are admin! ✅")

        await ctx.send(f"no, fuck off {ctx.author.name}")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        """ Clears Messages. Default is 5 """
        await ctx.channel.purge(limit=amount)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def status(self, ctx, *, status: str):
        """Changes the bot's 'playing' status"""
        await self.bot.change_presence(status=discord.Status.online, activity=discord.activity.Game(name=status))
        await ctx.send(f"{ctx.message.author.mention} just changed my 'playing' status to {status}")

#Add cog to bot
async def setup(bot):
    await bot.add_cog(Admin(bot))