import webbrowser



def displayScreen(images,mousePressed,ruleweb):
    button(images,mousePressed,ruleweb)
    

def button(images,mousePressed,ruleweb):
    image(images['rules_b_img'],0,height-40,40,40)
    if mousePressed and mouseX < 40 and mouseY > height - 40:
        openrules(ruleweb)
def openrules(ruleweb):
    webbrowser.open_new(ruleweb)
    
