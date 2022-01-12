import functions as f
import random
import nameinput_system as n_sys
import back_up as b_u
# ==================================================
# alle global variable
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
target = 1
# ==================================================
#de main die gecalled wordt door de draw
def dice_systeem(sfx_files,mousePressed,players,turn):
    if state == -1:
         select_target(mousePressed,players,turn)
    elif state < 2:
        stroke(0)
        strokeWeight(5)
        knop(sfx_files,mousePressed,CORNERS,'#EA9C88',width/2.68,width/1.6,height/1.27,height/1.14,2,height/1.17)
        adddiceD6(mousePressed)
        adddiceD4(mousePressed)
        adddiceD10(mousePressed)
        totalCounter(CENTER,'#EA9C88',width/1.4, height/1.2,1.395,height/1.18)
        player_display(players,turn)
        next(mousePressed)
    elif state == 2 and not loaded:
        dual(players,turn)
# ==================================================
# loadSceen fuction on de achtergrond 1 keer te laden    
        
def loadScreen(images):
    pCount = n_sys.update_t_dis()['pCount']
    if pCount == 4:
        if state == -1:
            background(100)
        
        else:
            image(images['background_img'], 0, 0, width, height)
    elif pCount  ==2:
        image(images['background_img'], 0, 0, width, height)
# ==================================================
# systeem on je tegenstander te kiezen

def select_target(mousePressed,players,turn):
    strokeWeight(5)
    global target
    global state
    global loaded
    loaded = False
    pCount = n_sys.update_t_dis()['pCount']
# als je met twee spelers speelt dan is je tegenstander automatish de andere speler 
    if pCount == 2:
        if turn == 1:
            target = 2
        elif turn == 2:
            target == 1
        state = 0
# als je met vier spelers speelt dan kan je zelf een tegenstander kiezen 
    if pCount == 4:
        background(100)

# als het speler 1 zijn beurt is        
        if turn == 1:
            
            # kies speler 3 als tegenstander
            if (( width/2.45 > mouseX > width/3.265) and ( height/1.812 > mouseY > height/2.227)):
                stroke(255)
            else:
                stroke(0)
            fill(150)
            rectMode(CENTER)
            rect(width/2.8, height/2, width*0.1, height*0.1 , 20)
            fill(0)
            textSize(26)
            W = textWidth(players['player3'])
            W = (width - W) //2.9
            text(players['player3'],W, height/1.965)
            
            # kies speler 2 als tegenstander
            # if (( width/1.811 > mouseX > width/2.217) and ( height/1.812 > mouseY > height/2.227)):
            #     stroke(255)
            # else:
            #     stroke(0)
            # fill(150)
            # rect(width/2, height/2, width*0.1, height*0.1 , 20)
            # fill(0)
            # textSize(26)
            # W = textWidth(players['player2'])
            # W = (width - W) //2
            # text(players['player2'],W, height/1.965)
            
            # kies speler 4 als tegenstander
            if (( width/1.435 > mouseX > width/1.681) and (height/1.812 > mouseY > height/2.227)):
                stroke(255)
            else:
                stroke(0)
            fill(150)
            rect(width/1.55, height/2, width*0.1, height*0.1 , 20)
            fill(0)
            textSize(26)
            W = textWidth(players['player4'])
            W = (width - W) //1.525
            text(players['player4'],W, height/1.965)
            
            # speler 3
            if (( width/2.45 > mouseX > width/3.265) and ( height/1.812 > mouseY > height/2.227) and mousePressed):
                target = 3
                state += 1
                background('#5493BF')
            
            # speler 2
            # if (( width/1.811 > mouseX > width/2.217) and ( height/1.812 > mouseY > height/2.227)and mousePressed):
            #     target = 2
            #     state += 1
            #     background('#5493BF')
            
            # speler 4
            if (( width/1.435 > mouseX > width/1.681) and (height/1.812 > mouseY > height/2.227)and mousePressed):
                target = 4
                state += 1
                background('#5493BF')
            stroke(0)
 
# als het speler 2 zijn beurt is               
        if turn == 2:
            
            # kies speler 3 als tegenstander
            if (( width/2.45 > mouseX > width/3.265) and ( height/1.812 > mouseY > height/2.227)):
                stroke(255)
            else:
                stroke(0)
            fill(150)
            rectMode(CENTER)
            rect(width/2.8, height/2, width*0.1, height*0.1 , 20)
            fill(0)
            textSize(26)
            W = textWidth(players['player3'])
            W = (width - W) //2.9
            text(players['player3'],W, height/1.965)
            
            # # kies speler 1 als tegenstander
            # if (( width/1.811 > mouseX > width/2.217) and ( height/1.812 > mouseY > height/2.227)):
            #     stroke(255)
            # else:
            #     stroke(0)
            # fill(150)
            # rect(width/2, height/2, width*0.1, height*0.1 , 20)
            # fill(0)
            # textSize(26)
            # W = textWidth(players['player1'])
            # W = (width - W) //2
            # text(players['player1'],W, height/1.965)
            
            # kies speler 4 als tegenstander
            if (( width/1.435 > mouseX > width/1.681) and (height/1.812 > mouseY > height/2.227)):
                stroke(255)
            else:
                stroke(0)
            fill(150)
            rect(width/1.55, height/2, width*0.1, height*0.1 , 20)
            fill(0)
            textSize(26)
            W = textWidth(players['player4'])
            W = (width - W) //1.525
            text(players['player4'],W, height/1.965)
            
            #speler 3
            if (( width/2.45 > mouseX > width/3.265) and ( height/1.812 > mouseY > height/2.227) and mousePressed):
                target = 3
                state += 1
                background('#5493BF')
            
            # #speler 1
            # if (( width/1.811 > mouseX > width/2.217) and ( height/1.812 > mouseY > height/2.227)and mousePressed):
            #     target = 1
            #     state += 1
            #     background('#5493BF')
            
            #speler 4
            if (( width/1.435 > mouseX > width/1.681) and (height/1.812 > mouseY > height/2.227)and mousePressed):
                target = 4
                state += 1
                background('#5493BF')
            stroke(0)

# als speler 3 aan beurt is            
        if turn == 3:
            
            # kies speler 1 als tegenstander
            if (( width/2.45 > mouseX > width/3.265) and ( height/1.812 > mouseY > height/2.227)):
                stroke(255)
            else:
                stroke(0)
            fill(150)
            rectMode(CENTER)
            rect(width/2.8, height/2, width*0.1, height*0.1 , 20)
            fill(0)
            textSize(26)
            W = textWidth(players['player1'])
            W = (width - W) //2.9
            text(players['player1'],W, height/1.965)
            
            # # kies speler 4 als tegenstander
            # if (( width/1.811 > mouseX > width/2.217) and ( height/1.812 > mouseY > height/2.227)):
            #     stroke(255)
            # else:
            #     stroke(0)
            # fill(150)
            # rect(width/2, height/2, width*0.1, height*0.1 , 20)
            # fill(0)
            # textSize(26)
            # W = textWidth(players['player4'])
            # W = (width - W) //2
            # text(players['player4'],W, height/1.965)
            
            # kies speler 2 als tegenstander
            if (( width/1.435 > mouseX > width/1.681) and (height/1.812 > mouseY > height/2.227)):
                stroke(255)
            else:
                stroke(0)
            fill(150)
            rect(width/1.55, height/2, width*0.1, height*0.1 , 20)
            fill(0)
            textSize(26)
            W = textWidth(players['player2'])
            W = (width - W) //1.525
            text(players['player2'],W, height/1.965)
            
            # speler 1
            if (( width/2.45 > mouseX > width/3.265) and ( height/1.812 > mouseY > height/2.227) and mousePressed):
                target = 1
                state += 1
                background('#5493BF')
            
            # # speler 4
            # if (( width/1.811 > mouseX > width/2.217) and ( height/1.812 > mouseY > height/2.227)and mousePressed):
            #     target = 4
            #     state += 1
            #     background('#5493BF')
            
            # speler 2
            if (( width/1.435 > mouseX > width/1.681) and (height/1.812 > mouseY > height/2.227)and mousePressed):
                target = 2
                state += 1
                background('#5493BF')
            stroke(0)
        
# als speler 4 aan de beurt is        
        if turn == 4:
            
            # kies speler 1 als tegenstander
            if (( width/2.45 > mouseX > width/3.265) and ( height/1.812 > mouseY > height/2.227)):
                stroke(255)
            else:
                stroke(0)
            fill(150)
            rectMode(CENTER)
            rect(width/2.8, height/2, width*0.1, height*0.1 , 20)
            fill(0)
            textSize(26)
            W = textWidth(players['player1'])
            W = (width - W) //2.9
            text(players['player1'],W, height/1.965)
            
            # # kies speler 3 als tegenstander
            # if (( width/1.811 > mouseX > width/2.217) and ( height/1.812 > mouseY > height/2.227)):
            #     stroke(255)
            # else:
            #     stroke(0)
            # fill(150)
            # rect(width/2, height/2, width*0.1, height*0.1 , 20)
            # fill(0)
            # textSize(26)
            # W = textWidth(players['player3'])
            # W = (width - W) //2
            # text(players['player3'],W, height/1.965)
            
            # kies speler 2 als tegenstander
            if (( width/1.435 > mouseX > width/1.681) and (height/1.812 > mouseY > height/2.227)):
                stroke(255)
            else:
                stroke(0)
            fill(150)
            rect(width/1.55, height/2, width*0.1, height*0.1 , 20)
            fill(0)
            textSize(26)
            W = textWidth(players['player2'])
            W = (width - W) //1.525
            text(players['player2'],W, height/1.965)
            
            # speler 1
            if (( width/2.45 > mouseX > width/3.265) and ( height/1.812 > mouseY > height/2.227) and mousePressed):
                target = 1
                state += 1
                background('#5493BF')
            
            # # speler 3
            # if (( width/1.811 > mouseX > width/2.217) and ( height/1.812 > mouseY > height/2.227)and mousePressed):
            #     target = 3
            #     state += 1
            #     background('#5493BF')
            
            # speler 2
            if (( width/1.435 > mouseX > width/1.681) and (height/1.812 > mouseY > height/2.227)and mousePressed):
                target = 2
                state += 1
                background('#5493BF')
            stroke(0)

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
    
def player_display(players,turn):
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
    text(players['player'+str(turn)],width/48, height/20)
    text('totaal :'+ str(totaal1),width/48, height/8)
    if state == 1:
        fill(100)
    else :
        fill(150)
    rect(width/1.263, 0,width,height/5,5)
    fill(0)
    text(players['player' + str(target)],width/1.23, height/20)
    text('totaal :'+ str(totaal2),width/1.23, height/8)


def dual(players,turn):
    global loaded
    global totaal1
    global totaal2
    loaded = True
    fill (0,100)
    rect(0,0,width,height)
    if totaal1 > totaal2:
        fill(255)
        W = textWidth(players['player' +str(turn)] +' wins')
        W = (width - W) //2
        text(players['player' +str(turn)]+' wins',W,height/2)
    elif totaal2 > totaal1:
        fill(255)
        W = textWidth(players['player' + str(target)] +' wins')
        W = (width - W) //2
        text(players['player' + str(target)] +' wins',W,height/2)
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
    global cijferD4
    global cijferD10
    global cijferD6
    rectX1 = width/1.3
    rectX2 = width
    rectY1 = height/1.14
    rectY2 = height
    rectMode(CORNERS)
    fill('#EA9C88')
    rect(rectX1,rectY1,rectX2,rectY2)
    fill(0)
    text ('volgende',width/1.2,height/1.05)
    if mousePressed and (rectX1 < mouseX < rectX2)and(rectY1 < mouseY < rectY2 ) and pressed:
        cijfers = []
        cijferD4 = 0
        cijferD6 = 0
        cijferD10 = 0
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
    
def newBattle(dice,images, victim_dice):
    x=[width/1.92,width/1.67,width/1.92,width/1.67,width/1.92,width/1.67,width/1.92,width/1.67,width/1.92,width/1.67]
    y=[height/5.68,height/5.68,height/3.18,height/3.18,height/2.20,height/2.20,height/1.69,height/1.69,height/1.37,height/1.37]

    cijfers = []
    for i in range(len(dice)):
        if dice[i] == 'd6':
            cijfers.append(newD6(images,x[i],y[i]))
        elif dice[i] == 'd10':
             cijfers.append(newD10(images,x[i],y[i]))
        elif dice[i] == 'd4':
             cijfers.append(newD4(images,x[i],y[i]))
    if  victim_dice == 'd6':
        victim_cijfer = newD6(images,width/38.4,height/5.68)
    elif  victim_dice == 'd10':
        victim_cijfer = newD10(images,width/38.4,height/5.68)
    elif  victim_dice == 'd4':
        victim_cijfer = newD4(images,width/38.4,height/5.68)
    totaal = 0
    for i in cijfers:
            totaal += i
    if totaal > victim_cijfer:
        win = "attacker"
    elif totaal < victim_cijfer:
        win = "defender"
    else:
        win = "draw"
    return win
    
def newD6(images,x,y):
    cijferD6 = random.randint(1,6)
    image(images["D6-"+str(cijferD6)],x,y,100,100,)
    return cijferD6

    
def newD4(images,x,y):
    cijferD4 = random.randint(1,4)
    image(images["D4-"+str(cijferD4)],x,y,100,100,)
    return cijferD4

def newD10(images,x,y):
    cijferD10 = random.randint(1,10)
    image(images["D10-"+str(cijferD10)],x,y,100,100,)    
    return cijferD10  

    
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
        
    
def knop(sfx_files,mousePressed,mode,kleur,rectX1,rectX2,rectY1,rectY2,textbreedte,texthoogte):
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
        b_u.play_sfx("dobbel")
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
    global pressed,amountD4,amountD6,amountD10,cijfers,cijfersD10,cijfersD6,cijfersD4,totaal,totaal1,totaal2,getelt,state,loaded,target
    if state == 2:
        rectMode(CORNER)
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
        target = 1
        return 8
    return 6
