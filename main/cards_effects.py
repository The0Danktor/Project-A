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

def spotted(field):
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
        stepRange -= 1

def hongersnood(selectedTroop):
    a = 1
    #Zorgen dat peloton niet bewogen kan worden en niet kan aanvallen

def ratAttack(damageGiven):
    damageGiven -= 1

def freeze(selectedTroop):
    #zorgen dat auto en tank niet kan bewegen
    a = 1
    
def haversack(teams, turn, field):
    if player in team1:
        if a in field:
            field = field
        if b in field:
            field = "a" + field[1:]
        if c in field:
            field = "a" + field[1:]
        #etc en andersom

def shellshock(shellshockCounter):
    if selectedTroop == "peloton" and attacked == True and shellshockCounter > 0:
        damageTaken = 99
    #Zorgen dan peloton niet bewogen kan worden
    shellshockCounter -= 1
    
#Waarschijnlijk kloppen de variabelen niet, maar dat fix ik later. Dit is even een opzetje
