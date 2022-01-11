import functions as f

taal1 = True
taal2 = True


x = 1060
x2 = 660
mouse_down = False
mouse_down2 = False



def displayScreen(mousePressed,):
    #het menu wordt hier getekend
    menu(mousePressed)

    
    
    
def menu(mousePressed):
    stroke(0)
    strokeWeight(10)
    fill(150)
    rect(610,50,700,700,20)
    slider1(mousePressed)
    slider2(mousePressed)
    volume()




# de slider
def slider1(mousePressed):
    global x,mouse_down
    y = 150
    stroke(255)
    strokeWeight(10)
    line(660,150,1260,150)
    if  ((660 < mouseX < 1260 and  y -10 < mouseY < y + 10) or mouse_down) and mousePressed:
        mouse_down = True
        x = mouseX
        if x < 660:
            x = 660
        if x > 1260:
            x = 1260
    strokeWeight(7)
    stroke('#0BA821')
    line (660,150,x,150)
    noStroke()
    fill(255)
    ellipseMode(CENTER)
    ellipse(x,y,20,20)
    textSize(36)
    fill(0)
    text('music :',660,120)
def volume():
    music_volume = ((x-660)/6)-50
    return music_volume
def sfx():
    sfx_volume = ((x2-660)/6)-50
    return sfx_volume
          
    # de slider
def slider2(mousePressed):
    global x2,mouse_down2
    y2 = 250
    stroke(255)
    strokeWeight(10)
    line(660,250,1260,250)
    if  ((660 < mouseX <1260 and  y2 -10 < mouseY < y2 + 10) or mouse_down2) and mousePressed:
        mouse_down2 = True
        x2 = mouseX
        if x2 < 660:
            x2 = 660
        if x2 > 1260:
            x2 = 1260
    strokeWeight(7)
    stroke('#0BA821')
    line (660,250,x2,250)
    noStroke()
    fill(255)
    ellipseMode(CENTER)
    ellipse(x2,y2,20,20)
    textSize(36)
    fill(0)
    text('sfx :',660,220)

def play_sfx(sfx_files,sound):
    sfx = sfx_files[sound]
    sfx.play()
    sfx_volume = b_u.sfx()
    sfx.setGain(sfx_volume)
    sfx.rewind()

def mouseReleased_():
    global mouse_down, mouse_down2
    mouse_down = False
    mouse_down2 = False
