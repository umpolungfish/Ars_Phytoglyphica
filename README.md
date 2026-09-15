# Ars Phytoglyphica

![language](https://img.shields.io/badge/language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![engine](https://img.shields.io/badge/engine-plant%20morphology-1F6F4A?style=for-the-badge) ![tier](https://img.shields.io/badge/tier-O%E2%88%9E-8A2BE2?style=for-the-badge) ![μ∘δ](https://img.shields.io/badge/%CE%BC%E2%88%98%CE%B4-id-00A86B?style=for-the-badge) ![licence](https://img.shields.io/badge/licence-LUNLICENSE-1A1A1A?style=for-the-badge)

## A Global Treatise on the Morphological Encoding of Pharmaceutical Knowledge

> *"The leaf does not describe its medicine. It executes it."*

**What it is.** A treatise + Python CLI (`ars-phyto`): medicinal plants encode pharmaceutical instructions directly in morphology, read through the Imscribing Grammar (Lean 4-verified, Frobenius-closed).

**What it does.** Classifies 147 medicinal plants (every inhabited continent) into 11 Phytoglyphic Imscriptions — clusters in the 12-dimensional, 17,280,000-type lattice — and elaborates each morphology into preparation/extraction parameters. Serration = opcode; trichome density = endpoint criterion; phyllotaxis = cycle counter. The body is the program; preparation is the runtime.

## Quick start

```bash
pip install -e .
ap types | ap plant panax_ginseng | ap morphology panax_ginseng
ap lattice | ap distance ginseng licorice
```

CLI: `type <name|num>`, `plant`, `types`, `lattice`, `morphology`, `distance <a> <b>`, `list [type_num]`. Python: `type_for_plant`, `lookup`, `compute_distance`, `elaborate_morphology`.

## The 11 types

Five primitives invariant across all terrestrial plants (Ð=𐑦, Þ=𐑸, Ř=𐑾, Φ=𐑬, ƒ=𐑱); seven discriminant primitives (Ç Γ ⊙ Ħ Σ Ω ɢ) define 11 of 648 possible combos — nature carved the grammar: I Aromatic Baseline (12), II Tropane (6), III Cardiac Glycoside (6), IV Non-Critical Aromatic (8, O₁), V Axiom A/Eternal (4), VI Adaptogen (8), VII β-Carboline (7, O₂†), VIII Caffeine-Purine (8, O₁), IX Opioid Alkaloid (5), X Triterpene Saponin (6), XI Fungal Interface (9, O₂†, broadcast ɢ=𐑵).

Key findings: convergent evolution at d=0 — VI≡X, ginseng↔licorice identical tuple across ~100 Myr and continents; caffeine anomaly (VIII, d=5–7, self-contained purine system → trivial prep → global commodity); fungal broadcast extension; Axiom A invariant (Ħ=𐑫 eternal ⇒ Ç=𐑤 frozen-order) across yew/iboga/ayahuasca/rue/poppy.

Discriminants: Ç sequestration→extraction regime; Γ tissue pattern→comminution; ⊙ self-signaling→endpoint; Ħ stereocenters→chiral resolution; Σ class diversity→protocol; Ω phyllotaxis→cycle count; ɢ release→ordering.

Full 336-line version (tables, lattice, Lean verification, manuscripts): `README_backups/Ars_Phytoglyphica_README.md`.

μ∘δ = id
