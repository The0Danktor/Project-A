import nameinput_system as n_sys
import game_system as g_sys
import functions as f
import token_system as t_sys

game_turn = 1

# game background image loader
def loadScreen(images):
    image(images['game_img'], 0, 0, width, height)

# game display function [displays the game screen]
def displayScreen(players, turn, images, fields):
    
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
    f.textBox(width*0.1, height*0.85, width*0.1, height*0.1, 'Dice', 200, 0)
    f.textBox(width*0.25, height*0.85, width*0.1, height*0.1, 'Cards', 200, 0)
    
    fill(50)
    rect(width*0.7, height*0.24, width*0.2, height*0.38, 10)
    fill(255)
    text('Turns: ' + str(game_turn), f.center('Turns: ' + str(game_turn), width*0.19, height*0.1, 1) - (width / 2) + width*0.8, height*0.60)
    
    text('Tokens: ' + str(t_sys.get_tokens(turn)), f.center('Tokens: ' + str(t_sys.get_tokens(turn)), width*0.19, height*0.1, 1) - (width / 2) + width*0.8, height*0.50)

    
    fill(0)
    image(images['board_img'], width*0.1, height*0.18, width*0.4, height*0.64)
    # for k in [word for word in fields.keys() if word.endswith("x")]:
    #     ellipseMode(CENTER)
    #     ellipse(fields[k], fields[k[:-1] + 'y'], width*0.002, width*0.002)
    #     ellipseMode(CORNER)
        
    piece_locs = g_sys.getPieces()
    imageMode(CENTER)
    for piece in piece_locs:
        image(images['troll_img'], piece[0], piece[1], width*0.05, height*0.05)
    imageMode(CORNER)

# button click system
def mousePressed_(players, turn):
    global game_turn
    if width*0.7 < mouseX < width*0.9 and height*0.7 < mouseY < height*0.9:
        turn += 1
        if turn > n_sys.update_t_dis()['pCount']:
            turn = 1
            game_turn += 1    
        print(turn)
        return turn
    if width*0.1 < mouseX < width*0.2 and height*0.85 < mouseY < height*0.95:
        return -6
    if width*0.25 < mouseX < width*0.35 and height*0.85 < mouseY < height*0.95:
        return -9
    noStroke()
    return -8
