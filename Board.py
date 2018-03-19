
board = [[], [], [], [], [], [], [], [], [], [], []]
board[0]  = ["TL ", "___", "TW ", "___", "___", "___", "___", "___", "TW ", "___", "TL "]
board[1]  = ["___", "DW ", "___", "___", "___", "DW ", "___", "___", "___", "DW ", "___"]
board[2]  = ["TW ", "___", "TL ", "___", "DL ", "___", "DL ", "___", "TL ", "___", "TW "]
board[3]  = ["___", "___", "___", "TL ", "___", "___", "___", "TL ", "___", "___", "___"]
board[4]  = ["___", "___", "DL ", "___", "___", "___", "___", "___", "DL ", "___", "___"]
board[5]  = ["___", "DW ", "___", "___", "___", "___", "___", "___", "___", "DW ", "___"]
board[6]  = ["___", "___", "DL ", "___", "___", "___", "___", "___", "DL ", "___", "___"]
board[7]  = ["___", "___", "___", "TL ", "___", "___", "___", "TL ", "___", "___", "___"]
board[8]  = ["TW ", "___", "TL ", "___", "DL ", "___", "DL ", "___", "TL ", "___", "TW "]
board[9]  = ["___", "DW ", "___", "___", "___", "DW ", "___", "___", "___", "DW ", "___"]
board[10] = ["TL ", "___", "TW ", "___", "___", "___", "___", "___", "TW ", "___", "TL "]

values = {'A': 1, 'B': 4, 'C': 4,  'D': 2, 'E': 1, 'F': 4, 'G': 3,
          'H': 3, 'I': 1, 'J': 10, 'K': 5, 'L': 2, 'M': 4, 'N': 2,
          'O': 1, 'P': 4, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 2,
          'V': 5, 'W': 4, 'X': 8,  'Y': 3, 'Z': 10}

alphabet = "abcdefghijklmnopqrstuvwxyz"

empty = ["___", "DL ", "TL ", "DW ", "TW "]

def printB(board):
    print "     ",
    for i in range(1, 11):
        print " (" + str(i) + ") ",
    print "(11)" + "\n"
    for i in range(0, 11):
        if i<10:
            print " (" + str(i+1) + ")  ",
        else:
            print " (" + str(i+1) + ") ",
        for tile in board[i]:
            print tile  , " ",
        print "\n", "\n"

def addWord(word, x, y, dir):
    word = word.upper()
    if (dir=="right"):
        if (12-len(word)<x):
            print " Too far to the right"
            return 0
    if (dir=="down"):
        if (12-len(word)<y):
            print " Too far downwards"
            return 0
    pos = (x, y)
    for letter in word:
        board[pos[1]][pos[0]] = "[" + letter + "]"
        if (dir=="right"):
            pos = (pos[0]+1, y)
        else:
            pos = (x, pos[1]+1)

    print "\n" + "Added word " + word + "\n"
    printB(board)
