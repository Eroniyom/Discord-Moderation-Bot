# 🛡️ Discord Moderation Bot

A simple, extensible Discord moderation bot built with Python and discord.py. This bot provides essential moderation commands using modern slash commands and is designed to be easily customizable and extensible.

## ✨ Features

### 🛡️ Moderation Commands
- **`/kick`** - Kick a member from the server
- **`/ban`** - Ban a member from the server
- **`/timeout`** - Timeout a member (1 minute to 28 days)
- **`/untimeout`** - Remove timeout from a member
- **`/clear`** - Clear messages from a channel (1-100 messages)

### 📊 Information Commands
- **`/userinfo`** - Get detailed information about a user
- **`/serverinfo`** - Get detailed information about the server
- **`/help`** - Show available commands

### 🔧 Technical Features
- ✅ **Slash Commands** - Modern Discord command interface
- ✅ **Permission System** - Proper permission checks for all commands
- ✅ **Error Handling** - Comprehensive error handling and logging
- ✅ **Beautiful Embeds** - Professional-looking command responses
- ✅ **Extensible Design** - Easy to add new commands and features
- ✅ **Logging System** - Detailed logging for debugging and monitoring
- ✅ **Configuration Management** - Centralized configuration system

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- A Discord application and bot token

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/discord-moderation-bot.git
   cd discord-moderation-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env file and add your bot token
   ```

4. **Run the bot**
   ```bash
   python bot.py
   ```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Required
DISCORD_BOT_TOKEN=your_bot_token_here

# Optional
BOT_PREFIX=!
LOG_LEVEL=INFO
LOG_FILE=bot.log
```

### Bot Permissions

When inviting the bot to your server, make sure to grant the following permissions:

- **Send Messages** - To send command responses
- **Use Slash Commands** - To use slash commands
- **Manage Messages** - For the clear command
- **Kick Members** - For the kick command
- **Ban Members** - For the ban command
- **Moderate Members** - For timeout commands
- **Embed Links** - For rich embeds
- **Read Message History** - For message management

## 📚 Usage

### Moderation Commands

#### Kick a Member
```
/kick member:@username reason:Spamming
```

#### Ban a Member
```
/ban member:@username reason:Violating rules
```

#### Timeout a Member
```
/timeout member:@username minutes:60 reason:Being disruptive
```

#### Clear Messages
```
/clear amount:10
```

### Information Commands

#### Get User Information
```
/userinfo member:@username
```

#### Get Server Information
```
/serverinfo
```

## 🛠️ Development

### Project Structure

```
discord-moderation-bot/
├── bot.py              # Main bot file
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore file
├── env.example        # Environment variables example
├── README.md          # This file
└── CONTRIBUTING.md    # Contribution guidelines
```

### Adding New Commands

1. **Create a new cog** (recommended for organization):
   ```python
   class MyCommands(commands.Cog):
       def __init__(self, bot):
           self.bot = bot
       
       @discord.app_commands.command(name="mycommand", description="My command")
       async def my_command(self, interaction: discord.Interaction):
           await interaction.response.send_message("Hello!")
   ```

2. **Register the cog** in `bot.py`:
   ```python
   await bot.add_cog(MyCommands(bot))
   ```

### Customization

- **Colors**: Modify `Config.COLORS` in `config.py`
- **Emojis**: Modify `Config.EMOJIS` in `config.py`
- **Cooldowns**: Modify `Config.COOLDOWNS` in `config.py`
- **Features**: Toggle features in `Config.FEATURES` in `config.py`

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

1. Clone your fork
2. Create a virtual environment
3. Install dependencies
4. Create a `.env` file with your bot token
5. Run the bot and test your changes

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/discord-moderation-bot/issues) page
2. Create a new issue if your problem isn't already reported
3. Join our [Discord server](https://discord.gg/your-invite) for community support

## 🔮 Roadmap

- [ ] Database integration for moderation logs
- [ ] Auto-moderation features
- [ ] Welcome/goodbye messages
- [ ] Custom commands system
- [ ] Web dashboard
- [ ] Multi-language support
- [ ] Advanced logging and analytics

## 🙏 Acknowledgments

- [discord.py](https://github.com/Rapptz/discord.py) - The Discord API wrapper
- [Discord Developer Portal](https://discord.com/developers/applications) - For bot creation
- The Discord community for feedback and suggestions

---

**Made with ❤️ for the Discord community**

*If you find this bot helpful, please consider giving it a ⭐ on GitHub!*