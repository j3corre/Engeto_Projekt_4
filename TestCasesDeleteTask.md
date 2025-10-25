# Testovací případy pro jednoduchý Task manager pro pridat_ukol()
## TC31
Popis: Ověření, že volba čísla 3 v hlavním menu správně spustí funkci `odstranit_ukol()`.

Vstupní podmínky: Program zobrazuje hlavní menu.

Kroky testu:
1. Spusťte program.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 3 a potvrďte stisknutím klávesy Enter.

Očekávaný výsledek: Program spustí funkci `odstranit_ukol()`.

Skutečný výsledek: Funkce `odstranit_ukol()` byla spuštěna a program zobrazil výzvu k zadání čísla úkolu, který chceme odstranit.

Stav: **Pass**

Poznámky: Tento případ je důležitý, protože ověřuje zavolání a spuštění funkce pro odstranění úkolu.

---
## TC32
Popis: Ověření, že volba čísla 3 v hlavním menu správně spustí funkci `odstranit_ukol()` a odstranění úkolu proběhne.

Vstupní podmínky: Program zobrazuje hlavní menu.

Kroky testu:
1. Spusťte program.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 3 a potvrďte stisknutím klávesy Enter.
4. Program vypíše seznam úkolů, zadejte číslo úkolu, který se má odstranit.
5. Po odstranění program vypíše seznam úkolů bez odstraněného úkolu.

Očekávaný výsledek: Program spustí funkci `odstranit_ukol()` a odstraní vybraný úkol.

Skutečný výsledek: Funkce `odstranit_ukol()` byla spuštěna a program zobrazil výzvu k zadání čísla úkolu k odstranění. Po zadání čísla úkolu byl skutečně úkol odstraněn.

Stav: **Pass**

Poznámky: Tento případ je důležitý, protože ověřuje správnou funkčnost funkce pro odstranění úkolu.

---
## TC33
Popis: Ověření, že volba čísla 3 v hlavním menu správně spustí funkci `odstranit_ukol()` a nejde odstranit více úkolů, než existuje.

Vstupní podmínky: Program zobrazuje hlavní menu.

Kroky testu:
1. Spusťte program.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 3 a potvrďte stisknutím klávesy Enter.
4. Program vypíše seznam úkolů, zadejte číslo úkolu, který se má odstranit.
5. Po odstranění program vypíše seznam úkolů bez odstraněného úkolu.
6. Body 4 a 5 opakujte, až program vypíše hlášku *Žádné úkoly k odstranění*.

Očekávaný výsledek: Program spustí funkci `odstranit_ukol()` a odstraní postupně všechny úkoly.

Skutečný výsledek: Funkce `odstranit_ukol()` byla spuštěna a program zobrazil výzvu k zadání čísla úkolu k odstranění. Po zadání čísla úkolu byl skutečně úkol odstraněn. Po odstranění všech úkolů se vypsala hláška *Žádné úkoly k odstranění* a nešlo zadat další úkol k odstranění.

Stav: **Pass**

Poznámky: Tento případ je důležitý, protože ověřuje správnou funkčnost funkce po odstranění všech úkolů.

---
## TC34
Popis: Ověření, že volba čísla 3 v hlavním menu správně spustí funkci `odstranit_ukol()` a je ošetřeno zadání čísla úkolu mimo možný interval.

Vstupní podmínky: Program zobrazuje hlavní menu.

Kroky testu:
1. Spusťte program.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 3 a potvrďte stisknutím klávesy Enter.
4. Program vypíše seznam úkolů, zadejte větší číslo úkolu, než dostupný počet úkolů k odstranění.
5. Program vypíše upozornění *Neplatné číslo úkolu*.

Očekávaný výsledek: Program spustí funkci `odstranit_ukol()` a po zadání čísla úkolu mimo přípustný interval vypíše upozornění *Neplatné číslo úkolu*.

Skutečný výsledek: Funkce `odstranit_ukol()` byla spuštěna a program zobrazil výzvu k zadání čísla úkolu k odstranění. Po zadání čísla mimo přípustný interval se vypsala hláška *Neplatné číslo úkolu*.

Stav: **Pass**

Poznámky: Tento případ je důležitý, protože ověřuje správnou funkčnost funkce při zadání nesprávného čísla úkolu.

---
## TC35
Popis: Ověření, že volba čísla 3 v hlavním menu správně spustí funkci `odstranit_ukol()` a je ošetřeno zadání nečíselné hodnoty místo čísla úkolu k ostranění.

Vstupní podmínky: Program zobrazuje hlavní menu.

Kroky testu:
1. Spusťte program.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 3 a potvrďte stisknutím klávesy Enter.
4. Program vypíše seznam úkolů, zadejte něco jiného než celé číslo.
5. Program vypíše upozornění *Prosím zadejte platné celé číslo v intervalu 1 až N*, kde N je počet zadaných úkolů.

Očekávaný výsledek: Program spustí funkci `odstranit_ukol()` a po zadání jiné hodnoty než celého čísla vypíše upozornění *Prosím zadejte platné celé číslo v intervalu 1 až N*.

Skutečný výsledek: Funkce `odstranit_ukol()` byla spuštěna a program zobrazil výzvu k zadání čísla úkolu k odstranění. Po zadání jiné hodnoty než celého čísla se vypsala hláška *Prosím zadejte platné celé číslo v intervalu 1 až N*.

Stav: **Pass**

Poznámky: Tento případ je důležitý, protože ověřuje správnou funkčnost funkce při zadání nesmyslného čísla úkolu.

---