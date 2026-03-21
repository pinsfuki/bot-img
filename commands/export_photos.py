from discord.ext import commands
from services.date_parser import parse_date
from services.scanner import scanner
import discord


def setup(bot):
    @bot.slash_command(name='export_photos', description='Exporter les photos choisi par date et par salon')
    async def export_photos(ctx, date_debut : str, date_fin  : str , nom_export  : str):
        date_debut_converti = parse_date(date_debut)
        date_fin_converti = parse_date(date_fin)
        embed = discord.Embed(
            title = 'Info',
            description = (f'Ok je vais chercher les photos de {date_debut_converti} à {date_fin_converti} et ton fichier se nommera {nom_export} :)'),
            color=discord.Color.orange()
        )

        await ctx.respond(embed=embed)