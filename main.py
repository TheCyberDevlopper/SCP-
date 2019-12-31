import discord
from discord.ext import commands

token = 'YOUR_TOKEN'
bot = commands.Bot(command_prefix='$')
presence = "SCP: Secret Laboratorỳ"

SCP = {
    '001': {
      'name': 'Le Gardien de la Porte',
      'class': 'Euclide/Keter',
      'id': 'SCP-001'
    },
    '002': {
        'name': 'La salle a mangé',
        'class': 'Euclide',
        'id': 'SCP-002'
    },
    '003': {
        'name': 'Carte mère biologique',
        'class': 'Euclide',
        'id': 'SCP-003'
    },
    '004': {
        'name': 'Les 12 clés rouillées de la Porte',
        'class': 'Euclide',
        'id': 'SCP-004'
    },
    '005': {
        'name': 'Passe-Partout',
        'class': 'Sûr',
        'id': 'SCP-005'
    },
    '006': {
        'name': 'Fontaine de Jouvence',
        'class': 'Sûr',
        'id': 'SCP-006'
    },
    '007': {
        'name': 'Planète Abdominale',
        'class': 'Euclide',
        'id': 'SCP-007'
    },
    '008': {
        'name': 'Peste Zombie',
        'class': 'non autoriser',
        'id': 'SCP-008'
    },
    '009': {
        'name': 'Glace Rouge',
        'class': 'Euclide',
        'id': 'SCP-009'
    },
    '010': {
        'name': 'Colliers de Contrôle',
        'class': 'Sûr',
        'id': 'SCP-010'
    },
    '011': {
        'name': 'Statue commémorative de la Guerre de Sécession',
        'class': 'Sûr',
        'id': 'SCP-011'
    },
    '012': {
        'name': 'Une mauvaise Partition',
        'class': 'Euclide',
        'id': 'SCP-012'
    },
    '013': {
        'name': 'Cigarettes de la Femme en Bleu',
        'class': 'Sûr',
        'id': 'SCP-013'
    },
    '014': {
        'name': 'L\'Homme immortel',
        'class': 'Sûr',
        'id': 'SCP-014'
    },
    '015': {
        'name': 'Tuyaux du Cauchemar',
        'class': 'Euclide',
        'id': 'SCP-015'
    },
    '016': {
        'name': 'Micro-Organisme conscient',
        'class': 'Keter',
        'id': 'SCP-016'
    },
    '017': {
        'name': 'Ombre',
        'class': 'Keter',
        'id': 'SCP-017'
    },
    '018': {
        'name': 'Super Balle',
        'class': 'Euclide',
        'id': 'SCP-018'
    },
    '019': {
        'name': 'Le Pot aux Monstres',
        'class': 'Keter',
        'id': 'SCP-019'
    },
    '020': {
        'name': 'Moisissure invisible',
        'class': 'Keter',
        'id': 'SCP-020'
    },
    '021': {
        'name': 'Dragon de Peau',
        'class': 'Sûr',
        'id': 'SCP-021'
    },
    '022': {
        'name': 'La Morgue',
        'class': 'Euclide',
        'id': 'SCP-022'
    },
    '023': {
        'name': 'Chien noir',
        'class': 'Euclide',
        'id': 'SCP-023'
    },
    '024': {
        'name': 'Jeu Télé de la Mort',
        'class': 'Euclide',
        'id': 'SCP-024'
    },
    '025': {
        'name': 'Une Garde-Robe usée',
        'class': 'Sûr',
        'id': 'SCP-025'
    },
    '026': {
        'name': 'Retenue scolaire',
        'class': 'Euclide',
        'id': 'SCP-026'
    },
    '027': {
        'name': 'Le Dieu de la Vermine',
        'class': 'Euclide',
        'id': 'SCP-027'
    },
    '028': {
        'name': 'Savoir',
        'class': 'Sûr',
        'id': 'SCP-028'
    },
    '029': {
        'name': 'La Fille des Ombres',
        'class': 'Keter',
        'id': 'SCP-029'
    },
    '030': {
        'name': 'L\'Homunculus',
        'class': 'Sûr',
        'id': 'SCP-030'
    },
    '031': {
        'name': 'Qu\'est-ce que l\'Amour ?',
        'class': 'Sûr',
        'id': 'SCP-031'
    },
    '032': {
        'name': 'L\'Épouse du Frère',
        'class': 'Euclide',
        'id': 'SCP-032'
    },
    '033': {
        'name': 'Le Nombre manquant',
        'class': 'Euclide',
        'id': 'SCP-033'
    },
    '034': {
        'name': 'Couteau rituel en Obsidienne',
        'class': 'Sûr',
        'id': 'SCP-034'
    },
    '035': {
        'name': 'Masque possessif',
        'class': 'Keter',
        'id': 'SCP-035'
    },
    '036': {
        'name': 'Le Pèlerinage de Réincarnation des Yazidi (Kiras Guhorîn)',
        'class': 'Sûr',
        'id': 'SCP-036'
    },
    '037': {
        'name': 'Étoile naine',
        'class': 'Euclide',
        'id': 'SCP-037'
    },
    '038': {
        'name': ' L\'Arbre du Tout',
        'class': 'Sûr',
        'id': 'SCP-038'
    },
    '039': {
        'name': ' Ingénieurs nasiques',
        'class': 'Euclide',
        'id': 'SCP-039'
    },
    '040': {
        'name': 'Enfant de l\'Évolution',
        'class': 'Euclide',
        'id': 'SCP-040'
    },
    '041': {
        'name': 'Patient à Émission de Pensées',
        'class': 'Sûr',
        'id': 'SCP-041'
    },
    '042': {
        'name': 'Un Cheval autrefois ailé',
        'class': 'Sûr',
        'id': 'SCP-042'
    },
    '043': {
        'name': 'Les Beatles',
        'class': 'Sûr',
        'id': 'SCP-043'
    },
    '044': {
        'name': 'Canon à Fission moléculaire de la Seconde Guerre Mondiale',
        'class': 'Sûr',
        'id': 'SCP-044'
    },
    '045': {
        'name': 'Convertisseur atmosphérique',
        'class': 'Sûr',
        'id': 'SCP-045'
    }
}

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(presence))
    print('%s connected' % (bot.user))

def wiki(id):
    msg = 'Name: %s\nClass: %s\nId: %s' % (SCP[id]['name'], SCP[id]['class'], SCP[id]['id'])
    return msg

@bot.command()
async def scp(ctx, id):
    await ctx.send(wiki(id))

bot.run(token)
