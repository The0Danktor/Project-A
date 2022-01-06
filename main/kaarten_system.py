import functions as f
import random as r
import nameinput_system as n_sys
cardsNeg = {"Trench Feet": "Je pelotons bewegen de volgende ronde 1 stap minder",
"Hongersnood": "Pelotons op het slagveld kunnen 1 ronde niet bewegen en aanvallen",
"Rat Attack": "Eerstvolgende gevecht doe je 1 schade minder",
"Freeze": "Alle auto's en tanks kunnen 1 ronde niet bewegen",
"Verloren Haversack": "De laatst gebruikte troep moet 2 stappen terug zetten",
"Shellshock": "Je peloton kan 2 ronden niet bewegen, aanvallen of verdedigen"}
cardsNegPulled = []
cardsListNeg = ["Trench Feet", "Hongersnood", "Rat Attack", "Freeze", "Verloren Haversack", "Shellshock"]
cardsPos = {"Keep Digging": "Je volgende aanval doet 1 extra schade",
"Kabiem!!!": "Je kan 1 keer aanvallen op een afstand van 2 vakken",
"Body Armor": "Eerstvolgende gevecht nemen je troepen 50% schade",
"Spotted": "Je kunt 1 aanval ontwijken door 2 stappen opzij te gaan",
"Op Volle Toeren": "Komende 3 rondes heb je dubbel inkomen",
"Gasmasker": "Je bent voor 1 ronde beschermd tegen een gasaanval"}
cardsPosPulled = []
cardsListPos = ["Keep Digging", "Kabiem!!!", "Body Armor", "Spotted", "Op Volle Toeren", "Gasmasker"]
inv1 = ["Trench Feet", "Hongersnood", "Rat Attack", "Freeze", "Trench Feet", "Hongersnood", "Rat Attack", "Freeze", "Rat Attack"]
inv2 = ["Trench Feet", "Hongersnood", "Rat Attack", "Freeze", "Trench Feet", "Hongersnood", "Rat Attack", "Freeze", "Rat Attack"]
inv3 = []
inv4 = []
cardAmount1 = 0
cardAmount2 = 0
cardAmount3 = 0
cardAmount4 = 0
chosenPlayer = 1
chosenPlayerInv = 0
cardState = 0
selectedCardNum = -1
playerCount = n_sys.update_t_dis()['pCount']



def displayScreen(images, turn, players):
    global chosenPlayer

        
def loadScreen(images, turn, players):
    image(images['menu_img'], 0, 0, width, height)
    
    global chosenPlayer, playerCount
    
    f.textBox(width/2-width/8, height/3, width/8*2, height/14, 'Dobbelen')
    f.textBox(width/2-width/8, height/2, width/8*2, height/14, str(playerCount))    #==Alleen voor test==#
    
    if playerCount == 2:
        if chosenPlayer == 1:
            f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, players['player1'], 100)
            f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, players['player2'])               
        elif chosenPlayer == 2:
            f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, players['player1'])
            f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, players['player2'], 100)
        else:
            f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, players['player1'])
            f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, players['player2'])
            
    if playerCount == 4:
        if chosenPlayer == 1:
            f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, players['player1'], 100)
            f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, players['player2'])
            f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, players['player3'])
            f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, players['player4'])
        elif chosenPlayer == 2:
            f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, players['player1'])
            f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, players['player2'], 100)
            f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, players['player3'])
            f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, players['player4'])
        elif chosenPlayer == 3:
            f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, players['player1'])
            f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, players['player2'])
            f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, players['player3'], 100)
            f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, players['player4'])
        elif chosenPlayer == 4:
            f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, players['player1'])
            f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, players['player2'])
            f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, players['player3'])
            f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, players['player4'], 100)
        else:
            f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, players['player1'])
            f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, players['player2'])
            f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, players['player3'])
            f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, players['player4'])
   
    if playerCount == 2 and chosenPlayer == 3:
        f.textBox(width/2-width/5, height*6.5/8, width/5*2, height/10, "Terug naar menu")
        
    if playerCount == 4 and chosenPlayer == 5:
        f.textBox(width/2-width/5, height*6.5/8, width/5*2, height/10, "Terug naar menu")


def mousePressed_(images, turn, players):
    global cardsNeg, cardsListNeg, cardsPos, cardsListPos, inv1, inv2, inv3, inv4, cardAmount1, cardAmount2, cardAmount3, cardAmount4, chosenPlayer, cardsNegPulled, cardsPosPulled, chosenPlayerInv, selectedCard, cardState, selectedCardNum, playerCount
    import functions as f
    
    if playerCount == 4:
        if width/2-width/8 < mouseX < width/2+width/8 and height/3 < mouseY < height/3+height/14 and chosenPlayer < 5:     #Rollen voor alle spelers
            if chosenPlayer == 1:
                roll(inv1, cardAmount1, images, turn, players)

            elif chosenPlayer == 2:
                roll(inv2, cardAmount2, images, turn, players)

            elif chosenPlayer == 3:
                roll(inv3, cardAmount3, images, turn, players)
            
            elif chosenPlayer == 4:
                roll(inv4, cardAmount4, images, turn, players)
            
            elif chosenPlayer != 1 or 2 or 3 or 4 or 5:
                f.textBox(width/2-200, height*3.5/8, 400, 90, "Kies een speler")
                
    elif playerCount == 2:
        if width/2-width/8 < mouseX < width/2+width/8 and height/3 < mouseY < height/3+height/14 and chosenPlayer < 3:     #Rollen voor alle spelers
            if chosenPlayer == 1:
                roll(inv1, cardAmount1, images, turn, players)

            elif chosenPlayer == 2:
                roll(inv2, cardAmount2, images, turn, players)

            elif chosenPlayer != 1 or 2 or 3 or 4 or 5:
                f.textBox(width/2-200, height*3.5/8, 400, 90, "Kies een speler")
    
    if playerCount == 2:
        if width/2-width/5 < mouseX < width/2+width/5 and  height*6.5/8 < mouseY < height*6.5/8+height/10 and chosenPlayer == 3:     #Terug knop
            return 8
            chosenPlayer = 1
        else:
            return 9
    elif playerCount == 4:
        if width/2-width/5 < mouseX < width/2+width/5 and  height*6.5/8 < mouseY < height*6.5/8+height/10 and chosenPlayer == 5:     #Terug knop
            return 8
            chosenPlayer = 1
        else:
            return 9


def cardCheck():
    global cardsNeg, cardsListNeg, cardsPos, cardsListPos, inv1, inv2, inv3, inv4, cardAmount1, cardAmount2, cardAmount3, cardAmount4, chosenPlayer, cardsNegPulled, cardsPosPulled
    if len(cardsListNeg) == 0:
        cardsListNeg = cardsNegPulled
        cardsListNeg = list(set(cardsListNeg).intersection(inv1, inv2, inv3, inv4))
        cardsNegPulled = []
    if len(cardsListPos) == 0:
        cardsListPos = cardsPosPulled
        cardsListPos = list(set(cardsListPos).intersection(inv1, inv2, inv3, inv4))
        cardsPosPulled = []
    
    if len(list(set(cardsListNeg).intersection(inv1, inv2, inv3, inv4))) == 0:
        cardsListNeg.append("Rat Attack")
        cardsListNeg.append("Trench Feet")
        cardsListNeg.append("Hongersnood")
        cardsListNeg.append("Verloren Haversack")
    if len(list(set(cardsListPos).intersection(inv1, inv2, inv3, inv4))) == 0:
        cardsListPos.append("Kabiem!!!")
        cardsListPos.append("Op Volle Toeren")
        cardsListPos.append("Spotted")
        
def pulledCardCheck(images, turn, players):
    global cardsNeg, cardsListNeg, cardsPos, cardsListPos, inv1, inv2, inv3, inv4, cardAmount1, cardAmount2, cardAmount3, cardAmount4, chosenPlayer, cardsNegPulled, cardsPosPulled
    
    cardsNegPulled = list(dict.fromkeys(cardsNegPulled))
    cardsPosPulled = list(dict.fromkeys(cardsPosPulled))

def roll(inv, cardAmount, images, turn, players):
    global cardsNeg, cardsListNeg, cardsPos, cardsListPos, inv1, inv2, inv3, inv4, cardAmount1, cardAmount2, cardAmount3, cardAmount4, chosenPlayer, cardsNegPulled, cardsPosPulled, chosenPlayerInv
    
    green = color(77, 189, 51)
    red = color(255, 0, 0)
    
    dice = int(random(1,7))
    cardCheck()
    if dice == 1 or dice == 2:
        cardGen = int(random(0, len(cardsListNeg)))
        randomCard = cardsListNeg[cardGen]
        cardDesc = cardsNeg[randomCard]
        cardsListNeg.remove(randomCard)
        cardsNegPulled.append(randomCard)
        inv.append(randomCard)
        pulledCardCheck(images, turn, players)
        cardAmount += 1
        chosenPlayer += 1
        loadScreen(images, turn, players)
        f.textBox(width/2-20, height/4, 40, 40, str(dice), 255, 0)
        fill(255)
        f.textBox(width/2-width/6, height/6*2.6, width*2/6, height/10, randomCard, red, 0)
        f.textBox(width/2-width/5, height*4.3/8, width*2/5, height/10, cardDesc)
    elif dice == 5 or dice == 6:
        cardGen = int(random(0, len(cardsListPos)))
        randomCard = cardsListPos[cardGen]
        cardDesc = cardsPos[randomCard]
        cardsListPos.remove(randomCard)
        cardsPosPulled.append(randomCard)
        inv.append(randomCard)
        pulledCardCheck(images, turn, players)
        cardAmount += 1
        chosenPlayer += 1
        loadScreen(images, turn, players)
        f.textBox(width/2-20, height/4, 40, 40, str(dice), 255, 0)
        fill(255)
        f.textBox(width/2-width/6, height/6*2.6, width*2/6, height/10, randomCard, green, 0)
        f.textBox(width/2-width/5, height*4.3/8, width*2/5, height/10, cardDesc)
    else:
        chosenPlayer += 1
        loadScreen(images, turn, players)
        fill(0)
        f.textBox(width/2-width/5, height*3.5/8, width/5*2, height/10, "Je mag geen kaart pakken")
    f.textBox(width/2-20, height/4, 40, 40, str(dice), 255, 0)
