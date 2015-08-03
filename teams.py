from time import sleep
import random 

def restart():
    teams = 0
    teams = input('hoeveel teams? ')
    out = random.randrange(1, (teams+1))
    print(out)
    restart()

restart()
sleep(10)
