# Discord-Ollama-Bot

A lightweight Discord bot that connects to a locally running Ollama server, allowing users to ask questions directly from Discord.

⚠️ Note
This project does NOT include Ollama.
Users must install and run Ollama themselves.

# Ollama Setup (Required)

Download Ollama from the official website:
https://ollama.com

Pull a model (example):

ollama pull gemma3:4b


Start the Ollama server:

ollama serve

# Create .env File (Required)

Users must manually create a .env file in the project root.

DISCORD_BOT_TOKEN=YOUR_TOKEN_DISCORD_HERE
OLLAMA_URL=http://localhost:11434/api/chat
OLLAMA_MODEL=gemma3:4b

# Security
1. Never share your Discord bot token
2. Do NOT commit .env to GitHub
3. Add .env to .gitignore

📁 Project Structure
.
├── app.py              # Application entry point
├── bot.py              # Discord bot logic
├── requirements.txt    # Python dependencies
├── .env                # User-created (NOT committed)
└── README.md

⚙️ Requirements
- Python 3.9+
- Ollama (installed & running by the user)
- Discord Bot Token
