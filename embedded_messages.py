from minecraft import Status
import discord


def server_overview(status: Status, address: str, modpack: str) -> discord.Embed:
    embed = discord.Embed(title="Minecraft Server")
    if status == Status.ON:
        color = 0x33D17A
        status = "online"
    else:
        color = 0xE01B24
        status = "offline"

    embed = discord.Embed(
        title="Minecraft Server",
        description=f"The server is currently {status}",
        colour=color,
    )

    embed.add_field(name="Server Address", value=address, inline=True)
    embed.add_field(name="Modpack", value=modpack, inline=True)

    return embed


def server_status_change(status: Status) -> discord.Embed:
    if status == Status.ON:
        return discord.Embed(
            title="The server has opened!",
            colour=0x33D17A,
            description="It's time! The server gods have opened the gates to minecraft",
        )
    else:
        return discord.Embed(
            title="The server went offline.",
            colour=0xE01B24,
            description="Thats it, playtime is over. See you next time o/",
        )
