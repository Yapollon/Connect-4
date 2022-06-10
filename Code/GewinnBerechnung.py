# 6.5.22
# Jan & Luis
# Task Gewinnberechnung

"""
überprüfte die auf horizontaler Ebene aneinander liegende Steine, welche die gleiche Farbe haben.
wenn es mindestens 4 in einer Reihe sind, wird True zurückgegeben, ansonsten False
"""


def horizontal(spieler, liste, posi):
    # Anzahl an Steinen, der gleichen Farbe, die aneinander liegen
    anzahl = 0
    # koordinaten von der reihe die gewinnt.
    gewinn = []
    
    # die x und y Werte stehen für die aktuell Position, die gerade überprüft wird
    x = posi[0]  # die x Coordinate
    y = posi[1]  # die y Coordinate
    
    # nach rechts
    while liste[x, y].status == spieler:
        anzahl += 1
        gewinn.append(liste[x, y])
        
        x += 1
        if x > 7:  # überprüft, ob es im Feld liegt
            break
    
    # nach links
    x = posi[0] - 1
    if x > 0:  # im Feld?
        while liste[x, y].status == spieler:
            anzahl += 1
            gewinn.append(liste[x, y])
            
            x -= 1
            if x < 1:
                break
    
    return anzahl >= 4, gewinn


def vertikal(spieler, liste, posi):
    # Anzahl an Steinen, der gleichen Farbe, die aneinander liegen
    anzahl = 0
    gewinn = []
    
    # die x und y Werte stehen für die aktuell Position, die gerade überprüft wird
    x = posi[0]  # die x Coordinate
    y = posi[1]  # die y Coordinate
    
    # nach rechts
    while liste[x, y].status == spieler:
        anzahl += 1
        gewinn.append(liste[x, y])
        
        y += 1
        if y > 6:  # überprüft, ob es im Feld liegt
            break
    
    # nach links
    y = posi[1] - 1
    if y > 0:  # im Feld?
        while liste[x, y].status == spieler:
            anzahl += 1
            gewinn.append(liste[x, y])
            
            y -= 1
            if y < 1:
                break
    
    return anzahl >= 4, gewinn


def diagonal_links(spieler, liste, posi):
    # Anzahl an Steinen, der gleichen Farbe, die aneinander liegen
    anzahl = 0
    gewinn = []
    
    # die x und y Werte stehen für die aktuell Position, die gerade überprüft wird
    x = posi[0]  # die x Coordinate
    y = posi[1]  # die y Coordinate
    
    # nach oben
    while liste[x, y].status == spieler:
        anzahl += 1
        gewinn.append(liste[x, y])
        
        y += 1
        x -= 1
        if y > 6 or x < 1:  # überprüft, ob es im Feld liegt
            break
    
    # nach unten
    x = posi[0] + 1 
    y = posi[1] - 1
    if y >= 1 and x <= 7:  # im Feld?
        while liste[x, y].status == spieler:
            anzahl += 1
            gewinn.append(liste[x, y])
            
            y -= 1
            x += 1
            if y < 1 or x > 7:
                break
    
    return anzahl >= 4, gewinn


def diagonal_rechts(spieler, liste, posi):
    # Anzahl an Steinen, der gleichen Farbe, die aneinander liegen
    anzahl = 0
    gewinn = []
    
    # die x und y Werte stehen für die aktuell Position, die gerade überprüft wird
    x = posi[0]  # die x Coordinate
    y = posi[1]  # die y Coordinate
    
    # nach oben
    while liste[x, y].status == spieler:
        anzahl += 1
        gewinn.append(liste[x, y])
        
        y += 1
        x += 1
        if y > 6 or x > 7:  # überprüft, ob es im Feld liegt
            break
    
    # nach unten
    x = posi[0] - 1 
    y = posi[1] - 1
    
    if y >= 1 and x >= 1:  # im Feld?
        while liste[x, y].status == spieler:
            anzahl += 1
            gewinn.append(liste[x, y])
            
            y -= 1
            x -= 1
            if y < 1 or x < 1:
                break
    
    return anzahl >= 4, gewinn


def gewinn_berechnen(liste, posi):
    
    # die Zahl die für den Spieler steht (1 oder 2)
    spieler = liste[posi[0], posi[1]].status
    #print(spieler)
    h = horizontal(spieler, liste, posi)
    v = vertikal(spieler, liste, posi)
    dl = diagonal_links(spieler, liste, posi)
    dr = diagonal_rechts(spieler, liste, posi)
    
    if h[0]:
        return h[1]
    elif v[0]:
        return v[1]
    elif dl[0]:
        return dl[1]
    elif dr[0]:
        return dr[1]
    else:
        return None


if __name__ == "__main__":
    from Slot import Slot

    # feld wird Erstellt
    xWidth = 7
    yHeight = 6
        
    slots = {}
        
    for x in range(1, (xWidth + 1)):
        for y in range(1, (yHeight + 1)):
            slots[x, y] = Slot((x, y), 1)
    
    # es werden Objekte angegeben, weil Leon die einzelnen Positionen mit der Klasse Slots initialisiert
    print(gewinn_berechnen(slots, (7, 3)))
