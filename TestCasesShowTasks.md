
# Testovací případy pro jednoduchý Task manager pro hlavni_menu()
## TC21
Popis: Ověření, že volba čísla 2 v hlavním menu správně spustí funkci `zobrazit_ukoly()`.

Vstupní podmínky: Program zobrazuje hlavní menu.

Kroky testu:
1. Spusťte program.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 2 a potvrďte stisknutím klávesy Enter.

Očekávaný výsledek: Program spustí funkci `zobrazit_ukoly()`.

Skutečný výsledek: Funkce `zobrazit_ukoly()` byla spuštěna a program zobrazil zadané úkoly.

Stav: **Pass**

Poznámky: Tento případ je důležitý, protože ověřuje základní funkčnost `zobrazit_ukoly()`.

---
## TC22
Popis: Ověření, že volba čísla 2 v hlavním menu správně spustí funkci `zobrazit_ukoly()`.

Vstupní podmínky: Program zobrazuje hlavní menu.

Kroky testu:
1. Spusťte program.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 2 a potvrďte stisknutím klávesy Enter.
4. Program vypíše *Žádné úkoly k zobrazení*.

Očekávaný výsledek: Program spustí funkci `zobrazit_ukoly()` a vypíše upozornění *Žádné úkoly k zobrazení*, protože dosud nebyl zadán žádný úkol.

Skutečný výsledek: Funkce `zobrazit_ukoly()` byla spuštěna a program zobrazil upozornění
```
Seznam úkolů:
Žádné úkoly k zobrazení.
```
Stav: **Pass**

Poznámky: Funkce zafungovala správně, protože seznam úkolů byl prázdný.

---