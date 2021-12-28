import functions as f

saved_state = 0

# menu background image loader
def loadScreen(images):
    image(images['main_img'], 0, 0, width, height)

# # menu display function [displays the menu screen]
# def displayScreen(images):
#     # f.textBox(0.25*width, 0.1*height, 0.5*width, 0.1*height, 'Start Game', 75, 255)
#     # f.textBox(0.25*width, 0.25*height, 0.5*width, 0.1*height, 'Settings', 75, 255)
#     # f.textBox(0.25*width, 0.4*height, 0.5*width, 0.1*height, 'Exit Game', 75, 255)

# # button click system
# def mousePressed_():
#     if (0.75*width > mouseX > 0.25*width) and (0.2*height > mouseY > 0.1*height):
#         return 5
#     elif (0.75*width > mouseX > 0.25*width) and (0.35*height > mouseY > 0.25*height):
#         return 0
#     elif (0.75*width > mouseX > 0.25*width) and (0.5*height > mouseY > 0.4*height):
#         exit()
    
#     return 0

# menu display function [displays the menu screen]
def displayScreen(images):
    fill('#e5f7e4')
    rect(width*0.640, height*0.203, width*0.310, height*0.581)
    if (width*0.665 < mouseX < width*0.910) and (height*0.203 < mouseY < height*0.404):
        #refresh(1, images)
        image(images['start_img'], width*0.655, height*0.203, width*0.265, height*0.201)
        image(images['settings_img'], width*0.650, height*0.401, width*0.290, height*0.198)
        image(images['exit_img'], width*0.684, height*0.585, width*0.208, height*0.189)
    elif (width*0.650 < mouseX < width*0.940) and (height*0.401 < mouseY < height*0.599):
        image(images['start_img'], width*0.665, height*0.213, width*0.245, height*0.181)
        image(images['settings_img'], width*0.640, height*0.391, width*0.310, height*0.218)
        image(images['exit_img'], width*0.684, height*0.585, width*0.208, height*0.189)
        #refresh(2, images)
    elif (width*0.684 < mouseX < width*0.892) and (height*0.575 < mouseY < height*0.784):
        image(images['start_img'], width*0.665, height*0.213, width*0.245, height*0.181)
        image(images['settings_img'], width*0.650, height*0.401, width*0.290, height*0.198)
        image(images['exit_img'], width*0.674, height*0.575, width*0.228, height*0.209)
        #refresh(3, images)
    else:
        image(images['start_img'], width*0.665, height*0.213, width*0.245, height*0.181)
        image(images['settings_img'], width*0.650, height*0.401, width*0.290, height*0.198)
        image(images['exit_img'], width*0.684, height*0.585, width*0.208, height*0.189)
        refresh(0, images)
    
def refresh(state, images):
    global saved_state, cooldown
    if state != saved_state:
        saved_state = state
        loadScreen(images)
        
# button click system
def mousePressed_():
    if (width*0.665 < mouseX < width*0.910) and (height*0.203 < mouseY < height*0.404):
        return 5
    elif (width*0.650 < mouseX < width*0.940) and (height*0.401 < mouseY < height*0.599):
        return 0
    elif (width*0.684 < mouseX < width*0.892) and (height*0.575 < mouseY < height*0.784):
        exit()
    
    return 0
