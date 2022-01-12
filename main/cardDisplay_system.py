import functions as f
import random as r
import kaarten_system as k_sys
import back_up as b
add_library("minim")
global cardsNeg, cardsListNeg, cardsPos, cardsListPos, inv1, inv2, inv3, inv4, cardAmount1, cardAmount2, cardAmount3, cardAmount4, chosenPlayer, cardsNegPulled, cardsPosPulled, chosenPlayerInv
cardsNeg = {"Trench Feet": "Je pelotons bewegen de volgende ronde 1 stap minder",
"Hongersnood": "Pelotons op het slagveld kunnen 1 ronde niet bewegen en aanvallen",
"Rat Attack": "Eerstvolgende gevecht doe je 1 schade minder",
"Freeze": "Alle auto's en tanks kunnen 1 ronde niet bewegen",
"Verloren Haversack": "De laatst gebruikte troep moet 2 stappen terug zetten",
"Shellshock": "Je peloton kan 2 ronden niet bewegen, aanvallen of verdedigen"}
cardsListNeg = ["Trench Feet", "Hongersnood", "Rat Attack", "Freeze", "Verloren Haversack", "Shellshock"]
posTestList = ["Trench Feet", "Hongersnood", "Rat Attack", "Freeze", "Verloren Haversack", "Shellshock"]
cardsPos = {"Keep Digging": "Je volgende aanval doet 1 extra schade",
"Kabiem!!!": "Je kan 1 keer aanvallen op een afstand van 2 vakken",
"Body Armor": "Eerstvolgende gevecht nemen je troepen 50% schade",
"Spotted": "Je kunt 1 aanval ontwijken door 2 stappen opzij te gaan",
"Op Volle Toeren": "Komende 3 rondes heb je dubbel inkomen",
"Gasmasker": "Je bent voor 1 ronde beschermd tegen een gasaanval"}
cardsListPos = ["Keep Digging", "Kabiem!!!", "Body Armor", "Spotted", "Op Volle Toeren", "Gasmasker"]
negTestList = ["Keep Digging", "Kabiem!!!", "Body Armor", "Spotted", "Op Volle Toeren", "Gasmasker"]
cardState = 0
selectedCardNum = -1
name = ''

def displayScreen(turn, players):
    global chosenPlayer, name
    
    chosenPlayer = turn

def loadScreen(images, turn, players):
    global chosenPlayer, chosenPlayerInv, cardState, name, im
    global inv1, inv2, inv3, inv4, cardsNegPulled, cardsPosPulled
    
    inv1 = k_sys.update_k_dis()['inv1']
    inv2 = k_sys.update_k_dis()['inv2']
    inv3 = k_sys.update_k_dis()['inv3']
    inv4 = k_sys.update_k_dis()['inv4']
    cardsNegPulled = k_sys.update_k_dis()['cardsNegPulled']
    cardsPosPulled = k_sys.update_k_dis()['cardsNegPulled']
    inv1_dict = k_sys.update_k_dis()['inv1_dict']
    inv2_dict = k_sys.update_k_dis()['inv2_dict']
    inv3_dict = k_sys.update_k_dis()['inv3_dict']
    inv4_dict = k_sys.update_k_dis()['inv4_dict']
    
    chosenPlayer = turn
    name = 'player' + str(turn)
    name = players[name]
    image(images['background_img'], 0, 0, width, height)
    im = images['menu_img']
    f.textBox(width/5, -5, width/5*3, height/10, name)
    f.textBox(width-height/10, 0, height/10, height/10, "Terug")
    
    if chosenPlayer == 1:
        displayCards(inv1)
    elif chosenPlayer == 2:
        displayCards(inv2)
    elif chosenPlayer == 3:
        displayCards(inv3)
    elif chosenPlayer == 4:
        displayCards(inv4)
    
    cardState = 0
    
def mousePressed_(images, turn, players):
    global cardsNeg, cardsListNeg, cardsPos, cardsListPos, inv1, inv2, inv3, inv4, cardAmount1, cardAmount2, cardAmount3, cardAmount4, chosenPlayer, cardsNegPulled, cardsPosPulled, chosenPlayerInv, cardState
    
    if chosenPlayer == 1:       #Display en knoppen door middel van loop (Maximum display aan te passen door "i < 11" aan te passen)
        i = 1
        while len(inv1) >= i and i < 11:
            cardButton(i, inv1)
            i += 1
    
    if chosenPlayer == 2:
        i = 1
        while len(inv2) >= i and i < 11:
            cardButton(i, inv2)
            i += 1
    
    if chosenPlayer == 3:
        i = 1
        while len(inv3) >= i and i < 11:
            cardButton(i, inv3)
            i += 1
    
    if chosenPlayer == 4:
        i = 1
        while len(inv4) >= i and i < 11:
            cardButton(i, inv4)
            i += 1
    
    if width/6*2 < mouseX < width/6*4 and height/10*6 < mouseY < height/10*6+height/6 and chosenPlayer == 1 and cardState == 1 and (selectedCard == "Spotted" or selectedCard == "Kabiem!!!"):
        useCard(inv1)
        loadScreen(images, turn, players)
    
    if width/6*2 < mouseX < width/6*4 and height/10*6 < mouseY < height/10*6+height/6 and chosenPlayer == 2 and cardState == 1 and (selectedCard == "Spotted" or selectedCard == "Kabiem!!!"):
        useCard(inv2)
        loadScreen(images, turn, players)

    if width/6*2 < mouseX < width/6*4 and height/10*6 < mouseY < height/10*6+height/6 and chosenPlayer == 3 and cardState == 1 and (selectedCard == "Spotted" or selectedCard == "Kabiem!!!"):
        useCard(inv3)
        loadScreen(images, turn, players)

    if width/6*2 < mouseX < width/6*4 and height/10*6 < mouseY < height/10*6+height/6 and chosenPlayer == 4 and cardState == 1 and (selectedCard == "Spotted" or selectedCard == "Kabiem!!!"):
        useCard(inv4)
        loadScreen(images, turn, players)
    
    if width-height/10 < mouseX < width and  0 < mouseY < height/10:     #Terug knop
        return 8
    else:
        return 10

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
        if selectedCard == "Spotted" or selectedCard == "Kabiem!!!":
            f.textBox(width/6*2, height/10*6, width/3, height/6, "Kaart Gebruiken")
        else:
            f.textBox(width/6*2, height/10*6, width/3, height/6, "Kaart is actief")
        if selectedCard in cardsListNeg:
            f.textBox(width/6, height/10*9, width/6*4, height/9, cardsNeg[selectedCard])
        else:
            f.textBox(width/6, height/10*9, width/6*4, height/9, cardsPos[selectedCard])
        cardState = 1

def useCard(inv):
    global cardsNeg, cardsListNeg, cardsPos, cardsListPos, inv1, inv2, inv3, inv4, cardAmount1, cardAmount2, cardAmount3, cardAmount4, chosenPlayer, cardsNegPulled, cardsPosPulled, chosenPlayerInv, selectedCard, selectedCardNum, cardState
    b.play_sfx("draw")
    if selectedCard in posTestList:
        cardsPosPulled.append(selectedCard)
    else:
        cardsNegPulled.append(selectedCard)
    del inv[selectedCardNum]
    selectedCardNum = -1
