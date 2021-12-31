import nameinput_system as n_sys
import functions as f
import game_system as g_sys

tokens_eco = 3
tokens = {}
pelotons = {}
autos = {}
tanks = {}

def tokenbegin_Refresh():
    global tokens, pelotons, autos, tanks
    modeSpecs = n_sys.update_t_dis() ['modeSpecs']
    g_sys.createPieces()

    tokens = {
    'tokensP1': modeSpecs['tokens'],
    'tokensP2': modeSpecs['tokens'],
    'tokensP3': modeSpecs['tokens'],
    'tokensP4': modeSpecs['tokens']
    }
    pelotons = {
    'pelotonsP1': modeSpecs['pelotons'],
    'pelotonsP2': modeSpecs['pelotons'],
    'pelotonsP3': modeSpecs['pelotons'],
    'pelotonsP4': modeSpecs['pelotons']
    }
    autos = {
    'autosP1': modeSpecs['autos'],
    'autosP2': modeSpecs['autos'],
    'autosP3': modeSpecs['autos'],
    'autosP4': modeSpecs['autos']
    }
    tanks = {
    'tanksP1': modeSpecs['tanks'],
    'tanksP2': modeSpecs['tanks'],
    'tanksP3': modeSpecs['tanks'],
    'tanksP4': modeSpecs['tanks']
    }


def token_teller(turn,textX1,textY2,boxed = False,X1=0,Y1=0,X2=0,Y2=0):
    if boxed:
        rect(X1,Y1,X2,Y2,10)
    text('tokens:' + str(tokens['tokensP' + str(turn)]),textX1,textY2)
    
# request information
def get_tokens(turn):
    player_tokens = tokens['tokensP' + str(turn)]
    return player_tokens

def get_pelotons(turn):
    player_pelotons = pelotons['pelotonsP' + str(turn)]
    return player_pelotons

def get_autos(turn):
    player_autos = autos['autosP' + str(turn)]
    return player_autos

def get_tanks(turn):
    player_tanks = tanks['tanksP' + str(turn)]
    return player_tanks

# modify information
def token_per_turn(turn):
    global tokens
    tokens['tokensP' + str(turn)] += calculateIncome(turn)
    
# token bonus for having a piece on the opposite side
def calculateIncome(turn):
    income = 0
    piece_locs = g_sys.getPieces()
    fields = g_sys.getFields()
    pCount = n_sys.update_t_dis()['pCount']
    if turn == 1:
        colour = 'red'
    elif turn == 2:
        colour = 'green'
    elif turn == 3:
        colour = 'blue'
    else:
        colour = 'yellow'
    
    if (pCount == 2 and turn == 1) or (pCount == 4 and (turn == 1 or turn == 2)):
        locs = ['b1', 'd1', 'f1', 'h1']
    else:
        locs = ['b8', 'd8', 'f8', 'h8']
    
    for field in locs:
        result = False
        for piece in piece_locs:
            if piece[4] == colour:
                if round(piece[0], 2) == round(fields[field + 'x'], 2) and round(piece[1], 2) == round(fields[field + 'y'], 2):
                    result = True
                    saved_piece = piece
        if result == True:
            piece = saved_piece
            if piece[3] == 's':
                income += 2
            elif piece[3] == 'c':
                income += 3
            elif piece[3] == 't':
                income += 4
    return income + tokens_eco
                
def tokens_remove(turn, amount):
    global tokens
    tokens['tokensP' + str(turn)] -= amount

def tokens_add(turn, amount):
    global tokens
    tokens['tokensP' + str(turn)] += amount
    
def pelotons_remove(turn, amount=1):
    global pelotons
    pelotons['pelotonsP' + str(turn)] -= amount
    
def autos_remove(turn, amount=1):
    global autos
    autos['autosP' + str(turn)] -= amount
    
def tanks_remove(turn, amount=1):
    global tanks
    tanks['tanksP' + str(turn)] -= amount
    
    
