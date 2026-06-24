"""
Ars Phytoglyphica — Type-lattice navigator.

Bridges the 11-type Ars Phytoglyphica lattice with the IG catalog for plants
that are already imscribed. Computes structural distances between types, maps
plants to their canonical type, and navigates the type lattice.
"""

from __future__ import annotations
import sys
import json
from pathlib import Path
from typing import Optional

_HERE = Path(__file__).parent
_ROOT = _HERE.parent

from .types import TYPES, PlantType, PRIM_KEYS, type_for_plant, type_by_num, type_by_name

# Try to load the IG catalog
_CATALOG_PATH = _ROOT / 'data' / 'IG_catalog.json'
_catalog_entries: dict[str, dict] = {}
_catalog_loaded = False


def _load_catalog() -> None:
    """Load the IG catalog into memory (idempotent)."""
    global _catalog_entries, _catalog_loaded
    if _catalog_loaded:
        return
    if _CATALOG_PATH.exists():
        try:
            with open(_CATALOG_PATH, encoding='utf-8') as f:
                data = json.load(f)
            if isinstance(data, list):
                for entry in data:
                    name = entry.get('name', '')
                    if name:
                        _catalog_entries[name] = entry
            elif isinstance(data, dict):
                _catalog_entries = data
            _catalog_loaded = True
        except Exception:
            pass


def _tuple_from_entry(entry: dict) -> list[str]:
    """Extract a 12-value tuple list from a catalog entry."""
    vals = []
    for k in PRIM_KEYS:
        v = entry.get(k, '—')
        vals.append(v)
    return vals


def _hamming_distance(tup_a: list[str], tup_b: list[str]) -> int:
    """Count differing primitive positions."""
    return sum(1 for a, b in zip(tup_a, tup_b) if a != b)


def lookup(plant_name: str) -> dict:
    """
    Look up a plant and return its type information.

    Returns dict with: name, type_num, type_name, tier, tuple, description,
    representatives, in_catalog (bool), catalog_name (if found).
    """
    # First check our 11-type lattice
    ptype = type_for_plant(plant_name)
    if ptype is None:
        # Try the IG catalog
        _load_catalog()
        name_lower = plant_name.lower()
        for cat_name, entry in _catalog_entries.items():
            if name_lower in cat_name.lower() or cat_name.lower() in name_lower:
                tup = _tuple_from_entry(entry)
                # Find closest type
                best_type = None
                best_dist = 999
                for t in TYPES:
                    d = _hamming_distance(tup, list(t.tuple12))
                    if d < best_dist:
                        best_dist = d
                        best_type = t
                return {
                    'name': plant_name,
                    'type_num': best_type.num if best_type else None,
                    'type_name': best_type.name if best_type else 'Unknown',
                    'tier': best_type.tier if best_type else '?',
                    'tuple': tup,
                    'description': entry.get('description', ''),
                    'representatives': [],
                    'in_catalog': True,
                    'catalog_name': cat_name,
                    'closest_type_distance': best_dist,
                }
        raise KeyError(f'Plant not found: {plant_name!r}')

    result = {
        'name': plant_name,
        'type_num': ptype.num,
        'type_name': ptype.name,
        'tier': ptype.tier,
        'tuple': list(ptype.tuple12),
        'description': ptype.description,
        'representatives': ptype.representatives,
        'in_catalog': False,
        'catalog_name': None,
    }
    # Overlay catalog entry if it exists (picks up novelty flags, plant-specific tuples, etc.)
    _load_catalog()
    name_lower = plant_name.lower()
    cat_entry = _catalog_entries.get(name_lower) or _catalog_entries.get(plant_name)
    if cat_entry is None:
        for cname, cval in _catalog_entries.items():
            if cname.lower() == name_lower:
                cat_entry = cval
                break
    if cat_entry:
        result['in_catalog'] = True
        result['catalog_name'] = cat_entry.get('name', plant_name)
        if cat_entry.get('description'):
            result['description'] = cat_entry['description']
        # Plant-specific tuple (may differ from canonical type tuple)
        plant_tup = _tuple_from_entry(cat_entry)
        if any(v != '—' for v in plant_tup):
            result['tuple'] = plant_tup
        for key in ('novelty_flag', 'novelty_note', 'novelty_refs'):
            if key in cat_entry:
                result[key] = cat_entry[key]
    return result


def list_plants(type_num: Optional[int] = None) -> list[str]:
    """List all plants, optionally filtered by type number (1-11)."""
    if type_num is not None:
        pt = type_by_num(type_num)
        if pt:
            return sorted(pt.representatives)
        return []
    plants = []
    for t in TYPES:
        plants.extend(t.representatives)
    return sorted(plants)


def type_distances() -> dict[tuple[int, int], int]:
    """Compute Hamming distances between all pairs of the 11 types."""
    dists: dict[tuple[int, int], int] = {}
    for i, t_a in enumerate(TYPES):
        for j, t_b in enumerate(TYPES):
            if i < j:
                d = _hamming_distance(list(t_a.tuple12), list(t_b.tuple12))
                dists[(t_a.num, t_b.num)] = d
    return dists



_ROMAN_MAP = {'i':1,'ii':2,'iii':3,'iv':4,'v':5,'vi':6,'vii':7,'viii':8,'ix':9,'x':10,'xi':11}

def _resolve_name(name: str):
    """Resolve a name to a 12-tuple. Handles type nums, roman numerals, type names, and plant names."""
    # Try Roman numeral
    roman_key = name.lower().strip()
    if roman_key in _ROMAN_MAP:
        pt = type_by_num(_ROMAN_MAP[roman_key])
        if pt:
            return list(pt.tuple12)
    # Try digit
    if name.isdigit():
        pt = type_by_num(int(name))
        if pt:
            return list(pt.tuple12)
    # Try type name
    pt = type_by_name(name)
    if pt:
        return list(pt.tuple12)
    # Try plant lookup
    info = lookup(name)
    return info['tuple']
def novel_plants() -> list[dict]:
    """Return catalog entries flagged as structural predictions (novelty_flag=True)."""
    _load_catalog()
    results = []
    for name, entry in _catalog_entries.items():
        if entry.get('novelty_flag'):
            tup = _tuple_from_entry(entry)
            best_type = None
            best_dist = 999
            for t in TYPES:
                d = _hamming_distance(tup, list(t.tuple12))
                if d < best_dist:
                    best_dist = d
                    best_type = t
            results.append({
                'name': name,
                'type_num': best_type.num if best_type else None,
                'type_name': best_type.name if best_type else 'Unknown',
                'tier': best_type.tier if best_type else '?',
                'tuple': tup,
                'novelty_note': entry.get('novelty_note', ''),
                'novelty_refs': entry.get('novelty_refs', []),
            })
    return sorted(results, key=lambda x: (x['type_num'] or 99, x['name']))


def compute_distance(name_a: str, name_b: str) -> dict:
    """Compute the structural distance between two plants or types."""
    tup_a = _resolve_name(name_a)
    tup_b = _resolve_name(name_b)
    d = _hamming_distance(tup_a, tup_b)
    conflicts = []
    for i, k in enumerate(PRIM_KEYS):
        if tup_a[i] != tup_b[i]:
            conflicts.append({'primitive': k, 'a': tup_a[i], 'b': tup_b[i]})
    return {
        'name_a': name_a,
        'name_b': name_b,
        'hamming_distance': d,
        'conflicts': conflicts,
    }
