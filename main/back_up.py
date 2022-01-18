import functions as f
add_library("minim")

#taal
taal1 = True
taal2 = True

#variables
x = 860
x2 = 960
mouse_down = False
mouse_down2 = False

sfx_files = ''


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
    #languageButton1(mousePressed)
    #languageButton2(mousePressed)
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
def sfx_gain():
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

    

# talenknop 1
def languageButton1(mousePressed):
    fill(255)
    f.textBox(660, 350, 150, 150, 'NL')
    fill(0)
    strokeWeight(10)

    if 660 < mouseX < 500 and 200 < mouseY < 300:
        print('NL')

# talenknop 2
def languageButton2(mousePressed):
    fill(255)
    f.textBox(1110, 350, 150, 150, 'EN')
    fill(0)
    strokeWeight(10)

    if 1010 < mouseX < 500 and 200 < mouseY < 300:
        print('EN')






def get_sfx(sfx_filess):
    global sfx_files
    sfx_files = sfx_filess
    return sfx_files


def play_sfx(sound):
    sfx = sfx_files[sound]
    sfx_volume = sfx_gain()
    sfx.setGain(sfx_volume)
    sfx.play()
    sfx.rewind()


def mouseReleased_():
    global mouse_down, mouse_down2
    mouse_down = False
    mouse_down2 = False
    
