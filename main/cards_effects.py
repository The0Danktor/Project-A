#==============================================================#
# Functies voor alle kaarten om de effecten juist te verwerken #
# Elke kaart heeft zijn eigen functie                          #
#==============================================================#

######################
# Positieve kaarten: #
######################


import random as r
import kaarten_system as k_sys


def keepDigging(turn):
    inv = k_sys.update_k_dis()['inv' + str(turn)]
    if inv['KeepDigging'] == 1:
        return True
    else:
        return False

def kabiem(attackRange):
    attackRange += 1

def bodyArmor(victim):
    if victim == 'red':
        turn = 1
    elif victim == 'green':
        turn = 2
    elif victim == 'blue':
        turn = 3
    elif victim == 'yellow':
        turn = 4
    
    inv = k_sys.update_k_dis()['inv' + str(turn)]
    if inv['BodyArmor'] == 1:
        return True
    else:
        return False

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

def opVolleToeren(inv_dict, income):
    if inv_dict["VolleToeren"] > 0:
        income = income * 2
        inv_dict["VolleToeren"] -= 1

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

def ratAttack(turn):
    inv = k_sys.update_k_dis()['inv' + str(turn)]
    if inv['RatAttack'] == 1:
        return True
    else:
        return False

def freeze(selectedTroop):
    if selectedTroop == "auto" or selectedTroop == "Tank":
        reach = 0
    
def haversack(teams, turn, field):
    if player in team1:
        if "a" in field:
            field = "a" + field[1:]
        if "b" in field:
            field = "a" + field[1:]
        if "c" in field:
            field = "a" + field[1:]
        if "d" in field:
            field = "b" + field[1:]
        if "e" in field:
            field = "c" + field[1:]
        if "f" in field:
            field = "d" + field[1:]
        if "g" in field:
            field = "e" + field[1:]
        if "h" in field:
            field = "f" + field[1:]
        if "i" in field:
            field = "g" + field[1:]
    elif player in team2:
        if "a" in field:
            field = "c" + field[1:]
        if "b" in field:
            field = "d" + field[1:]
        if "c" in field:
            field = "e" + field[1:]
        if "d" in field:
            field = "f" + field[1:]
        if "e" in field:
            field = "g" + field[1:]
        if "f" in field:
            field = "h" + field[1:]
        if "g" in field:
            field = "i" + field[1:]
        if "h" in field:
            field = "i" + field[1:]
        if "i" in field:
            field = "i" + field[1:]

def shellshock(shellshockCounter):
    if selectedTroop == "peloton":
        reach = 0
        if attacked == True:
            damageTaken = 99

    
    ############
    # Na Beurt #
    ############

inv1_dict = k_sys.update_k_dis()['inv1_dict']       #Ook allemaal nodg voor het uitvoeren van beide functies
inv2_dict = k_sys.update_k_dis()['inv2_dict']
inv3_dict = k_sys.update_k_dis()['inv3_dict']
inv4_dict = k_sys.update_k_dis()['inv4_dict']

cardsNegPulled = k_sys.update_k_dis()['cardsNegPulled']
cardsPosPulled = k_sys.update_k_dis()['cardsNegPulled']

inv1 = k_sys.update_k_dis()['inv1']
inv2 = k_sys.update_k_dis()['inv2']
inv3 = k_sys.update_k_dis()['inv3']
inv4 = k_sys.update_k_dis()['inv4']

def naBeurtKaart(inv_dict, inv):            #Moet 4x bij het switchen van ronde, 1x voor elke inv_dict       gebruikte inv_dict moet zelfde zijn als gebruikte inv       naBeurtKaart(inv1_dict, inv1)
    global cardsPosPulled, cardsNegPulled
    
    if inv_dict["TrenchFeet"] == 1:
        inv_dict["TrenchFeet"] = 0
        inv.remove("Trench Feet")
        
    if inv_dict["Hongersnood"] == 1:
        inv_dict["Hongersnood"] = 0
        inv.remove("Hongersnood")
        cardsNegPulled.append("Hongersnood")
    if inv_dict["RatAttack"] == 1:
        inv_dict["RatAttack"] = 0
        inv.remove("Rat Attack")
        cardsNegPulled.append("Rat Attack")
    if inv_dict["Freeze"] == 1:
        inv_dict["Freeze"] = 0
        inv.remove("Freeze")
        cardsNegPulled.append("Freeze")
    if inv_dict["Shellshock"] > 0:
        inv_dict["Shellshock"] -= 1
        if inv_dict["Shellshock"] == 0:
            inv.remove("Shellshock")
            cardsNegPulled.append("Shellshock")
    if inv_dict["VolleToeren"] > 0:
        inv_dict["VolleToeren"] -= 1
        if inv_dict["VolleToeren"] == 0:
            inv.remove("Op Volle Toeren")
            cardsPosPulled.append("Op Volle Toeren")
            
    ##############
    # Na Gevecht #
    ##############

def naVechtKaart(inv_dict, inv):          #4x na gevecht
    if inv_dict["KeepDigging"] == 1:
        inv_dict["KeepDigging"] = 0
        inv.remove("Keep Digging")
        cardsPosPulled.append("Keep Digging")
    if inv_dict["BodyArmor"] == 1:
        inv_dict["BodyArmor"] = 0
        inv.remove("Body Armor")
        cardsPosPulled.append("Body Armor")
