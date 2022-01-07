import functions as f

taal1 = True
taal2 = True


x = 1060
x2 = 1060
mouse_down = False
mouse_down2 = False



def displayScreen(mousePressed,mouseReleased):
    #het menu wordt hier getekend
    menu(mousePressed)
    #de eerste button
    languageButton1(mouseReleased)
    languageButton2(mouseReleased)
    background_()

    
    
    
def menu(mousePressed):
    stroke(0)
    strokeWeight(10)
    fill(150)
    rect(610,50,700,700,20)
    slider1(mousePressed)
    slider2(mousePressed)
    volume()
    soundeffects_()




# de slider
def slider1(mousePressed):
    global x,mouse_down
    y = 100
    stroke(255)
    strokeWeight(10)
    line(660,100,1260,100)
    if  ((660 < mouseX < 1260 and  y -10 < mouseY < y + 10) or mouse_down) and mousePressed:
        mouse_down = True
        x = mouseX
        if x < 660:
            x = 660
        if x > 1260:
            x = 1260
    strokeWeight(7)
    stroke('#0BA821')
    line (660,100,x,100)
    noStroke()
    fill(255)
    ellipseMode(CENTER)
    ellipse(x,y,20,20)

def volume():
    music_volume = ((x-660)/6)-50
    sfx_volume = ((x-660)/6)-50
    return music_volume
          
    # de slider
def slider2(mousePressed):
    global x2,mouse_down2
    y2 = 200
    stroke(255)
    strokeWeight(10)
    line(660,200,1260,200)
    if  ((660 < mouseX <1260 and  y2 -10 < mouseY < y2 + 10) or mouse_down2) and mousePressed:
        mouse_down2 = True
        x2 = mouseX
        if x2 < 660:
            x2 = 660
        if x2 > 1260:
            x2 = 1260
    strokeWeight(7)
    stroke('#0BA821')
    line (660,200,x2,200)
    noStroke()
    fill(255)
    ellipseMode(CENTER)
    ellipse(x2,y2,20,20)
    print(x2-660)

def soundeffects_():
    #fill(0,((x2-660)//6))
    soundeffects = ((x2-660)/6)-50
    sfx2_volume = ((x2-660)/6)-50
    return soundeffects
    
    

def mouseReleased_():
    global mouse_down, mouse_down2
    mouse_down = False
    mouse_down2 = False

def languageButton1(mousePressed):
    global taal1
    #if #mousePressed and (mouseButton == LEFT):
    fill(200)
    #rect(660, 350, 100, 100)
    f.textBox(700, 350, 100, 100, 'NL')
    fill(0)
    strokeweight(10)
    #text('Nederlands', 660, 350, 100, 100)
    if 700 < mouseX < 500 and 450 < mouseY < 400:
        print('Nederlands')
    #elif mousePressed and (mouseButton == RIGHT):
        #fill(255)
    #else:
        #fill('#050505')
    #strokeWeight(10)

    #rect(660, 350, 100, 100)
    
def languageButton2(mousePressed):
    global taal2
    fill(200)
    #rect(1010, 350, 100, 100)
    f.textBox(1110, 350, 100, 100, 'EN')
    strokeweight(10)
    fill(0)
    #text('English', 1010, 350, 100, 100)
    if 1110 < mouseX < 1400 and 450 < mouseY < 400:
        print('English')
    #if mousePressed and (mouseButton == LEFT):

    #elif mousePressed and (mouseButton == RIGHT):
        #fill(255)
    #else:
        #fill('#050505')
    #strokeWeight(10)

    #rect(1010, 350, 100, 100)
