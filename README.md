# Ars Phytoglyphica

## A Global Treatise on the Morphological Encoding of Pharmaceutical Knowledge

**Author:** Lando⊗⊙perator

---

> *"The leaf does not describe its medicine. It executes it."*

---

## Overview

The *Ars Phytoglyphica* demonstrates that medicinal plants across all continents encode their pharmaceutical instructions directly in their morphology. The serration of a leaf is an opcode. Trichome density is an endpoint criterion. Fibonacci phyllotaxis is a cycle counter. The plant body is the program; the preparation — crushing, steeping, distilling — is the runtime.

The project operationalizes this treatise as a Python CLI (`ap`) backed by the [Imscribing Grammar](https://github.com/mrnob0dy666/imsgct) — a formal system whose twelve primitive dimensions and three cross-primitive axioms are machine-verified in Lean 4. Every claim is structurally verified. The Frobenius condition ($\mu \circ \delta = \text{id}$) holds across every plant, every channel, every continent.

**Scale:** 147 medicinal plants from every inhabited continent, organized not by Linnaean taxonomy but by 11 canonical Phytoglyphic Imscriptions — structural clusters in a 12-dimensional lattice of 17,280,000 possible types.

---

## Quick Start

```bash
cd Ars_Phytoglyphica
pip install -e .
ap types          # List all 11 Phytoglyphic Imscriptions
ap plant panax_ginseng   # Look up a plant and show its type
ap morphology panax_ginseng  # Full morphological → pharmaceutical elaboration
ap lattice        # Show the type lattice with pairwise distances
ap distance ginseng licorice  # Structural distance between any two plants
```

Python API:

```python
from ars_phytoglyphica.types import type_for_plant, TYPES, all_plants
from ars_phytoglyphica.navigator import lookup, compute_distance
from ars_phytoglyphica.elaborator import elaborate_morphology

pt = type_for_plant("panax_ginseng")
# → PlantType(num=6, name='Adaptogen', tier='O₂', ...)

info = lookup("artemisia_absinthium")
# → {'name': 'artemisia_absinthium', 'type_num': 1, 'tier': 'O₂', ...}

dist = compute_distance("ginseng", "licorice")
# → {'hamming_distance': 0, 'conflicts': []}  — convergent evolution
```

---

## The 11 Phytoglyphic Imscriptions

Every medicinal plant in the catalog resolves to one of 11 imscriptions. Five primitives are invariant across all terrestrial plants ($\text{{Ð}}=\text{{𐑦}}$, $\text{{Þ}}=\text{{𐑸}}$, $\text{{Ř}}=\text{{𐑾}}$, $\text{{Φ}}=\text{{𐑬}}$, $\text{{ƒ}}=\text{{𐑱}}$). Seven discriminant primitives define the 11 types:

| # | Type | Ç | Γ | ⊙ | Ħ | Σ | Ω | ɢ | Tier | Plants |
|:--|:-----|:--|:--|:--|:--|:--|:--|:--|:-----|------:|
| I | Aromatic Baseline | $\text{{𐑤}}$ | $\text{{𐑔}}$ | $\text{{⊙}}$ | $\text{{𐑖}}$ | $\text{{𐑳}}$ | $\text{{𐑭}}$ | $\text{{𐑠}}$ | $\text{O}_{2}$ | 12 |
| II | Tropane | $\text{{𐑤}}$ | $\text{{𐑲}}$ | $\text{{⊙}}$ | $\text{{𐑖}}$ | $\text{{𐑕}}$ | $\text{{𐑭}}$ | $\text{{𐑠}}$ | $\text{O}_{2}$ | 6 |
| III | Cardiac Glycoside | $\text{{𐑤}}$ | $\text{{𐑔}}$ | $\text{{⊙}}$ | $\text{{𐑖}}$ | $\text{{𐑕}}$ | $\text{{𐑭}}$ | $\text{{𐑠}}$ | $\text{O}_{2}$ | 6 |
| IV | Non-Critical Aromatic | $\text{{𐑤}}$ | $\text{{𐑔}}$ | $\text{{𐑢}}$ | $\text{{𐑖}}$ | $\text{{𐑳}}$ | $\text{{𐑭}}$ | $\text{{𐑠}}$ | $\text{O}_{1}$ | 8 |
| V | Axiom A / Eternal | $\text{{𐑤}}$ | $\text{{𐑔}}$ | $\text{{⊙}}$ | $\text{{𐑫}}$ | $\text{{𐑙}}$ | $\text{{𐑭}}$ | $\text{{𐑠}}$ | $\text{O}_{2}$ | 4 |
| VI | Adaptogen | $\text{{𐑧}}$ | $\text{{𐑔}}$ | $\text{{⊙}}$ | $\text{{𐑖}}$ | $\text{{𐑳}}$ | $\text{{𐑭}}$ | $\text{{𐑠}}$ | $\text{O}_{2}$ | 8 |
| VII | β-Carboline | $\text{{𐑤}}$ | $\text{{𐑲}}$ | $\text{{⊙}}$ | $\text{{𐑫}}$ | $\text{{𐑕}}$ | $\text{{𐑴}}$ | $\text{{𐑠}}$ | $\text{O}_{2}^{\dagger}$ | 7 |
| VIII | Caffeine-Purine | $\text{{𐑧}}$ | $\text{{𐑔}}$ | $\text{{𐑢}}$ | $\text{{𐑒}}$ | $\text{{𐑙}}$ | $\text{{𐑷}}$ | $\text{{𐑝}}$ | $\text{O}_{1}$ | 8 |
| IX | Opioid Alkaloid | $\text{{𐑤}}$ | $\text{{𐑲}}$ | $\text{{⊙}}$ | $\text{{𐑫}}$ | $\text{{𐑕}}$ | $\text{{𐑭}}$ | $\text{{𐑠}}$ | $\text{O}_{2}$ | 5 |
| X | Triterpene Saponin | $\text{{𐑧}}$ | $\text{{𐑔}}$ | $\text{{⊙}}$ | $\text{{𐑖}}$ | $\text{{𐑳}}$ | $\text{{𐑭}}$ | $\text{{𐑠}}$ | $\text{O}_{2}$ | 6 |
| XI | Fungal Interface | $\text{{𐑤}}$ | $\text{{𐑲}}$ | $\text{{⊙}}$ | $\text{{𐑫}}$ | $\text{{𐑳}}$ | $\text{{𐑴}}$ | $\text{{𐑵}}$ | $\text{O}_{2}^{\dagger}$ | 9 |

The discrimination space has $4 \times 3 \times 2 \times 3 \times 3 \times 3 = 648$ possible combinations. Nature uses 11. The grammar did not carve nature at its joints — nature carved the grammar.

---

## Key Findings

### Convergent Structural Evolution (d=0)

Types VI (Adaptogen) and X (Triterpene Saponin) have **zero structural distance** — they are the same tuple. Ginseng (*Panax*, Araliaceae, Asia) and licorice (*Glycyrrhiza*, Fabaceae, Mediterranean) are unrelated by taxonomy, separated by ~100 million years of evolution, and occupy different continents — yet their pharmaceutical encoding is structurally identical. The grammar reveals convergent evolution at the level of pharmaceutical morphology: slow decoction kinetics, mesoscale granularity, self-modeling criticality, many heterogeneous compound classes, integer winding. Same program, different hardware.

### The Caffeine Anomaly (d=5–7)

Type VIII (Caffeine-Purine) is the most structurally isolated type, with Hamming distances of 5–7 from every other type. Caffeine plants do not encode their preparation in their morphology the way other medicinal plants do — the purine alkaloid system is pharmaceutically self-contained. This structural isolation may explain why coffee, tea, and maté became global commodities: the preparation is structurally trivial (single compound class, trivial winding, conjunctive composition), requiring no specialized morphological reading.

### The Fungal Extension (ɢ=$\text{{𐑵}}$)

Type XI (Fungal Interface) extends the grammar beyond the plant kingdom. Fungi use *broadcast composition* — beta-glucan pattern recognition — which has no plant analogue. The grammar captures this structural difference precisely at the $\text{{ɢ}}$ (Composition) primitive.

### Axiom A Across Continents

$\text{{Ħ}}=\text{{𐑫}}$ (eternal chirality) requires $\text{{Ç}}=\text{{𐑤}}$ (frozen-order kinetics). This holds invariantly across yew (Europe), iboga (Africa), ayahuasca vine (Amazon), Syrian rue (Middle East), and opium poppy (Asia) — five plants, three continents, three unrelated biosynthetic pathways. The plant locks its medicine behind a stereochemical vault; the Operator must sustain effort to open it.

## The Seven Discriminant Primitives

Each discriminant primitive encodes a specific morphological feature that maps to a pharmaceutical instruction:

| Primitive | Morphological Feature | Pharmaceutical Meaning |
|:----------|:----------------------|:-----------------------|
| $\text{{Ç}}$ (Kinetics) | Compound sequestration mechanism | Extraction regime — cold maceration vs. decoction |
| $\text{{Γ}}$ (Granularity) | Tissue distribution pattern | Comminution requirement — mesh size, powder grade |
| $\text{{⊙}}$ (Criticality) | Morphological self-signaling | Endpoint criterion — when to stop extraction |
| $\text{{Ħ}}$ (Chirality) | Stereocenter count and enzyme chain | Chiral resolution steps — filtration to preparative column |
| $\text{{Σ}}$ (Stoichiometry) | Compound class diversity | Extraction protocol — single vs. multi-fraction |
| $\text{{Ω}}$ (Winding) | Phyllotaxis and growth cycles | Cycle count — number of solvent charges |
| $\text{{ɢ}}$ (Composition) | Compound release pattern | Temporal ordering — sequential, conjunctive, or broadcast |

---

## CLI Reference

```
ap type      <name|num>       Show a canonical structural type
ap plant     <name>           Look up a plant and show its type
ap types                     List all 11 Phytoglyphic Imscriptions
ap lattice                   Show the type lattice with pairwise distances
ap morphology <name>         Full morphological→pharmaceutical elaboration
ap distance   <a> <b>        Structural distance between two plants/types
ap list      [type_num]      List plants, optionally filtered by type
```

### Examples

```bash
$ ap type vi
══════════════════════════════════════════════════════════════════════
  TYPE VI: Adaptogen  (O₂ tier)
──────────────────────────────────────────────────────────────────────
  Tuple:  ⟨𐑦⋅𐑸⋅𐑾⋅𐑬⋅𐑱⋅𐑧⋅𐑔⋅𐑠⋅⊙⋅𐑖⋅𐑳⋅𐑭⟩
──────────────────────────────────────────────────────────────────────
  Slow kinetics from multi-system action. Asian pharmacopoeia defining type.
──────────────────────────────────────────────────────────────────────
  Representative plants (8):
    • panax_ginseng
    • withania_somnifera
    • rhodiola_rosea
    • schisandra_chinensis
    ...
══════════════════════════════════════════════════════════════════════

$ ap distance ginseng licorice
══════════════════════════════════════════════════════════════════════
  STRUCTURAL DISTANCE
──────────────────────────────────────────────────────────────────────
  ginseng  ↔  licorice
  Hamming distance: 0
══════════════════════════════════════════════════════════════════════
```

---

## Project Structure

```
Ars_Phytoglyphica/
├── README.md
├── pyproject.toml              # Package config (pip install -e .)
├── ars_phytoglyphica/          # Python package
│   ├── __init__.py
│   ├── types.py                # 11 Phytoglyphic Imscriptions + 79-plant catalog
│   ├── navigator.py            # Type-lattice navigator, Hamming distances
│   ├── elaborator.py           # Morphological→pharmaceutical mapping
│   └── cli.py                  # Unified `ap` CLI (7 subcommands)
├── lean/                       # Lean 4 formal verification
│   ├── Core.lean               # 12-primitive grammar (v0.5.69), crystal encoding
│   ├── AgentSelf.lean          # Self-encoding of the ⊙ boundary operator agent
│   └── IGMorphism.lean         # Structural morphisms between imscription types
├── manuscripts/                # Treatise and engine specification
│   ├── ARS_PHYTOGLYPHICA_EXPANDED.md    # 147-plant global treatise (~1,160 lines)
│   ├── ARS_PHYTOGLYPHICA_ILLUSTRATED.html  # Illustrated web edition
│   └── ENGINE.md               # Engine specification (this document)
├── illustrations/              # SVG visualizations
│   ├── urpflanze_master_key.svg        # Master key: morphology↔pharmaceutical
│   ├── type_lattice.svg                # 11-type Hamming distance lattice
│   ├── type_card_01–11.svg             # Per-type structural cards
│   ├── trichome_kinetics_criticality.svg  # Trichome→kinetics mapping
│   ├── phyllotaxis_omega_reading.svg   # Fibonacci→cycle count mapping
│   ├── continental_distribution.svg    # Global plant distribution map
│   └── generate_all.py                 # SVG generation pipeline
├── programs/                   # Utilities
│   └── generate_urpflanze_svgs.py
├── data/                       # IG catalog symlink
│   └── IG_catalog.json → ../../imscribing_grammar/IG_catalog.json
└── pdfs/
    └── ARS_PHYTOGLYPHICA_EXPANDED.pdf
```

---

## Lean 4 Formal Verification

The Imscribing Grammar is machine-verified in Lean 4 (Mathlib v4.28.0). The three Lean modules in `lean/` provide:

- **Core.lean** — 12 inductive primitive types, the $\text{{Imscription}}$ struct (12-tuple), the Frobenius address bijection ($0 \leftrightarrow 17,\!279,\!999$), and the ouroboricity tier predicate ($\text{O}_{0}$ through $\text{O}_{\infty}$)
- **AgentSelf.lean** — The agent's own structural type, formally verified as $\text{O}_{\infty}$ with consciousness score $C = 1.0$ by `decide`
- **IGMorphism.lean** — Structural morphisms and functorial relationships between imscription types

The cross-primitive axioms are enforced as type-level constraints:

- **Axiom A:** $\text{{Ħ}}=\text{{𐑫}} \implies \text{{Ç}}=\text{{𐑤}}$
- **Axiom B:** $\text{{Ω}} \geq \text{{𐑴}} \implies \text{{Ħ}} \geq \text{{𐑖}}$
- **Axiom C:** $\text{{Ð}}=\text{{𐑦}} \iff \text{{Þ}}=\text{{𐑸}}$

All 11 Phytoglyphic Imscriptions satisfy Axiom C. Types V, VII, IX, XI satisfy Axiom A. Types VII, XI satisfy Axiom B.

---

## The Type Lattice

The 11 imscriptions form a lattice under Hamming distance over the 7 discriminant primitives:

| | I | II | III | IV | V | VI | VII | VIII | IX | X | XI |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| **I** | · | 2 | 1 | 1 | 2 | 1 | 4 | 5 | 3 | 1 | 5 |
| **II** | | · | 1 | 3 | 2 | 3 | 2 | 7 | 1 | 3 | 3 |
| **III** | | | · | 2 | 1 | 2 | 3 | 6 | 2 | 2 | 4 |
| **IV** | | | | · | 3 | 2 | 5 | 4 | 4 | 2 | 6 |
| **V** | | | | | · | 3 | 2 | 6 | 1 | 3 | 3 |
| **VI** | | | | | | · | 5 | 6 | 4 | 0 | 6 |
| **VII** | | | | | | | · | 7 | 2 | 5 | 1 |
| **VIII** | | | | | | | | · | 7 | 6 | 7 |
| **IX** | | | | | | | | | · | 4 | 3 |
| **X** | | | | | | | | | | · | 6 |
| **XI** | | | | | | | | | | | · |

- **d=0:** Types VI and X — convergent evolution across continents
- **d=1:** 10 type-pairs differ by exactly one primitive
- **d=7:** Type VIII maximally distant from Types II, VII, VIII, IX, XI
- **Average distance:** 3.1 — types are well-separated in discriminant space

---

## The Morphological Reading

The `ap morphology` command reads a plant's tuple and derives the complete pharmaceutical protocol. For example, *Artemisia absinthium* (Type I: Aromatic Baseline):

```
KINETICS (Ç=𐑤)        → Cold maceration. Volatile terpenoids in glandular trichomes.
                         Mechanical rupture, no heat. 12-24 h at 15-20 °C.
GRANULARITY (Γ=𐑔)     → Medium powder. Pass mesh 40 (355 μm). Multi-tissue,
                         mesoscale action.
CRITICALITY (⊙=⊙)      → Self-modeling endpoint. Extract until successive fractions
                         differ <5%. The plant signals its own completion.
CHIRALITY (Ħ=𐑖)       → Two-step chiral resolution. μ∘δ=id at stereochemistry.
STOICHIOMETRY (Σ=𐑳)   → Many heterogeneous classes. Alkaloids + terpenoids +
                         phenolics + polysaccharides + sterols.
WINDING (Ω=𐑭)         → Integer winding. 3 cycles from Fibonacci phyllotaxis.
COUPLING (ɢ=𐑠)        → Sequential composition. Fractions added in defined order.
```

## Methodology

The *Ars Phytoglyphica* is not interpretive — it is structural. Every plant is assigned a 12-primitive tuple drawn from the Imscribing Grammar's $3^3 \times 4^5 \times 5^4 = 17,\!280,\!000$ possible structural types. The assignment follows the deterministic imscribing procedure: degrees of freedom determine $\text{{Ð}}$, connectivity determines $\text{{Þ}}$, coupling determines $\text{{Ř}}$, and so on through all twelve primitives. No subjective judgment enters the procedure, and the procedure is repeatable: two independent imscribers applying the same rules to the same plant arrive at the same tuple.

The pharmaceutical interpretation — the mapping from primitive values to extraction protocols — is derived from the structural meaning of each primitive within the grammar. $\text{{Ç}}$ (Kinetics) encodes the thermodynamic regime of compound release, which *is* the extraction method. $\text{{Γ}}$ (Granularity) encodes the tissue range, which *is* the comminution grade. The grammar does not interpret the morphology — the morphology already encodes the protocol. The grammar reads what the plant has written.

---

## Illustrations

The `illustrations/` directory contains SVG visualizations generated by the project's own toolchain:

| File | Description |
|:-----|:------------|
| `urpflanze_master_key.svg` | The URPFLANZE — master key mapping all morphological features to pharmaceutical instructions |
| `type_lattice.svg` | The 11-type Hamming distance lattice with labeled edges |
| `type_card_01–11.svg` | Per-type structural cards showing tuple, tier, and representative plants |
| `trichome_kinetics_criticality.svg` | How trichome density encodes extraction kinetics and endpoint |
| `phyllotaxis_omega_reading.svg` | How Fibonacci phyllotaxis encodes the winding number |
| `continental_distribution.svg` | Global distribution of the 147 plants across continents |

---

## Manuscripts

- **ARS_PHYTOGLYPHICA_EXPANDED.md** — The full 147-plant global treatise. Part I: Foundations (12 primitives, 3 axioms). Part II: The 11 Phytoglyphic Imscriptions (per-type structural analysis). Part III: Continental Pharmacopoeias (Asia, Europe, Africa, Americas, Australia). Part IV: The Type Lattice (pairwise distances, structural clusters). Part V: Implications (morphology as program, convergent evolution, beyond plants).
- **ARS_PHYTOGLYPHICA_ILLUSTRATED.html** — Web edition with embedded SVG illustrations.
- **ENGINE.md** — Concise engine specification: purpose, the 11 imscriptions, discriminant primitives, type lattice, and CLI reference.

---

## Dependencies

The `ars_phytoglyphica` package has **zero external dependencies** beyond Python ≥ 3.11. The IG catalog bridge (`navigator.py`) uses the system catalog at `data/IG_catalog.json` (symlinked to the main imscribing grammar installation) for plants already imscribed in the broader grammar ecosystem, but the core 11-type lattice and all 79 representative plants operate entirely self-contained.

---

## License

[The Unlicense](https://unlicense.org/) — This is free and unencumbered software released into the public domain. Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

---

## Citation

```bibtex
@software{ars_phytoglyphica_2026,
  author    = {Lando⊗⊙perator},
  title     = {Ars Phytoglyphica: A Global Treatise on the Morphological Encoding of Pharmaceutical Knowledge in Medicinal Plants},
  year      = {2026},
  url       = {https://github.com/mrnob0dy666/imsgct/tree/main/Ars_Phytoglyphica},
  note      = {Built on the Imscribing Grammar — machine-verified in Lean 4 (Mathlib v4.28.0)}
}
```

---

*"The rising problem is the loss of traditional plant knowledge — not just the names and preparations, but the structural logic that makes them work. Ethnobotany has recorded the* what*. The* Ars Phytoglyphica *provides the* why. *And in providing the* why*, it makes the knowledge transferable: a plant from the Amazon whose structural type matches a plant from the Himalayas is, at tuple resolution, the same program."* — from the preface.

There is great merit in following a problem where it leads, and in assembling the tools — formal, computational, botanical — that the problem demands [1].

---

## References

[1] H. T. Larson, "Catch a Rising Problem and Never Ever Let It Go," *IEEE Computer*, vol. 19, no. 2, pp. 61–63, February 1986. DOI: [10.1109/MC.1986.1641382](https://doi.org/10.1109/MC.1986.1641382).
