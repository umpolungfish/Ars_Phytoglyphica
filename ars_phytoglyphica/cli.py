"""
Ars Phytoglyphica — Unified CLI.

  ap type      <name|num>       Show a canonical structural type
  ap plant     <name>           Look up a plant and show its type
  ap types                     List all 11 Phytoglyphic Imscriptions
  ap lattice                   Show the type lattice with pairwise distances
  ap morphology <name>         Full morphological→pharmaceutical elaboration
  ap distance   <a> <b>        Structural distance between two plants/types
  ap list      [type_num]      List plants, optionally filtered by type

Run `ap <command> --help` for per-command options.
"""

from __future__ import annotations
import argparse
import sys

from .types import TYPES, PRIM_KEYS, type_for_plant, type_by_num, type_by_name, all_plants
from .navigator import lookup, list_plants, type_distances, compute_distance
from .elaborator import elaborate_morphology, format_morphology_report


def _render_tuple(tup: list[str]) -> str:
    return '⟨' + '⋅'.join(tup) + '⟩'


# ─── ap type ───────────────────────────────────────────────────────

_ROMAN_MAP = {'i':1,'ii':2,'iii':3,'iv':4,'v':5,'vi':6,'vii':7,'viii':8,'ix':9,'x':10,'xi':11}

def cmd_type(args: argparse.Namespace) -> int:
    # Try numeric first
    pt = None
    if args.type.isdigit():
        pt = type_by_num(int(args.type))
    # Try Roman numeral
    roman_key = args.type.lower().strip()
    if pt is None and roman_key in _ROMAN_MAP:
        pt = type_by_num(_ROMAN_MAP[roman_key])
    if pt is None:
        pt = type_by_name(args.type)
    if pt is None:
        print(f'Type not found: {args.type!r}')
        print('Valid types: I-XI (1-11) or by name (e.g., "Adaptogen")')
        return 1

    width = 72
    print('═' * width)
    print(f'  TYPE {_roman(pt.num)}: {pt.name}  ({pt.tier} tier)')
    print('─' * width)
    print(f'  Tuple:  {_render_tuple(list(pt.tuple12))}')
    print('─' * width)
    print(f'  {pt.description}')
    print('─' * width)
    print(f'  Representative plants ({len(pt.representatives)}):')
    for r in pt.representatives:
        print(f'    • {r}')
    print('═' * width)
    return 0


def _roman(n: int) -> str:
    return ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI'][n]


# ─── ap plant ──────────────────────────────────────────────────────

def cmd_plant(args: argparse.Namespace) -> int:
    try:
        info = lookup(args.name)
    except KeyError as e:
        print(f'Not found: {e}')
        return 1

    width = 72
    print('═' * width)
    print(f'  PLANT  {info["name"]}')
    print('─' * width)
    tup = info['tuple']
    print(f'  Type    : {_roman(info["type_num"])}. {info["type_name"]}  ({info["tier"]})')
    print(f'  Tuple   : {_render_tuple(tup)}')
    if info.get('in_catalog'):
        print(f'  Catalog : {info["catalog_name"]}')
        if 'closest_type_distance' in info:
            print(f'  d(type) : {info["closest_type_distance"]} (primitive mismatches)')
    print('─' * width)
    if info.get('representatives'):
        print(f'  Sibling plants (same type):')
        for r in info['representatives']:
            if r != info['name']:
                print(f'    • {r}')
    print('═' * width)
    return 0


# ─── ap types ──────────────────────────────────────────────────────

def cmd_types(_args: argparse.Namespace) -> int:
    width = 80
    disc = ['Ç', 'Γ', '⊙', 'Ħ', 'Σ', 'Ω', 'ɢ']
    print('═' * width)
    print('  ARS PHYTOGLYPHICA — 11 PHYTOGLYPHIC IMSCRIPTIONS')
    print('─' * width)
    header = f'  {"#":<3} {"Type":<24} {"Tier":<5} {"Plants":<6} ' + ' '.join(f'{p:<3}' for p in disc)
    print(header)
    print('─' * width)
    for t in TYPES:
        vals = [t.tuple12[PRIM_KEYS.index(p)] for p in disc]
        row = f'  {_roman(t.num):<3} {t.name:<24} {t.tier:<5} {len(t.representatives):<6} '
        row += ' '.join(f'{v:<3}' for v in vals)
        print(row)
    print('═' * width)
    print(f'  Invariant across all terrestrial plants: Ð=𐑦, Þ=𐑸, Ř=𐑾, Φ=𐑬, ƒ=𐑱')
    print('═' * width)
    return 0


# ─── ap lattice ────────────────────────────────────────────────────

def cmd_lattice(_args: argparse.Namespace) -> int:
    dists = type_distances()
    width = 72
    print('═' * width)
    print('  TYPE LATTICE — Pairwise Hamming Distances')
    print('─' * width)

    # Header
    nums = [t.num for t in TYPES]
    header = '     ' + ''.join(f'{_roman(n):>5}' for n in nums)
    print(header)
    print('─' * width)

    for i, t_a in enumerate(TYPES):
        row = f'  {_roman(t_a.num):<3}'
        for j, t_b in enumerate(TYPES):
            if i == j:
                row += f'  {"·":>3}'
            elif i < j:
                d = dists.get((t_a.num, t_b.num), 0)
                row += f'  {d:>3}'
            else:
                d = dists.get((t_b.num, t_a.num), 0)
                row += f'  {d:>3}'
        print(row)

    print('═' * width)
    print('  Type key:')
    for t in TYPES:
        print(f'    {_roman(t.num):<3} {t.name}')
    print('═' * width)
    return 0


# ─── ap morphology ─────────────────────────────────────────────────

def cmd_morphology(args: argparse.Namespace) -> int:
    try:
        info = lookup(args.name)
    except KeyError as e:
        print(f'Not found: {e}')
        return 1

    tup = info['tuple']
    morph = elaborate_morphology(tup)
    report = format_morphology_report(
        info['name'], info['type_name'], info['tier'], tup, morph
    )
    print(report)
    return 0


# ─── ap distance ───────────────────────────────────────────────────

def cmd_distance(args: argparse.Namespace) -> int:
    result = compute_distance(args.a, args.b)
    width = 72
    print('═' * width)
    print(f'  STRUCTURAL DISTANCE')
    print('─' * width)
    print(f'  {result["name_a"]}  ↔  {result["name_b"]}')
    print(f'  Hamming distance: {result["hamming_distance"]}')
    if result['conflicts']:
        print('─' * width)
        print('  Differing primitives:')
        for c in result['conflicts']:
            print(f'    {c["primitive"]}:  {c["a"]}  ≠  {c["b"]}')
    print('═' * width)
    return 0


# ─── ap list ───────────────────────────────────────────────────────

def cmd_list(args: argparse.Namespace) -> int:
    raw = args.type.lower().strip() if args.type else None
    type_num = _ROMAN_MAP.get(raw, int(raw) if raw and raw.isdigit() else None) if raw else None
    plants = list_plants(type_num)
    width = 60
    if type_num:
        pt = type_by_num(type_num)
        print(f'Type {_roman(type_num)}: {pt.name} ({len(plants)} plants)')
    else:
        print(f'All plants ({len(plants)}):')
    print('─' * width)
    for p in plants:
        print(f'  • {p}')
    return 0


# ─── main ──────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        prog='ap',
        description='Ars Phytoglyphica — morphological encoding of pharmaceutical knowledge',
    )
    sub = parser.add_subparsers(dest='command', metavar='COMMAND')

    p_type = sub.add_parser('type', help='Show a canonical structural type')
    p_type.add_argument('type', help='Type number (1-11) or name (e.g. Adaptogen)')

    p_plant = sub.add_parser('plant', help='Look up a plant')
    p_plant.add_argument('name', help='Plant name (e.g. panax_ginseng)')

    sub.add_parser('types', help='List all 11 Phytoglyphic Imscriptions')

    sub.add_parser('lattice', help='Show type lattice with pairwise distances')

    p_morph = sub.add_parser('morphology', help='Full morphological→pharmaceutical elaboration')
    p_morph.add_argument('name', help='Plant name or type name')

    p_dist = sub.add_parser('distance', help='Structural distance between two plants/types')
    p_dist.add_argument('a', help='First plant/type')
    p_dist.add_argument('b', help='Second plant/type')

    p_list = sub.add_parser('list', help='List plants, optionally filtered by type')
    p_list.add_argument('type', nargs='?', help='Type number (1-11)')

    args = parser.parse_args()

    dispatch = {
        'type':       cmd_type,
        'plant':      cmd_plant,
        'types':      cmd_types,
        'lattice':    cmd_lattice,
        'morphology': cmd_morphology,
        'distance':   cmd_distance,
        'list':       cmd_list,
    }

    if args.command not in dispatch:
        parser.print_help()
        sys.exit(0)

    sys.exit(dispatch[args.command](args))


if __name__ == '__main__':
    main()
