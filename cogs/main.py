import discord
import asyncio
import random
from discord.ext import commands

client = discord.Client()

version = 1.0
bot = commands.Bot(command_prefix='!', description='Iniciar comandos.')

startup_extensions =["welcome"]

COR =0xff0000
msg_id = None
msg_user = None

@client.event
async def on_ready():
    print('BOT ONLINE - Olá Mundo!')
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_member_join(member):
  canal = client.get_channel("456969201777639426")
  regras = client.get_channel("457590389939896340")
  msg = "**Bem Vindo {}, leia as {} e bom jogo!**".format(member.mention, regras.mention)
  await client.send_message(canal, msg)

@client.event
async def on_member_remove(member):
  canal = client.get_channel("456969201777639426")
  msg = "**Adeus, {} Volte Sempre, ~~Ou não~~**".format(member.mention)
  await client.send_message(canal, msg)
@client.event
async def on_message(message):
    if message.content.lower().startswith("!rank"):
     embed = discord.Embed(
        title="Escolha seu rank!",
        color=COR,
        description="- Bronze = 🥉\n"
                    "- Prata = 🥈\n"
                    "- Ouro = 🥇\n"
                    "- Platina = 🚀\n"   
                    "- Diamante = 🏆",)

     botmsg = await client.send_message(message.channel,embed=embed)
     await client.add_reaction(botmsg, "🥉")
     await client.add_reaction(botmsg, "🥈")
     await client.add_reaction(botmsg, "🥇")
     await client.add_reaction(botmsg, "🚀")
     await client.add_reaction(botmsg, "🏆")
     global msg_id
     msg_id = botmsg.id
     global msg_user
     msg_user = message.author
    if message.content.lower().startswith('!invite'):
        await client.send_message(message.channel, "**Aqui está o invite para o nosso servidor : **https://discord.gg/gvFp92T 😀")
    if message.content.lower().startswith('!random'):
        choice = random.randint(1,5)
        if choice == 1:
           await client.send_message(message.channel, '{} A sua classe aleatória escolhida foi : **Guerreiro <:machado:457613796501094402>**'.format(message.author.mention))
        if choice == 2:
           await client.send_message(message.channel, '{} A sua classe aleatória escolhida foi : **Engenheiro ⚙**'.format(message.author.mention))
        if choice == 3:
           await client.send_message(message.channel, '{} A sua classe aleatória escolhida foi : **Assasino 🔪**'.format(message.author.mention))
        if choice == 4:
           await client.send_message(message.channel, '{} A sua classe aleatória escolhida foi : **Mago 🧙**'.format(message.author.mention))
        if choice == 5:
           await client.send_message(message.channel, '{} A sua classe aleatória escolhida foi : **Caçador 🏹**'.format(message.author.mention))

    if message.content.lower().startswith('!random'):
        choice = random.randint(1,18)
        if choice == 1:
            await client.send_message(message.channel, '{} A sua forja aleatória escolhida foi : **Underpass 🔨**'.format(message.author.mention))
        if choice == 2:
            await client.send_message(message.channel, '{} A sua forja aleatória escolhida foi : **Goblin Gulch 🔨**'.format(message.author.mention))
        if choice == 3:
           await client.send_message(message.channel, '{} A sua forja aleatória escolhida foi : **Gun Town 🔨**'.format(message.author.mention))
        if choice == 4:
           await client.send_message(message.channel, '{} A sua forja aleatória escolhida foi : **Outpost 🔨**'.format(message.author.mention))
        if choice == 5:
           await client.send_message(message.channel, '{} A sua forja aleatória escolhida foi : **Northport 🔨**'.format(message.author.mention))
        if choice == 6:
           await client.send_message(message.channel, '{} A sua forja aleatória escolhida foi : **Crossing 🔨**'.format(message.author.mention))
        if choice == 7:
           await client.send_message(message.channel, '{} A sua forja aleatória escolhida foi : **Valley 🔨**'.format(message.author.mention))
        if choice == 8:
           await client.send_message(message.channel, '{} A sua forja aleatória escolhida foi : **Coldmist Village 🔨**'.format(message.author.mention))
        if choice == 9:
           await client.send_message(message.channel, '{} A sua forja aleatória escolhida foi : **Icehaven 🔨**'.format(message.author.mention))
        if choice == 10:
           await client.send_message(message.channel, '{} A sua forja aleatória escolhida foi : **Jaguar’s Claws 🔨**'.format(message.author.mention))
        if choice == 11:
           await client.send_message(message.channel, '{} A sua forja aleatória escolhida foi : **Forbidden Swamp 🔨**'.format(message.author.mention))
        if choice == 12:
           await client.send_message(message.channel, '{} A sua forja aleatória escolhida foi : **Lost Forge 🔨**'.format(message.author.mention))
        if choice == 13:
           await client.send_message(message.channel, '{} A sua forja aleatória escolhida foi : **Lumberfall 🔨**'.format(message.author.mention))
        if choice == 14:
           await client.send_message(message.channel, '{} A sua forja aleatória escolhida foi : **Fungal Forest 🔨**'.format(message.author.mention))
        if choice == 15:
           await client.send_message(message.channel, '{} A sua forja aleatória escolhida foi : **Jade Gardens 🔨**'.format(message.author.mention))
        if choice == 16:
           await client.send_message(message.channel, '{} A sua forja aleatória escolhida foi : **Autumn Fields 🔨**'.format(message.author.mention))
        if choice == 17:
           await client.send_message(message.channel, '{} A sua forja aleatória escolhida foi : **Trinity Hills 🔨**'.format(message.author.mention))
        if choice == 18:
           await client.send_message(message.channel, '{} A sua forja aleatória escolhida foi : **Sentinel Hold 🔨**'.format(message.author.mention))
@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji =="🥉" and msg_id == msg_id and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bronze", msg.server.roles)
     await client.add_roles(user, role)
     await asyncio.sleep(0.2)
     msgaddelo = await client.send_message(msg.channel, "Foi adicionado o cargo **Bronze** a {}".format(msg_user.mention))
     await asyncio.sleep(10)
     await client.delete_message(msgaddelo)
     print("add")

    if reaction.emoji =="🥈" and msg_id == msg_id and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Prata", msg.server.roles)
     await client.add_roles(user, role)
     await asyncio.sleep(0.2)
     msgaddelo = await client.send_message(msg.channel, "Foi adicionado o cargo **Prata** a {}".format(msg_user.mention))
     await asyncio.sleep(10)
     await client.delete_message(msgaddelo)
     print("add")

    if reaction.emoji =="🥇" and msg_id == msg_id and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Ouro", msg.server.roles)
     await client.add_roles(user, role)
     await asyncio.sleep(0.2)
     msgaddelo = await client.send_message(msg.channel, "Foi adicionado o cargo **Ouro** a {}".format(msg_user.mention))
     await asyncio.sleep(10)
     await client.delete_message(msgaddelo)
     print("add")

    if reaction.emoji =="🚀" and msg_id == msg_id and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Platina", msg.server.roles)
     await client.add_roles(user, role)
     await asyncio.sleep(0.2)
     msgaddelo = await client.send_message(msg.channel, "Foi adicionado o cargo **Platina** a {}".format(msg_user.mention))
     await asyncio.sleep(10)
     await client.delete_message(msgaddelo)
     print("add")

    if reaction.emoji =="🏆" and msg_id == msg_id and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Diamante", msg.server.roles)
     await client.add_roles(user, role)
     await asyncio.sleep(0.2)
     msgaddelo = await client.send_message(msg.channel, "Foi adicionado o cargo **Diamante** a {}".format(msg_user.mention))
     await asyncio.sleep(10)
     await client.delete_message(msgaddelo)
     print("add")

@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji =="🥉" and msg_id == msg_id and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bronze", msg.server.roles)
     await client.remove_roles(user, role)
     await asyncio.sleep(0.2)
     msgaddelo = await client.send_message(msg.channel, "Foi removido o cargo **Bronze** a {}".format(msg_user.mention))
     await asyncio.sleep(10)
     await client.delete_message(msgaddelo)
     print("remove")

    if reaction.emoji =="🥈" and msg_id == msg_id and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Prata", msg.server.roles)
     await client.remove_roles(user, role)
     await asyncio.sleep(0.2)
     msgaddelo = await client.send_message(msg.channel, "Foi removido o cargo **Prata** a {}".format(msg_user.mention))
     await asyncio.sleep(10)
     await client.delete_message(msgaddelo)
     print("remove")

    if reaction.emoji =="🥇" and msg_id == msg_id and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Ouro", msg.server.roles)
     await client.remove_roles(user, role)
     await asyncio.sleep(0.2)
     msgaddelo = await client.send_message(msg.channel, "Foi removido o cargo **Ouro** a {}".format(msg_user.mention))
     await asyncio.sleep(10)
     await client.delete_message(msgaddelo)
     print("remove")

    if reaction.emoji =="🚀" and msg_id == msg_id and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Platina", msg.server.roles)
     await client.remove_roles(user, role)
     await asyncio.sleep(0.2)
     msgaddelo = await client.send_message(msg.channel, "Foi removido o cargo **Platina** a {}".format(msg_user.mention))
     await asyncio.sleep(10)
     await client.delete_message(msgaddelo)
     print("remove")

    if reaction.emoji == "🏆" and msg_id == msg_id and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Diamante", msg.server.roles)
     await client.remove_roles(user, role)
     await asyncio.sleep(0,2)
     msgaddelo = await client.send_message(msg.channel, "Foi removido o cargo **Diamante** a {}".format(msg_user.mention))
     await asyncio.sleep(10)
     await client.delete_message(msgaddelo)
     print("remove")

client.run(process.env.token)