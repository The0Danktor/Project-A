# center function [used to center text] {args: center(text to center, maximum width, maximum height)}
def center(txt, maxW, maxH, increase = 0):
    tempSize = 0.1*maxH
    textSize(tempSize)
    while textWidth(txt) > maxW:
        tempSize -= 1
        textSize(tempSize)
    if increase == True:
        tempSize += increase
        textSize(tempSize)
    minW = (width - textWidth(txt)) / 2
    return minW

# simplified center function [used to center text in the middle of the screen] {args: simpleCenter(text to center)
def simpleCenter(txt):
    w = textWidth(txt)
    w = (width - w) // 2
    return w

# text box function [used to display a box with text] {args: textBox(x1, y1, width, height, text to display, color of box, color of text, scalar of font)}
def textBox(rectW1, rectH1, rectW2, rectH2, txt, rectColor = 50, txtColor = 255, scalar = 0.8):
    fill(rectColor)
    rect(rectW1, rectH1, rectW2, rectH2, 10)
    fill(txtColor)
    text(txt, center(txt, rectW2, rectH2) + ((rectW1 + rectW2 / 2) - width*0.5), rectH1 + (rectH2 / 2) + ((textAscent()*scalar + textDescent()*scalar) / 2) - textDescent()*scalar) 
