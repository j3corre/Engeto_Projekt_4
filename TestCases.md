
# Testovací případy pro jednoduchý Task manager
## TC01
Popis: Ověření, že volba čísla 1 v hlavním menu správně spustí funkci `pridat_ukol()`.

Vstupní podmínky: Program zobrazuje hlavní menu.

Kroky testu:
1. Spusťte program.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 1 a potvrďte stisknutím klávesy Enter.

Očekávaný výsledek: Program spustí funkci `pridat_ukol()`.

Skutečný výsledek: Funkce `pridat_ukol()` byla spuštěna a program zobrazil výzvu k zadání nového úkolu.

Stav: **Pass**

Poznámky: Tento případ je důležitý, protože ověřuje základní navigaci z hlavního menu a funkčnost jedné z klíčových funkcí programu.

---
## TC02
Popis: Ověření, že volba čísla 2 v hlavním menu správně spustí funkci `zobrazit_ukoly()`.

Vstupní podmínky: Program zobrazuje hlavní menu.

Kroky testu:
1. Spusťte program.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 2 a potvrďte stisknutím klávesy Enter.

Očekávaný výsledek: Program spustí funkci `zobrazit_ukoly()`.

Skutečný výsledek: Funkce `zobrazit_ukoly()` byla spuštěna a program zobrazil
```
Seznam úkolů:
Žádné úkoly k zobrazení.
```
Stav: **Pass**

Poznámky: Funkce zafungovala správně, protože seznam úkolů byl prázdný.

---
## TC03
Popis: Ověření, že volba čísla mimo interval 1 až 4 nebo jiné nepodporované hodnoty v hlavním menu správně je správně ošetřena.

Vstupní podmínky: Program zobrazuje hlavní menu.

Kroky testu:
1. Spusťte program.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte čísla mimo interval 1 až 4 nebo jinou nepodporovanou hodnotu a potvrďte stisknutím klávesy Enter.

Očekávaný výsledek: Program vypíše upozornění, že nebyla zadána správná volba.

Skutečný výsledek: Program vypsal hlášení
```
Neplatná volba, zkuste to znovu.
```
Stav: **Pass**

Poznámky: Program zafungoval správně, protože uživatel zadal neplatnou volbu a i tato možnost byla ošetřena.

---
## TC04
Popis: Ověření, že volba čísla 4 ukončí program.

Vstupní podmínky: Program zobrazuje hlavní menu.

Kroky testu:
1. Spusťte program.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 4 a potvrďte stisknutím klávesy Enter.

Očekávaný výsledek: Program vypíše hlášeku o konci programu a ukončí se.

Skutečný výsledek: Program vypsal hlášení
```
Konec programu.
```
Stav: **Pass**

Poznámky: Program zafungoval správně, došlo ke korektnímu ukončení.

---
