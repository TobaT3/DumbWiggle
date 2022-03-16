#StupidWiggle by Toba

import time
import sys

indent = 0
increaseIndent = True

text = input("Wiggle what text? ")
maxindent = int(input("How big a wiggle (in max. spaces)? "))
iswall = input("Do you want your wiggle to bounce off a wall or not? (true/false) ")
sleeptime = float(input("finally, how fast should it wiggle? Enter time it takes to write next line (in seconds), 0.1 reccomended for small wiggles, 0.05 for big ones "))

while True:
    if iswall == 'false':
        print(' ' * indent, end='')
        print(text)
    elif iswall == 'true':
        print(' ' * indent, end='')
        print(text, end='')
        print(' ' * ((maxindent - indent)+1), end='')
        print('|')

    if increaseIndent:
        indent += 1
    else:
        indent -= 1

    if indent > maxindent:
        increaseIndent = False
    elif indent == 1:
        increaseIndent = True

    time.sleep(sleeptime)
