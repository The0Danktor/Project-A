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
inv1 = ["Trench Feet", "Hongersnood", "Rat Attack", "Freeze", "Hongersnood", "Rat Attack", "Freeze", "Rat Attack"]        #Temporary Fill#
inv2 = ["Trench Feet", "Hongersnood", "Rat Attack", "Freeze", "Trench Feet", "Hongersnood", "Rat Attack"]                 #Temporary Fill#
inv3 = []
inv4 = []
chosenPlayer = turn        #Speler die aan de beurt is + in setup en reset
cardState = 0
selectedCardNum = -1
name = player + str(turn)

def loadScreen(images):
    image(images['menu_img'], 0, 0, width, height)

def loadScreen(images):
    global chosenPlayer, chosenPlayerInv, cardState
    image(images['menu_img'], 0, 0, width, height)
    f.textBox(width/5, -5, width/5*3, height/10, name)
    f.textBox(width-75, 0, 75, 75, "Terug")
    
    if chosenPlayer == 1:
        displayCards(inv1)
    elif chosenPlayer == 2:
        displayCards(inv2)
    elif chosenPlayer == 3:
        displayCards(inv3)
    elif chosenPlayer == 4:
        displayCards(inv4)
    
    cardState = 0
    
def mousePressed_():
    global cardsNeg, cardsListNeg, cardsPos, cardsListPos, inv1, inv2, inv3, inv4, cardAmount1, cardAmount2, cardAmount3, cardAmount4, chosenPlayer, cardsNegPulled, cardsPosPulled, chosenPlayerInv, cardState
    if 0 < chosenPlayer < 5:       #Display en knoppen door middel van loop (Maximum display aan te passen door "i < 11" aan te passen)
        i = 1
        while len(inv1) >= i and i < 11:
            cardButton(i, inv1)
            i += 1
    
    if width/6*2 < mouseX < width/6*4 and height/10*6 < mouseY < height/10*6+height/6 and chosenPlayer == 1 and cardState == 1:
        useCard(inv1)
        reset()
    
    if width/6*2 < mouseX < width/6*4 and height/10*6 < mouseY < height/10*6+height/6 and chosenPlayer == 2 and cardState == 1:
        useCard(inv2)
        reset()

    if width/6*2 < mouseX < width/6*4 and height/10*6 < mouseY < height/10*6+height/6 and chosenPlayer == 3 and cardState == 1:
        useCard(inv3)
        reset()

    if width/6*2 < mouseX < width/6*4 and height/10*6 < mouseY < height/10*6+height/6 and chosenPlayer == 4 and cardState == 1:
        useCard(inv4)
        reset()
    
    if width-75 < mouseX < width and  0 < mouseY < 75:
        a = 1
        exit()
        #state = ???

def displayCards(inv):
    global cardsNeg, cardsListNeg, cardsPos, cardsListPos, inv1, inv2, inv3, inv4, cardAmount1, cardAmount2, cardAmount3, cardAmount4, chosenPlayer, cardsNegPulled, cardsPosPulled, chosenPlayerInv

    a = 11-len(inv)
    b = 1 + a * 0.8333
    pos = b*width/20
    card = 0
    for cards in inv:
        f.textBox(pos, height/2-height/8, width/14, height/8, inv[card])
        pos += width/12
        card += 1
    if len(inv) == 0:
        f.textBox(width/3, height/2-height/8, width/3, height/8, "Je Hebt Geen Kaarten")

def cardButton(num, inv):
    global selectedCardNum, cardState, selectedCard
    num -= 1
    a = 11-len(inv)
    b = 1 + a * 0.8333
    pos = b * width / 20
    x1 = pos + width/12 * num
    x2 = x1 + width/14
    
    if x1 < mouseX < x2 and height/2-height/8 < mouseY < height/2:
        card = 0
        for cards in inv:
            f.textBox(pos, height/2-height/8, width/14, height/8, inv[card])
            pos += width/12
            card += 1
        f.textBox(x1, height/2-height/8, width/14, height/8, inv[num], 30)
        selectedCard = inv[num]
        selectedCardNum = num
        f.textBox(width/6*2, height/10*6, width/3, height/6, "Kaart Gebruiken")
        if selectedCard in cardsListNeg:
            f.textBox(width/6, height/10*9, width/6*4, height/9, cardsNeg[selectedCard])
        else:
            f.textBox(width/6, height/10*9, width/6*4, height/9, cardsPos[selectedCard])
        cardState = 1

def useCard(inv):
    global cardsNeg, cardsListNeg, cardsPos, cardsListPos, inv1, inv2, inv3, inv4, cardAmount1, cardAmount2, cardAmount3, cardAmount4, chosenPlayer, cardsNegPulled, cardsPosPulled, chosenPlayerInv, selectedCard, selectedCardNum, cardState
    f.textBox(width/2-width/8, height*3/8, width/8*2, height/14, inv[selectedCardNum] + " is gebruikt")
    del inv[selectedCardNum]
    #Toevoegen aan gebruikte deck
    selectedCardNum = -1

def reset():
    image(images['menu_img'], 0, 0, width, height)
    
    if chosenPlayer == 1:
        displayCards(inv1)
    elif chosenPlayer == 2:
        displayCards(inv2)
    elif chosenPlayer == 3:
        displayCards(inv3)
    elif chosenPlayer == 4:
        displayCards(inv4)
    
    f.textBox(width/5, 0, width/5*3, height/10, name)
    f.textBox(width-75, 0, 75, 75, "Terug")
    cardState = 0
