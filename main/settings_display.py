import test as f

taal1 = True
taal2 = True


x = 100
x2 = 100
mouse_down = False
mouse_down2 = False



def menu_draw():
    #het menu wordt hier getekend
    menu()
    #de eerste button
    languageButton1()
    languageButton2()

    
    
    
def menu():
    stroke(0)
    strokeWeight(10)
    fill(150)
    rect(50,50,500,500,20)
    slider1()
    slider2()
    #print((x-100)//4,(x2-100)//4)


# de slider
def slider1():
    global x,mouse_down
    y = 100
    stroke(255)
    strokeWeight(10)
    line(100,100,500,100)
    if  ((100 < mouseX < 500 and  y -10 < mouseY < y + 10) or mouse_down) and mousePressed:
        mouse_down = True
        x = mouseX
        if x < 100:
            x = 100
        if x > 500:
            x = 500
    strokeWeight(7)
    stroke('#0BA821')
    line (100,100,x,100)
    noStroke()
    fill(255)
    ellipse(x,y,20,20)

    
    # de slider
def slider2():
    global x2,mouse_down2
    y2 = 200
    stroke(255)
    strokeWeight(10)
    line(100,200,500,200)
    if  ((100 < mouseX < 500 and  y2 -10 < mouseY < y2 + 10) or mouse_down2) and mousePressed:
        mouse_down2 = True
        x2 = mouseX
        if x2 < 100:
            x2 = 100
        if x2 > 500:
            x2 = 500
    strokeWeight(7)
    stroke('#0BA821')
    line (100,200,x2,200)
    noStroke()
    fill(255)
    ellipse(x2,y2,20,20)

def mouseReleased():
    global mouse_down, mouse_down2
    mouse_down = False
    mouse_down2 = False

def languageButton1():
    global taal1
    if mousePressed and (mouseButton == LEFT):
        fill(200)
    elif mousePressed and (mouseButton == RIGHT):
        fill(255)
    else:
        fill('#050505')
    strokeWeight(10)

    rect(100, 350, 100, 100)
    
def languageButton2():
    global taal2
    if mousePressed and (mouseButton == LEFT):
        fill(200)
    elif mousePressed and (mouseButton == RIGHT):
        fill(255)
    else:
        fill('#050505')
    strokeWeight(10)

    rect(400, 350, 100, 100)
