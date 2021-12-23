# imports for other files
import nameinput_system as n_sys
import functions as f

# nameinput background image loader
def loadScreen(images):
    image(images['background_img'], 0, 0, width, height)

# nameinput display function [displays the nameinput screen]
def displayScreen(player, images):
    typing = n_sys.update_n_dis(player)['typing'] # synchronises variables with nameinput_system
    
    fill(102)
    rect(width*0.3, height*0.4, width*0.4, height*0.2, 25)
    fill(150)
    tempSize = height*0.08
    textSize(tempSize)
    title = "Enter name " + str(player) + ":"
    text(title, f.simpleCenter(title), height*0.41, width*0.4, height*0.2)
    while textWidth(typing) > width*0.38:
        tempSize -= 1
        textSize(tempSize)
    text(typing, f.simpleCenter(typing), height*0.51, width*0.38, height*0.1)
    
