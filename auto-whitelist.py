# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
from unicodedata import name
import discord

# IMPORT THE OS MODULE.
import os

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()


# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
 

async def givePatrolRole(ctx):
    guild = ctx.guilds[0]
    whiteListRole = guild.get_role(931900158860492830) #Space Ape
    exemptRoles = [guild.get_role(854747857931730985),  #Admins, Supreme Leaders, Mods
        guild.get_role(919736162795528284),
        guild.get_role(919740668983787580)]
    exemptNames = ["Lafferty, Daniel#7667"]
    membersFiltered = [member 
        for member in guild.members 
            if member.bot==False
            and len(intersection(member.roles, exemptRoles)) == 0
            and str(member) not in exemptNames
        ]
    membersByJoinDate = sorted(
        membersFiltered, key=lambda x: x.joined_at, reverse=False)
    for member in membersByJoinDate[:500]:
        print(f"{member};{member.joined_at}")
        #### UNCOMMENT BELOW TO ADD ROLE #####
        #await member.add_roles(whiteListRole, reason="One of the first 500 people to join.")            

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
intents = discord.Intents.default()
intents.members = True
bot = discord.Client(intents=intents)

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.


@bot.event
async def on_ready():
    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        #print(f"- {guild.id} (name: {guild.name})")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

    await givePatrolRole(bot)
    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    #print("SampleDiscordBot is in " + str(guild_count) + " guilds.")




# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)
