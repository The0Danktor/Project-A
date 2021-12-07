import nameinput_system as n_sys
import functions as f

# game background image loader
def loadScreen(images):
    image(images['game_img'], 0, 0, width, height)

# game display function [displays the game screen]
def displayScreen(players, turn):

    # Player name displays
    pCount = n_sys.update_t_dis()['pCount']
    mode = n_sys.update_t_dis()['mode']
    modeSpecs = n_sys.update_t_dis()['modeSpecs']
    
    # name displays
    stroke(0)
    strokeWeight(7)
    if pCount == 2:
        if turn == 1:
            stroke(255)
        else:
            stroke(0)
        f.textBox(width*0.2, height*0.05, width*0.1, height*0.1, players['player1'], '#FF0000', 0)
        if turn == 2:
            stroke(255)
        else:
            stroke(0)
        f.textBox(width*0.7, height*0.05, width*0.1, height*0.1, players['player2'], '#008000', 0)
    elif pCount == 4:
        if turn == 1:
            stroke(255)
        else:
            stroke(0)
        f.textBox(width*0.10, height*0.05, width*0.1, height*0.1, players['player1'], '#FF0000', 0)
        if turn == 2:
            stroke(255)
        else:
            stroke(0)
        f.textBox(width*0.33, height*0.05, width*0.1, height*0.1, players['player2'], '#008000', 0)
        if turn == 3:
            stroke(255)
        else:
            stroke(0)
        f.textBox(width*0.57, height*0.05, width*0.1, height*0.1, players['player3'], '#0000FF', 0)
        if turn == 4:
            stroke(255)
        else:
            stroke(0)
        f.textBox(width*0.80, height*0.05, width*0.1, height*0.1, players['player4'], '#FFFF00', 0)
    stroke(0)
    f.textBox(width*0.7, height*0.7, width*0.2, height*0.2, '--->', 200, 0)
    f.textBox(width*0.1, height*0.75, width*0.1, height*0.1, 'Dice', 200, 0)
    f.textBox(width*0.25, height*0.75, width*0.1, height*0.1, 'Cards', 200, 0)

# button click system
def mousePressed_(players, turn):
    if width*0.7 < mouseX < width*0.9 and height*0.7 < mouseY < height*0.9:
        turn += 1
        if turn > n_sys.update_t_dis()['pCount']:
            turn = 1
            
        print(turn)
        return turn
    if width*0.1 < mouseX < width*0.2 and height*0.75 < mouseY < height*0.85:
        return -6
    noStroke()
