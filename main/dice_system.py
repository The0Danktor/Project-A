import random
import nameinput_system as n_sys
pressed = True
amountD4 = 0
amountD6 = 0
amountD10 = 0
cijfers = []
cijferD10 = 0
cijferD6 = 0
cijferD4 = 0
totaal = 0
totaal1 = 0
totaal2 = 0
getelt = False
state = -1
loaded = False


def dice_systeem(mousePressed,players,turn):
    player(players,turn)
    # if state == -1:
    #     select_target()
    if state < 2:
        stroke(0)
        strokeWeight(5)
        knop(mousePressed,CORNERS,'#EA9C88',width/2.68,width/1.6,height/1.27,height/1.14,2,height/1.17)
        adddiceD6(mousePressed)
        adddiceD4(mousePressed)
        adddiceD10(mousePressed)
        totalCounter(CENTER,'#EA9C88',width/1.4, height/1.2,1.395,height/1.18)
        player_display(players)
        next(mousePressed)
    elif state == 2 and not loaded:
        dual(players)
        
def loadScreen():
    background('#5493BF')
    global state
    state = -1
def player(players,turn):
    player = players['player'+str(turn)]

# def select_target():
#     n_sys.
def mouseReleased_():
    global pressed
    pressed = True    

def old_numbers(textbreedte1,texthoogte1,textbreedte2,texthoogte2,textbreedte3,texthoogte3):
    global cijferD4
    global cijferD10
    global cijferD6
    oldD4 = cijferD4
    oldD6 = cijferD6
    oldD10 = cijferD10
    rectMode(CENTER)
    textSize(40)
    w1 = textWidth(str(cijferD4))
    w1 = (width - w1)//textbreedte1
    if oldD4 != 0:
        fill(255)
        rect(width/textbreedte1,texthoogte1,100,70)
        fill(0)
        text(str(cijferD4), w1 , texthoogte1)
    w2 = textWidth(str(cijferD6))
    w2 = (width - w2)//textbreedte2
    if oldD6 != 0:
        fill(255)
        rect(width/textbreedte2,texthoogte2,100,70)
        fill(0)
        text(str(cijferD6), w2 , texthoogte2)
    w3 = textWidth(str(cijferD10))
    w3 = (width - w3)//textbreedte3
    if oldD10 != 0:
        fill(255)
        rect(width/textbreedte3,texthoogte3,100,70)
        fill(0)
        text(str(cijferD10), w3 , texthoogte3)
    
def player_display(players):
    global totaal
    global totaal1
    global totaal2
    if state == 0:
        totaal1 = totaal
    elif state == 1:
        totaal2 = totaal
    rectMode(CORNERS)
    if state == 0:
        fill(100)
    else :
        fill(150)
    rect(0,0, width/4.8,height/5,5)
    fill(0)
    text(players['player1'],width/48, height/20)
    text('totaal :'+ str(totaal1),width/48, height/8)
    if state == 1:
        fill(100)
    else :
        fill(150)
    rect(width/1.263, 0,width,height/5,5)
    fill(0)
    text(players['player2'],width/1.23, height/20)
    text('totaal :'+ str(totaal2),width/1.23, height/8)


def dual(players):
    global loaded
    global totaal1
    global totaal2
    loaded = True
    fill (0,100)
    rect(0,0,width,height)
    if totaal1 > totaal2:
        fill(255)
        W = textWidth(players['player1'])
        W = (width - W) //2
        text(players['player1']+' wins',W,height/2)
    elif totaal2 > totaal1:
        fill(255)
        W = textWidth(players['player2'])
        W = (width - W) //2
        text(players['player2'] +' wins',W,height/2)
    elif totaal2 == totaal1:
        fill(255)
        W = textWidth('draw')
        W = (width - W) //2
        text('draw',W,height/2)
    

def next(mousePressed):
    global pressed
    global totaal
    global getelt
    global state
    global cijfers
    rectX1 = width/1.3
    rectX2 = width
    rectY1 = height/1.14
    rectY2 = height
    rectMode(CORNERS)
    fill('#EA9C88')
    rect(rectX1,rectY1,rectX2,rectY2)
    if mousePressed and (rectX1 < mouseX < rectX2)and(rectY1 < mouseY < rectY2 ) and pressed:
        cijfers = []
        totaal = 0
        getelt = False
        state += 1
        pressed = False
        if state == 1:
            noStroke()
            rectMode(CENTER)
            fill('#5493BF')
            rect(width/2,height/2,1000,400)
        
        
    
    
    
    
def totalCounter(mode,kleur,breedte,hoogte,textbreedte,texthoogte):
    global pressed
    global amountD4
    global amountD6
    global amountD10
    global cijfers
    global cijferD4
    global cijferD10
    global cijferD6
    global totaal
    global getelt
    if amountD4 == 0 and amountD6 == 0 and amountD10 == 0 and not getelt and pressed:
        for i in cijfers:
            totaal += i
        if totaal > 0:
            getelt = True
    
        
    
    
def diceD6(amount):
    global cijferD6
    if  amount > 0:
        cijferD6 = random.randint(1,6)
        strokeWeight(5)
        fill(255)
        rectMode(CENTER)
        rect(width/2, height/2, 100, 100 , 20)
        textSize(60)
        fill(0)
        text(str(cijferD6) ,width/2.04, height/1.93)

def diceD4(amount):
    global cijferD4
    if amount > 0:
        cijferD4 = random.randint(1,4)
        strokeWeight(5)
        fill(255)
        rectMode(CENTER)
        rect(width/2.5, height/2, 100, 100 , 20)
        textSize(60)
        fill(0)
        text(str(cijferD4) ,width/2.56, height/1.93)

    
def diceD10(amount):
    global cijferD10
    if amount > 0 :
        cijferD10 = random.randint(1,10)
        strokeWeight(5)
        fill(255)
        rectMode(CENTER)
        rect(width/1.67, height/2, 100, 100 , 20)
        textSize(60)
        fill(0)
        W = textWidth(str(cijferD10))
        W = (width - W) //1.66
        text(str(cijferD10) ,W, height/1.93)
 

       
def adddiceD6(mousePressed):
    global pressed
    global amountD6
    textSize(60)
    fill('#EA9C88')
    rectMode(CORNERS)
    rectX1 = width/2.11 
    rectX2 = width/1.90
    rectX3 = width/2
    rectY1 = height/1.41
    rectY2 = height/1.29
    rect(rectX1, rectY1, rectX2, rectY2)
    rect(rectX1, rectY1, rectX3, rectY2)
    fill(0)
    w = textWidth('+')
    w = (width - w) //2.05
    text('+', w , height/ 1.32)
    w = textWidth('-')
    w = (width - w) //1.945
    text('-', w , height/ 1.32)
    rectMode(CENTER)
    fill('#EA9C88')
    rect(rectX3, height/1.5, 100, 60)
    fill(0)
    textSize(40)
    w = textWidth(str(amountD6))
    w = (width - w)//2
    text(str(amountD6), w , height/1.465)
    if mousePressed and (rectX1 < mouseX < rectX3) and (rectY1 < mouseY < rectY2) and pressed:
        amountD6 += 1
        pressed = False
    if mousePressed and (rectX3 < mouseX < rectX2) and (rectY1 < mouseY < rectY2) and pressed:
        if amountD6 > 0:
            amountD6 -= 1
        pressed = False

def adddiceD10(mousePressed):
    global pressed
    global amountD10
    textSize(60)
    fill('#EA9C88')
    rectMode(CORNERS)
    rectX1 = width/1.748 
    rectX2 = width/1.6
    rectX3 = width/1.667
    rectY1 = height/1.41
    rectY2 = height/1.29
    rect(rectX1, rectY1, rectX2, rectY2)
    rect(rectX1, rectY1, rectX3, rectY2)
    fill(0)
    w = textWidth('+')
    w = (width - w) //1.7
    text('+', w , height/ 1.32)
    w = textWidth('-')
    w = (width - w) //1.624
    text('-', w , height/ 1.32)
    rectMode(CENTER)
    fill('#EA9C88')
    rect(rectX3, height/1.5, 100, 60)
    fill(0)
    textSize(40)
    w = textWidth(str(amountD10))
    w = (width - w)//1.664
    text(str(amountD10), w , height/1.465)
    if mousePressed and (rectX1 < mouseX < rectX3) and (rectY1 < mouseY < rectY2)and pressed:
        amountD10 += 1
        pressed = False
    if mousePressed and (rectX3 < mouseX < rectX2) and (rectY1 < mouseY < rectY2)and pressed:
        if amountD10 > 0:
            amountD10 -= 1
        pressed = False

def adddiceD4(mousePressed):
    global pressed
    global amountD4
    textSize(60)
    fill('#EA9C88')
    rectMode(CORNERS)
    rectX1 = width/2.68
    rectX2 = width/2.345
    rectX3 = width/2.498
    rectY1 = height/1.41
    rectY2 = height/1.29
    rect(rectX1, rectY1, rectX2, rectY2)
    rect(rectX1, rectY1, rectX3, rectY2)
    fill(0)
    w = textWidth('+')
    w = (width - w) //2.6
    text('+', w , height/ 1.32)
    w = textWidth('-')
    w = (width - w) //2.43
    text('-', w , height/ 1.32)
    rectMode(CENTER)
    fill('#EA9C88')
    rect(rectX3, height/1.5, 100, 60)
    fill(0)
    textSize(40)
    w = textWidth(str(amountD4))
    w = (width - w)//2.507
    text(str(amountD4), w , height/1.465)
    if mousePressed and (rectX1 < mouseX < rectX3) and (rectY1 < mouseY < rectY2) and pressed:
        amountD4 += 1
        pressed = False
    if mousePressed and (rectX3 < mouseX < rectX2) and (rectY1 < mouseY < rectY2) and pressed :
        if amountD4 > 0:
            amountD4 -= 1
        pressed = False
        
    
def knop(mousePressed,mode,kleur,rectX1,rectX2,rectY1,rectY2,textbreedte,texthoogte):
    global pressed
    global amountD4
    global amountD6
    global amountD10
    global cijfers
    global cijferD4
    global cijferD10
    global cijferD6
    fill(kleur)
    rectMode(mode)
    rectX1 = width/2.68
    rectX2 = width/1.6
    rectY1 = height/1.27
    rectY2 = height/1.14
    rect(rectX1, rectY1, rectX2, rectY2)
    textSize(60)
    fill(0)
    w = textWidth('dobbelen')
    w = (width - w) //textbreedte
    text('dobbelen', w , texthoogte)
    if mousePressed and (rectX1 < mouseX < rectX2)and(rectY1 < mouseY < rectY2 ) and pressed :
        old_numbers(2.56, height/2.6 ,2.04,height/2.6 ,1.66,height/2.6)
        diceD4(amountD4)
        diceD6(amountD6)
        diceD10(amountD10)
        if amountD4 > 0 and  pressed:
            amountD4 -= 1
            cijfers.append(cijferD4)
        if amountD6 > 0 and  pressed:
            amountD6 -= 1
            cijfers.append(cijferD6)
        if amountD10 > 0 and  pressed:
            amountD10 -= 1
            cijfers.append(cijferD10)
        if pressed: 
            pressed = False
            
def mousePressed_():
    global state
    if state == 2:
        rectMode(CORNER)
        state = -1
        return 8
    return 6
