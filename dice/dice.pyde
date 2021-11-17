import random
cijfer = random.randint(1,6)


def setup():
    fullScreen()
    background(0x984AE1)

def draw():
    global rectX1
    global rectX2
    global rectY1
    global rectY2
    knop()
    rectX1
    rectX2
    rectY1
    rectY2
    if mousePressed and (rectX1 < mouseX < rectX2)and(rectY1 < mouseY < rectY2 ):
        dice()
    



def dice():
    cijfer = random.randint(1,6)
    strokeWeight(5)
    frameRate(15)
    fill(255)
    rectMode(CENTER)
    rect(width/2, height/2, 100, 100 , 20)
    textSize(60)
    fill(0)
    text(str(cijfer) ,width/2.04, height/1.93)
    
def knop():
    global rectX1
    global rectX2
    global rectY1
    global rectY2
    fill('#82171B')
    rectMode(CORNERS)
    rectX1 = width/2.7
    rectX2 = width/1.6
    rectY1 = height/1.27
    rectY2 = height/1.14
    rect(rectX1, rectY1, rectX2, rectY2)
    textSize(60)
    fill(0)
    w = textWidth('dobbelen')
    w = (width - w) //2
    text('dobbelen', w , height/1.17)
