from asyncio import sleep

from discord import Member, Embed, Color, Message
from discord.ext.commands import Bot, command, Context

from database import ProfileModel


class Profiles(object):
    def __init__(self, bot: Bot):
        self.bot: Bot = bot

    # noinspection PyMethodMayBeStatic
    async def on_message(self, mes: Message):
        if mes.author.bot:
            return
        if mes.content == ':qa!':
            await mes.channel.send(content=f"{mes.author.mention} successfully exited vim!")

    @command()
    async def profile(self, ctx: Context, user: Member = None):
        if user is None:
            user = ctx.author
        model = ProfileModel.get_or_insert(user)
        em = Embed(
            title=f'Profile of {user.display_name}',
            description=model.bio,
        )
        em.set_author(name=user.display_name, icon_url=user.avatar_url)
        em.add_field(name="Age", value=str(model.age))
        em.add_field(name="Gender", value=model.gender)
        await ctx.send(embed=em)

    @command()
    async def setage(self, ctx: Context, newage: int):
        mes: Message
        if newage < 0:
            mes = await ctx.send(
                embed=Embed(
                    description="Please enter a valid age",
                    color=Color.red()))
        else:
            ProfileModel.update(age=newage).where(ProfileModel.uid == ctx.author.id).execute()
            mes = await ctx.send(
                embed=Embed(
                    description=f"Set your age to `{newage}`",
                    color=Color.green()))
        await sleep(10)
        await mes.delete()

    @command()
    async def setgender(self, ctx: Context, *, gender):
        mes: Message
        if len(gender) > 255 or len(gender) < 2:
            mes = await ctx.send(
                embed=Embed(
                    description="Please enter a valid  gender",
                    color=Color.red()))
        else:
            ProfileModel.update(gender=gender).where(ProfileModel.uid == ctx.author.id).execute()
            mes = await ctx.send(
                embed=Embed(
                    description=f"Set your gender to `{gender}`",
                    color=Color.green()))
        await sleep(10)
        await mes.delete()

    @command()
    async def setbio(self, ctx: Context, *, bio):
        mes: Message
        if len(bio) > 2012 or len(bio) < 2:
            mes = await ctx.send(
                embed=Embed(
                    description="Please enter a valid bio",
                    color=Color.red()))
        else:
            ProfileModel.update(gender=bio).where(ProfileModel.uid == ctx.author.id).execute()
            if len(bio) > 500:
                bio = bio[:500] + '\n...'
            bio = bio.replace('`', '`\u200b')
            mes = await ctx.send(
                embed=Embed(
                    description=f"Set your bio to ```\n{bio}\n```",
                    color=Color.green()))
        await sleep(10)
        await mes.delete()


def setup(bot: Bot):
    bot.add_cog(Profiles(bot))
