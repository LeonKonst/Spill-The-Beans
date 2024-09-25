import discord
import time
import random
from discord.ext import commands
import Settings 

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix='/', intents=intents)

# Each user has a cooldown until the next message
# Dictionary that saves 
user_last_dm = {}
# Change the value of the variable to alter the cooldown.
cooldown_seconds = Settings.cooldown 

# Probability percentage to reveal senders id (a value between 0 to 100).
probability = Settings.probability

# This part ensures that the limits of probability are being set. 
if probability > 100:
    probability = 100
elif probability < 0:
    probability = 0

# Channel ID that the bot will sent the messages:
channel_ID = Settings.channelID

# Bot's token
token = Settings.token

# Language
language = Settings.lang


# Function that checks if the id of the sender will be revealed.
def isRevealed(probability):
    # Produce random integer from 1 to 100.
    random_int = random.randint(1,100)
    # Check if this random integer is lower than the probability value.
    if random_int <= probability:
        return True
    return False

async def reportToUser(message, dm_content, language, isRevealed):
    if isRevealed:
        if language == "gr":
            await message.channel.send("Ατύχησες! Το μήνυμα σου είναι επώνυμο!")
            await bot.get_channel(channel_ID).send(f"\{dm_content} \n-<@{message.author.id}>")
        elif language == "en":
            await message.channel.send("Too bad! Your name is revealed!")
            await bot.get_channel(channel_ID).send(f"\{dm_content} \n-<@{message.author.id}>")                
    else:
        if language == "gr": 
            await message.channel.send("Το μήνυμα σου είναι ανώνυμο!")
            await bot.get_channel(channel_ID).send(f"{dm_content} \n**-Ανώνυμο**")
        elif language == "en":
            await message.channel.send("Your message is anonymous!")
            await bot.get_channel(channel_ID).send(f"{dm_content} \n**-Unknown**")

# Function that checks if the sender is in the cooldown period.
async def isOnhold (message, language):
    # Saves current time to a variable.
    current_time = time.time()
    # Saves the senders id to a variable.
    user_id = message.author.id
    # Checks if the users id is in the dictionary user_last_dm.
    if user_id in user_last_dm:
        # If this name is in the dictionary then:
        # Saves the time of last message to a variable.
        last_dm_time = user_last_dm[user_id]
        # And subtracts that time from current time. The result is saved to a variable.
        time_since_last_dm = current_time - last_dm_time
        # if this variable is less than the cooldown that was set then:
        if time_since_last_dm < cooldown_seconds:
            # It calculates the remaining time until the next message.
            remaining_time = cooldown_seconds - time_since_last_dm
            if language == "gr":
                await message.channel.send(f"Περίμενε άλλα {remaining_time:.1f} δευτερόλεπτα πριν στείλεις το επόμενο μήνυμα.")
            elif language == "en":
                await message.channel.send(f"Wait {remaining_time:.1f} second to sent the next message.")
            return True  
    # If it is a new user then it saves the current time to the dictionary with user_id as a key.   
    user_last_dm[user_id] = current_time
    return False

# Bot responds to the event of a message being sent. 
@bot.event
async def on_message(message):
    # Check if the message is DM. 
    dm_content = message.content
    if isinstance(message.channel, discord.DMChannel) and message.author != bot.user:
        # Save content text to a variable.
        # Check if user is onHold:
        if await isOnhold(message, language):
            return
        # Check if user will be revealed:
        await reportToUser(message, dm_content, language,isRevealed(probability))
    else:
        await bot.process_commands(message)

# Bot's Token
bot.run(token)