import nameinput_system as n_sys

modeSpecs = n_sys.update_t_dis()['modeSpecs']
tokenbegin_count = modeSpecs['tokens']
tokens_add = 3
tokens = 0

def test():

    fill(255)
    text(str(tokenbegin_count),100,100)
    text(str(tokens_add),300,300)
