from time import sleep
import random 

def restart():
    stenen = input('hoeveel stenen? ')
    stenen2 = stenen
    out = 0
    while stenen2 > 0:
        out = (out+random.randrange(1, 7))
        stenen2 = (stenen2-1)
    print(out)
    restart()

restart()
sleep(10)
