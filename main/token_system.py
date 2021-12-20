import nameinput_system as n_sys
import functions as f

modeSpecs = n_sys.update_t_dis()['modeSpecs']
tokenbegin_count = modeSpecs['tokens']
tokens_add = 3
tokens = {
'tokensP1': 0,
'tokensP2': 5,
'tokensP3': 10,
'tokensP4': 15
}
def token_teller(turn,textX1,textY2,boxed = False,X1=0,Y1=0,X2=0,Y2=0):
    if boxed:
        rect(X1,Y1,X2,Y2,10)
    text('tokens:' + str(tokens['tokensP' + str(turn)]),textX1,textY2)
    
def tokens(turn):
    return tokens['tokensP' + str(turn)]

        
def tokens_remove:
def tokens_add:
    
    
