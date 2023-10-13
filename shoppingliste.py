import sqlite3

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('shopping_list.db')
cursor = conn.cursor()

# Tabelle erstellen, wenn sie nicht existiert
cursor.execute('''
    CREATE TABLE IF NOT EXISTS shopping_list (
        id INTEGER PRIMARY KEY,
        item TEXT
    )
''')
conn.commit()

# Initialisierung der Einkaufsliste
shopping_list = []

# Funktion zur Aktualisierung der Anzeige der Einkaufsliste
def aktualisiere_anzeige():
    cursor.execute('SELECT * FROM shopping_list')
    rows = cursor.fetchall()
    print("Inhalt der Einkaufsliste: \n")
    for row in rows:
        print("[" + str(row[0]) + "]", row[1])

# Funktion zur Aktualisierung der Anzeige der Einkaufsliste
def aktualisiere_anzeige():
    cursor.execute('SELECT * FROM shopping_list')
    rows = cursor.fetchall()
    print("Inhalt der Einkaufsliste: \n")
    for row in rows:
        print("[" + str(row[0]) + "]", row[1])

# Funktionsdeklarationen

def hinzufügen_artikel(article):
    '''Artikel zur Einkaufsliste hinzufügen und in die Datenbank einfügen'''
    shopping_list.append(article)
    cursor.execute('INSERT INTO shopping_list (item) VALUES (?)', (article,))
    conn.commit()

def frag_nutzer_ob_artikel_hinzuzufügen():
    '''Benutzer nach einem Artikel fragen und diesen zur Einkaufsliste hinzufügen'''
    article = input("Bitte einen Artikel eingeben, der der Einkaufsliste hinzugefügt werden soll: ")
    hinzufügen_artikel(article)

def entfern_artikel_aus_liste(index):
    cursor.execute('SELECT * FROM shopping_list')
    rows = cursor.fetchall()
    if 1 <= index + 1 <= len(rows):
        cursor.execute('DELETE FROM shopping_list WHERE id = ?', (index + 1,))
        conn.commit()
    else:
        print("\nERROR: Unter dem angegebenen Index ist kein Artikel in der Liste zu finden")

# Benutzerinteraktion - Logik des Skripts

print("--- Dies ist eine einfache Einkaufsliste ---\n")

menu_txt = """
Was möchtest du machen:

      [1] Artikel hinzufügen
      [2] Shopping Liste anzeigen
      [3] Artikel entfernen
      ---------------------
      [4] Programm beenden
"""

while True:
    user_input = input(menu_txt + "\n")
    if user_input == '1':
        frag_nutzer_ob_artikel_hinzuzufügen()
    elif user_input == '2':
        aktualisiere_anzeige()
    elif user_input == '3':
        article_index = input("Bitte den Index des Artikels eingeben, der aus der Einkaufsliste entfernt werden soll: ")
        try:
            entfern_artikel_aus_liste(int(article_index) - 1)
        except ValueError:
            print("\nERROR: Bitte einen passenden Index als Ziffer angeben")
    elif user_input == '4':
        conn.close()
        exit(0)  # Erfolgreich beendet
    else:
        print("Ungültige Eingabe")
