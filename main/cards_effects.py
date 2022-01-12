#==============================================================#
# Functies voor alle kaarten om de effecten juist te verwerken #
# Elke kaart heeft zijn eigen functie                          #
#==============================================================#

######################
# Positieve kaarten: #
######################


import random as r


def keepDigging(damageGiven):
    damageGiven += 1

def kabiem(attackRange):
    attackRange += 1

def bodyArmor(damageTaken):
    damageTaken = damageTaken / 2

def spotted(field):         #Zorgen dat deze als optie komt zodra je aangevallen word
    letter = field[1:]

    pos = field[1:]
    if 2 < pos < 6:
        a = r.randint(1,2)    #randomises jump direction if possible 
        if a == 1:
            pos += 2
        else:
            pos -= 2
    elif pos >= 6:            #goes left if right is impossible
        pos -= 2
    elif pos <= 2:            #goes right if left is impossible
        pos += 2
    
    field = letter + str(pos)

def opVolleToeren(toerenCounter, income):
    if toerenTeller > 0:
        income = income * 2
        toerenCounter -= 1

def gasmasker(field, gasfield):
    if field in gasfield:
        gasDamageTaken = 0

######################
# Negatieve kaarten: #
######################

def trenchFeet(selectedTroop, stepRange):
    if selectedTroop == "peloton":
        reach -= 1

def hongersnood(selectedTroop):
    a = 1
    #Zorgen dat peloton niet bewogen kan worden en niet kan aanvallen

def ratAttack(damageGiven):
    damageGiven -= 1

def freeze(selectedTroop):
    if selectedTroop == "auto" or selectedTroop == "Tank":
        reach = 0
    
def haversack(teams, turn, field):
    if player in team1:
        if a in field:
            field = "a" + field[1:]
        if b in field:
            field = "a" + field[1:]
        if c in field:
            field = "a" + field[1:]
        if d in field:
            field = "b" + field[1:]
        if e in field:
            field = "c" + field[1:]
        if f in field:
            field = "d" + field[1:]
        if g in field:
            field = "e" + field[1:]
        if h in field:
            field = "f" + field[1:]
        if i in field:
            field = "g" + field[1:]
    elif player in team2:
        if a in field:
            field = "c" + field[1:]
        if b in field:
            field = "d" + field[1:]
        if c in field:
            field = "e" + field[1:]
        if d in field:
            field = "f" + field[1:]
        if e in field:
            field = "g" + field[1:]
        if f in field:
            field = "h" + field[1:]
        if g in field:
            field = "i" + field[1:]
        if h in field:
            field = "i" + field[1:]
        if i in field:
            field = "i" + field[1:]

def shellshock(shellshockCounter):
    if selectedTroop == "peloton" and attacked == True and shellshockCounter > 0:
        damageTaken = 99
        reach = 0
    shellshockCounter -= 1
