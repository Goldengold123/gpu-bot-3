def drawBoard(myEmojis):
    horizontal = '🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦'
    mainLine = '⬛⬛⬛🟦⬛⬛⬛🟦⬛⬛⬛'
    top = '⬛{0}⬛🟦⬛{1}⬛🟦⬛{2}⬛'.format(myEmojis[0], myEmojis[1], myEmojis[2])
    middle = '⬛{0}⬛🟦⬛{1}⬛🟦⬛{2}⬛'.format(myEmojis[3], myEmojis[4], myEmojis[5])
    bottom = '⬛{0}⬛🟦⬛{1}⬛🟦⬛{2}⬛'.format(myEmojis[6], myEmojis[7], myEmojis[8])
    board = '{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{9}\n{10}'.format(mainLine, top, mainLine, horizontal,
                                                                            mainLine, middle, mainLine,
                                                                            horizontal,
                                                                            mainLine, bottom, mainLine)
    return board


def win(myEmojis, piece):
    if myEmojis[0] == myEmojis[1] == myEmojis[2] == piece:
        return True
    elif myEmojis[3] == myEmojis[4] == myEmojis[5] == piece:
        return True
    elif myEmojis[6] == myEmojis[7] == myEmojis[8] == piece:
        return True
    elif myEmojis[0] == myEmojis[3] == myEmojis[6] == piece:
        return True
    elif myEmojis[1] == myEmojis[4] == myEmojis[7] == piece:
        return True
    elif myEmojis[2] == myEmojis[5] == myEmojis[8] == piece:
        return True
    elif myEmojis[1] == myEmojis[4] == myEmojis[8] == piece:
        return True
    elif myEmojis[2] == myEmojis[4] == myEmojis[6] == piece:
        return True
    else:
        return False


def draw(myEmojis):
    return (not (win(myEmojis, '❌'))) and (not (win(myEmojis, '⭕'))) and (myEmojis.count('❌') + myEmojis.count('⭕') == 9)


def check(emoji, myEmojis):
    return emoji in myEmojis

