import discord


def createEmbed(title, description, colour, names, values, inline):
    embed = discord.Embed(title=title,
                          description=description,
                          colour=colour)
    for i in range(len(names)):
        embed.add_field(name=names[i],
                        value=values[i],
                        inline=inline)
    return embed
