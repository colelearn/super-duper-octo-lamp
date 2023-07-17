import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='/')
@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user.name}')
@bot.command(Reaction_Time)
async def send_message(ctx, 1130348232355106929, message):
    channel = bot.get_channel(int(1130348232355106929))
    await channel.send(hello)
    await ctx.message.add_reaction(:smile:)
