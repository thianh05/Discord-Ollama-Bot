import os
import json
import asyncio
import aiohttp
import discord
from discord.ext import commands
from dotenv import load_dotenv

# =====================
# LOAD ENV
# =====================
ENV_PATH = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(ENV_PATH, override=True)

DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
OLLAMA_URL = os.getenv("OLLAMA_URL")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

if not DISCORD_TOKEN:
    raise ValueError(f"DISCORD_BOT_TOKEN not found in {ENV_PATH}")

if not OLLAMA_URL or not OLLAMA_MODEL:
    raise ValueError("OLLAMA_URL or OLLAMA_MODEL not found in .env")

# =====================
# DISCORD CONFIG
# =====================
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    intents=intents
)

# =====================
# EVENTS
# =====================
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

# =====================
# OLLAMA CALL (ASYNC STREAM)
# =====================
async def ask_ollama(prompt: str) -> str:
    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": True
    }

    answer_parts = []

    timeout = aiohttp.ClientTimeout(total=300)

    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.post(OLLAMA_URL, json=payload) as resp:
            async for line in resp.content:
                if not line:
                    continue
                try:
                    data = json.loads(line.decode("utf-8"))
                    if "message" in data and "content" in data["message"]:
                        answer_parts.append(data["message"]["content"])
                except json.JSONDecodeError:
                    continue

    return "".join(answer_parts).strip()

# =====================
# COMMAND: !ask
# =====================
@bot.command()
async def ask(ctx, *, question: str = None):
    if not question:
        await ctx.send("Usage: `!ask your question`")
        return

    async with ctx.typing():
        try:
            answer = await ask_ollama(question)

            if not answer:
                await ctx.send("Model returned empty response.")
                return

            if len(answer) > 2000:
                for i in range(0, len(answer), 2000):
                    await ctx.send(answer[i:i+2000])
            else:
                await ctx.send(answer)

        except Exception as e:
            print("OLLAMA ERROR:", e)
            await ctx.send("Ollama API failed.")

# =====================
# RUN BOT
# =====================
def run_bot():
    bot.run(DISCORD_TOKEN)
