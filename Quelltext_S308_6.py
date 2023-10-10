import math

try:
    i = 0
    zahl = int(input("Geben Sie eine Zahl ein: "))
    
    while i < zahl:
        if i % 2 == 0 and i > 10:
            wert = math.sqrt(i)
            print("Die Wurzel von " + str(i) + " ist: " + str(wert))
        else:
            wert = math.pow(i, 2)
            print("Das Quadrat von " + str(i) + " ist: " + str(wert))
        
        i = i + 1

except Exception as e:
    print("Es ist folgender Fehler aufgetreten: \n" + str(e))
