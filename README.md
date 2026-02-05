# Discord-Ollama-Bot

A lightweight Discord bot that connects to a locally running Ollama server and allows users to ask questions directly from Discord.
Note : This project does NOT include Ollama.
Users must install and run Ollama themselves.

# Ollama Setup :
* Download from the official site: https://ollama.com
* Pull a model (ex) : ollama pull gemma3:4b
* Start Ollama Server : ollama serve

# Create .env : 
DISCORD_BOT_TOKEN=YOUR_TOKEN_DISCORD_HERE
OLLAMA_URL=http://localhost:11434/api/chat
OLLAMA_MODEL=gemma3:4b

# Project Structure :
├── app.py              # Application entry point
├── bot.py              # Discord bot logic
├── requirements.txt    # Python dependencies
├── .env                # User-created (NOT committed)
└── README.md

# Requirements : 
1 - Python 3.9+
2 - Ollama (installed & running by ususer
3 - Discord Bot Token

