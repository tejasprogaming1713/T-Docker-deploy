import discord
from discord.ext import commands
import asyncio
import itertools
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ───────────────────────────────────────────────
# 🔥 ANIMATED STARTUP SPINNER (Console Animation)
# ───────────────────────────────────────────────
async def animate_startup():
    spinner = itertools.cycle(["🔵", "🟣", "🔮", "✨"])
    for _ in range(20):
        print(f"\rStarting bot {next(spinner)}", end="", flush=True)
        await asyncio.sleep(0.08)
    print("\n✨ Bot is now online!")

# ───────────────────────────────────────────────
# 🤖 Bot Events
# ───────────────────────────────────────────────
@bot.event
async def on_ready():
    print("⚡ Preparing systems...")
    await animate_startup()
    print(f"✅ Logged in as: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")


# ───────────────────────────────────────────────
bot.run(TOKEN)
