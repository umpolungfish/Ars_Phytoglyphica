
#!/usr/bin/env python3
"""Generate all 11 type card SVGs for Ars Phytoglyphica."""
import os
OUT = os.path.dirname(os.path.abspath(__file__))

# Color palette
BG = "#0d1117"; SF = "#161b22"; BD = "#30363d"; GD = "#d4a017"
HL = "#e94560"; OR = "#f77f00"; TE = "#06d6a0"; PU = "#9b59b6"
MT = "#a2d6f9"; WH = "#f0f6fc"; GR = "#8b949e"; OL = "#7d8c4e"

TIER_C = {"O_2": HL, "O_1": OR, "O_2d": PU}
CONT_C = {"Europe": HL, "Asia": OR, "Africa": TE, "Americas": PU, "Oceania": MT}

TYPES = [
    (1,"Aromatic Baseline","O_2","\U00010464","\U00010454","\u2299","\U00010456","\U00010473","\U0001046D","\U00010460",["Europe","Asia","Africa","Americas","Oceania"],"Wormwood","Frozen-order kinetics. Volatile terpenoids in glandular trichomes."),
    (2,"Tropane","O_2","\U00010464","\U00010472","\u2299","\U00010456","\U00010455","\U0001046D","\U00010460",["Europe","Africa"],"Belladonna","Local granularity at cholinergic synapses. Tropane alkaloids in vacuolar storage."),
    (3,"Cardiac Glycoside","O_2","\U00010464","\U00010454","\u2299","\U00010456","\U00010455","\U0001046D","\U00010460",["Europe"],"Foxglove","Frozen kinetics with mesoscale cardiac targeting. Cardenolide-only class."),
    (4,"Non-Critical Aromatic","O_1","\U00010464","\U00010454","\U00010462","\U00010456","\U00010473","\U0001046D","\U00010460",["Europe","Asia","Africa","Americas"],"Chamomile","Sub-critical: no self-modeling loop. Wide flavonoid diversity."),
    (5,"Axiom A / Eternal","O_2d","\U00010464","\U00010454","\u2299","\U0001046B","\U00010459","\U0001046D","\U00010460",["Europe","Americas"],"Yew","Eternal chirality with singular stoichiometry. Most extreme plant type."),
    (6,"Adaptogen","O_2","\U00010467","\U00010454","\u2299","\U00010456","\U00010473","\U0001046D","\U00010460",["Asia","Africa","Americas"],"Ginseng","Slow kinetics unique among O_2 types. Mesoscale stress-response targeting."),
    (7,"Beta-Carboline","O_2d","\U00010464","\U00010472","\u2299","\U0001046B","\U00010455","\U00010474","\U00010460",["Asia","Africa","Americas"],"Ayahuasca","Binary winding: MAOi + DMT activation. Eternal harmala chirality."),
    (8,"Caffeine-Purine","O_1","\U00010467","\U00010454","\U00010462","\U00010452","\U00010459","\U00010477","\U0001045D",["Asia","Africa","Americas"],"Coffee","Simplest plant type. Trivial winding. One-step chirality. Conjunctive."),
    (9,"Opioid Alkaloid","O_2","\U00010464","\U00010472","\u2299","\U0001046B","\U00010455","\U0001046D","\U00010460",["Europe","Asia","Africa","Americas"],"Opium Poppy","Local mu-opioid targeting. Eternal morphinan chirality."),
    (10,"Triterpene Saponin","O_2","\U00010467","\U00010454","\u2299","\U00010456","\U00010473","\U0001046D","\U00010460",["Asia"],"Licorice","Slow kinetics. Glycyrrhizin self-modeling through foam-index feedback."),
    (11,"Fungal Interface","O_2d","\U00010464","\U00010472","\u2299","\U0001046B","\U00010473","\U00010474","\U00010475",["Asia"],"Reishi","Binary winding. Broadcast composition: only type with unordered release."),
]

VW = {"\U00010477":15,"\U00010452":28,"\U0001045D":40,"\U00010474":42,"\U00010455":48,"\U00010459":50,
      "\U00010467":55,"\U00010454":65,"\U00010472":68,"\U00010473":75,"\U00010460":78,
      "\U00010464":82,"\U0001046D":85,"\U0001046B":92,"\U00010475":95,"\u2299":100,"\U00010462":35}

PRIM_COL = {"C":OR,"G":TE,"phi":HL,"H":PU,"S":MT,"O":GD,"q":OL}
PRIM_LAB = {"C":"Kinetics","G":"Granularity","phi":"Criticality","H":"Chirality","S":"Stoichiometry","O":"Winding","q":"Composition"}

def card(t):
    n,name,tier,C,G,phi,H,S,O,q,cont,rep,desc = t
    tc = TIER_C.get(tier, GR)
    prims = [("C",C,OR),("G",G,TE),("phi",phi,HL),("H",H,PU),("S",S,MT),("O",O,GD),("q",q,OL)]
    
    parts = []
    parts.append(f'<rect x="0" y="0" width="360" height="420" fill="{BG}" rx="14"/>')
    parts.append(f'<rect x="0" y="0" width="360" height="420" fill="{SF}" rx="14" stroke="{BD}" stroke-width="1"/>')
    parts.append(f'<rect x="14" y="14" width="332" height="6" fill="{tc}" rx="3"/>')
    parts.append(f'<rect x="274" y="22" width="64" height="26" fill="{tc}" rx="13"/>')
    tier_disp = tier.replace("_2d","\u2082\u2020").replace("_2","\u2082").replace("_1","\u2081")
    parts.append(f'<text x="306" y="40" fill="{BG}" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">{tier_disp}</text>')
    parts.append(f'<text x="28" y="42" fill="{GD}" font-size="11" font-family="sans-serif" font-weight="bold">Type {["","I","II","III","IV","V","VI","VII","VIII","IX","X","XI"][n]}</text>')
    parts.append(f'<text x="28" y="72" fill="{WH}" font-size="20" font-family="sans-serif" font-weight="bold">{name}</text>')
    parts.append(f'<text x="28" y="94" fill="{GR}" font-size="10" font-family="sans-serif">{rep}</text>')
    parts.append(f'<line x1="28" y1="110" x2="332" y2="110" stroke="{GD}" stroke-width="0.5"/>')
    
    by = 128
    for sym,val,color in prims:
        lvl = VW.get(val, 50) / 100.0
        parts.append(f'<text x="32" y="{by+16}" fill="{color}" font-size="14" font-family="sans-serif" font-weight="bold">{sym}</text>')
        parts.append(f'<text x="32" y="{by+28}" fill="{GR}" font-size="8" font-family="sans-serif">{PRIM_LAB[sym]}</text>')
        parts.append(f'<rect x="100" y="{by+2}" width="210" height="20" fill="{BD}" rx="4"/>')
        fw = int(210*lvl)
        parts.append(f'<rect x="100" y="{by+2}" width="{fw}" height="20" fill="{color}" rx="4"/>')
        parts.append(f'<text x="{100+fw+10}" y="{by+17}" fill="{WH}" font-size="13" font-family="sans-serif" font-weight="bold">{val}</text>')
        by += 30
    
    cy = by + 6
    parts.append(f'<text x="28" y="{cy}" fill="{GR}" font-size="9" font-family="sans-serif">Present on:</text>')
    cx = 85
    row_y = cy - 9
    for cont in cont:
        cc = CONT_C.get(cont, GR)
        tw = len(cont)*7+16
        parts.append(f'<rect x="{cx}" y="{row_y}" width="{tw}" height="18" fill="{cc}" rx="9"/>')
        parts.append(f'<text x="{cx+tw//2}" y="{row_y+13}" fill="{BG}" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">{cont}</text>')
        cx += tw + 8
        if cx > 310:
            cx = 85; row_y += 24
    
    dy = row_y + 36
    parts.append(f'<text x="28" y="{dy}" fill="{GR}" font-size="9" font-family="sans-serif">{desc[:70]}</text>')
    
    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 420" width="360" height="420">\n'
    svg += '\n'.join(parts)
    svg += '\n</svg>'
    return svg

for t in TYPES:
    fn = f"type_card_{t[0]:02d}_{t[1].lower().replace(' ','_').replace('/','_')}.svg"
    path = os.path.join(OUT, fn)
    with open(path, 'w') as f:
        f.write(card(t))
    print(f"  Generated: {fn}")

print(f"\nAll {len(TYPES)} type cards generated in {OUT}")
