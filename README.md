# Generátor Sudoku v Pythonu

Tento projekt je konzolová aplikace napsaná v jazyce Python, která slouží ke generování a řešení hlavolamů Sudoku. Vznikl jako zápočtový program a využívá algoritmus vyhledávání do hloubky s návratem (Backtracking).

## 🌟 Hlavní funkce

* **Dvě velikosti herního pole:**
    * Klasické Sudoku (9x9).
    * Hexadecimální Sudoku (16x16), které pro lepší čitelnost používá znaky 0-9 a A-G.
* **Tři úrovně obtížnosti:**
    * **Lehká:** Nejméně smazaných políček, program garantuje, že hráč nebude muset hádat (lze vyřešit čistou logikou).
    * **Střední:** Více smazaných políček, střední náročnost.
    * **Těžká:** Maximální možné smazání políček při zachování unikátního řešení.
* **Garance unikátnosti:** Každé vygenerované zadání má matematicky garantované právě jedno řešení.

## 🚀 Jak program spustit

Program nevyžaduje instalaci žádných externích knihoven, stačí mít nainstalovaný čistý Python (verze 3.x).

1. Stáhněte si zdrojový kód.
2. Otevřete terminál (příkazovou řádku) ve složce s programem.
3. Spusťte skript pomocí příkazu:
   ```bash
   python sudoku.py

více detailů naleznete v dokumentaci
