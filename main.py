"""
main.py: čtvrtý projekt do Engeto Online Python Akademie - jednoduchý Task manager.

author: Jan Bláha
email: jan.blaha@bcas.cz
"""

def hlavni_menu():
    print("\nSprávce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Ukončit program")

def pridat_ukol():
    nazev = input("Zadejte název úkolu: ")
    popis = input("Zadejte popis úkolu: ")
    ukoly.append({"nazev": nazev, "popis": popis})
    print(f"Úkol '{nazev}' byl přidán.")

def zobrazit_ukoly():
    print("\nSeznam úkolů:")
    if not ukoly:
        print("Žádné úkoly k zobrazení.")
    for i, ukol in enumerate(ukoly, 1):
        print(f"{i}. {ukol['nazev']} - {ukol['popis']}")

def odstranit_ukol():
    zobrazit_ukoly()
    if not ukoly:
        print("Žádné úkoly k odstranění.")
        return
    try:
        index = int(input("Zadejte číslo úkolu, který chcete odstranit: ")) - 1
        if 0 <= index < len(ukoly):
            odstraneny_ukol = ukoly.pop(index)
            print(f"Úkol '{odstraneny_ukol['nazev']}' byl odstraněn.")
        else:
            print("Neplatné číslo úkolu.")
    except ValueError:
        print(f"Prosím zadejte platné celé číslo v intervalu 1 až {len(ukoly)}.")

def main():
    print("Vítejte v programu Task manager.")

    while True:
        hlavni_menu()
        volba = input("Vyberte možnost (1-4): ")

        if volba == '1':
            pridat_ukol()
        elif volba == '2':
            zobrazit_ukoly()
        elif volba == '3':
            odstranit_ukol()
        elif volba == '4':
            print("\nKonec programu.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")  

ukoly = []

main()