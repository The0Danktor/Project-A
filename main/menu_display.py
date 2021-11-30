import functions as f

# menu background image loader
def loadScreen(images):
    image(images['menu_img'], 0, 0, width, height)

# menu display function [displays the menu screen]
def displayScreen():
    f.textBox(0.25*width, 0.1*height, 0.5*width, 0.1*height, 'Start Game', 75, 255)
    f.textBox(0.25*width, 0.25*height, 0.5*width, 0.1*height, 'Settings', 75, 255)
    f.textBox(0.25*width, 0.4*height, 0.5*width, 0.1*height, 'Exit Game', 75, 255)

# button click system
def mousePressed_():
    if (0.75*width > mouseX > 0.25*width) and (0.2*height > mouseY > 0.1*height):
        return 5
    elif (0.75*width > mouseX > 0.25*width) and (0.35*height > mouseY > 0.25*height):
        return 0
    elif (0.75*width > mouseX > 0.25*width) and (0.5*height > mouseY > 0.4*height):
        exit()
    
    return 0
