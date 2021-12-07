import random

# setup global variables
player = 0  # stores which player's name is being edited
typing = '' # stores the name that is being edited
chars = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", \
         "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", \
         "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "_"} # stores all allowed characters
pCount = 2  # stores the current setting for amount of players
mode = 1    # stores the current mode
modeSpecs = {
             'speeltijd' : '15m - 30m',
             'tokens'    : 10,
             'pelotons'  : 5,
             'autos'     : 2,
             'tanks'     : 0
}

# key press function, used to register input and apply it to the string
def keyInput(key_):
    global typing, chars
    if len(typing) < 12:     # prevents names that are longer than 12 letters
        if key_ in chars:
            typing += key_   # adds pressed key to the string
        if key_ == ' ':
            typing += '_'    # adds a '_' to the string when space is pressed
    if key_ == BACKSPACE:
        typing = typing[:-1] # removes last digit
    if key_ == DELETE:
        typing = ''          # empties the string

# returns the name being edited
def returnName():
    global typing, player
    if typing != '':
        return typing                  # returns the string containing the name being edited
    else:
        return 'Player ' + str(player) # returns the default name
    
# shuffles the names to be in a random order
def shuffleNames(players):
    global pCount
    values_list = players.values()
    if pCount == 2:
        values_list = values_list[:2]
    values_list_ = []
    
    temp_list = list(values_list)
    for i in temp_list:
        rng = random.randint(0, len(values_list) - 1)
        value = values_list[rng]
        values_list.remove(value)
        values_list_.append(value)
    c = 1
    for i in values_list_:
        players['player'+ str(c)] = i
        c += 1

# forcefully update the string containing the name being edited
def setTyping(txt):
    global typing
    typing = txt

# synchronises variables with nameinput_display
def update_n_dis(player_):
    global typing, player
    player = player_
    ret = {
           'typing' : typing
    }
    return ret

# synchronises variables with title_display and game_display
def update_t_dis():
    global pCount, mode, modeSpecs
    ret = {
           'pCount'    : pCount,
           'mode'      : mode,
           'modeSpecs' : modeSpecs
    }
    return ret

# change player count on request
def playerCount():
    global pCount
    if pCount == 2:
        pCount = 4
    elif pCount == 4:
        pCount = 2
    return pCount

# change mode on request
def changeMode():
    global mode, modeSpecs
    if mode == 3:
        mode = 1
        modeSpecs = {
             'speeltijd' : '15m - 30m',
             'tokens'    : 10,
             'pelotons'  : 5,
             'autos'     : 2,
             'tanks'     : 0
        }
    elif mode == 1:
        mode = 2
        modeSpecs = {
             'speeltijd' : '30m - 60m',
             'tokens'    : 15,
             'pelotons'  : 7,
             'autos'     : 2,
             'tanks'     : 1
        }
    elif mode == 2:
        mode = 3
        modeSpecs = {
             'speeltijd' : '45m - 90m',
             'tokens'    : 15,
             'pelotons'  : 8,
             'autos'     : 4,
             'tanks'     : 2
        }
