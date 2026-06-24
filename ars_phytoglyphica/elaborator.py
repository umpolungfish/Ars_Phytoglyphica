"""
Ars Phytoglyphica — Morphological elaborator.

Maps the structural primitives of a plant type to their pharmaceutical meaning.
Each primitive encodes a morphological feature that, when read correctly, tells
the practitioner how to prepare the medicine. The plant body IS the program.
"""

from __future__ import annotations

PRIM_KEYS = ["Ð","Þ","Ř","Φ","ƒ","Ç","Γ","ɢ","⊙","Ħ","Σ","Ω"]

# Ç (Kinetics) — extraction regime encoded in compound sequestration
_KINETICS = {
    '𐑤': ('Cold maceration', 'Frozen-order kinetics. Volatile/thermolabile compounds sequestered in glandular '
           'trichomes or resin canals — mechanical rupture required, no heat. 12-24 h at 15-20 °C.'),
    '𐑧': ('Decoction', 'Activated kinetics. Compounds require sustained thermal energy for extraction — '
           'typically non-volatile, heat-stable constituents. 15-30 min at 85-95 °C.'),
    '𐑪': ('Percolation', 'Diffusive kinetics. Gravity-driven solvent passage through comminuted material. '
           'Ambient temperature, extended contact time.'),
    '𐑺': ('Distillation', 'Barrier kinetics. Phase-separated extraction — steam or vacuum. For essential '
           'oils and volatile fractions that cross the liquid-vapor barrier.'),
}

# Γ (Granularity) — tissue range encoded in comminution requirement
_GRANULARITY = {
    '𐑔': ('Mesoscale (medium powder)', 'Pass mesh 40 (355 μm). The plant acts on 2-4 related tissue systems. '
           'Surface area sufficient for multi-tissue distribution without systemic overload.'),
    '𐑲': ('Universal (fine powder)', 'Pass mesh 100 (150 μm). The compound class targets all major tissue '
           'systems indiscriminately — neural, cardiac, smooth muscle, glandular. Fine comminution ensures '
           'uniform systemic exposure.'),
    '𐑚': ('Coarse (cut)', '2-4 mm pieces. Local or single-tissue action. Minimal comminution preserves '
           'structural integrity for mild preparations.'),
}

# ⊙ (Criticality) — endpoint criterion encoded in morphological self-signaling
_CRITICALITY = {
    '⊙': ('Self-modeling endpoint', 'The plant signals extraction completion through its own morphology. '
          'Trichome density, leaf color, or aromatic intensity indicates the Frobenius fixed point — '
          'extract until successive fractions differ <5%. The plant monitors its own extraction.'),
    '𐑢': ('Sub-critical endpoint', 'Stop before saturation at 70-80% efficiency. Gentle preparations '
          'where full extraction would introduce undesirable constituents. The plant signals "enough" '
          'before "all".'),
    '𐑮': ('Near-critical endpoint', 'Continue past threshold. Successive fractions differ <2%. For '
          'preparations requiring exhaustive but controlled extraction.'),
}

# Ħ (Chirality) — stereochemical fidelity steps
_CHIRALITY = {
    '𐑖': ('Two-step chiral resolution', 'Matched write/read pair — biosynthesis produces one enantiomer, '
          'receptor reads that same enantiomer. Filter through cloth, then decant after 24 h settling. '
          'μ∘δ=id at chiral resolution (the Frobenius minimum for stereochemistry).'),
    '𐑫': ('Eternal chirality', 'Indefinite Markov chain of chiral fidelity. Multiple stereocenters, '
          'multiple enzymatic steps. Full chiral separation: preparative column or liquid-liquid partition. '
          'Chiral information preserved across unlimited processing steps.'),
    '𐑒': ('Single-step chiral', 'One chiral selection event. Filter through coarse cloth or paper. '
          'Single stereocenter, single enzyme.'),
    '𐑓': ('Racemic / no separation', 'Use as-is. No chiral resolution. The preparation does not depend '
          'on stereochemical purity.'),
}

# Σ (Stoichiometry) — compound class diversity
_STOICHIOMETRY = {
    '𐑳': ('Many heterogeneous classes', 'Alkaloids + terpenoids + phenolics + polysaccharides + sterols. '
          'The plant is a multi-compound pharmacy. Each class may require different extraction conditions — '
          'the dominant class sets the protocol, others ride along.'),
    '𐑕': ('Few compound classes', '2-4 related structural classes. Typically one dominant pharmacophore '
          'with variants. Example: morphinan alkaloids with methylation variants.'),
    '𐑙': ('Single compound class', 'One structural backbone. All active compounds are variants of a '
          'single pharmacophore. High specificity, narrow therapeutic window.'),
}

# Ω (Winding) — preparation cycles encoded in phyllotaxis
_WINDING = {
    '𐑭': ('Integer winding (3 cycles)', 'Fibonacci phyllotaxis encodes the cycle count. The number of '
          'parastichies or the divergence angle (≈137.5°) counts the extraction iterations. Three complete '
          'solvent charges on the marc. ℤ-period.'),
    '𐑴': ('Binary winding (2 cycles)', 'Two-state morphology — e.g., bark/leaf dimorphism, or binary '
          'MAO inhibition gate. ℤ₂-period. Two extraction cycles.'),
    '𐑷': ('Trivial winding (1 cycle)', 'No cyclic pattern in morphology. Single-pass extraction. '
          'The plant does not encode iteration in its growth pattern.'),
}

# ɢ (Coupling) — compound release pattern
_COUPLING = {
    '𐑠': ('Sequential composition', 'Compounds activate in defined temporal order: first A, then B, then C. '
          'Extraction sequence is prescribed — add fractions one after another, evaluate each before combining.'),
    '𐑝': ('Conjunctive composition', 'All active compounds activate simultaneously in a single preparation '
          'step. Combine and extract together — no temporal ordering required.'),
    '𐑵': ('Broadcast composition', 'Pattern-recognition release. Compounds signal through broadcast pattern '
          'matching (e.g., beta-glucan immune recognition). No fixed order — the extraction method determines '
          'which compounds appear.'),
}

# Φ (Parity) — solvent polarity
_PARITY = {
    '𐑬': ('Hydroethanolic (bilateral bridge)', '45-55% ethanol v/v in water. The bilateral solvent bridges '
          'aqueous and lipophilic phases simultaneously. Standard for most aromatic and alkaloid preparations.'),
    '𐑗': ('Water (aqueous)', '100% aqueous, pH 6-7. For polar constituents: polysaccharides, tannins, '
          'some glycosides.'),
    '𐑿': ('Dilute aqueous', '5-10% ethanol v/v. Slightly enhanced lipophilic reach.'),
    '𐑯': ('Anhydrous ethanol', '>95% ethanol. For highly lipophilic constituents.'),
    '𐑹': ('Fixed oil / CO₂', 'Cold-pressed oil or supercritical CO₂. For the most non-polar fractions.'),
}

# ƒ (Fidelity) — concentration target
_FIDELITY = {
    '𐑱': ('1× standard', 'No reduction. Proportional yield — what you extract is what you administer. '
          'Linear fidelity.'),
    '𐑞': ('2× concentrated', 'Reduce to half volume. Quadratic fidelity — concentration increases '
          'potency non-linearly.'),
    '𐑐': ('3× highly concentrated', 'Reduce to one-third volume. Cubic fidelity. Standardize to marker '
          'compound. Requires assay verification.'),
}


def elaborate_morphology(tuple_vals: list[str]) -> dict:
    """
    Derive the pharmaceutical interpretation of a plant's morphological encoding.

    tuple_vals: ordered list [Ð, Þ, Ř, Φ, ƒ, Ç, Γ, ɢ, ⊙, Ħ, Σ, Ω]

    Returns a dict with human-readable morphological→pharmaceutical mappings.
    """
    def _get(idx: int, table: dict) -> tuple[str, str]:
        val = tuple_vals[idx] if idx < len(tuple_vals) else ''
        return table.get(val, ('—', f'Unrecognised: {val!r}'))

    # Primitive indices in the tuple
    kin_name, kin_desc = _get(5, _KINETICS)
    gran_name, gran_desc = _get(6, _GRANULARITY)
    crit_name, crit_desc = _get(8, _CRITICALITY)
    chir_name, chir_desc = _get(9, _CHIRALITY)
    stoi_name, stoi_desc = _get(10, _STOICHIOMETRY)
    wind_name, wind_desc = _get(11, _WINDING)
    coup_name, coup_desc = _get(7, _COUPLING)
    par_name, par_desc = _get(3, _PARITY)
    fid_name, fid_desc = _get(4, _FIDELITY)

    return {
        'kinetics': (kin_name, kin_desc),
        'granularity': (gran_name, gran_desc),
        'criticality': (crit_name, crit_desc),
        'chirality': (chir_name, chir_desc),
        'stoichiometry': (stoi_name, stoi_desc),
        'winding': (wind_name, wind_desc),
        'coupling': (coup_name, coup_desc),
        'parity': (par_name, par_desc),
        'fidelity': (fid_name, fid_desc),
    }


def format_morphology_report(plant_name: str, type_name: str, tier: str,
                             tuple_vals: list[str], morphology: dict) -> str:
    """Render a complete morphological→pharmaceutical report."""
    width = 72
    lines = []
    lines.append('═' * width)
    lines.append(f'  ARS PHYTOGLYPHICA — Morphological Reading')
    lines.append('─' * width)
    lines.append(f'  Plant     : {plant_name}')
    lines.append(f'  Type      : {type_name}  ({tier} tier)')
    lines.append(f'  Tuple     : ⟨{"⋅".join(tuple_vals)}⟩')
    lines.append('─' * width)
    lines.append('  MORPHOLOGICAL FEATURE  →  PHARMACEUTICAL MEANING')
    lines.append('─' * width)

    rows = [
        ('Kinetics (Ç)',       morphology['kinetics']),
        ('Granularity (Γ)',    morphology['granularity']),
        ('Criticality (⊙)',    morphology['criticality']),
        ('Chirality (Ħ)',      morphology['chirality']),
        ('Stoichiometry (Σ)',  morphology['stoichiometry']),
        ('Winding (Ω)',        morphology['winding']),
        ('Coupling (ɢ)',       morphology['coupling']),
        ('Parity (Φ)',         morphology['parity']),
        ('Fidelity (ƒ)',       morphology['fidelity']),
    ]
    for label, (name, desc) in rows:
        lines.append(f'  {label}')
        lines.append(f'    → {name}')
        # Word-wrap the description
        words = desc.split()
        line = '      '
        for w in words:
            if len(line) + len(w) + 1 > width - 2:
                lines.append(line.rstrip())
                line = '      ' + w + ' '
            else:
                line += w + ' '
        lines.append(line.rstrip())
        lines.append('')

    lines.append('═' * width)
    lines.append('  "The leaf does not describe its medicine. It executes it."')
    lines.append('═' * width)
    return '\n'.join(lines)
