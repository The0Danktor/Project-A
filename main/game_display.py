import nameinput_system as n_sys
import functions as f

game_turn = 1

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
    f.textBox(width*0.7, height*0.7, width*0.2, height*0.2, str(game_turn) + '--->', 200, 0)
    f.textBox(width*0.1, height*0.75, width*0.1, height*0.1, 'Dice', 200, 0)
    f.textBox(width*0.25, height*0.75, width*0.1, height*0.1, 'Cards', 200, 0)
    draw_hexagon(width*0.5, height*0.5, 50)
    
def draw_hexagon(x, y, side):
    strokeWeight(2)
    stroke(255)
    noFill()
    beginShape()
    vertex(( x + side * sin(PI/2), y + side * cos(PI/2)))
    vertex(( x + side * sin(PI/6), y + side * cos(PI/6)))
    vertex(( x + side * sin(11 * PI/6), y + side * cos(11 * PI/6)))
    vertex(( x + side * sin(3 * PI/2), y + side * cos(3 * PI/2)))
    vertex(( x + side * sin(7 * PI/6), y + side * cos(7 * PI/6)))
    vertex(( x + side * sin(5 * PI/6), y + side * cos(5 * PI/6)))
    endShape(CLOSE)
    noStroke()

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
    if width*0.1 < mouseX < width*0.2 and height*0.75 < mouseY < height*0.85:
        return -6
    noStroke()
    return -8
