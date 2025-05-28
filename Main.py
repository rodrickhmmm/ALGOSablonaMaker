# Importování modulů
import os
import json
import time
from datetime import date

# KONFIGURACE BAREV
# btw ano, vim ze tohle by se dalo jednoduse vyresit importováním nejakeho package s tema barvama uz nakonfigurovanyma ale idc xdd
cervena = "\033[31;49;1m"
zluta = "\033[33;49;1m"
modra = '\033[34;49;1m'
zelena = "\033[32;49;1m"
bila = "\033[0m"


# vymazá vše co je na obrazovce
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# zadání výchozího nastavení
default_settings = {
    "autorprogramu": "default_value",
    "cestaulozeni": "default_value",
    "jednodussimenu": "False"
}

# definuje uložení nastavení
def ulozit_nastaveni():
    nastaveni = {
        "autorprogramu": autorprogramu,
        "cestaulozeni": cestaulozeni,
        "jednodussimenu": jednodussimenu
    }

    with open("settings.json", "w", encoding="utf-8") as file:
        json.dump(nastaveni, file, ensure_ascii=False, indent=4)

# importuje nastavení
def import1():
    global autorprogramu, cestaulozeni, jednodussimenu
    if os.path.exists("settings.json"):
        with open("settings.json", "r", encoding="utf-8") as file:
            try:
                nastaveni = json.load(file)
                autorprogramu = nastaveni.get("autorprogramu", "default_value")
                cestaulozeni = nastaveni.get("cestaulozeni", "default_value")
                jednodussimenu = nastaveni.get("jednodussimenu", "False")
            except json.JSONDecodeError:
                input(cervena + "Soubor settings.json je poškozen, vytvářím výchozí nastavení. Press enter to continue..." + bila)
                with open("settings.json", "w", encoding="utf-8") as file:
                    json.dump(default_settings, file, ensure_ascii=False, indent=4)
                import1()
    else:
        input(cervena + "Nastavení nebylo nalezeno, vytvářím výchozí nastavení. Press enter to continue..." + bila)
        with open("settings.json", "w", encoding="utf-8") as file:
            json.dump(default_settings, file, ensure_ascii=False, indent=4)
        import1()
        clear()


import1()

# credits obrazovka
def credits():
    clear()
    print(bila + "Vytvořil a naprogramoval Rodrick_ (Tomáš Kučera) v roce 2025.")
    print(modra + "https://github.com/rodrickhmmm/ALGOSablonaMaker")
    time.sleep(2)
    main_menu()
# jednodussimenu---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
vybrani = 1

def jednodussi_menu():
    vybratFile = 1
    print(modra + bila + "===", zelena + "ALGO Šablona Maker - Jednoduchý menu", bila + "===")
    
    if vybrani == 1:
        vybratFile == 1
        clear()
    else:
        print(modra + "Vyber, jakou šablonu chceš použít")
        print(zluta + "1 - Počítání")
        print(zluta + "2 - Grafika")
        vybratFile = int(input(bila + "Vyber: " + zelena))
    
        
    if vybratFile == 1:
        clear()
        soubor_cesta = "sablony/Sablona1.txt"
    elif vybratFile == 2:
        clear()
        soubor_cesta = "sablony/SablonaGrafika.txt"
    elif vybratFile == 0:
        global jednodussimenu
        jednodussimenu = "False"
        ulozit_nastaveni()
        clear()
        main_menu()
    else:
        print(cervena + "Jseš debil??? Vyber 1 nebo 2!!!!")
        exit()
        
    # Uživatelský vstup
    today = date.today().strftime('%d-%m-%Y')
    nazevslozky = today
    nadpis = input(zelena + "Název programu v komentáři: " + zelena)
    autor = autorprogramu
    popis = input(zelena + "Popis programu v komentáři: " + zelena)
    lekce = (input(zelena + "Číslo lekce: " + zelena))
    program = (input(zelena + "Číslo programu: " + zelena))
    ulozitSoubor = "L" + lekce + "P" + program + "_" + nadpis + ".py"  # Vytvoření .py souboru
    # Cesta složky
    newpath = os.path.join(cestaulozeni, nazevslozky)


    # Kontrola složky
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        print(zluta + "Složka", newpath, "byla vytvořena.")
    else:
        print(zluta + "Složka", newpath, "již existuje.")

    # Přečtení obsahu šablony
    with open(soubor_cesta, "r", encoding="utf-8") as soubor:
        obsah = soubor.read()

    # Vytvoření hlavičky souboru
    hlavicka = f"""# ===============================
# Program: {nadpis} 
# Autor: {autor}
# Popis: {popis} 
# ===============================


"""

    # Sestavení finálního obsahu
    finalni_obsah = hlavicka + obsah

    # Uložení souboru do složky
    cesta_k_souboru = os.path.join(newpath, ulozitSoubor)
    with open(cesta_k_souboru, "w", encoding="utf-8") as soubor:
        soubor.write(finalni_obsah)

    print(zelena + "Soubor byl úspěšně uložen jako", cesta_k_souboru, ".")



# hlavní menu---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main_menu():
    if jednodussimenu == "True":
        jednodussi_menu()
    elif jednodussimenu == "False":
        print(modra + cervena + "===", modra + "ALGO Šablona Maker", cervena + "===")
        print(modra + "[1]" + bila, "Generátor Šablon")
        print(modra + "[2]" + bila, "Nastavení")
        print(modra + "[3]" + bila, "Credits")
        print(modra + "[4]" + bila, "Exit")

        Choose = int(input(bila + "Vyber: " + zelena))
        
        if Choose >= 5:
            print("Jseš debil?? Vyber 1 - 4!!!!!")
            exit()
        elif Choose == 1:
            clear()
            maker()
        elif Choose == 2:
            clear()
            settings_menu()
        elif Choose == 3:
            clear()
            credits()
        elif Choose == 4:
            clear()
            exit()
        
# šablona maker---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def maker():
    print(modra + bila + "===", modra + "ALGO Šablona Maker", bila + "===")
    print(modra + "Vyber, jakou šablonu chceš použít")
    print(zluta + "1 - Počítání")
    print(zluta + "2 - Grafika")

    vybratFile = int(input(bila + "Vyber: " + zelena))

    if vybratFile == 1:
        soubor_cesta = "sablony/Sablona1.txt"
    elif vybratFile == 2:
        soubor_cesta = "sablony/SablonaGrafika.txt"
    else:
        print(cervena + "Jseš debil??? Vyber 1!!!!")
        exit()
        
    # Uživatelský vstup
    today = date.today().strftime('%d-%m-%Y')
    nazevslozky = input(zelena + "Název složky, do které chceš program uložit (stačí zadat enter pokud je název složky datum): " + zelena)
    if nazevslozky == "":
        nazevslozky = today
    nadpis = input(zelena + "Jaký chceš, aby byl název programu v komentáři: " + zelena)
    autor = input(zelena + "Autor programu (stačí zadat enter pokud je autor výchozí): " + zelena)
    if autor == "":
        autor = autorprogramu
        
    popis = input(zelena + "Zadej popis programu: " + zelena)
    ulozitSoubor = input(zelena + "Zadej název souboru (bez přípony): " + zelena) + ".py"  # Vytvoření .py souboru
    # Cesta složky
    newpath = os.path.join(cestaulozeni, nazevslozky)


    # Kontrola složky
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        print(zluta + "Složka", newpath, "byla vytvořena.")
    else:
        print(zluta + "Složka", newpath, "již existuje.")

    # Přečtení obsahu šablony
    with open(soubor_cesta, "r", encoding="utf-8") as soubor:
        obsah = soubor.read()

    # Vytvoření hlavičky souboru
    hlavicka = f"""# ===============================
# Program: {nadpis} 
# Autor: {autor}
# Popis: {popis} 
# ===============================


"""

    # Sestavení finálního obsahu
    finalni_obsah = hlavicka + obsah

    # Uložení souboru do složky
    cesta_k_souboru = os.path.join(newpath, ulozitSoubor)
    with open(cesta_k_souboru, "w", encoding="utf-8") as soubor:
        soubor.write(finalni_obsah)

    print(zelena + "Soubor byl úspěšně uložen jako", cesta_k_souboru, ".")

# nastavení menu---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# otazky v nastaveni
def otazka1():
    clear()
    global autorprogramu
    autorprogramu = input(modra + "Zadej, kdo je výchozí autor programu: "+ bila)
    ulozit_nastaveni()
    clear()
    settings_menu()
def otazka2():
    clear()
    global cestaulozeni
    cestaulozeni = input(modra + "Zadej cestu kam se má program uložit (např. C:/Users/JanNovak/Python) : "+ bila)
    ulozit_nastaveni()
    clear()
    settings_menu()
def otazka3():
    clear()
    global jednodussimenu
    jednodussimenu = input(modra + "Chceš zapnout jednodušší menu? [True/False]: "+ bila)
    ulozit_nastaveni()
    clear()
    settings_menu()

def settings_menu():
    clear()
    print(modra + "Nastevní" + bila)
    print(modra + "[1]" + bila, "Autor programu:", modra + autorprogramu + bila)
    print(modra + "[2]" + bila, "Cesta, kde se má soubor vytvořit:", modra + cestaulozeni + bila)
    print(modra + "[3]" + bila, "Jednodusší menu pro ušetření času:", modra + jednodussimenu + bila)
    print(modra + "[4]" + bila, "Zpet")
    vyber = input("Vyber: ")
    if vyber == "1":
        clear()
        otazka1()
        ulozit_nastaveni()
    elif vyber == "2":
        clear()
        otazka2()
        ulozit_nastaveni()
    elif vyber == "3":
        clear()
        otazka3()
    elif vyber == "4":
        if jednodussimenu == "False":
            clear()
            main_menu()
        else:
            clear()
            jednodussi_menu()
        
# vyvolání main menu
main_menu()