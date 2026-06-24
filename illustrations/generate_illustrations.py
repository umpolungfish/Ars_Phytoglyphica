#!/usr/bin/env python3
"""
Ars Phytoglyphica — Illustration Generator
Generates SVG illustrations for all 11 Phytoglyphic Imscriptions, continental distribution,
type lattice, and representative botanical diagrams.
Author: Lando⊗⊙perator
"""

import os
import math
from dataclasses import dataclass
from typing import List, Tuple, Dict, Optional

OUT = os.path.dirname(os.path.abspath(__file__))

# ─── Color palette ───────────────────────────────────────────────
C_GOLD   = "#D4A017"
C_DEEP   = "#1a1a2e"
C_SURFACE = "#16213e"
C_ACCENT = "#0f3460"
C_HIGHLIGHT = "#e94560"
C_ORANGE = "#f77f00"
C_TEAL   = "#06d6a0"
C_PURPLE = "#7209b7"
C_MINT   = "#a2d6f9"
C_CREAM  = "#fdf0d5"
C_WHITE  = "#f8f9fa"
C_GREY   = "#6c757d"
C_BROWN  = "#8B4513"
C_GREEN  = "#2d6a4f"
C_LEAF   = "#40916c"
C_SAGE   = "#95d5b2"
C_BARK   = "#5c4033"

TIER_COLORS = {"O₀": "#6c757d", "O₁": "#f77f00", "O₂": "#e94560", "O₂†": "#7209b7", "O_∞": "#06d6a0"}
CONT_COLORS = {"Europe": "#e94560", "Asia": "#f77f00", "Africa": "#06d6a0", "Americas": "#7209b7", "Oceania": "#a2d6f9"}

# ─── The 11 Structural Types ─────────────────────────────────────
@dataclass
class StructuralType:
    num: int
    name: str
    tier: str
    C: str  # kinetics
    G: str  # granularity
    phi: str  # criticality
    H: str  # chirality
    S: str  # stoichiometry
    O: str  # winding
    q: str  # composition
    continents: List[str]
    representative: str
    description: str

TYPES = [
    StructuralType(1, "Aromatic Baseline", "O₂", "𐑤", "𐑔", "⊙", "𐑖", "𐑳", "𐑭", "𐑠",
        ["Europe", "Asia", "Africa", "Americas", "Oceania"], "Wormwood (Artemisia absinthium)",
        "Frozen-order kinetics from volatile terpenoids in glandular trichomes. Mesoscale granularity across 2–4 tissue systems. Self-modeling criticality via aromatic intensity feedback."),
    StructuralType(2, "Tropane", "O₂", "𐑤", "𐑲", "⊙", "𐑖", "𐑕", "𐑭", "𐑠",
        ["Europe", "Africa"], "Belladonna (Atropa belladonna)",
        "Local granularity — tropane alkaloids target cholinergic synapses exclusively. Frozen-order kinetics in vacuolar storage. Narrow compound class diversity."),
    StructuralType(3, "Cardiac Glycoside", "O₂", "𐑤", "𐑔", "⊙", "𐑖", "𐑕", "𐑭", "𐑠",
        ["Europe"], "Foxglove (Digitalis purpurea)",
        "Frozen-order kinetics with mesoscale cardiac targeting. Narrow compound class — cardenolides only. Self-modeling through toxicity gradient encoding."),
    StructuralType(4, "Non-Critical Aromatic", "O₁", "𐑤", "𐑔", "𐑢", "𐑖", "𐑳", "𐑭", "𐑠",
        ["Europe", "Asia", "Africa", "Americas"], "Chamomile (Matricaria chamomilla)",
        "Sub-critical — no self-modeling loop. Gentler aromatic action. Wide compound diversity across flavonoids and terpenoids."),
    StructuralType(5, "Axiom A / Eternal", "O₂†", "𐑤", "𐑔", "⊙", "𐑫", "𐑙", "𐑭", "𐑠",
        ["Europe", "Americas"], "Yew (Taxus baccata)",
        "Eternal chirality with singular stoichiometry — one compound class preserved across unlimited Markov steps. The most structurally extreme plant type."),
    StructuralType(6, "Adaptogen", "O₂", "𐑧", "𐑔", "⊙", "𐑖", "𐑳", "𐑭", "𐑠",
        ["Asia", "Africa", "Americas"], "Ginseng (Panax ginseng)",
        "Slow kinetics distinguished from all other O₂ types. Mesoscale granularity across stress-response systems. Wide compound diversity."),
    StructuralType(7, "β-Carboline", "O₂†", "𐑤", "𐑲", "⊙", "𐑫", "𐑕", "𐑴", "𐑠",
        ["Asia", "Africa", "Americas"], "Ayahuasca (Banisteriopsis caapi)",
        "Binary winding — MAO inhibition + DMT activation as a two-cycle process. Eternal chirality in the harmala alkaloid pathway."),
    StructuralType(8, "Caffeine-Purine", "O₁", "𐑧", "𐑔", "𐑢", "𐑒", "𐑙", "𐑷", "𐑝",
        ["Asia", "Africa", "Americas"], "Coffee (Coffea arabica)",
        "The structurally simplest type. Trivial winding, singular stoichiometry, conjunctive composition, one-step chirality."),
    StructuralType(9, "Opioid Alkaloid", "O₂", "𐑤", "𐑲", "⊙", "𐑫", "𐑕", "𐑭", "𐑠",
        ["Europe", "Asia", "Africa", "Americas"], "Opium Poppy (Papaver somniferum)",
        "Local granularity at μ-opioid receptors. Eternal chirality in the morphinan pathway. Integer winding through latex lancing cycles."),
    StructuralType(10, "Triterpene Saponin", "O₂", "𐑧", "𐑔", "⊙", "𐑖", "𐑳", "𐑭", "𐑠",
        ["Asia"], "Licorice (Glycyrrhiza glabra)",
        "Slow kinetics with mesoscale granularity. The glycyrrhizin pathway shows self-modeling through foam-index feedback."),
    StructuralType(11, "Fungal Interface", "O₂†", "𐑤", "𐑲", "⊙", "𐑫", "𐑳", "𐑴", "𐑵",
        ["Asia"], "Reishi (Ganoderma lucidum)",
        "Binary winding from dual-phase extraction. Broadcast composition — polysaccharides, triterpenes, and proteins released without fixed order. The only broadcast-composition type."),
]


# ─── SVG utilities ────────────────────────────────────────────────

def svg_tag(w: int, h: int, content: str, viewbox: Optional[str] = None) -> str:
    vb = viewbox or f"0 0 {w} {h}"
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{w}" height="{h}">\n{content}\n</svg>'

def rect(x, y, w, h, fill, rx=0, stroke="none", sw=0):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"'
    if rx: s += f' rx="{rx}"'
    if stroke != "none": s += f' stroke="{stroke}" stroke-width="{sw}"'
    return s + '/>'

def circle(cx, cy, r, fill, stroke="none", sw=0):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def text(x, y, content, fill=C_WHITE, size=14, anchor="start", font="monospace", bold=False, cls=""):
    fw = "bold" if bold else "normal"
    return f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" font-family="{font}" font-weight="{fw}" text-anchor="{anchor}">{content}</text>'

def line(x1, y1, x2, y2, stroke, sw=1, dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def path(d, fill="none", stroke=C_WHITE, sw=1):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def group(content, transform="", cls=""):
    t = f' transform="{transform}"' if transform else ""
    return f'<g{t}>\n{content}\n</g>'


# ─── Type Card: Single type illustration ─────────────────────────

def generate_type_card(t: StructuralType) -> str:
    """Generate an SVG type card for a single structural type."""
    W, H = 340, 440
    
    # Background
    bg = rect(0, 0, W, H, C_DEEP, rx=12)
    
    # Tier badge
    tier_c = TIER_COLORS.get(t.tier, C_GREY)
    badge = rect(W-80, 16, 64, 28, tier_c, rx=14)
    tier_txt = text(W-48, 36, t.tier, C_DEEP, size=13, anchor="middle", bold=True)
    
    # Type number
    num_txt = text(20, 32, f"Type {t.num}", C_GOLD, size=11, bold=True)
    
    # Type name
    name_txt = text(20, 62, t.name, C_WHITE, size=20, bold=True)
    
    # Representative plant
    rep_txt = text(20, 84, t.representative, C_GREY, size=10)
    
    # Divider
    div = line(20, 100, W-20, 100, C_GOLD, sw=0.5)
    
    # Primitive labels and values — 7 primitives arranged as radial bars
    prims = [
        ("Ç", t.C, "Kinetics", C_ORANGE),
        ("Γ", t.G, "Granularity", C_TEAL),
        ("φ̂", t.phi, "Criticality", C_HIGHLIGHT),
        ("Ħ", t.H, "Chirality", C_PURPLE),
        ("Σ", t.S, "Stoichiometry", C_MINT),
        ("Ω", t.O, "Winding", C_GOLD),
        ("ɢ", t.q, "Composition", C_SAGE),
    ]
    
    bar_start_y = 120
    bar_h = 22
    bar_gap = 28
    bar_w = 190
    label_x = 30
    bar_x = 95
    
    for i, (sym, val, label, color) in enumerate(prims):
        y = bar_start_y + i * bar_gap
        
        # Symbol
        sym_t = text(label_x, y + 16, sym, color, size=13, bold=True)
        # Label
        lab_t = text(label_x, y + 30, label, C_GREY, size=8)
        # Bar background
        bar_bg = rect(bar_x, y + 4, bar_w, bar_h, C_ACCENT, rx=4)
        # Bar fill (proportional length based on value "level")
        val_levels = {"𐑷": 0.1, "𐑒": 0.25, "𐑴": 0.35, "𐑕": 0.45, "𐑙": 0.45, "𐑧": 0.5, "𐑔": 0.6, "𐑲": 0.6, "𐑳": 0.7, "𐑤": 0.75, "𐑫": 0.85, "𐑭": 0.8, "𐑠": 0.7, "𐑝": 0.4, "𐑵": 0.9, "⊙": 0.95, "𐑢": 0.3}
        lvl = val_levels.get(val, 0.5)
        fill_w = int(bar_w * lvl)
        bar_fill = rect(bar_x, y + 4, fill_w, bar_h, color, rx=4)
        # Value text on bar
        val_t = text(bar_x + fill_w + 8, y + 20, val, C_WHITE, size=13, bold=True)
    
    # Continental presence
    cont_y = bar_start_y + 7 * bar_gap + 10
    cont_label = text(20, cont_y, "Present on:", C_GREY, size=10)
    cont_tags = ""
    cx = 20
    for continent in t.continents:
        cc = CONT_COLORS.get(continent, C_GREY)
        cont_tags += f'\n{rect(cx, cont_y + 8, len(continent)*7+12, 18, cc, rx=9)}'
        cont_tags += f'\n{text(cx + len(continent)*3.5 + 6, cont_y + 21, continent, C_DEEP, size=9, anchor="middle")}'
        cx += len(continent)*7 + 20
    
    # Description
    desc_y = cont_y + 40
    # Simple text wrapping for description
    words = t.description.split()
    lines = []
    current = ""
    for w in words:
        if len(current + " " + w) < 52:
            current = (current + " " + w).strip()
        else:
            lines.append(current)
            current = w
    if current:
        lines.append(current)
    
    desc_txts = ""
    for j, line_text in enumerate(lines[:4]):  # max 4 lines
        desc_txts += f'\n{text(20, desc_y + j*16, line_text, C_GREY, size=9)}'
    
    return svg_tag(W, H, bg + badge + tier_txt + num_txt + name_txt + rep_txt + div +
                   "".join([sym_t if isinstance(sym_t, str) else "" for sym_t in [""]]) +
                   bar_bg + bar_fill + val_t + cont_label + cont_tags + desc_txts)

# Actually let me rewrite this more cleanly
print("Base utilities loaded.")
