import asyncio
import random
import string
import nltk
import minesweeper
import discord
import os

nltk.download('words')
from nltk.corpus import words
from decimal import *
from discord.ext import commands

bot = commands.Bot(command_prefix='!', help_command=None)

dumdums = [397105296327049216]

if os.environ.get("DISCORD_BOT_TOKEN"):
    TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
else:
    from credentials import TOKEN


# Connecting to Discord

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


# Latency

@bot.command(name='ping', help='pong')
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(bot.latency))


# Stop

@bot.command(name='stop', help='stops the bot')
async def stop(ctx):
    if ctx.author.id == 428295738011680769:
        await ctx.send('Stopping...')
        await ctx.bot.logout()


# Help Command

@bot.group(invoke_without_command=True)
async def help(ctx, command: str):
    if command == None:
        helpList = discord.Embed(title="Help",
                                 description="Use !help <command> for more info on a command. You can also "
                                             "use !help <category> for more info on a category.",
                                 color=ctx.author.color)
        helpList.add_field(name="Bot", value="help, ping, stop")
        helpList.add_field(name="Math", value="add, subtract, multiply, divide")
        helpList.add_field(name="Games", value="playTicTacToe, playHangman, playMinesweeper, playNumberGuessingGame")
        helpList.add_field(name="Miscellaneous", value="uppercase, lowercase, repeat, spamPing, trollSpamPing")
    elif command == "help":
        helpList = discord.Embed(title="Help", description="Prints help message", color=ctx.author.color)
        helpList.add_field(name="Syntax", value="!help")
    elif command == "ping":
        helpList = discord.Embed(title="Ping", description="Pong", color=ctx.author.color)
        helpList.add_field(name="Syntax", value="!ping")
    elif command == "stop":
        helpList = discord.Embed(title="Stop", description="Restarts", color=ctx.author.color)
        helpList.add_field(name="Syntax", value="!stop")
    elif command == "add":
        helpList = discord.Embed(title="Add", description="Adds 2 numbers.", color=ctx.author.color)
        helpList.add_field(name="Syntax", value="!add [number] [number]")
    elif command == "subtract":
        helpList = discord.Embed(title="Subtract", description="Subtracts 2 numbers.", color=ctx.author.color)
        helpList.add_field(name="Syntax", value="!subtract [number] [number]")
    elif command == "multiply":
        helpList = discord.Embed(title="Multiply", description="Multiplies 2 numbers.", color=ctx.author.color)
        helpList.add_field(name="Syntax", value="!multiply [number] [number]")
    elif command == "divide":
        helpList = discord.Embed(title="Divide", description="Divides 2 numbers.", color=ctx.author.color)
        helpList.add_field(name="Syntax", value="!divide [number] [number]")
    elif command == "playTicTacToe":
        helpList = discord.Embed(title="Tic Tac Toe", description="GAME: Tic Tac Toe for 2 players.",
                                 color=ctx.author.color)
        helpList.add_field(name="Syntax", value="!playTicTacToe")
    elif command == "playHangman":
        helpList = discord.Embed(title="Hangman", description="GAME: Hangman | uses en_US dictionary",
                                 color=ctx.author.color)
        helpList.add_field(name="Syntax", value="!playHangman")
    elif command == "playMinesweeper":
        helpList = discord.Embed(title="Minesweeper", description="GAME: Minesweeper | numbers: :one: :two: :three: "
                                                                  ":four: :five: :six: :seven: :eight:, empty: :poop:, "
                                                                  "mine: :bomb:", color=ctx.author.color)
        helpList.add_field(name="Syntax", value="!playMinesweeper [rows] [columns] [mines]")
    elif command == "playNumberGuessingGame":
        helpList = discord.Embed(title="Number Guessing Game", description="GAME: Guess an integer between a and b.",
                                 color=ctx.author.color)
        helpList.add_field(name="Syntax", value="!playNumberGuessingGame [a] [b]")
    elif command == "uppercase":
        helpList = discord.Embed(title="Uppercase", description="Converts a string to uppercase",
                                 color=ctx.author.color)
        helpList.add_field(name="Syntax", value="!uppercase [text]")
    elif command == "lowercase":
        helpList = discord.Embed(title="Lowercase", description="Converts a string to lowercase",
                                 color=ctx.author.color)
        helpList.add_field(name="Syntax", value="!lowercase [text]")
    elif command == "repeat":
        helpList = discord.Embed(title="Repeat", description="Repeats a string some number of times; \"inf\" means "
                                                             "until !stop is used", color=ctx.author.color)
        helpList.add_field(name="Syntax", value="!lowercase [text]")
    elif command == "spamPing":
        helpList = discord.Embed(title="Spam Ping", description="Spam Pings a user", color=ctx.author.color)
        helpList.add_field(name="Syntax", value="!spamPing [userID] [count]")
    elif command == "trollSpamPing":
        helpList = discord.Embed(title="Troll Spam Ping", description="A crucial tactic part of defeating America and "
                                                                      "Trump", color=ctx.author.color)
        helpList.add_field(name="Syntax", value="!trollSpamPing [userID] [message]")
    else:
        helpList = discord.Embed(title="Command Not Found", color=ctx.author.color)
    await ctx.send(embed=helpList)


# Math


# Addition

@bot.command(name='add', help='Adds 2 numbers.')
async def add(self, a: Decimal, b: Decimal):
    mySum = float(str(a + b))
    await self.send(mySum)


# Subtraction

@bot.command(name='subtract', help='Subtracts 2 numbers.')
async def subtract(self, a: Decimal, b: Decimal):
    diff = float(str(a - b))
    await self.send(diff)


# Multiplication

@bot.command(name='multiply', help='Multiplies 2 numbers.')
async def multiply(self, a: Decimal, b: Decimal):
    product = float(str(a * b))
    await self.send(product)


# Division

@bot.command(name='divide', help='Divides 2 numbers.')
async def divide(self, a: Decimal, b: Decimal):
    quotient = float(str(a / b))
    await self.send(quotient)


# Spam Ping

@bot.command(name='spamPing', help='Spam Ping')
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

@bot.command(name='trollSpamPing', help='A crucial tactic part of defeating America and Trump')
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

@bot.command(name='repeat', help='repeats user')
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

@bot.command(name='uppercase', help='converts a string to uppercase')
async def uppercase(ctx, *, msg):
    upper = msg.upper()
    await ctx.send(upper)


# Lowercase

@bot.command(name='lowercase', help='converts a string to lowercase')
async def lowercase(ctx, *, msg):
    lower = msg.lower()
    await ctx.send(lower)


# Number Game

@bot.command(name='playNumberGuessing', help='GAME: Guess an integer between a and b.')
async def playNumberGuessing(ctx, a: int, b: int):
    num = random.randint(a, b)
    count = 0
    guess = 1.2
    await ctx.send('Player please send a message.')
    msg = await bot.wait_for("message")
    user = ctx.author
    await ctx.send('Guess an integer between ' + str(a) + ' and ' + str(b) + '.')
    while guess != num:
        guess = await bot.wait_for("message")
        if user == guess.author:
            if int(guess.content) > num:
                await ctx.send('Too high!')
                count += 1
            elif int(guess.content) < num:
                await ctx.send('Too low!')
                count += 1
            elif int(guess.content) == num:
                count += 1
                await ctx.send('You guessed the number in ' + str(count) + ' tries! Congrats! ||😡||')
                break


# Tic Tac Toe

@bot.command(name='playTicTacToe', help='GAME: Tic Tac Toe for 2 players.')
async def playTicTacToe(ctx):
    if ctx.author.id == 322493122598797323:
        await ctx.send('No.')
    else:
        await ctx.send('Player 1 please send a message.')
        msg1 = await bot.wait_for('message')
        user1 = msg1.author
        channel1 = msg1.channel
        await ctx.send('Player 2 please send a message.')
        msg2 = await bot.wait_for('message')
        user2 = msg2.author
        channel2 = msg2.channel
        letters = {
            'A': '🇦',
            'B': '🇧',
            'C': '🇨',
            'D': '🇩',
            'E': '🇪',
            'F': '🇫',
            'G': '🇬',
            'H': '🇭',
            'I': '🇮'
        }
        filled = []
        possibleMoves = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

        def drawBoard():
            horizontal = '--------------------------------------'
            mainLine = '⬛⬛⬛ | ⬛⬛⬛ | ⬛⬛⬛'
            top = '⬛{0}⬛ | ⬛{1}⬛ | ⬛{2}⬛'.format(letters['A'], letters['B'], letters['C'])
            middle = '⬛{0}⬛ | ⬛{1}⬛ | ⬛{2}⬛'.format(letters['D'], letters['E'], letters['F'])
            bottom = '⬛{0}⬛ | ⬛{1}⬛ | ⬛{2}⬛'.format(letters['G'], letters['H'], letters['I'])
            board = '{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{9}\n{10}'.format(mainLine, top, mainLine, horizontal,
                                                                                    mainLine, middle, mainLine,
                                                                                    horizontal,
                                                                                    mainLine, bottom, mainLine)
            return board

        def win(myBoard, piece):
            if myBoard['A'] == myBoard['B'] == myBoard['C'] == piece:
                return True
            elif myBoard['D'] == myBoard['E'] == myBoard['F'] == piece:
                return True
            elif myBoard['G'] == myBoard['H'] == myBoard['I'] == piece:
                return True
            elif myBoard['A'] == myBoard['D'] == myBoard['G'] == piece:
                return True
            elif myBoard['B'] == myBoard['E'] == myBoard['H'] == piece:
                return True
            elif myBoard['C'] == myBoard['F'] == myBoard['I'] == piece:
                return True
            elif myBoard['A'] == myBoard['E'] == myBoard['I'] == piece:
                return True
            elif myBoard['C'] == myBoard['E'] == myBoard['G'] == piece:
                return True
            else:
                return False

        def draw(myBoard, myFilled):
            return (not (win(myBoard, '❌'))) and (not (win(myBoard, '⭕'))) and len(myFilled) == 9

        while not (draw(letters, filled)) and not (win(letters, '❌')) and not (win(letters, '⭕')):

            await ctx.send(drawBoard() + '\n' + 'Player 1, send the letter of where you would like to go.')

            def check1(m):
                return (m.author == user1 and
                        m.channel == channel1 and
                        not (m.content.upper() in filled) and
                        m.content.upper() in possibleMoves)

            move1 = await bot.wait_for('message', check=check1)
            letters[move1.content.upper()] = '❌'
            filled.append(move1.content.upper())
            if win(letters, '❌'):
                await ctx.send('Congrats! Player 1 has won!' + '\n' + drawBoard())
                break
            if draw(letters, filled):
                await ctx.send('The 2 players have drawn! HAHA, that means I win!' + '\n' + drawBoard())
                break
            await ctx.send(drawBoard() + '\n' + 'Player 2, send the letter of where you would like to go.')

            def check2(m):
                return (m.author == user2 and
                        m.channel == channel2 and
                        not (m.content.upper() in filled) and
                        m.content.upper() in possibleMoves)

            move2 = await bot.wait_for('message', check=check2)
            letters[move2.content.upper()] = '⭕'
            filled.append(move2.content.upper())
            if win(letters, '⭕'):
                await ctx.send('Congrats! Player 2 has won!' + '\n' + drawBoard())
                break


# Hangman

@bot.command(name='playHangman', help='GAME: hangman, uses en_US dictionary')
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

@bot.command(name='playMinesweeper', help='GAME: minesweeper, numbers, poo=empty, bomb=mine')
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


@bot.command()
async def rule(ctx, num: int):
    await ctx.send(rules[int(num)])


bot.run(TOKEN)
