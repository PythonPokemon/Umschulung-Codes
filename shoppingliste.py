# NOTE: Beim Beenden des Skripts wird die Einkaufsliste gelöscht -> später Inhalt in Datei/Datenbank speichern
# 
# Wunschfunktionen:
# - Wie ist das eigentlich mit Gramm bzw. Gewichtsangaben? -> TODO später
# - Einkäufe gruppieren (List in List?)


shopping_list = []

# Funktionsdeklarationen

def hinzufügen_artikel(article): # artikel hinzufügen
    '''Artkel zur Shopping Liste hinzufügen'''
    shopping_list.append(article)


def frag_nutzer_ob_artikel_hinzuzufügen(): # frag nutzer um artikel hinzu
    '''Benutzer nach Artikel fragen und diesen der shopping list hinzufügen'''
    article = input("Bitte einen Artikel eingeben, der der Einkaufsliste hinzugefügt werden soll: ")
    hinzufügen_artikel(article)


def ausgabe_shopping_liste(): #ausgabe shopping liste
    print("Inhalt der Einkaufsliste: \n")
    for index, article in enumerate(shopping_list):
        print("[" + str(index + 1) + "]", article)

# Artikle aus Liste entfernen
# pop() nutzen, da Benutzer später nur Index angeben soll, nicht Namen des Artikels
def entfern_artikel_aus_liste(index):
    shopping_list.pop(index)


def frag_nutzer_ob_artikel_entfernt_werden_soll():
    '''Benutzer nach Artikel fragen und diesen aus der shopping list entfernen'''
    article_index = input("Bitte den Index des Artikels eingeben, der aus der Einkaufsliste entfernt werden soll: ")
    try:
        entfern_artikel_aus_liste(int(article_index) - 1)
    except IndexError:
        print("\nERROR: Unter dem angegebenen Index ist kein Artikel in der Liste zu finden")
    except ValueError:
        print("\nERROR: Bitte einen passenden Index als Ziffer angeben")
    except Exception as e:
        print("\nERROR: Folgender Fehler ist aufgetreten: " + e.args[0])


# Funktionsaufrufe - Logik unseres Skripts

# Benutzer nach Aktion fragen

print("--- Dies ist eine simple aber coole Einkaufsliste ---\n")

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
     ausgabe_shopping_liste()
    elif user_input == '3':
        frag_nutzer_ob_artikel_entfernt_werden_soll()
    elif user_input == '4':
        exit(0)  # erfolgreich beendet
    else:
        print("Ungültige Eingabe")
        # exit(1)  # nicht erfolgreich beendet

print(shopping_list)
# - Gurken
# - Tomaten
# - Bier 
