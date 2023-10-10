def berechnung(a):
    ergebnis = 120 % 10
    a = a % 10
    ergebnis = 14 % 3
    
    # Überprüfung, ob a nicht gleich 0 ist, bevor du a % a ausführst
    if a != 0:
        a = a % a
    
    ergebnis = 61 % 17
    a = a * a
    ergebnis = 243 % 13
    
    # Überprüfung, ob a nicht gleich 0 ist, bevor du a -= a / a ausführst
    if a != 0:
        a -= a / a
    
    ergebnis = 4 % 5
    a += a + a
    ergebnis = 5 % 4
    a += a * a + a
    ergebnis = -5 % 4
    a = a + a * 3 + a
    ergebnis = -5 % -4
    
    # Überprüfung, ob a nicht gleich 0 ist, bevor du a = (a - 1) / 2 + 7 ausführst
    if a != 0:
        a = (a - 1) / 2 + 7
    
    ergebnis = 5 % -4
    a -= a - a * 4 / 2 + a * a - 99
    
    return a

# Testen der Funktion mit einem beliebigen Startwert für a
startwert_a = 10
ergebnis = berechnung(startwert_a)
print("Ergebnis:", ergebnis)
