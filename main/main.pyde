# ==================================================
# main file, used for controlling everything
# ==================================================

# imports for other files
import title_display as t_dis
import nameinput_display as n_dis
import menu_display as m_dis
import esc_display as e_dis
import game_display as g_dis
import nameinput_system as n_sys
import dice_system as d_sys
add_library("minim")

# setup global variables
state = 0
backup_state = 0
players = {
           'player1' : 'Player 1',
           'player2' : 'Player 2',
           'player3' : 'Player 3',
           'player4' : 'Player 4'
}
turn = 1
images = {}
clicked = False
NO_ESCAPE = '0'

# ==================================================
# state 0 = menu
# state 1/4 = nameinput player1/4
# state 5 = start screen
# state 6 = dice
# state 7 = esc menu
# state 8 = game active
# ==================================================

# setup function
def setup():
    # Import images
    global images
    images = {
              'board_img' : loadImage("board3.png"),
              'title_img' : loadImage("titlescreen.png"),
              'menu_img'  : loadImage("camo.png"),
              'game_img'  : loadImage("test_background.jpg")
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
        d_sys.dice_systeem(mousePressed,players)
    elif state == 7:
        e_dis.displayScreen()
    elif state == 8:
        g_dis.displayScreen(players, turn)

# ==================================================

# mouse press function
def mousePressed():
    global clicked, players, state, turn
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
    elif state == 7:
        state = e_dis.mousePressed_()
        if state == -1:
            state = backup_state
    elif state == 8:
        ret = g_dis.mousePressed_(players, turn)
        if ret > 0:
            turn = ret
        else:
            state = ret * -1
        
    if saved_state != state:
        refresh()

def mouseReleased():
    global clicked
    clicked = False
    
    d_sys.mouseReleased_()
    
def refresh():
    global state
    if state == 0:
        m_dis.loadScreen(images)
    elif state in (1,2,3,4):
        n_dis.loadScreen(images)
    elif state == 5:
        t_dis.loadScreen(images)
    elif state == 6:
        d_sys.loadScreen()
    elif state == 8:
        g_dis.loadScreen(images)

# ==================================================

# key press function
def keyPressed():
    global backup_state
    if key == ESC:
        this.key = NO_ESCAPE
        if state != 0:
            if state != 7:
                fill(0, 100)
                rectMode(CORNER)
                rect(0, 0, width, height)
                backup_state = state
                state = 7
            else:
                state = backup_state
                refresh()
    global state, players
        
    # nameinput_system key input
    if 1 <= state <= 4:
        if key != ENTER and key != RETURN:
            n_sys.keyInput(key)
        else:
            players['player' + str(state)] = n_sys.returnName()
            state = 5
            t_dis.loadScreen(images)
        
        
