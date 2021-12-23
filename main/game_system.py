import nameinput_system as n_sys

fields = {}
piece_locs = ()
mouse_down = False
current = 0

def createPieces():
    global piece_locs
    piece_locs = [
                  [width*0.140, height*0.285, 0, 's', 'blue'],
                  [width*0.180, height*0.250, 1, 'c', 'yellow'],
                  [width*0.260, height*0.250, 2, 't', 'yellow']
                  ]
    print(piece_locs)
    
def getPieces():
    global piece_locs
    return piece_locs

def getFields():
    global fields
    return fields

def createPiece(field = 'b1', type='s', colour='green'):
    global piece_locs
    piece_locs.append([fields[field + 'x'], fields[field + 'y'], len(piece_locs), type, colour])

def mousePressed_(turn):
    global current
    
    saved = width
    for pos in piece_locs:
        distance = sqrt((pos[0] - mouseX)**2 + (pos[1] - mouseY)**2)
        if distance < saved:
            saved = distance
            current = pos[2]
    
    pCount = n_sys.update_t_dis()['pCount']
    if (pCount == 2 and turn == 1) or (pCount == 4 and (turn == 1 or turn == 2)):
        turn_locs = ['b8', 'd8', 'f8', 'h8']
        field = 'h8'
    else:
        turn_locs = ['b1', 'd1', 'f1', 'h1']
        field = 'h1'
    for loc in turn_locs:
        distance = sqrt((fields[loc + 'x'] - mouseX)**2 + (fields[loc + 'y'] - mouseY)**2)
        if distance < saved:
            saved = distance
            field = loc
    result = True
    for piece in piece_locs:
        if round(piece[0], 2) == round(fields[field + 'x'], 2) and round(piece[1], 2) == round(fields[field + 'y'], 2):
            result = False
    if result == True:
        if ((mouseX - fields[field + "x"])**2 + (mouseY - fields[field + "y"])**2 < (width*0.018)**2):
            if turn == 1:
                colour = 'red'
            elif turn == 2:
                colour = 'green'
            elif turn == 3:
                colour = 'blue'
            else:
                colour = 'yellow'
            createPiece(field, 't', colour)

def draw_(mouse_pressed, turn):
    global piece_locs, mouse_down, current
    if (((mouseX - piece_locs[current][0])**2 + (mouseY - piece_locs[current][1])**2 < (width*0.018)**2) and mouse_pressed) or (mouse_down == True):
        if (turn == 1 and piece_locs[current][4] == 'red')\
        or (turn == 2 and piece_locs[current][4] == 'green')\
        or (turn == 3 and piece_locs[current][4] == 'blue')\
        or (turn == 4 and piece_locs[current][4] == 'yellow'):
            mouse_down = True
            piece_locs[current][0] = mouseX
            piece_locs[current][1] = mouseY

def mouseReleased_():
    global piece_loc, mouse_down, current
    if mouse_down == True:
        mouse_down = False
        saved = width
        loc = 'a7x'
        for k in [word for word in fields.keys() if word.endswith("x")]:
            distance = sqrt((fields[k] - mouseX)**2 + (fields[k[:-1] + 'y'] - mouseY)**2)
            if distance < saved:
                saved = distance
                loc = k
        piece_locs[current][0] = fields[loc]
        piece_locs[current][1] = fields[loc[:-1] + 'y']
            

def createField():
    global fields
    x_offset = width*0.04
    y_offset = height*0.0715
    x_start = width*0.140
    y_start_1 = height*0.285
    y_start_2 = height*0.250
    
    fields = {
              "a7x" : x_start + x_offset * 0, "a7y" : y_start_1 + y_offset * 0,
              "a6x" : x_start + x_offset * 0, "a6y" : y_start_1 + y_offset * 1,
              "a5x" : x_start + x_offset * 0, "a5y" : y_start_1 + y_offset * 2,
              "a4x" : x_start + x_offset * 0, "a4y" : y_start_1 + y_offset * 3,
              "a3x" : x_start + x_offset * 0, "a3y" : y_start_1 + y_offset * 4,
              "a2x" : x_start + x_offset * 0, "a2y" : y_start_1 + y_offset * 5,
              "a1x" : x_start + x_offset * 0, "a1y" : y_start_1 + y_offset * 6,
              
              "b8x" : x_start + x_offset * 1, "b8y" : y_start_2 + y_offset * 0,
              "b7x" : x_start + x_offset * 1, "b7y" : y_start_2 + y_offset * 1,
              "b6x" : x_start + x_offset * 1, "b6y" : y_start_2 + y_offset * 2,
              "b5x" : x_start + x_offset * 1, "b5y" : y_start_2 + y_offset * 3,
              "b4x" : x_start + x_offset * 1, "b4y" : y_start_2 + y_offset * 4,
              "b3x" : x_start + x_offset * 1, "b3y" : y_start_2 + y_offset * 5,
              "b2x" : x_start + x_offset * 1, "b2y" : y_start_2 + y_offset * 6,
              "b1x" : x_start + x_offset * 1, "b1y" : y_start_2 + y_offset * 7,
              
              "c7x" : x_start + x_offset * 2, "c7y" : y_start_1 + y_offset * 0,
              "c6x" : x_start + x_offset * 2, "c6y" : y_start_1 + y_offset * 1,
              "c5x" : x_start + x_offset * 2, "c5y" : y_start_1 + y_offset * 2,
              "c4x" : x_start + x_offset * 2, "c4y" : y_start_1 + y_offset * 3,
              "c3x" : x_start + x_offset * 2, "c3y" : y_start_1 + y_offset * 4,
              "c2x" : x_start + x_offset * 2, "c2y" : y_start_1 + y_offset * 5,
              "c1x" : x_start + x_offset * 2, "c1y" : y_start_1 + y_offset * 6,
              
              "d8x" : x_start + x_offset * 3, "d8y" : y_start_2 + y_offset * 0,
              "d7x" : x_start + x_offset * 3, "d7y" : y_start_2 + y_offset * 1,
              "d6x" : x_start + x_offset * 3, "d6y" : y_start_2 + y_offset * 2,
              "d5x" : x_start + x_offset * 3, "d5y" : y_start_2 + y_offset * 3,
              "d4x" : x_start + x_offset * 3, "d4y" : y_start_2 + y_offset * 4,
              "d3x" : x_start + x_offset * 3, "d3y" : y_start_2 + y_offset * 5,
              "d2x" : x_start + x_offset * 3, "d2y" : y_start_2 + y_offset * 6,
              "d1x" : x_start + x_offset * 3, "d1y" : y_start_2 + y_offset * 7,
              
              "e7x" : x_start + x_offset * 4, "e7y" : y_start_1 + y_offset * 0,
              "e6x" : x_start + x_offset * 4, "e6y" : y_start_1 + y_offset * 1,
              "e5x" : x_start + x_offset * 4, "e5y" : y_start_1 + y_offset * 2,
              "e4x" : x_start + x_offset * 4, "e4y" : y_start_1 + y_offset * 3,
              "e3x" : x_start + x_offset * 4, "e3y" : y_start_1 + y_offset * 4,
              "e2x" : x_start + x_offset * 4, "e2y" : y_start_1 + y_offset * 5,
              "e1x" : x_start + x_offset * 4, "e1y" : y_start_1 + y_offset * 6,
              
              "f8x" : x_start + x_offset * 5, "f8y" : y_start_2 + y_offset * 0,
              "f7x" : x_start + x_offset * 5, "f7y" : y_start_2 + y_offset * 1,
              "f6x" : x_start + x_offset * 5, "f6y" : y_start_2 + y_offset * 2,
              "f5x" : x_start + x_offset * 5, "f5y" : y_start_2 + y_offset * 3,
              "f4x" : x_start + x_offset * 5, "f4y" : y_start_2 + y_offset * 4,
              "f3x" : x_start + x_offset * 5, "f3y" : y_start_2 + y_offset * 5,
              "f2x" : x_start + x_offset * 5, "f2y" : y_start_2 + y_offset * 6,
              "f1x" : x_start + x_offset * 5, "f1y" : y_start_2 + y_offset * 7,
              
              "g7x" : x_start + x_offset * 6, "g7y" : y_start_1 + y_offset * 0,
              "g6x" : x_start + x_offset * 6, "g6y" : y_start_1 + y_offset * 1,
              "g5x" : x_start + x_offset * 6, "g5y" : y_start_1 + y_offset * 2,
              "g4x" : x_start + x_offset * 6, "g4y" : y_start_1 + y_offset * 3,
              "g3x" : x_start + x_offset * 6, "g3y" : y_start_1 + y_offset * 4,
              "g2x" : x_start + x_offset * 6, "g2y" : y_start_1 + y_offset * 5,
              "g1x" : x_start + x_offset * 6, "g1y" : y_start_1 + y_offset * 6,
              
              "h8x" : x_start + x_offset * 7, "h8y" : y_start_2 + y_offset * 0,
              "h7x" : x_start + x_offset * 7, "h7y" : y_start_2 + y_offset * 1,
              "h6x" : x_start + x_offset * 7, "h6y" : y_start_2 + y_offset * 2,
              "h5x" : x_start + x_offset * 7, "h5y" : y_start_2 + y_offset * 3,
              "h4x" : x_start + x_offset * 7, "h4y" : y_start_2 + y_offset * 4,
              "h3x" : x_start + x_offset * 7, "h3y" : y_start_2 + y_offset * 5,
              "h2x" : x_start + x_offset * 7, "h2y" : y_start_2 + y_offset * 6,
              "h1x" : x_start + x_offset * 7, "h1y" : y_start_2 + y_offset * 7,
              
              "i7x" : x_start + x_offset * 8, "i7y" : y_start_1 + y_offset * 0,
              "i6x" : x_start + x_offset * 8, "i6y" : y_start_1 + y_offset * 1,
              "i5x" : x_start + x_offset * 8, "i5y" : y_start_1 + y_offset * 2,
              "i4x" : x_start + x_offset * 8, "i4y" : y_start_1 + y_offset * 3,
              "i3x" : x_start + x_offset * 8, "i3y" : y_start_1 + y_offset * 4,
              "i2x" : x_start + x_offset * 8, "i2y" : y_start_1 + y_offset * 5,
              "i1x" : x_start + x_offset * 8, "i1y" : y_start_1 + y_offset * 6
              }
    return fields
