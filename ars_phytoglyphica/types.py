"""
Ars Phytoglyphica — 11 Phytoglyphic Imscriptions and global plant catalog.
"""

from __future__ import annotations
from typing import NamedTuple

PRIM_KEYS = ["Ð","Þ","Ř","Φ","ƒ","Ç","Γ","ɢ","⊙","Ħ","Σ","Ω"]

class PlantType(NamedTuple):
    num: int
    name: str
    tier: str
    tuple12: tuple
    description: str
    representatives: list[str]

TYPES: list[PlantType] = [
    PlantType(1, 'Aromatic Baseline', 'O₂',
        ('𐑦', '𐑸', '𐑾', '𐑬', '𐑱', '𐑤', '𐑔', '𐑠', '⊙', '𐑖', '𐑳', '𐑭'),
        'Frozen-order kinetics from volatile terpenoids. Mesoscale granularity. Self-modeling criticality.',
        ['artemisia_absinthium', 'artemisia_vulgaris', 'salvia_officinalis', 'rosmarinus_officinalis', 'thymus_vulgaris', 'mentha_piperita', 'lavandula_angustifolia', 'melissa_officinalis', 'hyssopus_officinalis', 'origanum_vulgare', 'achillea_millefolium', 'tanacetum_parthenium']
    ),
    PlantType(2, 'Tropane', 'O₂',
        ('𐑦', '𐑸', '𐑾', '𐑬', '𐑱', '𐑤', '𐑲', '𐑠', '⊙', '𐑖', '𐑕', '𐑭'),
        'Fine granularity from tropane alkaloid distribution. Few compound classes.',
        ['atropa_belladonna', 'hyoscyamus_niger', 'datura_stramonium', 'mandragora_officinarum', 'brugmansia_suaveolens', 'duboisia_myoporoides']
    ),
    PlantType(3, 'Cardiac Glycoside', 'O₂',
        ('𐑦', '𐑸', '𐑾', '𐑬', '𐑱', '𐑤', '𐑔', '𐑠', '⊙', '𐑖', '𐑕', '𐑭'),
        'Few compound classes from cardenolide pathway specificity.',
        ['digitalis_purpurea', 'digitalis_lanata', 'convallaria_majalis', 'nerium_oleander', 'strophanthus_kombe', 'urginea_maritima']
    ),
    PlantType(4, 'Non-Critical Aromatic', 'O₁',
        ('𐑦', '𐑸', '𐑾', '𐑬', '𐑱', '𐑤', '𐑔', '𐑠', '𐑢', '𐑖', '𐑳', '𐑭'),
        'Sub-critical endpoint. Many compound classes. Gentle extraction.',
        ['matricaria_chamomilla', 'calendula_officinalis', 'tilia_cordata', 'sambucus_nigra_flos', 'viola_tricolor', 'althaea_officinalis', 'malva_sylvestris', 'plantago_lanceolata']
    ),
    PlantType(5, 'Axiom A / Eternal', 'O₂',
        ('𐑦', '𐑸', '𐑾', '𐑬', '𐑱', '𐑤', '𐑔', '𐑠', '⊙', '𐑫', '𐑙', '𐑭'),
        'Eternal chirality. Single compound class.',
        ['taxus_baccata', 'catharanthus_roseus', 'podophyllum_peltatum', 'camptotheca_acuminata']
    ),
    PlantType(6, 'Adaptogen', 'O₂',
        ('𐑦', '𐑸', '𐑾', '𐑬', '𐑱', '𐑧', '𐑔', '𐑠', '⊙', '𐑖', '𐑳', '𐑭'),
        'Slow kinetics from multi-system action. Asian pharmacopoeia defining type.',
        ['panax_ginseng', 'panax_quinquefolius', 'withania_somnifera', 'rhodiola_rosea', 'schisandra_chinensis', 'eleutherococcus_senticosus', 'ocimum_tenuiflorum', 'astragalus_membranaceus']
    ),
    PlantType(7, 'β-Carboline', 'O₂†',
        ('𐑦', '𐑸', '𐑾', '𐑬', '𐑱', '𐑤', '𐑲', '𐑠', '⊙', '𐑫', '𐑕', '𐑴'),
        'Universal granularity. Eternal chirality. Binary winding for MAO inhibition gate.',
        ['banisteriopsis_caapi', 'peganum_harmala', 'tabernanthe_iboga', 'pausinystalia_yohimbe', 'voacanga_africana', 'psychotria_viridis', 'diplopterys_cabrerana']
    ),
    PlantType(8, 'Caffeine-Purine', 'O₁',
        ('𐑦', '𐑸', '𐑾', '𐑬', '𐑱', '𐑧', '𐑔', '𐑝', '𐑢', '𐑒', '𐑙', '𐑷'),
        'Slow kinetics from purine release. Single-step chirality. Single class. Trivial winding.',
        ['coffea_arabica', 'coffea_canephora', 'camellia_sinensis', 'ilex_guayusa', 'ilex_paraguariensis', 'cola_acuminata', 'paullinia_cupana', 'theobroma_cacao']
    ),
    PlantType(9, 'Opioid Alkaloid', 'O₂',
        ('𐑦', '𐑸', '𐑾', '𐑬', '𐑱', '𐑤', '𐑲', '𐑠', '⊙', '𐑫', '𐑕', '𐑭'),
        'Universal granularity from laticifer permeation. Eternal chirality from multiple stereocenters.',
        ['papaver_somniferum', 'mitragyna_speciosa', 'lactuca_virosa', 'chelidonium_majus', 'eschscholzia_californica']
    ),
    PlantType(10, 'Triterpene Saponin', 'O₂',
        ('𐑦', '𐑸', '𐑾', '𐑬', '𐑱', '𐑧', '𐑔', '𐑠', '⊙', '𐑖', '𐑳', '𐑭'),
        'Slow kinetics from saponin decoction. Many heterogeneous compounds.',
        ['glycyrrhiza_glabra', 'glycyrrhiza_uralensis', 'centella_asiatica', 'bacopa_monnieri', 'gynostemma_pentaphyllum', 'panax_notoginseng']
    ),
    PlantType(11, 'Fungal Interface', 'O₂†',
        ('𐑦', '𐑸', '𐑾', '𐑬', '𐑱', '𐑤', '𐑲', '𐑵', '⊙', '𐑫', '𐑳', '𐑴'),
        'Broadcast composition from beta-glucan immune signaling. Eternal chirality. Many compounds.',
        ['ganoderma_lucidum', 'cordyceps_militaris', 'cordyceps_sinensis', 'trametes_versicolor', 'hericium_erinaceus', 'lentinula_edodes', 'psilocybe_cubensis', 'inonotus_obliquus', 'grifola_frondosa']
    ),
]

def type_for_plant(plant_name: str) -> PlantType | None:
    name_lower = plant_name.lower()
    for t in TYPES:
        for rep in t.representatives:
            if rep.lower() == name_lower or name_lower in rep.lower() or rep.lower() in name_lower:
                return t
    return None

def type_by_num(num: int) -> PlantType | None:
    for t in TYPES:
        if t.num == num:
            return t
    return None

def type_by_name(name: str) -> PlantType | None:
    name_lower = name.lower()
    for t in TYPES:
        if name_lower in t.name.lower():
            return t
    return None

def all_plants() -> list[str]:
    plants = []
    for t in TYPES:
        plants.extend(t.representatives)
    return sorted(plants)
