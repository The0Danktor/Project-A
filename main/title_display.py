# imports for other files
import functions as f
import nameinput_system as n_sys
import token_system as t_sys

req_refresh = False

#title background image loader
def loadScreen(images):
    global req_refresh
    req_refresh = True

# title display function [displays the title screen]
def displayScreen(player1, player2, player3, player4, images):
    global req_refresh
    
    # background refresh
    if req_refresh == True:
        image(images['background_img'], 0, 0, width, height)
        req_refresh = False
    
    # Player name displays
    scalar = 0.8
    pCount = n_sys.update_t_dis()['pCount']
    mode = n_sys.update_t_dis()['mode']
    modeSpecs = n_sys.update_t_dis()['modeSpecs']
    
    t_sys.tokenbegin_Refresh()
    
    stroke(0)
    strokeWeight(7)
    if pCount == 4:
        f.textBox(width*0.7, height*0.08, width*0.2, height*0.15, player1, '#FF0000', 0, scalar)
        f.textBox(width*0.7, height*0.31, width*0.2, height*0.15, player2, '#008000', 0, scalar)
        f.textBox(width*0.7, height*0.54, width*0.2, height*0.15, player3, '#0000FF', 0, scalar)
        f.textBox(width*0.7, height*0.77, width*0.2, height*0.15, player4, '#FFFF00', 0, scalar)
        f.textBox(width*0.77, height*0.94, width*0.06, height*0.04, 'shuffle')
    elif pCount == 2:
        f.textBox(width*0.7, height*0.31, width*0.2, height*0.15, player1, '#FF0000', 0, scalar)
        f.textBox(width*0.7, height*0.54, width*0.2, height*0.15, player2, '#008000', 0, scalar)
        f.textBox(width*0.77, height*0.71, width*0.06, height*0.04, 'shuffle')
    
    f.textBox(width*0.1, height*0.08, width*0.2, height*0.15, 'Players: ' + str(pCount))
    f.textBox(width*0.1, height*0.31, width*0.2, height*0.15, 'Mode: ' + str(mode))
    fill(50)
    rect(width*0.1, height*0.54, width*0.2, height*0.38, 10)
    
    # start button
    f.textBox(width*0.35, height*0.4, width*0.3, height*0.2, 'start')
    noStroke()
    
    # texts above player name displays
    fill(200)
    if pCount == 4:
        text('Click to edit player 1:', f.center('Click to edit player 1:', width*0.2, height*0.1) - (width / 2) + width*0.8, height*0.07)
        text('Click to edit player 2:', f.center('Click to edit player 2:', width*0.2, height*0.1) - (width / 2) + width*0.8, height*0.30)
        text('Click to edit player 3:', f.center('Click to edit player 3:', width*0.2, height*0.1) - (width / 2) + width*0.8, height*0.53)
        text('Click to edit player 4:', f.center('Click to edit player 4:', width*0.2, height*0.1) - (width / 2) + width*0.8, height*0.76)
    elif pCount == 2:
        text('Click to edit player 1:', f.center('Click to edit player 1:', width*0.2, height*0.1) - (width / 2) + width*0.8, height*0.30)
        text('Click to edit player 2:', f.center('Click to edit player 2:', width*0.2, height*0.1) - (width / 2) + width*0.8, height*0.53)
    text('Click to change:', f.center('Click to change:', width*0.2, height*0.1) - (width / 2) + width*0.2, height*0.07)
    text('Click to change:', f.center('Click to change:', width*0.2, height*0.1) - (width / 2) + width*0.2, height*0.30)
    
    # white overlays
    fill(0)
    if pCount == 4:
        text('Click to edit player 1:', f.center('Click to edit player 1:', width*0.2, height*0.1, 1) - (width / 2) + width*0.8, height*0.07)
        text('Click to edit player 2:', f.center('Click to edit player 2:', width*0.2, height*0.1, 1) - (width / 2) + width*0.8, height*0.30)
        text('Click to edit player 3:', f.center('Click to edit player 3:', width*0.2, height*0.1, 1) - (width / 2) + width*0.8, height*0.53)
        text('Click to edit player 4:', f.center('Click to edit player 4:', width*0.2, height*0.1, 1) - (width / 2) + width*0.8, height*0.76)
    elif pCount == 2:
        text('Click to edit player 1:', f.center('Click to edit player 1:', width*0.2, height*0.1, 1) - (width / 2) + width*0.8, height*0.30)
        text('Click to edit player 2:', f.center('Click to edit player 2:', width*0.2, height*0.1, 1) - (width / 2) + width*0.8, height*0.53)
    text('Click to change:', f.center('Click to change:', width*0.2, height*0.1, 1) - (width / 2) + width*0.2, height*0.07)
    text('Click to change:', f.center('Click to change:', width*0.2, height*0.1, 1) - (width / 2) + width*0.2, height*0.30)
    
    fill(255)
    # mode info
    text('Time: ' + modeSpecs['speeltijd'], f.center('Time: ' + modeSpecs['speeltijd'], width*0.19, height*0.1, 1) - (width / 2) + width*0.2, height*0.60)
    text('Tokens: ' + str(modeSpecs['tokens']), f.center('Tokens: ' + str(modeSpecs['tokens']), width*0.19, height*0.1, 1) - (width / 2) + width*0.2, height*0.68)
    text('Pelotons: ' + str(modeSpecs['pelotons']), f.center('Pelotons: ' + str(modeSpecs['pelotons']), width*0.19, height*0.1, 1) - (width / 2) + width*0.2, height*0.74)
    text('Autos: ' + str(modeSpecs['autos']), f.center('Autos: ' + str(modeSpecs['autos']), width*0.19, height*0.1, 1) - (width / 2) + width*0.2, height*0.82)
    text('Tanks: ' + str(modeSpecs['tanks']), f.center('Tanks: ' + str(modeSpecs['tanks']), width*0.19, height*0.1, 1) - (width / 2) + width*0.2, height*0.90)
    
# button click system
def mousePressed_(images, players):
    # right buttons
    pCount = n_sys.update_t_dis()['pCount']
    if pCount == 4:
        if width*0.7 < mouseX < width*0.9 and height*0.08 < mouseY < height*0.23:
            n_sys.setTyping(players['player1'])
            return 1
        if width*0.7 < mouseX < width*0.9 and height*0.31 < mouseY < height*0.46:
            n_sys.setTyping(players['player2'])
            return 2
        if width*0.7 < mouseX < width*0.9 and height*0.54 < mouseY < height*0.69:
            n_sys.setTyping(players['player3'])
            return 3
        if width*0.7 < mouseX < width*0.9 and height*0.77 < mouseY < height*0.92:
            n_sys.setTyping(players['player4'])
            return 4
        if width*0.77 < mouseX < width*0.83 and height*0.94 < mouseY < height*0.98:
            n_sys.shuffleNames(players)
            
    elif pCount == 2:
        if width*0.7 < mouseX < width*0.9 and height*0.31 < mouseY < height*0.46:
            n_sys.setTyping(players['player1'])
            return 1
        if width*0.7 < mouseX < width*0.9 and height*0.54 < mouseY < height*0.69:
            n_sys.setTyping(players['player2'])
            return 2
        if width*0.77 < mouseX < width*0.83 and height*0.71 < mouseY < height*0.74:
            n_sys.shuffleNames(players)
            
    # left/center buttons        
    if width*0.1 < mouseX < width*0.3 and height*0.08 < mouseY < height*0.23:
        n_sys.playerCount()
        loadScreen(images)
    if width*0.1 < mouseX < width*0.3 and height*0.31 < mouseY < height*0.46:
        n_sys.changeMode()
    if width*0.35 < mouseX < width*0.65 and height*0.4 < mouseY < height*0.6:
        return 8
    
    #failsafe
    return 5
