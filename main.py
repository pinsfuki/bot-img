import discord #permet d'avoir les commandes pour config le bot
from discord.ext import commands
from dotenv import load_dotenv #permet de charger le token du bot pour faire le lien mais sans que ça soit dans le code directement
import os #permet d'importer des options pour intéragir avec l'os

load_dotenv() #permet de charger la variable qui se trouve dans .env

api_key = os.getenv('discord_token') #créer un variable qui appel la variable qui contient le token 

intents = discord.Intents.default() #ça permet au bot de pouvoir avoir les fonctions de défaut, voir les messages (pas leur contenu complet au début), voir les salons, etc...
intents.message_content = True # autorise à lire les messages, analyser les messages, etc...

bot = commands.Bot(command_prefix='/',intents=intents, auto_sync_commands=True) #création du bot (le client) et lui donnes les permissions (les intents) qui sont définits plus haut

@bot.event #ça permet de dire à discord que la fonction dessous est un evenement du bot
async def on_ready(): #ici je déclare la foction on_ready qui est asynchrone
    print('Je suis en ligne')#et quand l'event se déclanch e bien il print je suis en ligne dans le terminal, ça me montre quand il est en ligne 

bot.load_extensions('commands.ping', 'commands.export_photos') #permet de charger la commande ping.py

bot.run(api_key) #lance le bot 