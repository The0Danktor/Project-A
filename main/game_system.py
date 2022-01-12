import nameinput_system as n_sys
import token_system as t_sys
import upgrades_display as u_dis
import dice_system as d_sys

fields = {}        # a list of all fields on the board
field_names = ('a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7',
               'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
               'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7',
               'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
               'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7',
               'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
               'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7',
               'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8',
               'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7'
               )   # a list of all fields by name
piece_locs = ()    # a list of all piece locations on the board
valid_locs = []    # a list of valid locations for the current piece to move to
mouse_down = False # indicates rather a piece is being moved
current = 0        # indicates the current piece being moved [by index in piece_locs]
backupx = 0        # stores origional x location of a piece being moved for return
backupy = 0        # stores origional y location of a piece being moved for return
choosing = False   # indicates rather the player is choosing a new piece or not
choosing_info = {} # required info for after the player has chosen
plays = 2          # amount of actions left for the turn
trained = 0        # amount of troops trained/entered during the turn
clicked = False

# creates an unused background piece used to counter empty list issues
def createPieces():
    global piece_locs, current
    piece_locs = [[0, 0, 0, 'unused', 'unused']]
    current = 0
    
def resetTurn(turn):
    global plays, trained
    plays = 2 + u_dis.get_generaal(turn)
    # print(plays, u_dis.get_generaal(turn), turn)
    trained = 0

def increaseTrained():
    global trained
    trained += 1
    
# updates choosing in game_display
def updateChoosing():
    global choosing
    return choosing
    
# returns a list of all pieces
def getPieces():
    global piece_locs
    return piece_locs

# retunrs a list of all fields on the board
def getFields():
    global fields
    return fields

# retunrs the amount of actions left
def getActions():
    global plays
    return plays

# retunrs a list of all valid fields on the board
def getValids():
    global valid_locs, mouse_down
    return [valid_locs, mouse_down]

# creates a new piece on the board [s = soldier, c = car, t = tank]
def createPiece(field = 'b1', type = 's', colour='green'):
    global piece_locs
    piece_locs.append([fields[field + 'x'], fields[field + 'y'], len(piece_locs), type, colour])
    
# returns all pieces attacking another piece
def getAttackingPieces(loc, reach):
    global valid_locs
    
    valid_locs = []
    newloc = gridify(loc[:-1])
    checkMovement(newloc, reach, True)
                
# mousePressed() imported from main
def mousePressed_(turn):
    global current, mouse_down, choosing, choosing_info, plays, trained
    
    if choosing == False:
    # reset the current piece being moved to the piece closest to the cursor
        if mouse_down != True:
            saved = width
            for pos in piece_locs:
                distance = sqrt((pos[0] - mouseX)**2 + (pos[1] - mouseY)**2)
                if distance < saved:
                    saved = distance
                    current = pos[2]
        
        # piece creation system
        if plays > 0:
            if t_sys.get_pelotons(turn) > 0 or t_sys.get_autos(turn) > 0 or t_sys.get_tanks(turn) > 0:
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
                        choosing_info['field'] = field
                        choosing_info['colour'] = colour
                        choosing = True
    else:
        if width*0.285 < mouseX < width*0.315 and height*0.400 < mouseY < height*0.450:
            if t_sys.get_pelotons(turn) > 0 and t_sys.get_tokens(turn) >= 4:
                choosing = False
                createPiece(choosing_info['field'], 's', choosing_info['colour'])
                t_sys.pelotons_remove(turn)
                t_sys.tokens_remove(turn, 4)
                
                trained += 1
                if trained == 1:
                    plays -= 1
                elif trained == 4:
                    plays -= 1
        elif width*0.285 < mouseX < width*0.315 and height*0.475 < mouseY < height*0.525:
            if t_sys.get_autos(turn) > 0 and t_sys.get_tokens(turn) >= 6:
                choosing = False
                createPiece(choosing_info['field'], 'c', choosing_info['colour'])
                t_sys.autos_remove(turn)
                t_sys.tokens_remove(turn, 6)
                
                trained += 1
                if trained == 1:
                    plays -= 1
                elif trained == 4:
                    plays -= 1
        elif width*0.285 < mouseX < width*0.315 and height*0.550 < mouseY < height*0.600:
            if t_sys.get_tanks(turn) > 0 and t_sys.get_tokens(turn) >= 9:
                choosing = False
                createPiece(choosing_info['field'], 't', choosing_info['colour'])
                t_sys.tanks_remove(turn)
                t_sys.tokens_remove(turn, 9)
                
                trained += 1
                if trained == 1:
                    plays -= 1
                elif trained == 4:
                    plays -= 1
        elif (mouseX < width*0.275 or mouseX > width*0.325) or (mouseY < height*0.375 or mouseY > height*0.625):
            choosing = False

# draw() imported from main

def draw_(mouse_pressed, turn,images):
    global piece_locs, mouse_down, current, backupx, backupy, valid_locs, choosing, plays, clicked
    
    # returns if the player is choosing
    if choosing == True:
        return
    
    # piece pickup/movement system
    if plays > 0:
        pCount = n_sys.update_t_dis()['pCount']
        if (((mouseX - piece_locs[current][0])**2 + (mouseY - piece_locs[current][1])**2 < (width*0.018)**2) and mouse_pressed) or (mouse_down == True):
            # check if the piece belongs to the current player
            if (turn == 1 and piece_locs[current][4] == 'red')\
            or (turn == 2 and piece_locs[current][4] == 'green')\
            or (turn == 3 and piece_locs[current][4] == 'blue')\
            or (turn == 4 and piece_locs[current][4] == 'yellow'):
                
                # code on piece pickup
                if mouse_down == False:
                    mouse_down = True
                    backupx = piece_locs[current][0]
                    backupy = piece_locs[current][1]
                    loc = 'a7x'
                    for k in [word for word in fields.keys() if word.endswith("x")]:
                        if round(piece_locs[current][0], 2) == round(fields[k], 2) and round(piece_locs[current][1], 2) == round(fields[k[:-1] + 'y'], 2):
                            loc = k
                    reach = 0
                    if piece_locs[current][3] == 's':
                        reach = 3
                    if piece_locs[current][3] == 'c':
                        reach = 5
                    if piece_locs[current][3] == 't':
                        reach = 2
                    valid_locs = []
                    newloc = gridify(loc[:-1])
                    checkMovement(newloc, reach)
                # code during piece pickup
                # if width*0.1 + height*0.025 < mouseX < width*0.5 - height*0.025 and height*0.205 < mouseY < height*0.805:
    
                #     piece_locs[current][0] = mouseX
                #     piece_locs[current][1] = mouseY
                
                piece_locs[current][0] = mouseX
                piece_locs[current][1] = mouseY
                if mouseX < width*0.1 + height*0.025: # check if the mouse is on the left side of the board
                    piece_locs[current][0] = width*0.1 + height*0.025
                if mouseX > width*0.5 - height*0.025: # check if the mouse is on the right side of the board
                    piece_locs[current][0] = width*0.5 - height*0.025
                if mouseY < height*0.205:             # check if the mouse is on the top side of the board
                    piece_locs[current][1] = height*0.205
                if mouseY > height*0.805:             # check if the mouse is on the bottom side of the board
                    piece_locs[current][1] = height*0.805
            elif clicked == False:
                clicked = True
                loc = 'a7x'
                for k in [word for word in fields.keys() if word.endswith("x")]:
                    if round(piece_locs[current][0], 2) == round(fields[k], 2) and round(piece_locs[current][1], 2) == round(fields[k[:-1] + 'y'], 2):
                        loc = k
                reach = 1
                getAttackingPieces(loc, reach)
                dices = []
                
                if turn == 1:
                    colour = 'red'
                elif turn == 2:
                    colour = 'green'
                elif turn == 3:
                    colour = 'blue'
                else:
                    colour = 'yellow'
                    
                if turn == 1:
                    team_colour = 'green'
                elif turn == 2:
                    team_colour = 'red'
                elif turn == 3:
                    team_colour = 'yellow'
                else:
                    team_colour = 'blue'
                    
                if piece_locs[current][4] == team_colour and pCount == 4:
                    return
                
                for field in valid_locs:
                    for piece in piece_locs:
                        if round(piece[0], 2) == round(fields[field + 'x'], 2) and round(piece[1], 2) == round(fields[field + 'y'], 2):
                            pCount = n_sys.update_t_dis()['pCount']
                            if piece[4] == colour or (pCount == 4 and piece[4] == team_colour):
                                if piece[3] == 's':
                                    dices.append('d6')
                                if piece[3] == 'c':
                                    dices.append('d4')
                                if piece[3] == 't':
                                    dices.append('d10')
                print(dices)
                if len(dices) != 0:
                    plays -= 1
                    d_sys.newBattle(dices,images)
                    #hier kan je je functie callen
                        

# mouseReleased() imported from main
def mouseReleased_():
    global piece_loc, mouse_down, current, fields, backupx, backupy, valid_locs, choosing, plays, clicked
    
    clicked = False
    
    # returns if the player is choosing
    if choosing == True:
        return
    
    # piece placement system
    if mouse_down == True:
        mouse_down = False
        
        # finds the nearset location to place piece in
        saved = width
        loc = 'a7x'
        for k in [word for word in fields.keys() if word.endswith("x")]:
            distance = sqrt((fields[k] - mouseX)**2 + (fields[k[:-1] + 'y'] - mouseY)**2)
            if distance < saved:
                saved = distance
                loc = k
                
        # checks if location is valid
        if loc[:-1] in valid_locs:
            piece_locs[current][0] = fields[loc]
            piece_locs[current][1] = fields[loc[:-1] + 'y']
        else:
            piece_locs[current][0] = backupx
            piece_locs[current][1] = backupy
        if round(piece_locs[current][0], 2) != round(backupx, 2) or round(piece_locs[current][1], 2) != round(backupy, 2):
            plays -= 1

def gridify(loc):
    column = loc[:-1]
    row = int(loc[1:])
    if column == 'a' or column == 'c' or column == 'e' or column == 'g' or column == 'i':
        row += 0.5
    return [column, row]

# validate movement
def checkMovement(loc, reach = 1, inverse = False):
    if reach > 0:
        column = loc[0]
        row = loc[1]
        #up/down
        checkIfValid(reach, column + str(int(row + 1)),inverse)
        checkIfValid(reach, column + str(int(row - 1)),inverse)
        #left/right
        if column == 'a':
            checkIfValid(reach, 'b' + str(int(row + 0.5)),inverse)
            checkIfValid(reach, 'b' + str(int(row - 0.5)),inverse)
        elif column == 'b':
            checkIfValid(reach, 'a' + str(int(row + 0.5)),inverse)
            checkIfValid(reach, 'a' + str(int(row - 0.5)),inverse)
            checkIfValid(reach, 'c' + str(int(row + 0.5)),inverse)
            checkIfValid(reach, 'c' + str(int(row - 0.5)),inverse)
        elif column == 'c':
            checkIfValid(reach, 'b' + str(int(row + 0.5)),inverse)
            checkIfValid(reach, 'b' + str(int(row - 0.5)),inverse)
            checkIfValid(reach, 'd' + str(int(row + 0.5)),inverse)
            checkIfValid(reach, 'd' + str(int(row - 0.5)),inverse)
        elif column == 'd':
            checkIfValid(reach, 'c' + str(int(row + 0.5)),inverse)
            checkIfValid(reach, 'c' + str(int(row - 0.5)),inverse)
            checkIfValid(reach, 'e' + str(int(row + 0.5)),inverse)
            checkIfValid(reach, 'e' + str(int(row - 0.5)),inverse)
        elif column == 'e':
            checkIfValid(reach, 'd' + str(int(row + 0.5)),inverse)
            checkIfValid(reach, 'd' + str(int(row - 0.5)),inverse)
            checkIfValid(reach, 'f' + str(int(row + 0.5)),inverse)
            checkIfValid(reach, 'f' + str(int(row - 0.5)),inverse)
        elif column == 'f':
            checkIfValid(reach, 'e' + str(int(row + 0.5)),inverse)
            checkIfValid(reach, 'e' + str(int(row - 0.5)),inverse)
            checkIfValid(reach, 'g' + str(int(row + 0.5)),inverse)
            checkIfValid(reach, 'g' + str(int(row - 0.5)),inverse)
        elif column == 'g':
            checkIfValid(reach, 'f' + str(int(row + 0.5)),inverse)
            checkIfValid(reach, 'f' + str(int(row - 0.5)),inverse)
            checkIfValid(reach, 'h' + str(int(row + 0.5)),inverse)
            checkIfValid(reach, 'h' + str(int(row - 0.5)),inverse)
        elif column == 'h':
            checkIfValid(reach, 'g' + str(int(row + 0.5)),inverse)
            checkIfValid(reach, 'g' + str(int(row - 0.5)),inverse)
            checkIfValid(reach, 'i' + str(int(row + 0.5)),inverse)
            checkIfValid(reach, 'i' + str(int(row - 0.5)),inverse)
        elif column == 'i':
            checkIfValid(reach, 'h' + str(int(row + 0.5)),inverse)
            checkIfValid(reach, 'h' + str(int(row - 0.5)),inverse)

def checkIfValid(reach, loc, inverse):
    global valid_locs
    if loc in field_names:
        result = True
        for piece in piece_locs:
            if round(piece[0], 2) == round(fields[loc + 'x'], 2) and round(piece[1], 2) == round(fields[loc + 'y'], 2):
                result = False
        if inverse == True:
            result = not result
        if result == True:
            if not loc in valid_locs:
                valid_locs.append(loc)
            newloc = gridify(loc)
            checkMovement(newloc, reach - 1)

# creates the field
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
