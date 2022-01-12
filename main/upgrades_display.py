import functions as f
import token_system as t_sys
import game_system as g_sys

eco = {
    'ecoP1': 0,
    'ecoP2': 0,
    'ecoP3': 0,
    'ecoP4': 0
    }
ecoPrice = {
    'ecolvl0': 5,
    'ecolvl1': 8,
    'ecolvl2': 12
    }
generaal = {
    'generaalP1': 0,
    'generaalP2': 0,
    'generaalP3': 0,
    'generaalP4': 0
    }
generaalPrice = {
    'generaallvl0': 6,
    'generaallvl1': 12
    }
artillerie = {
    'artillerieP1': 0,
    'artillerieP2': 0,
    'artillerieP3': 0,
    'artillerieP4': 0
    }
artilleriePrice = {
    'artillerielvl0': 10,
    'artillerielvl1': 12
    }
    
def displayScreen(turn,images):
    fill(50)
    stroke(0)
    strokeWeight(7)
    rect(width*0.15, height*0.175, width*0.7, height*0.65, 20)
    
    fill(150)
    if eco['ecoP' + str(turn)] == 0:
        image(images['eco_lvl1'], width*0.2, height*0.2, width*0.12, height*0.45)
    elif eco['ecoP' + str(turn)] == 1:
        image(images['eco_lvl2'], width*0.2, height*0.2, width*0.12, height*0.45) 
    elif eco['ecoP' + str(turn)] == 2:
        image(images['eco_lvl3'], width*0.2, height*0.2, width*0.12, height*0.45)
    else:
        image(images['eco_lvl3'], width*0.2, height*0.2, width*0.12, height*0.45)
        noStroke()
        fill(0,175)
        rect(width*0.199, height*0.2, width*0.121, height*0.45)
        stroke(0)
        strokeWeight(7)
        fill(150) 
        
    if eco['ecoP' + str(turn)] < 3:
        f.textBox(width*0.2, height*0.680, width*0.12, height*0.08, 'upgrade', 200, 0)
    else:
        f.textBox(width*0.2, height*0.680, width*0.12, height*0.08, 'max', 200, 0)
    
    if generaal['generaalP' + str(turn)] == 0:
        image(images['generaal_lvl1'], width*0.44, height*0.2, width*0.12, height*0.45)
    elif generaal['generaalP' + str(turn)] == 1:
        image(images['generaal_lvl2'], width*0.44, height*0.2, width*0.12, height*0.45) 
    else:
        image(images['generaal_lvl2'], width*0.44, height*0.2, width*0.12, height*0.45)
        noStroke()
        fill(0,175)
        rect(width*0.439, height*0.2, width*0.121, height*0.45)
        stroke(0)
        strokeWeight(7)
        fill(150) 
    
    if generaal['generaalP' + str(turn)] < 2:
        f.textBox(width*0.44, height*0.680, width*0.12, height*0.08, 'upgrade', 200, 0)
    else:
        f.textBox(width*0.44, height*0.680, width*0.12, height*0.08, 'max', 200, 0)
        
    if artillerie['artillerieP' + str(turn)] == 0:
        image(images['art_lvl1'], width*0.68, height*0.2, width*0.12, height*0.45)
    elif artillerie['artillerieP' + str(turn)] == 1:
        image(images['art_lvl2'], width*0.68, height*0.2, width*0.12, height*0.45)
    else:
        image(images['art_lvl2'], width*0.68, height*0.2, width*0.12, height*0.45)
        noStroke()
        fill(0,175)
        rect(width*0.679, height*0.2, width*0.121, height*0.45)
        stroke(0)
        strokeWeight(7)
        fill(150)
    
    if artillerie['artillerieP' + str(turn)] < 2:
        f.textBox(width*0.68, height*0.680, width*0.12, height*0.08, 'upgrade', 200, 0)
    else:
        f.textBox(width*0.68, height*0.680, width*0.12, height*0.08, 'max', 200, 0)

    
def upgrade_refresh():
    global eco,generaal,artillerie
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
def get_eco(turn):
    global eco
    return eco['ecoP' + str(turn)]

def get_generaal(turn):
    global generaal
    return generaal['generaalP' + str(turn)]
            
def get_artillerie(turn):
    global artillerie
    return artillerie['artillerieP' + str(turn)]
        
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
    (width*0.15, height*0.175, width*0.7, height*0.65, 20)
    if not(width*0.15 < mouseX < width*0.85 and height*0.175 < mouseY < height*0.825):
        return 8
    if eco['ecoP' + str(turn)] < 3:
        if width*0.2 < mouseX < width*0.32 and height*0.680 < mouseY < height*0.760 and t_sys.get_tokens(turn) >= ecoPrice['ecolvl'+ str(eco['ecoP'+ str(turn)])]:
            t_sys.tokens_remove(turn, ecoPrice['ecolvl'+ str(eco['ecoP'+ str(turn)])])
            upgrade_eco(turn)
    
    if generaal['generaalP' + str(turn)] < 2:
        if width*0.44 < mouseX < width*0.56 and height*0.680 < mouseY < height*0.760 and t_sys.get_tokens(turn) >= generaalPrice['generaallvl'+ str(generaal['generaalP'+ str(turn)])]:
            t_sys.tokens_remove(turn, generaalPrice['generaallvl'+ str(generaal['generaalP'+ str(turn)])])
            upgrade_generaal(turn)
    
    if artillerie['artillerieP' + str(turn)] < 2:
        if width*0.68 < mouseX < width*0.80 and height*0.680 < mouseY < height*0.760 and t_sys.get_tokens(turn) >= artilleriePrice['artillerielvl'+ str(artillerie['artillerieP'+ str(turn)])]:
            t_sys.tokens_remove(turn, artilleriePrice['artillerielvl'+ str(artillerie['artillerieP'+ str(turn)])])
            upgrade_artillerie(turn)
    return 12
