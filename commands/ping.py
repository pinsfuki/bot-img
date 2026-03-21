from discord.ext import commands

def setup(bot):
    @bot.slash_command(name="ping", description="Check the bot's latency.")
    async def ping(ctx):
        await ctx.respond(f'pong ! La lattence est de {bot.latency}')