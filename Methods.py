import random
from Board import *

def checkValid(word):
    with open("Wordlist.txt", "r") as database:
        for data in database:
            if (data[:len(data)-2].upper()==word.upper()):
                return True
        return False

def scorezero(word, x, y, dir):
    num = 0
    doubles = 0
    triples = 0
    for i in range(0, len(word)):
        letter = word[i]
        if board[y][x]=="DL ":
            num += values[letter]*2
        elif board[y][x]=="TL ":
            num += values[letter]*3
        elif board[y][x]=="DW ":
            num += values[letter]
            doubles += 1
        elif board[y][x]=="TW ":
            num += values[letter]
            triples += 1
        else:
            num += values[letter]
        if (dir=="right"):
            x += 1
        else:
            y += 1
    return num * (2**doubles) * (3**triples)

def scoreone(word, pos, x, y, dir):
    num = 0
    doubles = 0
    triples = 0
    for i in range(0, len(word)):
        letter = word[i]
        if (int(i)!=int(pos)):
            if board[y][x]=="DL ":
                num += values[letter]*2
            elif board[y][x]=="TL ":
                num += values[letter]*3
            elif board[y][x]=="DW ":
                num += values[letter]
                doubles += 1
            elif board[y][x]=="TW ":
                num += values[letter]
                triples += 1
            else:
                num += values[letter]
        if (dir=="right"):
            x += 1
        else:
            y += 1
    num += values[word[pos]]
    return num * (2**doubles) * (3**triples)

def sort(words):
    sorted = []
    for i in range(-1, len(words)-1):
        maxs = 0
        maxi = 0
        for i in range(-1, len(words)):
            if (int(words[i][1])>=int(maxs)):
                maxs = words[i][1]
                maxi = i
        sorted.append(words[maxi])
        del(words[maxi])
    return sorted

def posswords(letters, length):
    words = []
    letters.upper()
    with open("Wordlist.txt", "r") as database:
        for data in database:
            data = data[:len(data)-2].upper()
            letterscopy = letters.upper()
            datacopy = data.upper()
            matches = 0
            for letter in letterscopy:
                if letter in data:
                    matches += 1
                    letterscopy = letterscopy[1:]
                    l = list(data)
                    p = l.index(letter)
                    del(l[p])
                    data = "".join(l)
            if (matches==len(datacopy) and len(datacopy)<=length):
                words.append(datacopy)
        return words

def posswordswpos(letters, given, pos, length):
    given = given.upper()
    words = []
    letters = letters.upper()
    with open("Wordlist.txt", "r") as database:
        for data in database:
            data = data[:len(data)-2].upper()
            letterscopy = letters.upper()
            datacopy = data.upper()
            matches = 0
            l = list(data)
            if len(l)>pos:
                if str(l[pos])==given:
                    del(l[pos])
                    for letter in letterscopy:
                        if letter in l:
                            matches += 1
                            letterscopy = letterscopy[1:]
                            p = l.index(letter)
                            del(l[p])
            if (len(l)==0 and len(data)<=length):
                words.append(data)
        return words

def maxwordsS(words, x, y, dir):
    maxscore = 0
    maxwords = []
    for word in words:
        if scoreS(word, x, y, dir)>maxscore:
            maxscore = scoreS(word, x, y, dir)
    for word in words:
        if (scoreS(word, x, y, dir)==maxscore):
            maxwords.append(word)
    return (maxwords, maxscore)

def maxwords(words, pos, x, y, dir):
    maxscore = 0
    maxwords = []
    for word in words:
        if score(word, pos, x, y, dir)>maxscore:
            maxscore = score(word, pos, x, y, dir)
    for word in words:
        if (score(word, pos, x, y, dir)==maxscore):
            maxwords.append(word)
    return (maxwords, maxscore)

def firstmove(letters):
    words = posswords(letters, 6)
    if (len(words)>0):
        maxxes = maxwordsS(words, 5, 5, "right")
        for maxx in maxxes[0]:
            print (" Make word '" + str(maxx) + "' on the centre square. (Score: " + str(maxxes[1]) + ")")

def move(letters, given, x, y, dir):
    overallwords = []
    for i in range(0, 7):
        if (dir=="right"):
            maxlen = 11+i-x
        else:
            maxlen = 11+i-y
        words = posswordswpos(letters, given, i, maxlen)
        if (len(words)!=0):
            for word in words:
                if (dir=="right"):
                    sc = str(score(word, i, x-i, y, dir))
                else:
                    sc = str(score(word, i, x, y-i, dir))
                overallwords.append((word, sc))
    overallwords = sort(overallwords)
    for overallword in overallwords:
        print " " + str(overallword[0]) + "   (" + str(overallword[1]) + ")"

def onegiven(letters, given, givenpos, x, y, dir):
    overallwords = []
    if dir=="right":
        maxlen = 11-x
    else:
        maxlen = 11-y
    words = posswordswpos(letters, given, givenpos, maxlen)
    if (len(words)!=0):
        for word in words:
            sc = str(scoreone(word, givenpos, x, y, dir))
            overallwords.append((word, sc, x, y))
    return sort(overallwords)

def line(no, letters, dir):
    row = board[no]
    atleastone = False
    for x in range(0, 11):
        if row[x] not in empty:
            atleastone = True
    if atleastone:
        words = []
        for x in range(0, 11):
            available = []
            valid = False
            given = -1
            for x1 in range(x, 11):
                if row[x1] not in empty:
                    valid = True
                    given = row[x1][1]
                    givenpos = x1-x
                available.append((x1, row[x1] not in empty))
            if valid:
                words = words + onegiven(letters, given, givenpos, available[0][0], no, dir)
        words = sort(words)
        for word in words:
            spaces = ""
            for i in range(0, 10-len(word[0])):
                spaces = spaces + " "
            space = " "
            if int(word[1])>9:
                space = ""
            print " " + str(word[0]) + spaces + "(" + str(word[1]) + " points)" + space + "     x=" + str(word[2]+1) + ", y=" + str(word[3]+1)
