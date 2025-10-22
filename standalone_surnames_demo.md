# DEMONSTRACE: Anonymizace samostatných příjmení

## Problém (PŘED):
V textech smluv se často objevují příjmení samostatně, bez křestních jmen:

```
Eva Horváthová pronajímá Lukáši Procházkovi byt na ulici Mánesova 87, Brno.
Procházka se zavazuje platit Horváthové měsíční nájemné 15 000 Kč.
```

**Co se anonymizovalo:**
- ✅ "Eva Horváthová"
- ✅ "Lukáši Procházkovi"
- ❌ "Procházka" (samostatné příjmení - NEBYLO anonymizováno)
- ❌ "Horváthové" (samostatné příjmení v pádu - NEBYLO anonymizováno)

---

## Řešení (PO):

```
[[PERSON_1]] pronajímá [[PERSON_2]] byt na ulici [[ADDRESS_1]].
[[PERSON_2]] se zavazuje platit [[PERSON_1]] měsíční nájemné 15 000 Kč.
```

**Co se anonymizuje:**
- ✅ "Eva Horváthová" → [[PERSON_1]]
- ✅ "Lukáši Procházkovi" → [[PERSON_2]]
- ✅ "Procházka" → [[PERSON_2]] (samostatné příjmení)
- ✅ "Horváthové" → [[PERSON_1]] (samostatné příjmení v pádu)

---

## Příklad ze smlouvy 0:

**PERSON_6 (Eva Horváthová):**
- Eva Horváthová
- Horváthová (samostatné příjmení!)
- Horváthové (samostatné příjmení v pádu!)
- Evě Horváthové

**PERSON_7 (Lukáš Procházka):**
- Lukáš Procházka
- Procházkovi (samostatné příjmení v pádu!)
- Procházka (samostatné příjmení!)

---

## Jak to funguje:

### FÁZE 1: Nahrazení plných jmen
```
Eva Horváthová → [[PERSON_6]]
```

### FÁZE 2: Nahrazení přivlastňovacích tvarů
```
Horváthové dům → [[PERSON_6]] dům
```

### FÁZE 3: Nahrazení samostatných příjmení (NOVÉ!)
```
... platit Horváthové nájemné → ... platit [[PERSON_6]] nájemné
```

**Kontrola kontextu:**
- Pokud před/po příjmení je křestní jméno → NENAHRAZUJ (je to součást celého jména)
- Jinak → ANONYMIZUJ jako samostatné příjmení

---

## Výhody:

1. ✅ **Kompletní anonymizace** - i samostatná příjmení
2. ✅ **Kontextová detekce** - nenahrazuje, když je příjmení součást celého jména
3. ✅ **Všechny pády** - Horváthové, Procházkovi, Novákovi, atd.
4. ✅ **Správné přiřazení** - samostatné příjmení dostane stejný tag jako celé jméno

