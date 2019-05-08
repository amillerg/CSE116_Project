import operator

def topPlayers(playerList):
    top = {}
    ratio = 0
    for i in playerList:
        ratio = (i.kills / i.deaths)
        top[i] = ratio
top = {"p1": 1.0, "p2": .66, "p3": 2.7, "p4": .3, "p5": 9.0}

sorted_top = sorted(top.items(), key=operator.itemgetter(1))