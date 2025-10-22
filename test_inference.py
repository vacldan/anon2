#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test inference funkcí"""

import sys
import json
from pathlib import Path

# Načtení jmen z knihovny
def load_names_library(json_path: str = "cz_names.v1.json"):
    try:
        script_dir = Path(__file__).parent if '__file__' in globals() else Path.cwd()
        json_file = script_dir / json_path

        if not json_file.exists():
            print(f"⚠️  Varování: {json_path} nenalezen, používám prázdnou knihovnu!")
            return set()

        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        names = set()
        if 'firstnames_no_diac' in data:
            names.update(data['firstnames_no_diac'].get('M', []))
            names.update(data['firstnames_no_diac'].get('F', []))

        return names

    except Exception as e:
        print(f"⚠️  Chyba při načítání: {e}")
        return set()

CZECH_FIRST_NAMES = load_names_library()

import re, unicodedata
from typing import Optional

def normalize_for_matching(text: str) -> str:
    if not text: return ""
    n = unicodedata.normalize('NFD', text)
    no_diac = ''.join(c for c in n if not unicodedata.combining(c))
    return re.sub(r'[^A-Za-z]', '', no_diac).lower()

# Import funkcí z hlavního souboru
exec(open('Czech DOCX Anonymizer3.py').read().split('def main():')[0])

# Test inference
test_cases = [
    ('Petry', 'Novotné'),
    ('Petra', 'Novotná'),
    ('Veronice', 'Suché'),
    ('Veronika', 'Suchá'),
    ('Michalu', 'Říhovi'),
    ('Michal', 'Říha'),
]

print("\n" + "="*70)
print("TEST INFERENCE FUNKCÍ")
print("="*70)
print(f"{'Pozorovaný tvar':<30} → {'Nominativ':<30}")
print("-"*70)

for first, last in test_cases:
    first_nom = infer_first_name_nominative(first, last)
    last_nom = infer_surname_nominative(last)
    observed = f"{first} {last}"
    nominative = f"{first_nom} {last_nom}"
    print(f"{observed:<30} → {nominative:<30}")

print("="*70)
