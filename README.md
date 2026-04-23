# Generátor Sudoku v Pythonu

Tento projekt je konzolová aplikace napsaná v jazyce Python, která slouží ke generování a řešení hlavolamů Sudoku. Vznikl jako zápočtový program a využívá algoritmus vyhledávání do hloubky s návratem (Backtracking).

* **Dvě velikosti herního pole:**
    * Klasické Sudoku (9x9).
    * Hexadecimální Sudoku (16x16), které pro lepší čitelnost používá znaky 0-9 a A-G.
* **Tři úrovně obtížnosti:**
    * **Lehká:** Nejméně smazaných políček, program garantuje, že hráč nebude muset hádat (lze vyřešit čistou logikou).
    * **Střední:** Více smazaných políček, střední náročnost.
    * **Těžká:** Maximální možné smazání políček při zachování unikátního řešení.

