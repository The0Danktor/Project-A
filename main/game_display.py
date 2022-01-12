import nameinput_system as n_sys
import game_system as g_sys
import functions as f
import token_system as t_sys

game_turn = 1

# game background image loader
def loadScreen(images):
    image(images['background_img'], 0, 0, width, height)

# game display function [displays the game screen]
def displayScreen(players, turn, images, fields, mousePressed_):
    
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
    f.textBox(width*0.4, height*0.85, width*0.1, height*0.1, 'upgrade', 200, 0)
    
    fill(50)
    rect(width*0.7, height*0.20, width*0.2, height*0.42, 10)
    fill(255)
    text("Tokens: " + str(t_sys.get_tokens(turn)), f.center("Tokens: " + str(t_sys.get_tokens(turn)), width*0.19, height*0.1, 1) - (width / 2) + width*0.8, height*0.26)
    text("Pelotons: " + str(t_sys.get_pelotons(turn)), f.center("Pelotons: " + str(t_sys.get_pelotons(turn)), width*0.19, height*0.1, 1) - (width / 2) + width*0.8, height*0.32)
    text("Auto's: " + str(t_sys.get_autos(turn)), f.center("Auto's: " + str(t_sys.get_autos(turn)), width*0.19, height*0.1, 1) - (width / 2) + width*0.8, height*0.38)
    text("Tanks: " + str(t_sys.get_tanks(turn)), f.center("Tanks: " + str(t_sys.get_tanks(turn)), width*0.19, height*0.1, 1) - (width / 2) + width*0.8, height*0.44)
    text("Income per turn: " + str(t_sys.calculateIncome(turn)), f.center("Income per turn: " + str(t_sys.calculateIncome(turn)), width*0.19, height*0.1, 1) - (width / 2) + width*0.8, height*0.52)
    text("Actions left: " + str(g_sys.getActions()), f.center("Actions left: " + str(g_sys.getActions()), width*0.19, height*0.1, 1) - (width / 2) + width*0.8, height*0.58)

    fill(100)
    text('Turn: ' + str(game_turn), f.center('Turn: ' + str(game_turn), width*0.10, height*0.1, 1) - (width / 2) + width*0.8, height*0.87)

    noStroke()
    fill('#FF0000')
    rect(width*0.1,height*0.17,width*0.4,height*0.01)
    fill('#008000')
    rect(width*0.1,height*0.82,width*0.4,height*0.01)
    if pCount == 4:
        fill('#FF0000')
        rect(width*0.1,height*0.17,width*0.4,height*0.01)
        fill('#008000')
        rect(width*0.3,height*0.17,width*0.2,height*0.01)
        fill('#0000FF')
        rect(width*0.1,height*0.82,width*0.4,height*0.01)
        fill('#FFFF00')
        rect(width*0.3,height*0.82,width*0.2,height*0.01)
    fill(0)
    image(images['board_img'], width*0.1, height*0.18, width*0.4, height*0.64)
    
    valid_locs = g_sys.getValids()[0]
    mouse_down = g_sys.getValids()[1]
    if mouse_down == True:
        for loc in valid_locs:
            ellipseMode(CENTER)
            ellipse(fields[loc + 'x'], fields[loc + 'y'], width*0.002, width*0.002)
            ellipseMode(CORNER)
            
    # for k in [word for word in fields.keys() if word.endswith("x")]:
    #     ellipseMode(CENTER)
    #     ellipse(fields[k], fields[k[:-1] + 'y'], width*0.002, width*0.002)
    #     ellipseMode(CORNER)
        
    piece_locs = g_sys.getPieces()
    imageMode(CENTER)
    
    fields = g_sys.getFields()
    if t_sys.get_pelotons(turn) > 0 or t_sys.get_autos(turn) > 0 or t_sys.get_tanks(turn) > 0:
        if pCount == 2 and mouse_down == False:
            if turn == 2:
                checkSpot('b1', images)
                checkSpot('d1', images)
                checkSpot('f1', images)
                checkSpot('h1', images)
            else: 
                checkSpot('b8', images)
                checkSpot('d8', images)
                checkSpot('f8', images)
                checkSpot('h8', images)
        elif pCount == 4 and mouse_down == False:
            if turn == 1 or turn == 2:
                checkSpot('b8', images)
                checkSpot('d8', images)
                checkSpot('f8', images)
                checkSpot('h8', images)
            else:
                checkSpot('b1', images)
                checkSpot('d1', images)
                checkSpot('f1', images)
                checkSpot('h1', images)
            
    for piece in piece_locs:
        if piece[4] != 'unused':
            image(images[str(piece[4]) + '_' + str(piece[3]) + '_img'], piece[0], piece[1], height*0.05, height*0.05)
    imageMode(CORNER)
    
    choosing = g_sys.updateChoosing()
    if choosing == True:
        fill(50)
        stroke(0)
        strokeWeight(7)
        rect(width*0.275, height*0.375, width*0.05, height*0.25, 20)
        if turn == 1:
            colour = 'red'
        elif turn == 2:
            colour = 'green'
        elif turn == 3:
            colour = 'blue'
        else:
            colour = 'yellow'
        fill(255)
        if t_sys.get_pelotons(turn) > 0:
            if t_sys.get_tokens(turn) >= 4:
                image(images[colour + '_s_img'], width*0.285, height*0.400, width*0.03, height*0.05)
            else:
                image(images['gray_s_img'], width*0.285, height*0.400, width*0.03, height*0.05)
            text('4 Tokens', f.center('4 Tokens', width*0.029, height*0.1, 1) - (width / 2) + width*0.300, height*0.450)
        else:
            text('none left', f.center('none left', width*0.029, height*0.1, 1) - (width / 2) + width*0.300, height*0.430)
        if t_sys.get_autos(turn) > 0:
            if t_sys.get_tokens(turn) >= 6:
                image(images[colour + '_c_img'], width*0.285, height*0.475, width*0.03, height*0.05)
            else:
                image(images['gray_c_img'], width*0.285, height*0.475, width*0.03, height*0.05)
            text('6 Tokens', f.center('6 Tokens', width*0.029, height*0.1, 1) - (width / 2) + width*0.300, height*0.525)
        if t_sys.get_tanks(turn) > 0:
            if t_sys.get_tokens(turn) >= 9:
                image(images[colour + '_t_img'], width*0.285, height*0.550, width*0.03, height*0.05)
            else:
                image(images['gray_t_img'], width*0.285, height*0.550, width*0.03, height*0.05)
            text('9 Tokens', f.center('9 Tokens', width*0.029, height*0.1, 1) - (width / 2) + width*0.300, height*0.600)
        
def checkSpot(field, images):
    piece_locs = g_sys.getPieces()
    fields = g_sys.getFields()
    result = True
    for piece in piece_locs:
        if round(piece[0], 2) == round(fields[field + 'x'], 2) and round(piece[1], 2) == round(fields[field + 'y'], 2):
            result = False
    if result == True:
        image(images['add_button_img'], fields[field + 'x'], fields[field + 'y'], height*0.05, height*0.05)
    
# button click system
def mousePressed_(players, turn):
    global game_turn
    if width*0.7 < mouseX < width*0.9 and height*0.7 < mouseY < height*0.9:
        turn += 1
        if turn > n_sys.update_t_dis()['pCount']:
            turn = 1
            game_turn += 1
        if game_turn > 1:
            t_sys.token_per_turn(turn)
        g_sys.resetTurn(turn)
        return turn
    if width*0.1 < mouseX < width*0.2 and height*0.85 < mouseY < height*0.95:
        return -6
    if width*0.25 < mouseX < width*0.35 and height*0.85 < mouseY < height*0.95:
        return -9
    if width*0.4 < mouseX < width*0.5 and height*0.85 < mouseY < height*0.95:
        return -12
    
    noStroke()
    return -8
