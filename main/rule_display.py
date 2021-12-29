import webbrowser



def displayScreen(images,mousePressed):
    button(images,mousePressed)
    

def button(images,mousePressed):
    image(images['rules_b_img'],0,height-40,40,40)
    if mousePressed and mouseX < 40 and mouseY > height - 40:
        openrules()
def openrules():
    webbrowser.open_new(r'file:///C:/Users/jamie/Documents/GitHub/Project-A/main/data/Regelboekje%20Duidelijk.pdf')
    
