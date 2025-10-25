# Testovací případy pro jednoduchý Task manager pro pridat_ukol()
## TC11
Popis: Ověření, že volba čísla 1 v hlavním menu správně spustí funkci `pridat_ukol()`.

Vstupní podmínky: Program zobrazuje hlavní menu.

Kroky testu:
1. Spusťte program.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 1 a potvrďte stisknutím klávesy Enter.

Očekávaný výsledek: Program spustí funkci `pridat_ukol()`.

Skutečný výsledek: Funkce `pridat_ukol()` byla spuštěna a program zobrazil výzvu k zadání nového úkolu.

Stav: **Pass**

Poznámky: Tento případ je důležitý, protože ověřuje zavolání a spuštění funkce pro přidání nového úkolu.

---
## TC12
Popis: Ověření, že volba čísla 1 v hlavním menu správně spustí funkci `pridat_ukol()` a dojde k přidání úkolu.

Vstupní podmínky: Program zobrazuje hlavní menu.

Kroky testu:
1. Spusťte program.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 1 a potvrďte stisknutím klávesy Enter.
4. Zadejte název úkolu a popis úkolu.
5. Program vypíše hlášku, že byl úkol přidán.

Očekávaný výsledek: Program spustí funkci `pridat_ukol()` a funkce přidá úkol.

Skutečný výsledek: Funkce `pridat_ukol()` byla spuštěna a program zobrazil výzvu k zadání nového úkolu. Po zadání názvu úkolu a popisu úkolu se vypíše potvrzovací hláška, že byl úkol přidán.

Stav: **Pass**

Poznámky: Tento případ je důležitý, protože ověřuje zavolání a spuštění funkce pro přidání nového úkolu i vlastní přidání nového úkolu.

---
## TC13
Popis: Ověření, že volba čísla 1 v hlavním menu správně spustí funkci `pridat_ukol()`.

Vstupní podmínky: Program zobrazuje hlavní menu.

Kroky testu:
1. Spusťte program.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 1 a potvrďte stisknutím klávesy Enter.
4. Zadejte název úkolu a popis úkolu.
5. Program vypíše hlášku, že byl úkol přidán.
6. V hlavním menu vyberte volbu 2.
7. Ověřte, že je nově přidaný úkol vypsaný na konci seznamu.

Očekávaný výsledek: Program spustí funkci `pridat_ukol()`, funkce přidá úkol, který se vypíše na konci seznamu.

Skutečný výsledek: Funkce `pridat_ukol()` byla spuštěna a program zobrazil výzvu k zadání nového úkolu. Po zadání názvu úkolu a popisu úkolu se vypíše potvrzovací hláška, že byl úkol přidán. Po volbě výpisu úkolů bude nově přidaný úkol na konci seznamu.

Stav: **Pass**

Poznámky: Tento případ je důležitý, protože ověřuje zavolání a spuštění funkce pro přidání nového úkolu i vlastní přidání nového úkolu. Současně testuje, že výpis úkolů vypíše i nově přidaný úkol.

---