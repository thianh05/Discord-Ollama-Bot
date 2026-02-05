# Discord-Ollama-Bot

A lightweight Discord bot that connects to a locally running Ollama server
and allows users to ask questions directly from Discord.

NOTE:
This project does NOT include Ollama.
Users must install and run Ollama themselves.

--------------------------------------------------
## Ollama Setup (Required)
1. Download Ollama from the official site: https://ollama.com
2. Pull a model (example): ollama pull gemma3:4b
3. Start the Ollama server: ollama serve
--------------------------------------------------

## Create .env File (Required)

Users must manually create a .env file in the project root.

DISCORD_BOT_TOKEN=YOUR_TOKEN_DISCORD_HERE

OLLAMA_URL=http://localhost:11434/api/chat

OLLAMA_MODEL=gemma3:4b

IMPORTANT:
- Never share your Discord bot token
- Do NOT commit the .env file to GitHub
- Add .env to .gitignore

--------------------------------------------------

## Requirements

1. Python 3.9+
2. Ollama (installed and running by the user)
3. Discord Bot Token
