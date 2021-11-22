import random

def setup():
    fullScreen()
    background('#5493BF')
    strokeWeight(5)

def draw():
    knop()
    adddiceD6()
    adddiceD4()
    adddiceD10()





def diceD6():
    cijferD6 = random.randint(1,6)
    strokeWeight(5)
    fill(255)
    rectMode(CENTER)
    rect(width/2, height/2, 100, 100 , 20)
    textSize(60)
    fill(0)
    text(str(cijferD6) ,width/2.04, height/1.93)

def diceD4():
    cijferD4 = random.randint(1,4)
    strokeWeight(5)
    fill(255)
    rectMode(CENTER)
    rect(width/2.5, height/2, 100, 100 , 20)
    textSize(60)
    fill(0)
    text(str(cijferD4) ,width/2.56, height/1.93)
    
def diceD10():
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
 
def mousePressed():
    print(mouseX, mouseY)
       
def adddiceD6():
    fill('#EA9C88')
    rectMode(CORNERS)
    rectX1 = width/2.11 
    rectX2 = width/1.90
    rectX3 = width/2
    rectY1 = height/1.41
    rectY2 = height/1.29
    rect(rectX1, rectY1, rectX2, rectY2)
    rect(rectX1, rectY1, rectX3, rectY2)
    if mousePressed and (rectX1 < mouseX < rectX3) and (rectY1 < mouseY < rectY2):
        diceD6()

def adddiceD10():
    fill('#EA9C88')
    rectMode(CORNERS)
    rectX1 = width/1.748 
    rectX2 = width/1.6
    rectX3 = width/1.667
    rectY1 = height/1.41
    rectY2 = height/1.29
    rect(rectX1, rectY1, rectX2, rectY2)
    rect(rectX1, rectY1, rectX3, rectY2)
    if mousePressed and (rectX1 < mouseX < rectX3) and (rectY1 < mouseY < rectY2):
        diceD10()

def adddiceD4():
    fill('#EA9C88')
    rectMode(CORNERS)
    rectX1 = width/2.68
    rectX2 = width/2.345
    rectX3 = width/2.498
    rectY1 = height/1.41
    rectY2 = height/1.29
    rect(rectX1, rectY1, rectX2, rectY2)
    rect(rectX1, rectY1, rectX3, rectY2)
    if mousePressed and (rectX1 < mouseX < rectX3) and (rectY1 < mouseY < rectY2):
        diceD4()
        
    
def knop():
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
    if mousePressed and (rectX1 < mouseX < rectX2)and(rectY1 < mouseY < rectY2 ):
        diceD4()
        diceD6()
        diceD10()
    #if mouseReleased and (rectX1 < mouseX < rectX2)and(rectY1 < mouseY < rectY2 ):
