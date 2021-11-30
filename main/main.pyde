# ==================================================
# main file, used for controlling everything
# ==================================================

# imports for other files
import title_display as t_dis
import nameinput_display as n_dis
import nameinput_system as n_sys
import menu_display as m_dis
import dice_system as d_sis
add_library("minim")

# setup global variables
state = 0
players = {
           'player1' : 'Player 1',
           'player2' : 'Player 2',
           'player3' : 'Player 3',
           'player4' : 'Player 4'
}
images = {}
clicked = False
NO_ESCAPE = '0'

# ==================================================
# state 0 = menu
# state 1/4 = nameinput player1/4
# state 5 = start screen
# state 6 = dice
# ==================================================

# setup function
def setup():
    # Import images
    global images
    images = {
              'board_img' : loadImage("board3.png"),
              'title_img' : loadImage("titlescreen.png"),
              'menu_img'  : loadImage("camo.png")
    }
    
    # size(1800,800)
    # this.surface.setResizable(True)
    # this.surface.setTitle("Trench Warfare")
    # this.surface.setLocation(100, 100)
    fullScreen()
    background(0)
    noStroke()
    fill(102)
    print(textSize)
    
    # menu & music
    m_dis.loadScreen(images)
    minim = Minim(this)
    sf = minim.loadFile("music1.mp3")
    sf.play()
    
    mainFont = createFont("SpecialElite-Regular.ttf", 18)
    textFont(mainFont)

# ==================================================

# draw function
def draw():
    global state, players
    
    # display loader
    if state == 0:
        m_dis.displayScreen()
    elif 1 <= state <= 4:
        n_dis.displayScreen(state, images)
    elif state == 5:
        t_dis.displayScreen(players['player1'], players['player2'], players['player3'], players['player4'], images)
    elif state == 6:
        d_sis.dice_systeem(mousePressed)

# ==================================================

# mouse press function
def mousePressed():
    global clicked, players, state
    if clicked == True:
        return
    else:
        clicked = True
        
    saved_state = state
    
    # button registration
    if state == 5:
        state = t_dis.mousePressed_(images, players)
    elif state == 0:
        state = m_dis.mousePressed_()
        
    if saved_state != state:
        if state == 0:
            m_dis.loadScreen(images)
        elif state in (1,2,3,4):
            n_dis.loadScreen(images)
        elif state == 5:
            t_dis.loadScreen(images)
        elif state == 6:
            background('#5493BF')

def mouseReleased():
    global clicked
    clicked = False
    
    d_sis.mouseReleased_()

# ==================================================

# key press function
def keyPressed():
    if key == ESC:
        this.key = NO_ESCAPE
        fill(0, 50)
        rect(0, 0, width, height)
        state = 1
    global state, players
        
    # nameinput_system key input
    if 1 <= state <= 4:
        if key != ENTER and key != RETURN:
            n_sys.keyInput(key)
        else:
            players['player' + str(state)] = n_sys.returnName()
            state = 5
            t_dis.loadScreen(images)
        
        
