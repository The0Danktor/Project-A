import functions as f

# esc display function [displays the esc screen]
def displayScreen():
    stroke(255)
    strokeWeight(7)
    f.textBox(width*0.1, height*0.4, width*0.2, height*0.2, 'EXIT', 200, 0)
    f.textBox(width*0.4, height*0.4, width*0.2, height*0.2, 'MENU', 200, 0)
    f.textBox(width*0.7, height*0.4, width*0.2, height*0.2, 'CONT', 200, 0)
    noStroke()
    
# button click system
def mousePressed_():
    if width*0.1 < mouseX < width*0.3 and height*0.4 < mouseY < height*0.6:
        exit()
    elif width*0.4 < mouseX < width*0.6 and height*0.4 < mouseY < height*0.6:
        return 0
    elif width*0.7 < mouseX < width*0.9 and height*0.4 < mouseY < height*0.6:
        return -1
    return 7
