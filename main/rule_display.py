#import webbrowser



# def displayScreen(images,mousePressed,ruleweb):
#     button(images,mousePressed,ruleweb)
    

# def button(images,mousePressed,ruleweb):
#     image(images['rules_b_img'],0,height-40,40,40)
#     if mousePressed and mouseX < 40 and mouseY > height - 40:
#         openrules(ruleweb)
# def openrules(ruleweb):
#     webbrowser.open_new(ruleweb)


import functions as f

backup = 0
page = 1

def displayScreen(images):
    global page
    image(images['rule_page_' + str(page + 0)], width*0.01, height*0.01, width*0.48, height*0.98)
    if page != 7:
        image(images['rule_page_' + str(page + 1)], width*0.51, height*0.01, width*0.48, height*0.98)
    else:
        fill(255)
        rect(width*0.52, height*0.02, width*0.46, height*0.96)
    
    image(images['close_img'],width*0.01, height*0.94, width*0.03, height*0.05)
    
    if page != 1:
        image(images['back_img'],width*0.03, height*0.84, width*0.03, height*0.05)
    if page != 6:
        image(images['forward_img'],width*0.94, height*0.84, width*0.03, height*0.05)

def mousePressed_():
    global page
    if width*0.03 < mouseX < width*0.06 and height*0.84 < mouseY < height*0.89 and page > 1:
        page -= 2
            
    if width*0.94 < mouseX < width*0.97 and height*0.84 < mouseY < height*0.89 and page < 6:
        page += 2
    
    if width*0.01 < mouseX < width*0.04 and height-height*0.06 < mouseY < height-height*0.01:
        return backup
    return 11
    
def setBackup(state):
    global backup, page
    backup = state
    page = 1
