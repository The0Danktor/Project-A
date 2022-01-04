eco = {
    'ecoP1': 1,
    'ecoP2': 1,
    'ecoP3': 1,
    'ecoP4': 1
    }
generaal = {
    'generaalP1': 1,
    'generaalP2': 1,
    'generaalP3': 1,
    'generaalP4': 1
    }
artillerie = {
    'artillerielP1': 1,
    'artillerieP2': 1,
    'artillerieP3': 1,
    'artillerieP4': 1
    }

    
def displayScreen():
    fill(50)
    stroke(0)
    strokeWeight(7)
    rect(width*0.275, height*0.375, width*0.05, height*0.25, 20)

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
    eco['ecoP' + str(turn)] += 1
    
def upgrade_generaal(turn):
    global generaal
    generaal['generaalP' + str(turn)] += 1
    
def upgrade_artillerie(turn):
    global artillerie
    artillerie['artillerieP' + str(turn)] += 1
