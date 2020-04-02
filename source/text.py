import discord, json, random
from discord.ext import commands
from search import ImageSearch

class Text(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="space")
    @commands.guild_only()
    async def space(self, ctx):
        """ A Simple Command that embeds an image of space """

        # Type to indicate progress
        async with ctx.typing():
            # Ensure we can use the API
            usage = None
            data = None
            with open("config/usage.json", "r") as f:
                data = json.load(f)
                usage = data['google']
                
            if usage < 100 and data != None:
                data['google'] = usage + 1
                with open("config/usage.json", "w") as f:
                    json.dump(data, f)
            else:
                await ctx.send("**Error**: Cannot get image...")
                return
            
            # Get string from the keywords file
            query = None
            with open("config/keywords.txt", "r") as f:
                line = next(f)
                for num, aline in enumerate(f, 2):
                    if random.randrange(num): continue
                    line = aline
                query = line.rstrip()

            if query == None:
                await ctx.send("**Error**: Cannot get image...")
                return

            # Search for the image
            google = ImageSearch()
            image = google.search(query)
            print("Embedding image \'{}\' (of \'{}\')".format(image, query))
            if image == None:
                await ctx.send("**Error**: Cannot get image...")
                return

            # Make the embed
            embed = discord.Embed(colour=0x333333)
            embed.set_author(name="Space Image", url="http://astrosoc.club/", icon_url=image)
            embed.set_image(url=image)

            await ctx.send(embed=embed)
    
    @commands.command(name="info")
    @commands.guild_only()
    async def info(self, ctx):
        print("Returning info")
        embed = discord.Embed(description="Little bot for adding voice roles, by http://donald108.com/ for http://astrosoc.club/", colour=0x5C77FF)
        embed.set_author(name="donald108", url="http://pa.ul.ms", icon_url="https://avatars3.githubusercontent.com/u/26580217?s=460&u=2b5115f75c19140924f46b314f762d14de398d35&v=4")

        await ctx.send(embed=embed)