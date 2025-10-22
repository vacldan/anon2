#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Debug test pro inference"""

import sys
import json
from pathlib import Path

# Načtení jmen z knihovny
def load_names_library(json_path: str = "cz_names.v1.json"):
    try:
        script_dir = Path(__file__).parent if '__file__' in globals() else Path.cwd()
        json_file = script_dir / json_path

        if not json_file.exists():
            return set()

        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        names = set()
        if 'firstnames_no_diac' in data:
            names.update(data['firstnames_no_diac'].get('M', []))
            names.update(data['firstnames_no_diac'].get('F', []))

        return names

    except Exception as e:
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

# Debug pro konkrétní případ
print("\n" + "="*70)
print("DEBUG: Suché → ?")
print("="*70)

obs = "Suché"
low = obs.lower()
print(f"Pozorované: {obs}")
print(f"Lowercase: {low}")
print(f"Končí na 'né': {low.endswith('né')}")
print(f"Končí na 'ké': {low.endswith('ké')}")
print(f"Končí na 'cké': {low.endswith('cké')}")

result = infer_surname_nominative(obs)
print(f"Výsledek: {result}")

print("\n" + "="*70)
print("DEBUG: Michalu → ?")
print("="*70)

first = "Michalu"
surname = "Říhovi"

print(f"Jméno: {first}, Příjmení: {surname}")
print(f"surname_lower: {surname.lower()}")
print(f"female_like: {surname.lower().endswith(('ová', 'á', 'ou', 'é'))}")

# Test mužského inference
from_male = _male_genitive_to_nominative(first)
print(f"_male_genitive_to_nominative('{first}'): {from_male}")

result = infer_first_name_nominative(first, surname)
print(f"infer_first_name_nominative('{first}', '{surname}'): {result}")

print("\n" + "="*70)
print("DEBUG: Michal v knihovně?")
print("="*70)
print(f"normalize_for_matching('Michal'): {normalize_for_matching('Michal')}")
print(f"'michal' in CZECH_FIRST_NAMES: {normalize_for_matching('Michal') in CZECH_FIRST_NAMES}")
