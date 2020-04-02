import discord, json, atexit
from discord.ext import commands
from voice import Voice
from text import Text
from apscheduler.schedulers.background import BackgroundScheduler

# Read the token
token = None
with open("config/tokens.json", "r") as f:
    data = json.load(f)
    token = data['discord']

# Register the bot
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), description="Bot for adding voice roles")

# Print when ready
@bot.event
async def on_ready():
    # Print we're connected
    print("Connected as {0} ({0.id})".format(bot.user))

    # Change the bot
    await bot.change_presence(activity=discord.Game("donald108.com"))
    print("Playing donald108.com")

# Add cogs
bot.add_cog(Voice(bot))
bot.add_cog(Text(bot))

# Job for the worker
def job():
    data = { 'google' : 0 }
    with open("config/usage.json", "w") as f:
        json.dump(data, f)
        print("Cleared usage.json file")

# Call the worker function every day
cron = BackgroundScheduler(deamon=True)
cron.add_job(func=job, trigger='interval', days=1)
cron.start()

# Register scheduler to shutdown
atexit.register(lambda: cron.shutdown(wait=False))

# Allow the bot to join
if token != None:
    bot.run(token)