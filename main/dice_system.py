import random

pressed = True
amountD4 = 0
amountD6 = 0
amountD10 = 0
cijfers = []
cijferD10 = 0
cijferD6 = 0
cijferD4 = 0
totaal = 0

# def setup():
#     fullScreen()
#     background('#5493BF')
#     strokeWeight(5)

# def draw():
#     dice_systeem()

def dice_systeem(mousePressed):
    stroke(0)
    strokeWeight(5)
    knop(mousePressed)
    adddiceD6(mousePressed)
    adddiceD4(mousePressed)
    adddiceD10(mousePressed)
    totalCounter(CENTER,'#EA9C88',width/1.4, height/1.2,1.395,height/1.18)


def mouseReleased_():
    global pressed
    pressed = True    

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
    if amountD4 == 0 and amountD6 == 0 and amountD10 == 0 and pressed:
        for i in cijfers:
            totaal += i
        rectMode(mode)
        fill('#EA9C88')
        rect(breedte, hoogte, 100, 100)
        fill(0)
        textSize(40)
        w = textWidth(str(totaal))
        w = (width - w)//textbreedte
        text(str(totaal), w , texthoogte)
        totaal = 0
        
    
    
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
        
    
def knop(mousePressed):
    global pressed
    global amountD4
    global amountD6
    global amountD10
    global cijfers
    global cijferD4
    global cijferD10
    global cijferD6
    fill('#EA9C88')
    rectMode(CORNERS)
    rectX1 = width/2.68
    rectX2 = width/1.6
    rectY1 = height/1.27
    rectY2 = height/1.14
    rect(rectX1, rectY1, rectX2, rectY2)
    textSize(60)
    fill(0)
    w = textWidth('dobbelen')
    w = (width - w) //2
    text('dobbelen', w , height/1.17)
    if mousePressed and (rectX1 < mouseX < rectX2)and(rectY1 < mouseY < rectY2 ) and pressed :
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
        
        
