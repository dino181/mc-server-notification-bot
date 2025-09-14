import discord
from discord.ext import tasks, commands
from discord.commands import SlashCommandGroup
from typing import Any
from config import save_config
from minecraft import Status, get_status
from embedded_messages import server_overview, server_status_change


class MinecraftServerCog(commands.Cog):
    def __init__(self, bot: discord.Bot, config: dict[str, Any] = None):
        self._bot: discord.Bot = bot
        self._config: dict[str, Any] = config

        self.check_server_status.start()
        self._current_server_status = Status.OFF

    minecraft_server = SlashCommandGroup(name="minecraft-server")

    @minecraft_server.command(description="Update server details")
    @discord.option(
        "address", type=str, description="The server address. Enter 'none' to remove it"
    )
    @discord.option(
        "modpack", type=str, description="The modpack. Enter 'none' to remove it"
    )
    async def update_server(
        self, ctx: discord.ApplicationContext, address: str, modpack: str
    ):
        modpack = None if modpack.lower() == "none" else modpack
        address = None if address.lower() == "none" else address
        self._config["mc_server_address"] = address
        self._config["mc_modpack_link"] = modpack
        save_config(self._config)

        embed = server_overview(
            self._current_server_status,
            self._config["mc_server_address"],
            self._config["mc_modpack_link"],
        )
        await ctx.respond(embed=embed)

    @minecraft_server.command(description="Get server status")
    async def status(self, ctx: discord.ApplicationContext):
        embed = server_overview(
            self._current_server_status,
            self._config["mc_server_address"],
            self._config["mc_modpack_link"],
        )
        await ctx.respond(embed=embed)

    @minecraft_server.command(
        description="Set the channel for notifications",
    )
    async def notification_channel(
        self, ctx: discord.ApplicationContext, channel: discord.TextChannel
    ):
        self._config["mc_notif_channel"] = channel.id
        res = save_config(self._config)
        if not res:
            await ctx.respond("Failed to update notification channel")
            return

        await ctx.respond(f"Updated the notification channel to {channel.name}")

    @tasks.loop(minutes=5)
    async def check_server_status(self):
        if self._config["mc_notif_channel"] is None:
            return

        channel = self._bot.get_channel(self._config["mc_notif_channel"])
        if not channel:
            return

        status = get_status(server_adress=self._config["mc_server_address"])
        if status != self._current_server_status:
            embed = server_status_change(status)
            await channel.send("@here", embed=embed)
            self._current_server_status = status
