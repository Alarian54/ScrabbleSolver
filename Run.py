from Methods import *

def runFirst():
    letters = raw_input(" Letters: ")
    firstmove(letters)
    runFirst()

def runMove():
    letters = raw_input(" Letters: ")
    words = posswords(letters, 6)
    for word in words:
        print " " + str(word)
    print ""
    runMove()

def runGiven():
    letters = raw_input(" Letters: ")
    given = raw_input(" Given letter: ")
    pos = raw_input(" Its position: ")
    words = posswordswpos(letters, given, int(pos), 6)
    for word in words:
        print " " + str(word)
    print ""
    runGiven()

print ""

#for letter in alphabet:
#    move("esjzoq"+letter, "k", 5, 5, "right")
#move("xocznj", "s", 8, 7, "down")
#runFirst()
#runMove()
#runGiven()

printB(board)

addWord("jot", 8, 0, "down")
addWord("squaw", 5, 1, "down")
addWord("amen", 9, 2, "down")
addWord("gadis", 7, 3, "down")
addWord("lex", 8, 4, "down")
addWord("widen", 5, 5, "right")
addWord("six", 6, 6, "right")

line(7, "lerczno", "right")

print ""
