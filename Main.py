# Importování modulů
import os

# KONFIGURACE BAREV 
cervena = "\033[31;49;1m"
zluta = "\033[33;49;1m"
modra = '\033[34;49;1m'
zelena = "\033[32;49;1m"
bila = "\033[0m"

# Úvodní text
print(modra + cervena + "===", modra + "ALGO Šablona Maker", cervena + "===")
print(modra + "Vyber, jakou šablonu chceš použít")
print(zluta + "1 - Počítání")

vybratFile = int(input(bila + "Vyber: " + zelena))

if vybratFile == 1:
    soubor_cesta = "Sablona.txt"
else:
    print(cervena + "Jseš debil??? Vyber 1!!!!")
    exit()
    
# Uživatelský vstup
nazevslozky = input(zelena + "Název složky, do které chceš program uložit: " + zelena)
nadpis = input(zelena + "Jaký chceš, aby byl název programu: " + zelena)
autor = input(zelena + "Autor programu: " + zelena)
popis = input(zelena + "Zadej popis programu: " + zelena)
ulozitSoubor = input(zelena + "Zadej název souboru (bez přípony): " + zelena) + ".py"  # Vytvoření .py souboru

# Cesta složky
newpath = os.path.join(r'C:\Users\c24kucera\OneDrive - Obchodní akademie T.G.M. Kostelec nad Orlicí\Fujthon\Programy', nazevslozky)

# Kontrola složky
if not os.path.exists(newpath):
    os.makedirs(newpath)
    print(zluta + "Složka '{newpath}' byla vytvořena.")
else:
    print(zluta + "Složka '{newpath}' již existuje.")

# Přečtení obsahu šablony
with open(soubor_cesta, "r", encoding="utf-8") as soubor:
    obsah = soubor.read()

# Vytvoření hlavičky souboru
hlavicka = f"""# ===============================
# Program: {nadpis} 
# Autor: {autor}
# Popis: {popis} 
#
# ===============================

"""

# Sestavení finálního obsahu
finalni_obsah = hlavicka + obsah

# Uložení souboru do složky
cesta_k_souboru = os.path.join(newpath, ulozitSoubor)
with open(cesta_k_souboru, "w", encoding="utf-8") as soubor:
    soubor.write(finalni_obsah)

print(zelena + "Soubor byl úspěšně uložen jako '{cesta_k_souboru}'.")
