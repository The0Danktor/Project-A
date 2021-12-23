import nameinput_system as n_sys
import functions as f

modeSpecs = n_sys.update_t_dis()['modeSpecs']
tokenbegin_count = modeSpecs['tokens']
tokens_eco = 3
tokens = {
'tokensP1': tokenbegin_count,
'tokensP2': tokenbegin_count,
'tokensP3': tokenbegin_count,
'tokensP4': tokenbegin_count
}
def tokenbegin_Refresh():
    global tokenbegin_count,tokens
    modeSpecs = n_sys.update_t_dis() ['modeSpecs']
    tokenbegin_count = modeSpecs['tokens']
    tokens = {
    'tokensP1': tokenbegin_count,
    'tokensP2': tokenbegin_count,
    'tokensP3': tokenbegin_count,
    'tokensP4': tokenbegin_count
    }
    print(tokenbegin_count)
def token_teller(turn,textX1,textY2,boxed = False,X1=0,Y1=0,X2=0,Y2=0):
    if boxed:
        rect(X1,Y1,X2,Y2,10)
    text('tokens:' + str(tokens['tokensP' + str(turn)]),textX1,textY2)
    
def get_tokens(turn):
    player_tokens = tokens['tokensP' + str(turn)]
    return player_tokens

def token_per_turn(turn):
    global tokens
    tokens['tokensP' + str(turn)] += tokens_eco
                
def tokens_remove(amount):
    global tokens
    tokens['tokensP' + str(turn)] -= amount

def tokens_add(turn):
    global tokens
    tokens['tokensP' + str(turn)] += amount
    
    
