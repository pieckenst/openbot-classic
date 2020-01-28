import discord
import asyncio
import random
from scripts import games 
from discord.ext import commands

class minigames(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def kubik(self, ctx): #кубик рандом
        kuboid = random.choice(games.kubik)
        embedkub = discord.Embed(title="<:game_die:643509937892229142> Play Roll Cube", color=0x00ff00)
        embedkub.add_field(name="You Got:", value=kuboid, inline=False)
        await ctx.send(embed=embedkub)

    @commands.command()
    async def monetka(self, ctx):
        mon = random.choice(games.monet)
        embedmonet = discord.Embed(title="<:moneybag:643869263937011732> Play Coint", color=0x00ff00)
        embedmonet.add_field(name="You Got:", value=mon, inline=False)
        await ctx.send(embed=embedmonet)

    @commands.command()
    async def casino(self, ctx):
        kasino1 = random.choice(games.casin_obj1)
        kasino2 = random.choice(games.casin_obj2)
        kasino3 = random.choice(games.casin_obj3)
        embedkas = discord.Embed(title="<:slot_machine:643869263937011732> Казино Три Арча",color=0x00ff00)
        embedkas.add_field(name="You Got:", value=kasino1, inline=True)
        embedkas.add_field(name="You Got:", value=kasino2, inline=True)
        embedkas.add_field(name="You Got:", value=kasino3, inline=True)
        await ctx.send(embed=embedkas)



def setup(bot):
    bot.add_cog(minigames(bot))
