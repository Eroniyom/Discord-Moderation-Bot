"""
Discord Moderation Bot
A simple and extensible Discord moderation bot with slash commands.
"""

import discord
from discord.ext import commands
import os
import logging
from datetime import datetime, timedelta
from config import Config

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix=Config.PREFIX,
    intents=intents,
    help_command=None
)

@bot.event
async def on_ready():
    """Event triggered when bot is ready."""
    logger.info(f'{bot.user} has connected to Discord!')
    logger.info(f'Bot ID: {bot.user.id}')
    logger.info(f'Connected to {len(bot.guilds)} guilds')
    
    # Set bot status
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="for moderation commands"
        )
    )
    
    # Sync slash commands
    try:
        synced = await bot.tree.sync()
        logger.info(f"Synced {len(synced)} slash commands")
    except Exception as e:
        logger.error(f"Failed to sync slash commands: {e}")

@bot.event
async def on_command_error(ctx, error):
    """Global error handler for prefix commands."""
    if isinstance(error, commands.CommandNotFound):
        return  # Ignore command not found errors
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don't have permission to use this command!")
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send("❌ I don't have the required permissions!")
    else:
        logger.error(f"Command error: {error}")
        await ctx.send("❌ An error occurred while executing the command!")

# Moderation Commands
class Moderation(commands.Cog):
    """Moderation commands for server management."""
    
    def __init__(self, bot):
        self.bot = bot
    
    @discord.app_commands.command(name="kick", description="Kick a member from the server")
    @discord.app_commands.describe(
        member="The member to kick",
        reason="Reason for the kick"
    )
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
        """Kick a member from the server."""
        # Permission checks
        if not interaction.user.guild_permissions.kick_members:
            await interaction.response.send_message(
                "❌ You don't have permission to kick members!",
                ephemeral=True
            )
            return
        
        if not interaction.guild.me.guild_permissions.kick_members:
            await interaction.response.send_message(
                "❌ I don't have permission to kick members!",
                ephemeral=True
            )
            return
        
        # Prevent self-moderation
        if member == interaction.user:
            await interaction.response.send_message(
                "❌ You cannot kick yourself!",
                ephemeral=True
            )
            return
        
        if member == self.bot.user:
            await interaction.response.send_message(
                "❌ You cannot kick me!",
                ephemeral=True
            )
            return
        
        # Prevent kicking higher role members
        if member.top_role >= interaction.user.top_role and interaction.user != interaction.guild.owner:
            await interaction.response.send_message(
                "❌ You cannot kick someone with equal or higher roles!",
                ephemeral=True
            )
            return
        
        try:
            await member.kick(reason=f"{reason} | {interaction.user}")
            
            embed = discord.Embed(
                title="👢 Member Kicked",
                description=f"**Member:** {member.mention}\n**Reason:** {reason}\n**Moderator:** {interaction.user.mention}",
                color=Config.COLORS['WARNING'],
                timestamp=datetime.now()
            )
            embed.set_footer(text=f"ID: {member.id}")
            
            await interaction.response.send_message(embed=embed)
            logger.info(f"{interaction.user} kicked {member} from {interaction.guild.name}")
            
        except Exception as e:
            await interaction.response.send_message(
                f"❌ Failed to kick member: {str(e)}",
                ephemeral=True
            )
            logger.error(f"Kick error: {e}")
    
    @discord.app_commands.command(name="ban", description="Ban a member from the server")
    @discord.app_commands.describe(
        member="The member to ban",
        reason="Reason for the ban"
    )
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
        """Ban a member from the server."""
        # Permission checks
        if not interaction.user.guild_permissions.ban_members:
            await interaction.response.send_message(
                "❌ You don't have permission to ban members!",
                ephemeral=True
            )
            return
        
        if not interaction.guild.me.guild_permissions.ban_members:
            await interaction.response.send_message(
                "❌ I don't have permission to ban members!",
                ephemeral=True
            )
            return
        
        # Prevent self-moderation
        if member == interaction.user:
            await interaction.response.send_message(
                "❌ You cannot ban yourself!",
                ephemeral=True
            )
            return
        
        if member == self.bot.user:
            await interaction.response.send_message(
                "❌ You cannot ban me!",
                ephemeral=True
            )
            return
        
        # Prevent banning higher role members
        if member.top_role >= interaction.user.top_role and interaction.user != interaction.guild.owner:
            await interaction.response.send_message(
                "❌ You cannot ban someone with equal or higher roles!",
                ephemeral=True
            )
            return
        
        try:
            await member.ban(reason=f"{reason} | {interaction.user}")
            
            embed = discord.Embed(
                title="🔨 Member Banned",
                description=f"**Member:** {member.mention}\n**Reason:** {reason}\n**Moderator:** {interaction.user.mention}",
                color=Config.COLORS['ERROR'],
                timestamp=datetime.now()
            )
            embed.set_footer(text=f"ID: {member.id}")
            
            await interaction.response.send_message(embed=embed)
            logger.info(f"{interaction.user} banned {member} from {interaction.guild.name}")
            
        except Exception as e:
            await interaction.response.send_message(
                f"❌ Failed to ban member: {str(e)}",
                ephemeral=True
            )
            logger.error(f"Ban error: {e}")
    
    @discord.app_commands.command(name="timeout", description="Timeout a member")
    @discord.app_commands.describe(
        member="The member to timeout",
        minutes="Duration in minutes (1-40320)",
        reason="Reason for the timeout"
    )
    async def timeout(self, interaction: discord.Interaction, member: discord.Member, minutes: int, reason: str = "No reason provided"):
        """Timeout a member for specified duration."""
        # Permission checks
        if not interaction.user.guild_permissions.moderate_members:
            await interaction.response.send_message(
                "❌ You don't have permission to timeout members!",
                ephemeral=True
            )
            return
        
        if not interaction.guild.me.guild_permissions.moderate_members:
            await interaction.response.send_message(
                "❌ I don't have permission to timeout members!",
                ephemeral=True
            )
            return
        
        # Duration validation
        if minutes < 1 or minutes > 40320:  # Max 28 days
            await interaction.response.send_message(
                "❌ Duration must be between 1 minute and 28 days (40320 minutes)!",
                ephemeral=True
            )
            return
        
        # Prevent self-moderation
        if member == interaction.user:
            await interaction.response.send_message(
                "❌ You cannot timeout yourself!",
                ephemeral=True
            )
            return
        
        if member == self.bot.user:
            await interaction.response.send_message(
                "❌ You cannot timeout me!",
                ephemeral=True
            )
            return
        
        # Prevent timing out higher role members
        if member.top_role >= interaction.user.top_role and interaction.user != interaction.guild.owner:
            await interaction.response.send_message(
                "❌ You cannot timeout someone with equal or higher roles!",
                ephemeral=True
            )
            return
        
        try:
            timeout_until = datetime.now() + timedelta(minutes=minutes)
            await member.timeout(timeout_until, reason=f"{reason} | {interaction.user}")
            
            embed = discord.Embed(
                title="🔇 Member Timed Out",
                description=f"**Member:** {member.mention}\n**Duration:** {minutes} minutes\n**Reason:** {reason}\n**Moderator:** {interaction.user.mention}",
                color=Config.COLORS['WARNING'],
                timestamp=datetime.now()
            )
            embed.set_footer(text=f"ID: {member.id}")
            
            await interaction.response.send_message(embed=embed)
            logger.info(f"{interaction.user} timed out {member} for {minutes} minutes in {interaction.guild.name}")
            
        except Exception as e:
            await interaction.response.send_message(
                f"❌ Failed to timeout member: {str(e)}",
                ephemeral=True
            )
            logger.error(f"Timeout error: {e}")
    
    @discord.app_commands.command(name="untimeout", description="Remove timeout from a member")
    @discord.app_commands.describe(member="The member to remove timeout from")
    async def untimeout(self, interaction: discord.Interaction, member: discord.Member):
        """Remove timeout from a member."""
        # Permission checks
        if not interaction.user.guild_permissions.moderate_members:
            await interaction.response.send_message(
                "❌ You don't have permission to remove timeouts!",
                ephemeral=True
            )
            return
        
        if not interaction.guild.me.guild_permissions.moderate_members:
            await interaction.response.send_message(
                "❌ I don't have permission to remove timeouts!",
                ephemeral=True
            )
            return
        
        try:
            await member.timeout(None, reason=f"Timeout removed by {interaction.user}")
            
            embed = discord.Embed(
                title="🔊 Timeout Removed",
                description=f"**Member:** {member.mention}\n**Moderator:** {interaction.user.mention}",
                color=Config.COLORS['SUCCESS'],
                timestamp=datetime.now()
            )
            embed.set_footer(text=f"ID: {member.id}")
            
            await interaction.response.send_message(embed=embed)
            logger.info(f"{interaction.user} removed timeout from {member} in {interaction.guild.name}")
            
        except Exception as e:
            await interaction.response.send_message(
                f"❌ Failed to remove timeout: {str(e)}",
                ephemeral=True
            )
            logger.error(f"Untimeout error: {e}")
    
    @discord.app_commands.command(name="clear", description="Clear messages from the channel")
    @discord.app_commands.describe(amount="Number of messages to clear (1-100)")
    async def clear(self, interaction: discord.Interaction, amount: int):
        """Clear specified number of messages."""
        # Permission checks
        if not interaction.user.guild_permissions.manage_messages:
            await interaction.response.send_message(
                "❌ You don't have permission to manage messages!",
                ephemeral=True
            )
            return
        
        if not interaction.guild.me.guild_permissions.manage_messages:
            await interaction.response.send_message(
                "❌ I don't have permission to manage messages!",
                ephemeral=True
            )
            return
        
        # Amount validation
        if amount < 1 or amount > 100:
            await interaction.response.send_message(
                "❌ Amount must be between 1 and 100!",
                ephemeral=True
            )
            return
        
        try:
            # Purge messages
            deleted = await interaction.channel.purge(limit=amount)
            
            embed = discord.Embed(
                title="🗑️ Messages Cleared",
                description=f"**Deleted:** {len(deleted)} messages\n**Moderator:** {interaction.user.mention}",
                color=Config.COLORS['SUCCESS'],
                timestamp=datetime.now()
            )
            
            # Send temporary response
            await interaction.response.send_message(embed=embed, ephemeral=True)
            logger.info(f"{interaction.user} cleared {len(deleted)} messages in {interaction.channel.name}")
            
        except Exception as e:
            await interaction.response.send_message(
                f"❌ Failed to clear messages: {str(e)}",
                ephemeral=True
            )
            logger.error(f"Clear error: {e}")

# Information Commands
class Information(commands.Cog):
    """Information commands for users and server."""
    
    def __init__(self, bot):
        self.bot = bot
    
    @discord.app_commands.command(name="userinfo", description="Get information about a user")
    @discord.app_commands.describe(member="The member to get information about")
    async def userinfo(self, interaction: discord.Interaction, member: discord.Member = None):
        """Get detailed information about a user."""
        if member is None:
            member = interaction.user
        
        # Get user roles (excluding @everyone)
        roles = [role.mention for role in member.roles[1:]]
        roles_str = ", ".join(roles) if roles else "No roles"
        
        embed = discord.Embed(
            title=f"👤 {member.display_name}",
            color=member.color,
            timestamp=datetime.now()
        )
        
        # Set thumbnail
        if member.avatar:
            embed.set_thumbnail(url=member.avatar.url)
        else:
            embed.set_thumbnail(url=member.default_avatar.url)
        
        # Add fields
        embed.add_field(name="📛 Username", value=f"{member.name}#{member.discriminator}", inline=True)
        embed.add_field(name="🆔 ID", value=member.id, inline=True)
        embed.add_field(name="📅 Account Created", value=f"<t:{int(member.created_at.timestamp())}:R>", inline=True)
        embed.add_field(name="📅 Joined Server", value=f"<t:{int(member.joined_at.timestamp())}:R>", inline=True)
        embed.add_field(name="🎭 Roles", value=roles_str[:1024], inline=False)
        
        # Add timeout info if applicable
        if member.timed_out_until:
            embed.add_field(name="🔇 Timed Out Until", value=f"<t:{int(member.timed_out_until.timestamp())}:R>", inline=True)
        
        embed.set_footer(text=f"Requested by {interaction.user}")
        
        await interaction.response.send_message(embed=embed)
    
    @discord.app_commands.command(name="serverinfo", description="Get information about the server")
    async def serverinfo(self, interaction: discord.Interaction):
        """Get detailed information about the server."""
        guild = interaction.guild
        
        # Get server statistics
        total_members = guild.member_count
        online_members = len([m for m in guild.members if m.status != discord.Status.offline])
        text_channels = len(guild.text_channels)
        voice_channels = len(guild.voice_channels)
        roles = len(guild.roles)
        emojis = len(guild.emojis)
        
        embed = discord.Embed(
            title=f"🏰 {guild.name}",
            color=Config.COLORS['INFO'],
            timestamp=datetime.now()
        )
        
        # Set server icon if available
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
        
        # Add fields
        embed.add_field(name="🆔 Server ID", value=guild.id, inline=True)
        embed.add_field(name="👑 Owner", value=guild.owner.mention, inline=True)
        embed.add_field(name="📅 Created", value=f"<t:{int(guild.created_at.timestamp())}:R>", inline=True)
        embed.add_field(name="👥 Total Members", value=total_members, inline=True)
        embed.add_field(name="🟢 Online Members", value=online_members, inline=True)
        embed.add_field(name="📝 Text Channels", value=text_channels, inline=True)
        embed.add_field(name="🔊 Voice Channels", value=voice_channels, inline=True)
        embed.add_field(name="🎭 Roles", value=roles, inline=True)
        embed.add_field(name="😀 Emojis", value=emojis, inline=True)
        embed.add_field(name="📊 Boost Level", value=guild.premium_tier, inline=True)
        
        embed.set_footer(text=f"Requested by {interaction.user}")
        
        await interaction.response.send_message(embed=embed)

# Help Command
class Help(commands.Cog):
    """Help command for the bot."""
    
    def __init__(self, bot):
        self.bot = bot
    
    @discord.app_commands.command(name="help", description="Show available commands")
    async def help_command(self, interaction: discord.Interaction):
        """Show help information."""
        embed = discord.Embed(
            title="🛡️ Discord Moderation Bot - Help",
            description="A simple and extensible Discord moderation bot with slash commands.",
            color=Config.COLORS['INFO']
        )
        
        embed.add_field(
            name="🛡️ Moderation Commands",
            value="`/kick` - Kick a member\n`/ban` - Ban a member\n`/timeout` - Timeout a member\n`/untimeout` - Remove timeout\n`/clear` - Clear messages",
            inline=False
        )
        
        embed.add_field(
            name="📊 Information Commands",
            value="`/userinfo` - Get user information\n`/serverinfo` - Get server information\n`/help` - Show this help",
            inline=False
        )
        
        embed.add_field(
            name="🔧 Features",
            value="• Slash commands\n• Permission checks\n• Beautiful embeds\n• Error handling\n• Logging\n• Extensible design",
            inline=False
        )
        
        embed.set_footer(text="Made with ❤️ for the Discord community")
        
        await interaction.response.send_message(embed=embed)

# Load cogs
async def setup():
    """Load all cogs."""
    await bot.add_cog(Moderation(bot))
    await bot.add_cog(Information(bot))
    await bot.add_cog(Help(bot))

# Main execution
if __name__ == "__main__":
    # Load cogs
    asyncio.run(setup())
    
    # Get bot token
    token = os.getenv('DISCORD_BOT_TOKEN')
    if not token:
        logger.error("DISCORD_BOT_TOKEN environment variable not found!")
        logger.error("Please create a .env file or set the environment variable.")
        exit(1)
    
    # Run bot
    try:
        bot.run(token)
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        exit(1)