import discord
from discord.ext import commands
from discord import app_commands

class SlashCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='ping', description='Replies with Pong!')
    async def ping(self, interaction: discord.Interaction):
        """Slash command: /ping"""
        await interaction.response.send_message('Pong!')

    @app_commands.command(
        name='test',
        description='Test command to reference roles, channels, and members.'
    )
    async def test(
        self,
        interaction: discord.Interaction,
        role: discord.Role,               # Accepts a role as input
        channel: discord.TextChannel,    # Accepts a text channel as input
        member: discord.Member,          # Accepts a member as input
        stringvariable: str                     # Accepts a stringvariable as input
    ):
        """Slash command: /test"""
        message = (
            f'**Role:** {role.mention}\n'
            f'**Channel:** {channel.mention}\n'
            f'**Member:** {member.mention}\n'
            f'**stringvariable:** {stringvariable}'  # Display the stringvariable
        )
        await interaction.response.send_message(message)


async def setup(bot):
    await bot.add_cog(SlashCog(bot))
