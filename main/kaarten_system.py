import functions as f
import random as r
add_library("minim")
global cardsNeg, cardsListNeg, cardsPos, cardsListPos, inv1, inv2, inv3, inv4, cardAmount1, cardAmount2, cardAmount3, cardAmount4, chosenPlayer, cardsNegPulled, cardsPosPulled, chosenPlayerInv
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



def displayScreen(images):
    global chosenPlayer

    f.textBox(width/2-width/8, height/3, width/8*2, height/14, 'Dobbelen')
    if chosenPlayer == 1:
        f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, 'Player 1', 100)
        f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, 'Player 2')
        f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, 'Player 3')
        f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, 'Player 4')
    elif chosenPlayer == 2:
        f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, 'Player 1')
        f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, 'Player 2', 100)
        f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, 'Player 3')
        f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, 'Player 4')
    elif chosenPlayer == 3:
        f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, 'Player 1')
        f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, 'Player 2')
        f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, 'Player 3', 100)
        f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, 'Player 4')
    elif chosenPlayer == 4:
        f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, 'Player 1')
        f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, 'Player 2')
        f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, 'Player 3')
        f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, 'Player 4', 100)
    else:
        f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, 'Player 1')
        f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, 'Player 2')
        f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, 'Player 3')
        f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, 'Player 4')
        
def loadScreen(images):
    image(images['menu_img'], 0, 0, width, height)
    
    global chosenPlayer

    f.textBox(width/2-width/8, height/3, width/8*2, height/14, 'Dobbelen')
    if chosenPlayer == 1:
        f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, 'Player 1', 100)
        f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, 'Player 2')
        f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, 'Player 3')
        f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, 'Player 4')
    elif chosenPlayer == 2:
        f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, 'Player 1')
        f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, 'Player 2', 100)
        f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, 'Player 3')
        f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, 'Player 4')
    elif chosenPlayer == 3:
        f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, 'Player 1')
        f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, 'Player 2')
        f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, 'Player 3', 100)
        f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, 'Player 4')
    elif chosenPlayer == 4:
        f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, 'Player 1')
        f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, 'Player 2')
        f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, 'Player 3')
        f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, 'Player 4', 100)
    else:
        f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, 'Player 1')
        f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, 'Player 2')
        f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, 'Player 3')
        f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, 'Player 4')



def mousePressed_():
    global cardsNeg, cardsListNeg, cardsPos, cardsListPos, inv1, inv2, inv3, inv4, cardAmount1, cardAmount2, cardAmount3, cardAmount4, chosenPlayer, cardsNegPulled, cardsPosPulled, chosenPlayerInv, selectedCard, cardState, selectedCardNum
    import functions as f
    
    if width*1/5-width/24 < mouseX < width*1/5+width/24.2 and height/10 < mouseY < height/10+height/9.8:    #Select P1
        reset()
        chosenPlayerInv = 1
        f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, 'Player 1', 150)
        f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, 'Player 2')
        f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, 'Player 3')
        f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, 'Player 4')

    if width*2/5-width/24 < mouseX < width*2/5+width/24.2 and height/10 < mouseY < height/10+height/9.8:     #Select P2
        reset()
        chosenPlayerInv = 2
        f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, 'Player 1')
        f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, 'Player 2', 150)
        f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, 'Player 3')
        f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, 'Player 4')
    
    if width*3/5-width/24 < mouseX < width*3/5+width/24.2 and height/10 < mouseY < height/10+height/9.8:       #Select P3
        reset()
        chosenPlayerInv = 3
        f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, 'Player 1')
        f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, 'Player 2')
        f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, 'Player 3', 150)
        f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, 'Player 4')
    
    if width*4/5-width/24 < mouseX < width*4/5+width/24.2 and height/10 < mouseY < height/10+height/9.8:         #Select P4
        reset()
        chosenPlayerInv = 4
        f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, 'Player 1')
        f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, 'Player 2')
        f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, 'Player 3')
        f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, 'Player 4', 150)

    if width/2-width/8 < mouseX < width/2+width/8 and height/3 < mouseY < height/3+height/14 and chosenPlayer < 5:     #Rollen voor alle spelers
        if chosenPlayer == 1:
            roll(inv1, cardAmount1)

        elif chosenPlayer == 2:
            roll(inv2, cardAmount2)

        elif chosenPlayer == 3:
            roll(inv3, cardAmount3)
            
        elif chosenPlayer == 4:
            roll(inv4, cardAmount4)
            
        elif chosenPlayer != 1 or 2 or 3 or 4 or 5:
            f.textBox(width/2-200, height*3.5/8, 400, 90, "Kies een speler")
        
    if chosenPlayer == 5 and width*1/5-width/24 < mouseX < width*1/5+width/24.2 and height/10 < mouseY < height/10+height/9.8:    #Zorgen dat je de kaarten van gekozen speler kan displayen
        f.textBox(width/2-width/8, height*6/8, width/8*2, height/14, "Kaarten Laten Zien")
        cardState = 0
    elif chosenPlayer == 5 and width*2/5-width/24 < mouseX < width*2/5+width/24.2 and height/10 < mouseY < height/10+height/9.8:
        f.textBox(width/2-width/8, height*6/8, width/8*2, height/14, "Kaarten Laten Zien")
        cardState = 0
    elif chosenPlayer == 5 and width*3/5-width/24 < mouseX < width*3/5+width/24.2 and height/10 < mouseY < height/10+height/9.8:
        f.textBox(width/2-width/8, height*6/8, width/8*2, height/14, "Kaarten Laten Zien")
        cardState = 0
    elif chosenPlayer == 5 and width*4/5-width/24 < mouseX < width*4/5+width/24.2 and height/10 < mouseY < height/10+height/9.8:
        f.textBox(width/2-width/8, height*6/8, width/8*2, height/14, "Kaarten Laten Zien")
        cardState = 0

    if width/2-width/8 < mouseX < width/2+width/8 and height*6/8 < mouseY < height*6/8+height/14 and chosenPlayer == 5 and cardState == 0:
        reset()
        displayCards()
        cardState = 1
        
        #================#
         #Later Nodig!!!
        #================#

    if width/2-width/8 < mouseX < width/2+width/8 and height*6/8 < mouseY < height*6/8+height/12 and cardState == 1:          #Kaarten gebruiken (Later nodig om effecten toe te passen)
        #Gekozen kaart verwijderen uit inventory van gekozen speler
        if chosenPlayerInv == 1 and selectedCardNum > -1:
            useCard(inv1)
        elif chosenPlayerInv == 2 and selectedCardNum > -1:
            useCard(inv2)
        elif chosenPlayerInv == 3 and selectedCardNum > -1:
            useCard(inv3)
        elif chosenPlayerInv == 4 and selectedCardNum > -1:
            useCard(inv4)

    if chosenPlayerInv == 1:       #Display en knoppen door middel van loop (Maximum display aan te passen door "i < 11" aan te passen)
        i = 1
        while len(inv1) >= i and i < 11:
            cardDisplay1(i, inv1)
            i += 1

    if chosenPlayerInv == 2:
        i = 1
        while len(inv2) >= i and i < 11:
            cardDisplay1(i, inv2)
            i += 1

    if chosenPlayerInv == 3:
        i = 1
        while len(inv3) >= i and i < 11:
            cardDisplay1(i, inv3)
            i += 1
        
    if chosenPlayerInv == 4:
        i = 1
        while len(inv4) >= i and i < 11:
            cardDisplay1(i, inv4)
            i += 1

def useCard(inv):
    global cardsNeg, cardsListNeg, cardsPos, cardsListPos, inv1, inv2, inv3, inv4, cardAmount1, cardAmount2, cardAmount3, cardAmount4, chosenPlayer, cardsNegPulled, cardsPosPulled, chosenPlayerInv, selectedCard, selectedCardNum, cardState
    f.textBox(width/2-width/8, height*3/8, width/8*2, height/14, inv[selectedCardNum] + " is gebruikt")
    del inv[selectedCardNum]
    selectedCardNum = -1

def cardDisplay1(num, inv):
    global cardsNeg, cardsListNeg, cardsPos, cardsListPos, inv1, inv2, inv3, inv4, cardAmount1, cardAmount2, cardAmount3, cardAmount4, chosenPlayer, cardsNegPulled, cardsPosPulled, chosenPlayerInv, selectedCard, selectedCardNum, cardState
    num -= 1
    x1 = width/12 + width/12 * num
    x2 = x1+width/14
    if x1 < mouseX < x2 and height-height/8 < mouseY < height:
        pos = width/12
        card = 0
        for cards in inv:
            f.textBox(pos, height-height/8, width/14, height/8, inv[card])
            pos += width/12
            card += 1
        f.textBox(x1, height-height/8, width/14, height/8, inv[num], 100)
        selectedCard = inv[num]
        selectedCardNum = num
        f.textBox(width/2-width/8, height*6/8, width/8*2, height/12, "Kaart Gebruiken")
        cardState = 1
        if selectedCard in cardsListNeg:
            f.textBox(width/8, height*5/8, width/8*6, 70, cardsNeg[selectedCard])
        else:
            f.textBox(width/8, height*5/8, width/8*6, 70, cardsPos[selectedCard])    
        
def cardInv():
    i = 1
            
def reset():
    #fullScreen()
    bg = loadImage("camo.png")
    image(bg,0,0,width,height)
    
    if chosenPlayer < 5:
        f.textBox(width/2-width/8, height/3, width/8*2, height/14, 'Dobbelen')
    
    if chosenPlayer == 1:
        f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, 'Player 1', 100)
        f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, 'Player 2')
        f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, 'Player 3')
        f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, 'Player 4')
    elif chosenPlayer == 2:
        f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, 'Player 1')
        f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, 'Player 2', 100)
        f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, 'Player 3')
        f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, 'Player 4')
    elif chosenPlayer == 3:
        f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, 'Player 1')
        f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, 'Player 2')
        f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, 'Player 3', 100)
        f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, 'Player 4')
    elif chosenPlayer == 4:
        f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, 'Player 1')
        f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, 'Player 2')
        f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, 'Player 3')
        f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, 'Player 4', 100)
    else:
        f.textBox(width*1/5-width/24, height/10, width/12.1, height/9.8, 'Player 1')
        f.textBox(width*2/5-width/24, height/10, width/12.1, height/9.8, 'Player 2')
        f.textBox(width*3/5-width/24, height/10, width/12.1, height/9.8, 'Player 3')
        f.textBox(width*4/5-width/24, height/10, width/12.1, height/9.8, 'Player 4')

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
        
def pulledCardCheck():
    global cardsNeg, cardsListNeg, cardsPos, cardsListPos, inv1, inv2, inv3, inv4, cardAmount1, cardAmount2, cardAmount3, cardAmount4, chosenPlayer, cardsNegPulled, cardsPosPulled
    
    cardsNegPulled = list(dict.fromkeys(cardsNegPulled))
    cardsPosPulled = list(dict.fromkeys(cardsPosPulled))

def displayCards():
    global cardsNeg, cardsListNeg, cardsPos, cardsListPos, inv1, inv2, inv3, inv4, cardAmount1, cardAmount2, cardAmount3, cardAmount4, chosenPlayer, cardsNegPulled, cardsPosPulled, chosenPlayerInv
    if chosenPlayerInv == 1:
        pos = width/12
        card = 0
        for cards in inv1:
            f.textBox(pos, height-height/8, width/14, height/8, inv1[card])
            pos += width/12
            card += 1

    elif chosenPlayerInv == 2:
        pos = width/12
        card = 0
        for cards in inv2:
            f.textBox(pos, height-height/8, width/14, height/8, inv2[card])
            pos += width/12
            card += 1

    elif chosenPlayerInv == 3:
        pos = width/12
        card = 0
        for cards in inv3:
            f.textBox(pos, height-height/8, width/14, height/8, inv3[card])
            pos += width/12
            card += 1

    elif chosenPlayerInv == 4:
        pos = width/12
        card = 0
        for cards in inv4:
            f.textBox(pos, height-height/8, width/14, height/8, inv4[card])
            pos += width/12
            card += 1

def roll(inv, cardAmount):
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
        pulledCardCheck()
        cardAmount += 1
        chosenPlayer += 1
        cardInv()
        reset()
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
        pulledCardCheck()
        cardAmount += 1
        chosenPlayer += 1
        cardInv()
        reset()
        f.textBox(width/2-20, height/4, 40, 40, str(dice), 255, 0)
        fill(255)
        f.textBox(width/2-width/6, height/6*2.6, width*2/6, height/10, randomCard, green, 0)
        f.textBox(width/2-width/5, height*4.3/8, width*2/5, height/10, cardDesc)
    else:
        chosenPlayer += 1
        reset()
        fill(0)
        f.textBox(width/2-width/5, height*3.5/8, width/5*2, height/10, "Je mag geen kaart pakken")
    f.textBox(width/2-20, height/4, 40, 40, str(dice), 255, 0)
