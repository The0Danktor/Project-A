import functions as f
import token_system as t_sys

eco = {
    'ecoP1': 0,
    'ecoP2': 0,
    'ecoP3': 0,
    'ecoP4': 0
    }
generaal = {
    'generaalP1': 0,
    'generaalP2': 0,
    'generaalP3': 0,
    'generaalP4': 0
    }
artillerie = {
    'artillerieP1': 0,
    'artillerieP2': 0,
    'artillerieP3': 0,
    'artillerieP4': 0
    }

    
def displayScreen(turn):
    print(eco['ecoP' + str(turn)],generaal['generaalP' + str(turn)],artillerie['artillerieP' + str(turn)])
    fill(50)
    stroke(0)
    strokeWeight(7)
    rect(width*0.15, height*0.175, width*0.7, height*0.65, 20)
    
    fill(150)
    if eco['ecoP' + str(turn)] < 3:
        f.textBox(width*0.2, height*0.680, width*0.12, height*0.08, 'upgrade', 200, 0)
    else:
        f.textBox(width*0.2, height*0.680, width*0.12, height*0.08, 'max', 200, 0)
    
    if generaal['generaalP' + str(turn)] < 2:
        f.textBox(width*0.44, height*0.680, width*0.12, height*0.08, 'upgrade', 200, 0)
    else:
        f.textBox(width*0.44, height*0.680, width*0.12, height*0.08, 'max', 200, 0)
    
    if artillerie['artillerieP' + str(turn)] < 2:
        f.textBox(width*0.68, height*0.680, width*0.12, height*0.08, 'upgrade', 200, 0)
    else:
        f.textBox(width*0.68, height*0.680, width*0.12, height*0.08, 'max', 200, 0)
    
def get_eco(turn):
    global eco
    return eco

def get_generaal(turn):
    global generaal
    return generaal
            
def get_artillerie(turn):
    global artillerie
    return artillerie
        
def upgrade_eco(turn):
    global eco
    if eco['ecoP' + str(turn)] < 3:
        eco['ecoP' + str(turn)] += 1
    
    if eco['ecoP' + str(turn)] == 1:
        t_sys.tokens_upgrade(turn,4)
    if eco['ecoP' + str(turn)] == 2:
        t_sys.tokens_upgrade(turn,5)
    if eco['ecoP' + str(turn)] == 3:
        t_sys.tokens_upgrade(turn,6)
        
    
def upgrade_generaal(turn):
    global generaal
    generaal['generaalP' + str(turn)] += 1
    
def upgrade_artillerie(turn):
    global artillerie
    artillerie['artillerieP' + str(turn)] += 1

def mousePressed_(turn):
    if eco['ecoP' + str(turn)] < 3:
        if width*0.2 < mouseX < width*0.32 and height*0.680 < mouseY < height*0.760:
            upgrade_eco(turn)
    
    if generaal['generaalP' + str(turn)] < 2:
        if width*0.44 < mouseX < width*0.56 and height*0.680 < mouseY < height*0.760:
            upgrade_generaal(turn)
    
    if artillerie['artillerieP' + str(turn)] < 2:
        if width*0.68 < mouseX < width*0.80 and height*0.680 < mouseY < height*0.760:
            upgrade_artillerie(turn)
