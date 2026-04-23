import random 
import copy
rozmer_pole = int(input("Zadej rozměr pole (9/16): "))
obtížnost = input("Zadej obtížnost (l = lehká/s = střední/t = těžká): ")

sudoku_pole = [[0 for _ in range(int(rozmer_pole))] for _ in range(int(rozmer_pole))]
# Vytvoří pole 9x9 nebo 16x16. Zatím ho naplníme nulami, které budou představovat prázdná místa
rozmer_ctverce = int(rozmer_pole ** 0.5) # Velikost jednoho čtverce (3 nebo 4)


def kontrola_cisla(pole, radek, sloupec, cislo):
    # funkce, která zkontroluje, zda je možné vložit číslo na danou pozici

    # 1. KONTROLA ŘÁDKU:
    for i in range(rozmer_pole):   # Projdeme všechna čísla v aktuálním řádku
        if pole[radek][i] == cislo:
            return False # Číslo už tam je, takže nemůžeme umístít

    # 2. KONTROLA SLOUPCE:
    for i in range(rozmer_pole):
        if pole[i][sloupec] == cislo:
            return False

    # 3. KONTROLA ČTVERCE 
    # Musíme zjistit, kde začíná čtverec, ve kterém jsme
    zacatek_radku = (radek // rozmer_ctverce) * rozmer_ctverce
    zacatek_sloupce = (sloupec // rozmer_ctverce) * rozmer_ctverce

    for i in range(int(rozmer_ctverce)):
        for j in range(int(rozmer_ctverce)):
            if pole[zacatek_radku + i][zacatek_sloupce + j] == cislo:
                return False

    # Pokud je vše v pořádku:
    return True

def vyplnit_sudoku(pole, rozmer):
    # Funkce, která vyplní sudoku pomocí rekurze
    for radek in range(rozmer):
        for sloupec in range(rozmer):
            if pole[radek][sloupec] == 0:   # Nalezeno prázdné místo  
                cisla = list(range(1, rozmer + 1)) # Vytvořím seznam čísel 1-9
                random.shuffle(cisla)   # náhodně je promíchám
                
                for cislo in cisla:
                    if kontrola_cisla(pole, radek, sloupec, cislo): # použijeme kontrolu a zkoušíme vložit nějaké číslo
                        pole[radek][sloupec] = cislo # Zapiš číslo


                        if vyplnit_sudoku(pole, rozmer): # Rekurzivním voláním zkouší dál 
                            return True
                        
                        pole[radek][sloupec] = 0 # Pokud to dál nešlo, smaže číslo a zkusí další v cyklu
                
                return False # Pokud žádné číslo nešlo vložit, vrací False
    return True              # Pokud je celé pole vyplněné, vrací True


def pocet_reseni(pole, rozmer):
    # Funkce, která spočítá počet řešení sudoku - podobná jako vyplňování, ale hledá další řešení
    for radek in range(rozmer): 
        for sloupec in range(rozmer): 
            if pole[radek][sloupec] == 0: # Nalezeno prázdné místo  
                pocet = 0
                for cislo in range(1, rozmer + 1):
                    if kontrola_cisla(pole, radek, sloupec, cislo): # použijeme kontrolu a zkoušíme vložit nějaké číslo
                        
                        pole[radek][sloupec] = cislo 
                        
                        pocet += pocet_reseni(pole, rozmer) # Pokud jsme vložili číslo, zkusíme dál hledat řešení. Pokud najdeme řešení, přičteme 1 k počtu 
                        
                        pole[radek][sloupec] = 0 # vynulujeme a zkousíme další číslo
                        
                        if pocet > 1: 
                            return 2 # pokud najdeme více řešení, rovnou vracíme 2
                
                return pocet 
    
    
    return 1 # pokud jsme prošli celé pole a nenašli žádné prázdné místo, znamená to, že jsme našli jedno řešení, takže vracíme 1


def logicke_reseni(pole, rozmer):
    # Funkce, která se pokusí vyřešit sudoku pouze logickými úvahami, bez hádání

    pracovni_pole = copy.deepcopy(pole) # Vytvoříme si kopii původního pole, abychom na něm mohli pracovat a nezměnili původní
    
    zmena = True # Proměnná, která nám bude říkat, jestli jsme v posledním kole něco doplnili - True = ano, False = ne 
    
  
    while zmena: # Dokud jsme v posledním kole něco doplnili, zkusíme to znovu
        zmena = False # Předpokládáme, že v tomto kole nic nenajdeme
        
        for i in range(rozmer):
            for j in range(rozmer):
                if pracovni_pole[i][j] == 0: 
                    
                    mozna_cisla = [] # Seznam možných čísel pro dané políčko
                    for cislo in range(1, rozmer + 1): 
                        if kontrola_cisla(pracovni_pole, i, j, cislo): 
                            mozna_cisla.append(cislo) 
                    
                    if len(mozna_cisla) == 1: #  Pokud je číslo jenom jedno, můžeme ho tam zapsat
                        pracovni_pole[i][j] = mozna_cisla[0] 
                        zmena = True 
                    
    for i in range(rozmer): # Zkontrolujeme, jestli někde nezůstala nula
        if 0 in pracovni_pole[i]: 
            return False 
            
    return True # Pokud jsme prošli celé pole a nenašli žádnou nulu, znamená to, že jsme našli řešení

def mazani_cisel(pole, rozmer, obtiznost):
    # Funkce, která maže čísla z vyplněného sudoku podle zvolené obtížnosti
    policka = []
    for i in range(rozmer): 
        for j in range(rozmer):
            policka.append((i,j))
    random.shuffle(policka) # Náhodně promícháme seznam pozic

    celkem_policek = rozmer * rozmer
    pocet_odebranych = 0
    
    # CÍLE:
    if obtiznost == "l":
        cil_odebrani = int(celkem_policek * 0.35) # 35% pryč + logické řešení
    elif obtiznost == "s":
        cil_odebrani = int(celkem_policek * 0.60) # 60% pryč
    else: 
        cil_odebrani = celkem_policek # Těžká - všechno co půjde

    for (i,j) in policka:
        
       
        if pocet_odebranych >= cil_odebrani: # Už jsme odebrali dost čísel
            break

        puvodni_hodnota = pole[i][j]
        pole[i][j] = 0 # Zkusíme smazat číslo
        
        if pocet_reseni(pole, rozmer) != 1: # Pokud není jediné řešení, vrátíme číslo zpět 
            pole[i][j] = puvodni_hodnota # Vracíme    
            continue

        if obtiznost == "l": # Kontrolujeme logické řešení pro lehkou obtížnost
            if not logicke_reseni(pole, rozmer):
                pole[i][j] = puvodni_hodnota # Vracíme (moc těžké)
                continue

        # Úspěšně smazáno
        pocet_odebranych += 1

    return pole

def vypis_sudoku(pole):
    # Funkce, která vypíše sudoku do konzole
    
    # 9x9:
    if rozmer_pole == 9: # oddělovací čára pro 9x9 sudoku
        print("-" * 25)
        for i in range(9):
            text_radku = "| "
            for j in range(9):
                cislo = pole[i][j]
                

                if cislo == 0:
                    symbol = "_"
                else:
                    symbol = str(cislo) 
                

                text_radku += symbol + " " # Přidání symbolu a mezery - řádek
                
                if (j + 1) % 3 == 0: # Svislá čára
                    text_radku += "| "
            
            print(text_radku) 
            if (i + 1) % 3 == 0: # Horizontální čára
                print("-" * 25)

    # 16x16:
    else:  
        print("-" * 41) # oddělovací čára pro 16x16 sudoku
        for i in range(16):
            text_radku = "| "
            for j in range(16):
                cislo = pole[i][j]
                
        
                if cislo == 0:
                    symbol = "_"
                elif cislo <= 9:
                    symbol = str(cislo) # Čísla 1-9 zůstávají jako čísla
                else:
                    symbol = chr(ord('A') + cislo - 10) # Čísla 10-16 převedeme do HEX (A-F)
                
                text_radku += symbol + " "
                
    
                if (j + 1) % 4 == 0: # Svislá čára po každých 4 číslech
                    text_radku += "| "
            
            print(text_radku)
            if (i + 1) % 4 == 0: # Horizontální čára po každých 4 řádcích
                print("-" * 41)

vyplnit_sudoku(sudoku_pole, rozmer_pole)
mazani_cisel(sudoku_pole, rozmer_pole, obtížnost)
vypis_sudoku(sudoku_pole)
