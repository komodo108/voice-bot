from discord.ext import commands
from discord.utils import get

class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #@commands.Cog.listener()
    #async def on_member_join(self, member):
        # TODO: Implement this at some point?
    #    pass

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        """ Listener called when a member joins or leaves a voice channel """

        # Always give the user the InVoice role when joining
        if before.channel == None:
            role = get(member.guild.roles, name="InVoice")
            await member.add_roles(role)

        if after.channel == None and "InVoice" in [r.name for r in member.roles]:
            role = get(member.guild.roles, name="InVoice")
            await member.remove_roles(role)

        # If the is admin, return
        if "Crew" in [r.name for r in member.roles]:
            return
        
        # Otherwise, mute the user if they are in the movie night channel
        if after.channel != None:
            if after.channel.name != "Movie Night" and after.channel.name != "AFK":
                await member.edit(mute=False)
            else:
                await member.edit(mute=True)