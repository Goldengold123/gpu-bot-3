import asyncio
import random
import string
# import enchant
import discord
import os

from decimal import *
from discord.ext import commands

bot = commands.Bot('!')

if os.environ.get("DISCORD_BOT_TOKEN"):
    TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
else:
    from credentials import TOKEN

# Connecting to Discord

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


# Addition

@bot.command(name='add', help='Adds 2 numbers.')
async def add(self, a: Decimal, b: Decimal):
    sum = float(str(a + b))
    await self.send(sum)


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

@bot.command(name='spam_ping', help='Spam Ping')
@commands.has_role('Premier of BC')
async def spam_ping(ctx, user_id, num: int):
    count = 0
    while count < num:
        count += 1
        await ctx.send("Ping " + str(count) + ": " + f"<@" + user_id + "> ")
        await asyncio.sleep(1)
    await ctx.send("Pinged " + str(count) + " times.")


# Troll Spam Ping

@bot.command(name='troll_spam_ping', help='A crucial tactic part of defeating America and Trump')
@commands.has_role('BC')
async def troll_spam_ping(ctx, user_id, message):
    if user_id == '428295738011680769':
        await ctx.send("Haha I'm immune!")
    else:
        while True:
            await ctx.send(f"<@" + user_id + "> " + " " + message)
            await asyncio.sleep(1)


# Latency

@bot.command(name='ping', help='pong')
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))


# Stop

@bot.command(name='stop', help='stops the bot')
@commands.has_role('Premier of BC')
async def stop(ctx):
    await ctx.send('Stopping...')
    await ctx.bot.logout()


# Repeat

@bot.command(name='repeat', help='repeats user')
async def repeat(ctx, *, msg):
    await ctx.send(msg)


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

@bot.command(name='numGame', help='Guess an integer between a and b.')
async def numGame(ctx, a: int, b: int):
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

@bot.command(name='tictactoe', help='Tic Tac Toe for 2 players.')
async def tictactoe(ctx):
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
                                                                                mainLine, middle, mainLine, horizontal,
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
            await ctx.send('The 2 players have drew! HAHA, that means I win!' + '\n' + drawBoard())
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

@bot.command(name='hangman', help='hangman game, uses en_US dictionary')
async def hangman(ctx):
    await ctx.send('Word Chooser, please send a message.')
    msg1 = await bot.wait_for('message')
    boss = msg1.author
    channel = msg1.channel
    await ctx.send('Word Chooser, DM me your secret word.')
    alphabet = list(string.ascii_lowercase)
    enUS = ['hello', 'apple']
    # enUS = enchant.Dict('en_US')

    def checkWordChooser(m):
        wordList = list(m.content)
        tempW = False
        for letter in wordList:
            if letter in alphabet:
                tempW = True
            else:
                tempW = False
                break
        tempE = enUS.check(m.content)
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
        print(1)
        await ctx.send(hangmanBoard[6 - lives] + '|   ' + ' '.join(blanks)
                       + '\n' + 'Congratulations! You guessed the word!')
    if lives <= 0:
        print(2)
        await ctx.send(hangmanBoard[6] + '|   ' + ' '.join(blanks)
                       + '\n' + 'The word chooser has won! The word was ' + word.content + '.')


# Minesweeper

@bot.command(name='minesweeper', help='numbers, poo=empty, bomb=mine')
async def minesweeper(ctx):
    await ctx.send("""||:poop:||||:poop:||||:one:||||:two:||||:bomb:||||:one:||||:one:||||:one:||||:one:||
||:poop:||||:poop:||||:one:||||:bomb:||||:two:||||:one:||||:one:||||:bomb:||||:one:||
||:poop:||||:poop:||||:one:||||:one:||||:one:||||:poop:||||:one:||||:one:||||:one:||
||:one:||||:one:||||:poop:||||:poop:||||:poop:||||:poop:||||:poop:||||:poop:||||:poop:||
||:bomb:||||:one:||||:poop:||||:poop:||||:poop:||||:poop:||||:poop:||||:poop:||||:poop:||
||:two:||||:two:||||:poop:||||:one:||||:one:||||:one:||||:one:||||:one:||||:one:||
||:bomb:||||:one:||||:poop:||||:one:||||:bomb:||||:one:||||:one:||||:bomb:||||:two:||
||:one:||||:one:||||:one:||||:two:||||:two:||||:one:||||:one:||||:three:||||:bomb:||
||:poop:||||:poop:||||:one:||||:bomb:||||:one:||||:poop:||||:poop:||||:two:||||:bomb:||""")
bot.run(TOKEN)
