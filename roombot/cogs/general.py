import discord
from discord.ext import commands
from roombot.database.room import Room
from roombot.database.settings import Settings
from roombot.utils.functions import load_cog
from roombot.utils.pagesembed import EmbedPagesEmbed

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = discord.Color.greyple()
        
    @commands.command()
    async def ping(self, ctx):
        s = Settings.get_for(ctx.guild.id)
        m = await ctx.send(s.get_text('ping'))
        ms = (m.created_at-ctx.message.created_at).total_seconds() * 1000
        await m.edit(content=s.get_text('pong').format(int(ms)))

    @commands.command()
    async def donate(self, ctx):
        embed = discord.Embed(
            color=discord.Color.blurple(),
            title=":heart: Support the cause! :flex:",
            description="blush:",
            url="https://paypal.me/KashTheKlub"
        ).set_author(
            name="Donate"
        ).set_thumbnail(
            url="https://pics.paypal.com/00/s/NzIyWDc4M1hQTkc/p/YjJjZjY4NmMtNGNhMy00MTVkLWIwZTQtNTQxZWU0OGIyYTYz/image_58.jpg"
        )
        return await ctx.send(embed=embed)

    @commands.command()
    async def about(self, ctx):
        embed = discord.Embed(
            color=discord.Color.blurple(),
            title="About Doombot",
            description='\n'.join([
                ":heart: [Paypal](https://paypal.me/KashTheKlub) Donate :flex:!",
                
            ).set_thumbnail(
            url="https://pics.paypal.com/00/s/NzIyWDc4M1hQTkc/p/YjJjZjY4NmMtNGNhMy00MTVkLWIwZTQtNTQxZWU0OGIyYTYz/image_58.jpg"
            )
        return await ctx.send(embed=embed)

    @commands.command()
    async def support(self, ctx):
        s = Settings.get_for(ctx.guild.id)
        return await ctx.send(s.get_text('support'))

    @commands.command()
    async def help(self, ctx, *args):
        s = Settings.get_for(ctx.guild.id)
        filtered_commands = []
        for arg in args:
            for c in self.bot.commands:
                if (c.name == arg or arg in c.aliases) and c not in filtered_commands:
                    filtered_commands.append(c)
        if len(filtered_commands) > 0:
            embed = discord.Embed(
                color=discord.Color.blurple(),
                title=s.get_text('help') )
            for command in filtered_commands:
                text = s.get_text('_commands')[command.name]
                embed.add_field(
                    name="**{}**    {} `{}`".format(text['_name'], s.get_text('alias'), "`, `".join(text['_aliases'])),
                    value='\n'.join(text['_help']),
                    inline=False )
            return await ctx.send(embed=embed)

        embeds = []
        for cog_name, cog in self.bot.cogs.items():
            cog_text = s.get_text('_cog')
            embed = discord.Embed(
                color=cog.color,
                title=s.get_text('help'),
                description='**{}**'.format(cog_text[cog_name]) )
            for command in sorted(cog.get_commands(), key=lambda c:c.name):
                text = s.get_text('_commands')[command.name]
                embed.add_field(
                    name="**{}**    {} `{}`".format(text['_name'], s.get_text('alias'), "`, `".join(text['_aliases'])),
                    value='\n'.join(text['_help']),
                    inline=False )
            embeds.append(embed)
        timed_out_embed = discord.Embed(
            color=discord.Color.blurple(),
            title=s.get_text('help') )
        await EmbedPagesEmbed(ctx, embeds, timed_out_embed).send()


def setup(bot):
    load_cog(bot, General(bot))