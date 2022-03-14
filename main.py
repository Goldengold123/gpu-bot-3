import os
import discord
from discord.ext import commands
import asyncio
import random
import string
from decimal import *
import minesweeper

import nltk
from nltk.corpus import words

from createHelpEmbeds import createHelpMainEmbed
from createHelpEmbeds import createHelpImportantEmbed
from createHelpEmbeds import createHelpMathEmbed
from createHelpEmbeds import createHelpGameEmbed
from createHelpEmbeds import createHelpFunnyEmbed
from createHelpEmbeds import createHelpOtherEmbed


from ticTacToe import drawBoard
from ticTacToe import win
from ticTacToe import draw
from ticTacToe import check

nltk.download('words')

# Token
if os.environ.get("DISCORD_BOT_TOKEN"):
    TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
else:
    from credentials import TOKEN

# Command Prefix
if os.environ.get("DISCORD_BOT_TOKEN"):
    commandPrefix = os.environ.get("commandPrefix")
else:
    from credentials import commandPrefix

# Client
intents = discord.Intents.default()
intents.reactions = True
bot = commands.Bot(command_prefix=commandPrefix, intents=intents)
bot.remove_command("help")

# Dumdums
dumdums = [397105296327049216, 296396903195607040]

# Variables
# Help
helpMessageInformation = [0, 0]

# Tic Tac Toe
ticTacToeMessageInformation = [0]
ticTacToeCurrentPlayer = 1
ticTacToePlayers = [" ", " "]
emojis = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮']


# Connecting to Discord
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


# Latency
@bot.command(aliases=["Ping"])
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(bot.latency))


# Stop
@bot.command(aliases=["Stop"])
async def stop(ctx):
    if ctx.author.id == 428295738011680769:
        await ctx.send('Stopping...')
        await ctx.bot.logout()


# Help Command
@bot.command(aliases=["Help"])
async def help(ctx):
    helpMainEmbed = discord.Embed(title="0️⃣ Commands",
                                  description="what",
                                  colour=discord.Color.red())
    createHelpMainEmbed(helpMainEmbed)
    message = await ctx.send(embed=helpMainEmbed)
    helpMessageInformation[0] = message
    helpMessageInformation[1] = ctx.author
    await message.add_reaction('0️⃣')
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')
    await message.add_reaction('3️⃣')
    await message.add_reaction('4️⃣')
    await message.add_reaction('5️⃣')


# Math
# Addition
@bot.command(aliases=['Add', 'sum', 'Sum'])
async def add(self, a: Decimal, b: Decimal):
    mySum = float(str(a + b))
    await self.send(mySum)


# Subtraction
@bot.command(aliases=['Subtract', 'minus', 'Minus'])
async def subtract(self, a: Decimal, b: Decimal):
    diff = float(str(a - b))
    await self.send(diff)


# Multiplication
@bot.command(aliases=['Multiply', 'times', 'Times'])
async def multiply(self, a: Decimal, b: Decimal):
    product = float(str(a * b))
    await self.send(product)


# Division
@bot.command(aliases=['Divide'])
async def divide(self, a: Decimal, b: Decimal):
    quotient = float(str(a / b))
    await self.send(quotient)


# Evaluate
@bot.command(aliases=['Evaluate', 'eval'])
async def evaluate(self, expression):
    answer = eval(expression)
    await self.send(answer)


# Dumdums
@bot.command(aliases=['AddDumdum', 'adddumdum', 'addDumDum', 'AddDumDum', 'ad', 'AD'])
async def addDumdum(ctx, user_id: int):
    if ctx.author.id == 266260596473856000 or ctx.author.id == 428295738011680769:
        dumdums.append(user_id)
        await ctx.send("Added dumdum", user_id)
    else:
        await ctx.send("you dont have perms to add a dumdum")


@bot.command(aliases=['RemoveDumdum', 'removedumdum', 'removeDumDum', 'RemoveDumDum', 'rd', 'RD'])
async def removeDumdum(ctx, user_id: int):
    if ctx.author.id == 266260596473856000 or ctx.author.id == 428295738011680769:
        if user_id in dumdums:
            dumdums.pop(user_id)
            await ctx.send("Removed dumdum", user_id)
        else:
            await ctx.send(user_id, "is not a dumdum")
    else:
        await ctx.send("you dont have perms to remove a dumdum")


# Spam Ping
@bot.command(aliases=['spamping', 'SpamPing', 'sp', 'SP'])
async def spamPing(ctx, user_id, num: int):
    if ctx.author.id == 428295738011680769 or ctx.author.id == 266260596473856000 or ctx.author.id == 322493122598797323:
        count = 0
        while count < num:
            count += 1
            await ctx.send("Ping " + str(count) + ": " + f"<@" + user_id + "> ")
            await asyncio.sleep(1)
        await ctx.send("Pinged " + str(count) + " times.")
    else:
        await ctx.send("You really think I gave random people access to this?")


# Troll Spam Ping
@bot.command(aliases=['trollspamping', 'TrollSpamPing', 'tsp', 'TSP'])
async def trollSpamPing(ctx, user_id, message):
    if user_id == '428295738011680769':
        await ctx.send("Haha I'm immune!")
    else:
        if ctx.author.id in dumdums:
            await ctx.send("no dumdums cant use this command")
        else:
            while True:
                await ctx.send(f"<@" + user_id + "> " + " " + message)
                await asyncio.sleep(1)


# Repeat
@bot.command(aliases=['Repeat'])
async def repeat(ctx, msg, count):
    if count == 'inf' and (
            ctx.author.id == 428295738011680769 or ctx.author.id == 266260596473856000 or ctx.author.id == 322493122598797323):
        while True:
            await ctx.send(msg)
            await asyncio.sleep(1)
    else:
        if ctx.author.id in dumdums:
            await ctx.send("no dumdums cant use this command")
        else:
            for i in range(int(count)):
                await ctx.send(msg)
                await asyncio.sleep(1)


# Uppercase
@bot.command(aliases=['Uppercase'])
async def uppercase(ctx, *, msg):
    upper = msg.upper()
    await ctx.send(upper)


# Lowercase
@bot.command(aliases=['Lowercase'])
async def lowercase(ctx, *, msg):
    lower = msg.lower()
    await ctx.send(lower)


# Number Game

@bot.command(aliases=['playnumberguessing', 'PlayNumberGuessing',
                      'playNumberGuess', 'playnumberguess', 'PlayNumberGuess',
                      'numberguessing', 'NumberGuessing', 'numberGuessing',
                      'numberguess', 'NumberGuess', 'numberGuess',
                      'numbergame', 'NumberGame', 'numberGame',
                      'playnumbergame', 'PlayNumberGame', 'playNumberGame'])
async def playNumberGuessing(ctx, a: int, b: int):
    num = random.randint(a, b)
    count = 0
    guess = num + 1
    user = ctx.author
    embed = discord.Embed(title="Number Guessing Game",
                          description="Guess an integer between " + str(a) + " and " + str(b) + ".",
                          colour=discord.Color.green())
    msg = await ctx.send(embed=embed)
    while guess != num:
        await msg.edit(embed=embed)
        userMessage = await bot.wait_for('message')
        guess = userMessage.content
        if user == userMessage.author:
            if not guess.isnumeric() or int(guess) < a or int(guess) > b:
                embed.add_field(name=guess, value="Invalid guess!", inline=False)
            elif int(guess) > num:
                count += 1
                embed.add_field(name=guess, value="Too high!", inline=False)
            elif int(guess) < num:
                count += 1
                embed.add_field(name=guess, value="Too low!", inline=False)
            elif int(guess) == num:
                count += 1
                embed.add_field(name=guess,
                                value="You guessed the number in " + str(count) + " tries! Congrats! ||😡||",
                                inline=False)
            else:
                embed.add_field(name=guess, value="Invalid guess!", inline=False)
            await userMessage.delete()


# Tic Tac Toe

@bot.command(aliases=['PlayTicTacToe', 'playtictactoe', 'tictactoe', 'TicTacToe', 'ticTacToe'])
async def playTicTacToe(ctx):
    global ticTacToeMessageInformation, ticTacToeCurrentPlayer, ticTacToeMessageInformation, ticTacToePlayers, emojis
    if ctx.author.id in dumdums:
        await ctx.send('No.')
        return

    ticTacToeMessageInformation = [0]
    ticTacToeCurrentPlayer = 1
    ticTacToePlayers = [" ", " "]
    emojis = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮']

    embed = discord.Embed(title="Tic Tac Toe",
                          description="Player 1: `" + str(ticTacToePlayers[0]) + "`\nPlayer2: `" + str(ticTacToePlayers[1]) + "`",
                          colour=discord.Color.green())
    embed.add_field(name="Player 1", value="React with ❌.", inline=False)
    embed.add_field(name="Player 2", value="React with ⭕.", inline=False)

    msg = await ctx.send(embed=embed)

    ticTacToeMessageInformation[0] = msg
    await msg.add_reaction('❌')
    await msg.add_reaction('⭕')


# Hangman

@bot.command(aliases=['PlayHangman', 'hangman', 'Hangman'])
async def playHangman(ctx):
    await ctx.send('Word Chooser, please send a message.')
    msg1 = await bot.wait_for('message')
    boss = msg1.author
    channel = msg1.channel
    await ctx.send('Word Chooser, DM me your secret word. Format: no spaces, all lowercase, only english characters. '
                   '(message will be ignored if criteria is not met)')
    alphabet = list(string.ascii_lowercase)

    def checkWordChooser(m):
        wordList = list(m.content)
        tempW = False
        for letter in wordList:
            if letter in alphabet:
                tempW = True
            else:
                tempW = False
                break
        tempE = ((m.content).lower()) in words.words()
        return m.author == boss and m.channel.type is discord.ChannelType.private and tempW and tempE

    word = await bot.wait_for('message', check=checkWordChooser)
    hangmanBoard = [
        '''
+--------+
|              |
|            
|  
|
''',
        '''
        +--------+
|              |
|             O
|       
|
''',
        '''
        +--------+
|              |
|             O
|              |
|
''',
        '''
        +--------+
|              |
|             O
|            -|
|
''',
        '''
        +--------+
|              |
|             O
|            -|-
|
''',
        '''
        +--------+
|              |
|             O
|            -|-
|           /
''',
        '''
        +--------+
|              |
|             O
|            -|-
|           /  \\
'''
    ]
    wordLength = len(word.content)
    blanks = []

    wrong = []

    def printWrong(myWrong):
        myString = ''
        for item in myWrong:
            myString += item
            myString += ', '
        return myString

    def checkGuess(m):
        tempG = False
        guessList = list(m.content)
        for letterGuess in guessList:
            if letterGuess in alphabet:
                tempG = True
            else:
                tempG = False
                break
        if m in wrong:
            return False
        else:
            return m.content in alphabet and m.channel == channel and tempG

    for i in range(wordLength):
        blanks.append('\_')

    lives = 6
    lettersLeft = wordLength
    while lives > 0 and lettersLeft > 0:
        await ctx.send(hangmanBoard[6 - lives] + '|   ' + ' '.join(blanks) + '\n'
                       + 'Your incorrect guesses are ' + printWrong(wrong) + '\n'
                       + 'Make a guess!')
        guess = await bot.wait_for('message', check=checkGuess)
        found = False
        for i in range(len(word.content)):
            if word.content[i] == guess.content:
                blanks[i] = '__' + guess.content + '__'
                lettersLeft -= 1
                found = True
        if found:
            await ctx.send('Correct!')
        else:
            lives -= 1
            await ctx.send('Incorrect! You lose 1 life.')
            wrong.append(guess.content)

    if lettersLeft <= 0:
        await ctx.send(hangmanBoard[6 - lives] + '|   ' + ' '.join(blanks)
                       + '\n' + 'Congratulations! You guessed the word!')
    if lives <= 0:
        print(2)
        await ctx.send(hangmanBoard[6] + '|   ' + ' '.join(blanks)
                       + '\n' + 'The word chooser has won! The word was ' + word.content + '.')


# Minesweeper

@bot.command(aliases=['PlayMinesweeper', 'minesweeper', 'Minesweeper'])
async def playMinesweeper(ctx, myRows: int, myColumns: int, myMines: int):
    if myRows <= 0:
        await ctx.send("WARNING! Row count must be at least 1...setting to default 10.")
        myRows = 10
    if myColumns <= 0:
        await ctx.send("WARNING! Mine count must be at least 1...setting to default 10.")
        myColumns = 10
    if myMines <= 0:
        await ctx.send("WARNING! Mine count must be at least 1...setting to default 10.")
        myMines = 10
    await ctx.send("WARNING! Generation of Minesweeper Grid may be unfinished, as a result of Discord's character "
                   "limit.")
    cols = myColumns
    rows = myRows
    generator = minesweeper.Generator(cols, rows)
    mines = myMines
    grid = generator.generate_raw(mines)
    minesweeperDict = {
        "M": "||:bomb:||",
        " ": "||:poop:||",
        "1": "||:one:||",
        "2": "||:two:||",
        "3": "||:three:||",
        "4": "||:four:||",
        "5": "||:five:||",
        "6": "||:six:||",
        "7": "||:seven:||",
        "8": "||:eight:||",
    }
    printThingy = """"""
    for item in grid:
        for item2 in item:
            printThingy += minesweeperDict[item2]
        printThingy += "\n"
    await ctx.send(printThingy)


# Rules

rules = [
    """:octagonal_sign:
> **Warn/Mute/Kick/Ban System:**
    
All offenses result in a **Warn** to serve as a log
**Mutes** are issued on repeated or more serious offenses
**Kicks** are issued on repeated serious offenses
**Bans** are issued after repeated kicks

The word of the Admins/Moderators is final""",
    """:one:
> No racial slurs or offensive language in any channel

Second instance and onward will result in a **Mute** of *one hour*""",
    """:two:
> No NSFW content outside of NSFW channels
Doing so will result in a **Mute** of *two hours*""",
    """:three:
> No spamming

Spamming in any channel (with the exception of #spam) will result in a **Mute** of *one hour*
Excessive Bot commands outside of Bot channels counts as spam
Unrelated images, videos, or large bodies of text will also count as spam

Spamming offensive language or NSFW content will result in a **Kick** for *twenty-four hours*

Spam-pinging will result in a **Mute** of *24 hours*""",
    """:four:
> No TTS messages

Second instance and onward will result in a **Mute** of *one hour*""",
    """:five:
> No alternate accounts

Unless you have a good reason, all alts will be kicked""",
    """:six:
> No bullying

Unless the recipient makes it clear that they are ok with it-

First instance will result in a **Mute** of *two hours*
Second instance will result in a **Mute** of *twenty-four hours*
Third instance and onward will result in a **Kick** of *twenty-four hours*"""
]


@bot.command(aliases=['Rule'])
async def rule(ctx, num: int):
    await ctx.send(rules[int(num)])


# Reaction is added
@bot.event
async def on_reaction_add(reaction, user: discord.Member = None):
    global ticTacToeCurrentPlayer
    if user.id == 718298166931488809:
        return

    # Reaction is on Help message
    needHelp = reaction.message == helpMessageInformation[0] and user == helpMessageInformation[1]
    if needHelp:
        if reaction.emoji == '0️⃣':
            helpMainEmbed = discord.Embed(title="0️⃣ Commands",
                                          description="what",
                                          colour=discord.Color.red())
            createHelpMainEmbed(helpMainEmbed)
            await reaction.message.edit(embed=helpMainEmbed)
        if reaction.emoji == '1️⃣':
            helpImportantEmbed = discord.Embed(title="1️⃣ Important Commands",
                                               description="Useful",
                                               colour=discord.Color.orange())
            createHelpImportantEmbed(helpImportantEmbed)
            await reaction.message.edit(embed=helpImportantEmbed)
        if reaction.emoji == '2️⃣':
            helpMathEmbed = discord.Embed(title="2️⃣ Math Commands",
                                          description="Math",
                                          colour=discord.Color.gold())
            createHelpMathEmbed(helpMathEmbed)
            await reaction.message.edit(embed=helpMathEmbed)
        if reaction.emoji == '3️⃣':
            helpGameEmbed = discord.Embed(title="3️⃣ Game Commands",
                                          description="Games",
                                          colour=discord.Color.green())
            createHelpGameEmbed(helpGameEmbed)
            await reaction.message.edit(embed=helpGameEmbed)
        if reaction.emoji == '4️⃣':
            helpFunnyEmbed = discord.Embed(title="4️⃣ Funny Commands",
                                           description="Funny",
                                           colour=discord.Color.blue())
            createHelpFunnyEmbed(helpFunnyEmbed)
            await reaction.message.edit(embed=helpFunnyEmbed)
        if reaction.emoji == '5️⃣':
            helpOtherEmbed = discord.Embed(title="5️⃣ Other Commands",
                                           description="Other",
                                           colour=discord.Color.purple())
            createHelpOtherEmbed(helpOtherEmbed)
            await reaction.message.edit(embed=helpOtherEmbed)

    # Reaction is on Tic Tac Toe message
    playingTicTacToe = reaction.message == ticTacToeMessageInformation[0]
    if playingTicTacToe:
        # Choose players
        if str(ticTacToePlayers[0]) == " " or str(ticTacToePlayers[1]) == " ":
            if reaction.emoji == '❌':
                ticTacToePlayers[0] = user
                await reaction.message.clear_reaction(reaction.emoji)
            if reaction.emoji == '⭕':
                ticTacToePlayers[1] = user
                await reaction.message.clear_reaction(reaction.emoji)

        # Update Embed
        embed = discord.Embed(title="Tic Tac Toe",
                              description="Player 1: `" + str(ticTacToePlayers[0]) + "`\nPlayer2: `" + str(ticTacToePlayers[
                                  1]) + "`",
                              colour=discord.Color.green())
        embed.clear_fields()

        if str(ticTacToePlayers[0]) == " ":
            embed.add_field(name="Player 1", value="React with ❌.", inline=False)
        if str(ticTacToePlayers[1]) == " ":
            embed.add_field(name="Player 2", value="React with ⭕.", inline=False)

        if str(ticTacToePlayers[0]) != " " and str(ticTacToePlayers[1]) != " ":
            embed.add_field(name="Board", value=drawBoard(emojis), inline=False)

            if not (draw(emojis) or win(emojis, '❌') or win(emojis, '⭕')):
                embed.add_field(name="Player " + str(ticTacToeCurrentPlayer) + ": `" + str(ticTacToePlayers[ticTacToeCurrentPlayer - 1]) + "`",
                                value="React with the letter of where you would like to go.",
                                inline=False)
            if not win(emojis, '❌') and not win(emojis, '⭕') and not draw(emojis):
                for emoji in emojis:
                    if emoji != '❌' and emoji != '⭕':
                        await reaction.message.add_reaction(emoji)
            else:
                for emoji in emojis:
                    await reaction.message.clear_reaction(emoji)

        await reaction.message.edit(embed=embed)

        # Play game
        if ((str(ticTacToePlayers[0]) != " " and str(ticTacToePlayers[1]) != " ")
                and (not (draw(emojis) or win(emojis, '❌') or win(emojis, '⭕')))
                and check(reaction.emoji, emojis)) and user == ticTacToePlayers[ticTacToeCurrentPlayer-1]\
                and reaction.emoji != '❌' and reaction.emoji != '⭕':
            if ticTacToeCurrentPlayer == 1:
                emojis[emojis.index(reaction.emoji)] = '❌'
            else:
                emojis[emojis.index(reaction.emoji)] = '⭕'

            embed.clear_fields()
            await reaction.message.clear_reaction(reaction.emoji)

            ticTacToeCurrentPlayer %= 2
            ticTacToeCurrentPlayer += 1
            embed.add_field(name="Board", value=drawBoard(emojis), inline=False)
            if win(emojis, '❌'):
                embed.add_field(name="Player 1: `" + str(ticTacToePlayers[ticTacToeCurrentPlayer - 1]) + "`",
                                value="Congrats! Player 1 has won!",
                                inline=False)
            elif win(emojis, '⭕'):
                embed.add_field(name="Player 2: `" + str(ticTacToePlayers[ticTacToeCurrentPlayer - 1]) + "`",
                                value="Congrats! Player 2 has won!",
                                inline=False)
            elif draw(emojis):
                embed.add_field(name="Draw",
                                value="The 2 players have drawn! HAHA, that means I win!",
                                inline=False)
            else:
                embed.add_field(name="Player " + str(ticTacToeCurrentPlayer) + ": `" + str(ticTacToePlayers[ticTacToeCurrentPlayer - 1]) + "`",
                                value="React with the letter of where you would like to go.",
                                inline=False)

        await reaction.message.edit(embed=embed)
    await reaction.message.remove_reaction(reaction.emoji, user)


bot.run(TOKEN)
