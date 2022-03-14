from credentials import commandPrefix


def createHelpMainEmbed(embed):
    embed.add_field(name=":one: Important",
                    value="Important commands.",
                    inline=False)

    embed.add_field(name=":two: Math",
                    value="Math commands.",
                    inline=False)

    embed.add_field(name=":three: Games",
                    value="Game commands.",
                    inline=False)

    embed.add_field(name=":four: Funny",
                    value="funny",
                    inline=False)

    embed.add_field(name=":five: Other",
                    value="Miscellaneous commands.",
                    inline=False)


def createHelpImportantEmbed(embed):
    embed.add_field(name="Help",
                    value="`" + commandPrefix + "help` Helps you.",
                    inline=False)

    embed.add_field(name="Ping",
                    value="`" + commandPrefix + "ping` Pong.",
                    inline=False)

    embed.add_field(name="Stop",
                    value="`" + commandPrefix + "stop` Stops if you are 428295738011680769.",
                    inline=False)


def createHelpMathEmbed(embed):
    embed.add_field(name="Add",
                    value="`" + commandPrefix + "add [number1] [number2]`\nAdds 2 numbers.\nReturns `number1 + "
                                                "number2`.",
                    inline=False)

    embed.add_field(name="Subtract",
                    value="`" + commandPrefix + "subtract [number1] [number2]`\nSubtracts 2 numbers.\nReturns "
                                                "`number1 - number2`.",
                    inline=False)

    embed.add_field(name="Multiply",
                    value="`" + commandPrefix + "multiply [number1] [number2]`\nMultiplies 2 numbers.\nReturns "
                                                "`number1 × number2`.",
                    inline=False)

    embed.add_field(name="Divide",
                    value="`" + commandPrefix + "divide [number1] [number2]`\nDivides 2 numbers.\nReturns `number1 ÷ "
                                                "number2`.",
                    inline=False)

    embed.add_field(name="Evaluate",
                    value="`" + commandPrefix + "evaluate [expression]`\nEvaluates an expression.",
                    inline=False)


def createHelpGameEmbed(embed):
    embed.add_field(name="Tic Tac Toe",
                    value="`" + commandPrefix + "playTicTacToe`\nTic Tac Toe for 2 players.",
                    inline=False)

    embed.add_field(name="Hangman",
                    value="`" + commandPrefix + "playHangman`\nHangman using an en_US dictionary.",
                    inline=False)

    embed.add_field(name="Minesweeper",
                    value="`" + commandPrefix + "playMinesweeper [rows] [columns] [mines]`\nMinesweeper\nNumbers: "
                                                ":one: :two: :three: :four: :five: :six: :seven: :eight:\nEmpty Space: "
                                                ":poop:\nMine: :bomb:.",
                    inline=False)

    embed.add_field(name="Number Guessing Game",
                    value="`" + commandPrefix + "playNumberGuessingGame [a] [b]`\nNumber Guessing Game\nGuess an "
                                                "integer between a and b.",
                    inline=False)


def createHelpFunnyEmbed(embed):
    embed.add_field(name="Repeat",
                    value="`" + commandPrefix + "repeat [text] [count]`\nRepeats a string count times\n`inf` means "
                                                "until `!stop` is used.",
                    inline=False)

    embed.add_field(name="Spam Ping",
                    value="`" + commandPrefix + "spamPing [userID] [count]`\nSpam pings a user.",
                    inline=False)

    embed.add_field(name="Troll Spam Ping",
                    value="`" + commandPrefix + "trollSpamPing [userID] [message]`\nA crucial tactic in defeating "
                                                "America.",
                    inline=False)

    embed.add_field(name="Add a dumdum",
                    value="`" + commandPrefix + "addDumdum [userID]`\nAdds a dumdum!",
                    inline=False)

    embed.add_field(name="Remove a dumdum",
                    value="`" + commandPrefix + "removeDumdum [userID]`\nRemoves a dumdum!",
                    inline=False)


def createHelpOtherEmbed(embed):
    embed.add_field(name="Uppercase",
                    value="`" + commandPrefix + "uppercase [text]`\nConverts a string to uppercase.",
                    inline=False)

    embed.add_field(name="Lowercase",
                    value="`" + commandPrefix + "lowercase [text]`\nConverts a string to lowercase.",
                    inline=False)
