# 📜 Discord Logger Bot
A simple Discord bot built with `discord.py` that logs messages, edits, and deletions to a local text file.
## 🔧 Features
- Logs all messages sent by users
- Logs message edits (before ➜ after)
- Logs deleted messages
- Saves logs to `discord_logs.txt` with timestamps
## 🛠 Requirements
- Python 3.8+
- `discord.py` library  
  Install with:
  ```bash
  pip install discord.py
  ```
## 🚀 Setup
1. Create a bot at https://discord.com/developers/applications
2. Enable **Message Content Intent** in Bot > Privileged Gateway Intents
3. Copy your bot token and paste it into `logger_bot.py`:
   ```python
   TOKEN = "YOUR_BOT_TOKEN"
   ```
4. Run the bot:
   ```bash
   python logger_bot.py
   ```
5. Logs will be saved to `discord_logs.txt` in the same folder.
## 📁 Example Log Entry
```
[2025-05-19 11:00:00] [MESSAGE] veyzoh in #general: hello everyone
[2025-05-19 11:01:05] [EDIT] veyzoh in #general: 'hello everyone' ➜ 'hello world'
[2025-05-19 11:02:00] [DELETE] veyzoh in #general: hello world
```
## 🧩 To Extend
- Add logging for member joins/leaves
- Send logs to a private channel instead of a file
- Include timestamps in Discord messages

## 👤 Author
Built by [@veyzohh](https://github.com/veyzohh)
