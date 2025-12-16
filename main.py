import discord
from discord.ext import commands
import os

# ----- BOT SETUP -----
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ----- BOT READY -----
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# ----- COMMANDS -----

# !hell -> says hi to everyone
@bot.command()
@commands.has_permissions(mention_everyone=True)
async def hell(ctx):
    await ctx.send("@everyone 👋 Hi everyone!")

# !hello -> simple reply
@bot.command()
async def hello(ctx):
    await ctx.send("Hello 👋")

# !kick @user reason
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
    await member.kick(reason=reason)
    await ctx.send(f"👢 {member} was kicked | Reason: {reason}")

# !ban @user reason
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No reason provided"):
    await member.ban(reason=reason)
    await ctx.send(f"🔨 {member} was banned | Reason: {reason}")

# !clear 10
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"🧹 Cleared {amount} messages", delete_after=3)

# ----- RUN BOT -----
bot.run(os.getenv("TOKEN"))


