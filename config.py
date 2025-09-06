"""
Configuration file for Discord Moderation Bot
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Bot configuration settings."""
    
    # Bot settings
    PREFIX = os.getenv('BOT_PREFIX', '!')
    TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    
    # Logging settings
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'bot.log')
    
    # Color scheme for embeds
    COLORS = {
        'SUCCESS': 0x00ff00,    # Green
        'ERROR': 0xff0000,      # Red
        'WARNING': 0xffa500,    # Orange
        'INFO': 0x0099ff,       # Blue
        'PURPLE': 0x9932cc,     # Purple
        'GOLD': 0xffd700        # Gold
    }
    
    # Emoji constants
    EMOJIS = {
        'SUCCESS': '✅',
        'ERROR': '❌',
        'WARNING': '⚠️',
        'INFO': 'ℹ️',
        'KICK': '👢',
        'BAN': '🔨',
        'TIMEOUT': '🔇',
        'CLEAR': '🗑️',
        'USER': '👤',
        'SERVER': '🏰'
    }
    
    # Command cooldowns (in seconds)
    COOLDOWNS = {
        'kick': 5,
        'ban': 5,
        'timeout': 3,
        'clear': 10
    }
    
    # Maximum values
    MAX_CLEAR_AMOUNT = 100
    MAX_TIMEOUT_MINUTES = 40320  # 28 days
    MIN_TIMEOUT_MINUTES = 1
    
    # Database settings (for future use)
    DATABASE_URL = os.getenv('DATABASE_URL')
    
    # API settings (for future use)
    API_BASE_URL = os.getenv('API_BASE_URL', 'https://api.example.com')
    
    # Feature flags
    FEATURES = {
        'logging': True,
        'auto_moderation': False,
        'welcome_messages': False,
        'custom_commands': False
    }
