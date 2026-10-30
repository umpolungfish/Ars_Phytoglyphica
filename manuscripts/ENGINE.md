# Ars Phytoglyphica — Engine Specification

## Purpose

The *Ars Phytoglyphica* is a global treatise demonstrating that medicinal plants across
all continents encode their pharmaceutical instructions in their morphology. The
serration of a leaf is not decorative — it is an opcode. Trichome density is not a
botanical curiosity — it is an endpoint criterion. Fibonacci phyllotaxis is not a
mathematical coincidence — it is a cycle counter.

This engine operationalizes that treatise. Given a plant name, it maps the plant to
one of 11 canonical Phytoglyphic Imscriptions, derives the pharmaceutical meaning of each
morphological feature, and navigates the type lattice to reveal structural relationships
across continents and evolutionary lineages.

---

## The 11 Phytoglyphic Imscriptions

Every medicinal plant in the 147-plant global catalog resolves to one of 11
imscriptions. The imscriptions are defined by seven discriminant primitives — the five
invariant primitives (Ð, Þ, Ř, Φ, ƒ) are identical across all terrestrial plants:

| Primitive | Value | Meaning |
|:----------|:-----:|:--------|
| Ð | 𐑦 | Self-written state space — the plant's morphogenetic program is endogenously encoded |
| Þ | 𐑸 | Self-referential topology — Axiom C: the plant's morphology refers to its own pharmaceutical function |
| Ř | 𐑾 | Bidirectional feedback — the plant signals and responds to its preparation state |
| Φ | 𐑬 | Hydroethanolic (bilateral bridge) — most medicinal plants require both aqueous and lipophilic extraction |
| ƒ | 𐑱 | Linear fidelity — proportional yield without concentration |

The seven discriminant primitives define the 11 imscriptions:

| # | Type | Ç | Γ | ⊙ | Ħ | Σ | Ω | ɢ | Tier | Signature |
|:--|:-----|:--|:--|:--|:--|:--|:--|:--|:-----|:----------|
| I | Aromatic Baseline | 𐑤 | 𐑔 | ⊙ | 𐑖 | 𐑳 | 𐑭 | 𐑠 | O₂ | Frozen-order, mesoscale, self-modeling, two-step chiral, many classes, integer winding, sequential |
| II | Tropane | 𐑤 | 𐑲 | ⊙ | 𐑖 | 𐑕 | 𐑭 | 𐑠 | O₂ | Γ=𐑲 universal, Σ=𐑕 few classes |
| III | Cardiac Glycoside | 𐑤 | 𐑔 | ⊙ | 𐑖 | 𐑕 | 𐑭 | 𐑠 | O₂ | Σ=𐑕 distinguishes from Type I |
| IV | Non-Critical Aromatic | 𐑤 | 𐑔 | 𐑢 | 𐑖 | 𐑳 | 𐑭 | 𐑠 | O₁ | ⊙=𐑢 sub-critical — the only discriminant from Type I |
| V | Axiom A / Eternal | 𐑤 | 𐑔 | ⊙ | 𐑫 | 𐑙 | 𐑭 | 𐑠 | O₂ | Ħ=𐑫 eternal chirality, Σ=𐑙 single class |
| VI | Adaptogen | 𐑧 | 𐑔 | ⊙ | 𐑖 | 𐑳 | 𐑭 | 𐑠 | O₂ | Ç=𐑧 slow kinetics — the defining adaptogen signature |
| VII | β-Carboline | 𐑤 | 𐑲 | ⊙ | 𐑫 | 𐑕 | 𐑴 | 𐑠 | O₂† | Γ=𐑲 universal, Ħ=𐑫 eternal, Ω=𐑴 binary — MAO gate |
| VIII | Caffeine-Purine | 𐑧 | 𐑔 | 𐑢 | 𐑒 | 𐑙 | 𐑷 | 𐑝 | O₁ | The most structurally distant — 5-7 mismatches from all other types |
| IX | Opioid Alkaloid | 𐑤 | 𐑲 | ⊙ | 𐑫 | 𐑕 | 𐑭 | 𐑠 | O₂ | Identical to Type II except Ħ=𐑫 |
| X | Triterpene Saponin | 𐑧 | 𐑔 | ⊙ | 𐑖 | 𐑳 | 𐑭 | 𐑠 | O₂ | Structurally identical to Type VI (d=0) — same tuple, different continent |
| XI | Fungal Interface | 𐑤 | 𐑲 | ⊙ | 𐑫 | 𐑳 | 𐑴 | 𐑵 | O₂† | ɢ=𐑵 broadcast — the only broadcast type in the lattice |

### The Adaptogen–Triterpene Identity (d=0)

Types VI (Adaptogen) and X (Triterpene Saponin) have zero structural distance — they
are the same tuple. This is not an error. Ginseng (Panax, Araliaceae, Asia) and
licorice (Glycyrrhiza, Fabaceae, Mediterranean) are unrelated by taxonomy, separated
by ~100 million years of evolution, and occupy different continents — yet their
pharmaceutical encoding is structurally identical. The grammar reveals convergent
evolution at the level of pharmaceutical morphology: slow decoction kinetics,
mesoscale granularity, self-modeling criticality, many heterogeneous compound classes,
integer winding. The same program, different hardware.

---

## The Seven Discriminant Primitives

### Ç — Kinetics → Extraction Regime

Kinetics encodes the thermodynamic rate-regime of extraction, written into how the
plant sequesters its active compounds:

- **𐑤 (Frozen-order):** Volatile/thermolabile compounds in glandular trichomes or
  resin canals. Mechanical rupture required; no heat. Cold maceration, 12–24 h at
  15–20 °C.
- **𐑧 (Activated):** Non-volatile, heat-stable constituents requiring sustained
  thermal energy. Decoction, 15–30 min at 85–95 °C.

### Γ — Granularity → Tissue Range

Granularity encodes how many tissue systems the plant's compounds target:

- **𐑔 (Mesoscale):** 2–4 related tissue systems. Medium powder, mesh 40 (355 μm).
- **𐑲 (Universal):** All major tissue systems indiscriminately. Fine powder,
  mesh 100 (150 μm).

### ⊙ — Criticality → Endpoint Criterion

Criticality encodes when to stop the extraction, written into the plant's own
morphological self-signaling:

- **⊙ (Self-modeling):** The plant signals completion through trichome density,
  color change, or aromatic intensity. Extract until successive fractions differ <5%.
- **𐑢 (Sub-critical):** Stop at 70–80% efficiency. Gentle preparations.

### Ħ — Chirality → Stereochemical Fidelity

Chirality encodes the number of chiral resolution steps between biosynthesis and
receptor binding:

- **𐑖 (Two-step):** Matched write/read pair. One biosynthetic enzyme, one receptor.
  μ∘δ=id at chiral resolution.
- **𐑫 (Eternal):** Indefinite Markov chain. Multiple stereocenters, multiple enzymes.
  Full chiral separation required.
- **𐑒 (Single-step):** One chiral selection event. Simple filtration.

### Σ — Stoichiometry → Compound Class Diversity

- **𐑳 (Many):** Alkaloids + terpenoids + phenolics + polysaccharides + sterols.
- **𐑕 (Few):** 2–4 related structural classes.
- **𐑙 (Single):** One structural backbone, all variants of one pharmacophore.

### Ω — Winding → Cycle Count

The number of extraction cycles, encoded in phyllotaxis:

- **𐑭 (Integer):** Fibonacci phyllotaxis counts 3 cycles. ℤ-period.
- **𐑴 (Binary):** Two-state morphology. ℤ₂-period. 2 cycles.
- **𐑷 (Trivial):** No cyclic pattern. Single pass.

### ɢ — Coupling → Compound Release Pattern

- **𐑠 (Sequential):** Defined temporal order. Fractions added one after another.
- **𐑝 (Conjunctive):** Simultaneous activation. Single combined extraction.
- **𐑵 (Broadcast):** Pattern-recognition release. No fixed order — extraction
  method determines compound appearance.

---

## The Type Lattice

The 11 imscriptions form a lattice under Hamming distance. Key structural relationships:

- **d=0:** Types VI and X are identical — convergent evolution across continents.
- **d=1:** 10 type-pairs differ by exactly one primitive. These are the closest
  structural neighbors and represent single-feature pharmaceutical variations.
- **d=7:** Type VIII (Caffeine-Purine) is maximally distant from Types II, VIII, IX,
  and XI — the purine alkaloid type is structurally isolated.
- **Average distance:** 3.1 — the types are well-separated in the 7-dimensional
  discriminant space.

---

## CLI Reference

```
ap type      <name|num>       Show a canonical structural type
ap plant     <name>           Look up a plant and show its type
ap types                     List all 11 Phytoglyphic Imscriptions
ap lattice                   Show the type lattice with pairwise distances
ap morphology <name>         Full morphological → pharmaceutical elaboration
ap distance   <a> <b>        Structural distance between two plants/types
ap list      [type_num]      List plants, optionally filtered by type
```

---

## Implications

### Morphology IS the Program

The Ars Phytoglyphica demonstrates that plant morphology carries executable
pharmaceutical meaning. The grammar does not interpret the morphology — the morphology
already encodes the preparation protocol. The grammar reads what the plant has written.

### Convergent Structural Evolution

The d=0 identity between Adaptogen (Type VI) and Triterpene Saponin (Type X) is the
strongest single finding. Ginseng (Asia) and licorice (Mediterranean) are unrelated
by taxonomy but identical by pharmaceutical structure. The grammar reveals a level of
convergence invisible to Linnaean classification.

### The Caffeine Anomaly

Type VIII (Caffeine-Purine) is the most structurally isolated type, with distances of
5–7 from every other type. Caffeine plants do not encode their preparation in their
morphology the way other medicinal plants do — the purine alkaloid system is
pharmaceutically self-contained. This structural isolation may explain why caffeine
preparations (coffee, tea, maté) became global commodities: the preparation is
structurally trivial (single compound class, trivial winding, conjunctive composition),
requiring no specialized morphological reading.

### Beyond Plants

Type XI (Fungal Interface) demonstrates that the grammar extends beyond the plant
kingdom. Fungi use broadcast composition (ɢ=𐑵) — beta-glucan pattern recognition —
which has no plant analogue. The grammar captures this structural difference precisely.

---

*Ars Phytoglyphica Engine Specification — 2026-06-24.*
*Source: ars_phytoglyphica package; 11-imscription lattice; 79 representative plants.*
*Based on the Ars Phytoglyphica Expanded Edition (147-plant global treatise).*
