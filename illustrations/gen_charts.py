#!/usr/bin/env python3
import os
OUT = os.path.dirname(os.path.abspath(__file__))
B='#0d1117';S='#161b22';D='#30363d';G='#d4a017';H='#e94560';O='#f77f00'
T='#06d6a0';P='#9b59b6';M='#a2d6f9';W='#f0f6fc';R='#8b949e'
TC={'O_2':H,'O_1':O,'O_2d':P}
CC={'Europe':H,'Asia':O,'Africa':T,'Americas':P,'Oceania':M}
TS=[(1,'Aromatic Baseline','O_2',['Europe','Asia','Africa','Americas','Oceania']),
(2,'Tropane','O_2',['Europe','Africa']),
(3,'Cardiac Glycoside','O_2',['Europe']),
(4,'Non-Critical Aromatic','O_1',['Europe','Asia','Africa','Americas']),
(5,'Axiom A / Eternal','O_2d',['Europe','Americas']),
(6,'Adaptogen','O_2',['Asia','Africa','Americas']),
(7,'Beta-Carboline','O_2d',['Asia','Africa','Americas']),
(8,'Caffeine-Purine','O_1',['Asia','Africa','Americas']),
(9,'Opioid Alkaloid','O_2',['Europe','Asia','Africa','Americas']),
(10,'Triterpene Saponin','O_2',['Asia']),
(11,'Fungal Interface','O_2d',['Asia'])]
CS=['Europe','Asia','Africa','Americas','Oceania']
RN=['','I','II','III','IV','V','VI','VII','VIII','IX','X','XI']

def hm():
    w,h=960,560;p=[]
    p.append('<rect x="0" y="0" width="%d" height="%d" fill="%s" rx="14"/>'%(w,h,B))
    p.append('<rect x="0" y="0" width="%d" height="%d" fill="%s" rx="14" stroke="%s" stroke-width="1"/>'%(w,h,S,D))
    p.append('<text x="40" y="52" fill="%s" font-size="22" font-family="sans-serif" font-weight="bold">Continental Distribution of the Eleven Structural Types</text>'%W)
    p.append('<text x="40" y="78" fill="%s" font-size="11" font-family="sans-serif">Each cell is a plant pharmaceutical type. Filled cells indicate presence on that continent.</text>'%R)
    p.append('<line x1="40" y1="98" x2="%d" y2="98" stroke="%s" stroke-width="0.5"/>'%(w-40,G))
    gx,gy=40,135;cw,ch=140,38;tw=210
    for ci,cont in enumerate(CS):
        cc=CC.get(cont,R);cx=gx+tw+ci*cw
        p.append('<text x="%d" y="%d" fill="%s" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">%s</text>'%(cx+cw//2,gy-10,cc,cont))
    for ti,(n,name,tier,cl) in enumerate(TS):
        ry=gy+ti*ch;tc=TC.get(tier,R)
        p.append('<rect x="%d" y="%d" width="%d" height="%d" fill="#21262d" rx="4"/>'%(gx,ry,tw,ch-2))
        p.append('<circle cx="%d" cy="%d" r="5" fill="%s"/>'%(gx+14,ry+ch//2,tc))
        p.append('<text x="%d" y="%d" fill="%s" font-size="12" font-family="sans-serif">%s: %s</text>'%(gx+28,ry+ch//2+5,W,RN[n],name))
        for ci,cont in enumerate(CS):
            cx=gx+tw+ci*cw
            if cont in cl:
                cc=CC.get(cont,R)
                p.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s22" rx="4"/>'%(cx,ry,cw,ch-2,cc))
                p.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s55" rx="4"/>'%(cx+3,ry+3,cw-6,ch-8,cc))
                p.append('<text x="%d" y="%d" fill="%s" font-size="18" font-family="sans-serif" text-anchor="middle" font-weight="bold">●</text>'%(cx+cw//2,ry+ch//2+5,cc))
            else:
                p.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s33" rx="4"/>'%(cx,ry,cw,ch-2,D))
    ly=gy+11*ch+35
    p.append('<text x="40" y="%d" fill="%s" font-size="10" font-family="sans-serif">Tier key:</text>'%(ly,R))
    lx=110
    for td,clr in [('O₁',O),('O₂',H),('O₂†',P)]:
        p.append('<circle cx="%d" cy="%d" r="5" fill="%s"/>'%(lx,ly-3,clr))
        p.append('<text x="%d" y="%d" fill="%s" font-size="10" font-family="sans-serif">%s</text>'%(lx+14,ly+1,W,td))
        lx+=60
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">
'%(w,h,w,h)+'
'.join(p)+'
</svg>'

def lattice():
    w,h=960,640;p=[]
    p.append('<rect x="0" y="0" width="%d" height="%d" fill="%s" rx="14"/>'%(w,h,B))
    p.append('<rect x="0" y="0" width="%d" height="%d" fill="%s" rx="14" stroke="%s" stroke-width="1"/>'%(w,h,S,D))
    p.append('<text x="40" y="45" fill="%s" font-size="22" font-family="sans-serif" font-weight="bold">Structural Type Lattice</text>'%W)
    p.append('<text x="40" y="70" fill="%s" font-size="11" font-family="sans-serif">Types arranged by criticality (vertical) and chirality (horizontal). Arrows indicate structural descent.</text>'%R)
    p.append('<line x1="40" y1="88" x2="%d" y2="88" stroke="%s" stroke-width="0.5"/>'%(w-40,G))
    # Node positions
    ND={8:(480,140),4:(320,240),1:(160,360),6:(320,360),10:(480,360),
        3:(120,480),2:(280,480),9:(440,480),5:(160,580),7:(340,580),11:(520,580)}
    ED=[(1,4),(1,2),(1,3),(1,6),(1,10),(4,8),(2,9),(9,5),(6,10),(9,7),(7,11)]
    for src,dst in ED:
        if src in ND and dst in ND:
            sx,sy=ND[src];dx,dy=ND[dst]
            p.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1" stroke-dasharray="4,4"/>'%(sx,sy,dx,dy,D))
    for ti,(x,y) in ND.items():
        tname=TS[ti-1][1];tier=TS[ti-1][2];tc=TC.get(tier,R)
        nw,nh=170,52
        p.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" rx="8" stroke="%s" stroke-width="1.5"/>'%(x-nw//2,y-nh//2,nw,nh,B,tc))
        p.append('<rect x="%d" y="%d" width="5" height="%d" fill="%s" rx="4"/>'%(x-nw//2,y-nh//2,nh,tc))
        p.append('<text x="%d" y="%d" fill="%s" font-size="9" font-family="sans-serif" font-weight="bold">Type %s</text>'%(x-nw//2+16,y-8,G,RN[ti]))
        p.append('<text x="%d" y="%d" fill="%s" font-size="13" font-family="sans-serif" font-weight="bold">%s</text>'%(x-nw//2+16,y+10,W,tname))
        td=tier.replace('_2d','₂†').replace('_2','₂').replace('_1','₁')
        p.append('<text x="%d" y="%d" fill="%s" font-size="9" font-family="sans-serif">%s</text>'%(x-nw//2+16,y+26,tc,td))
    for ty,label in [(140,'O₁'),(360,'O₂'),(580,'O₂†')]:
        p.append('<text x="800" y="%d" fill="%s" font-size="14" font-family="sans-serif" font-weight="bold">%s</text>'%(ty+6,R,label))
        p.append('<line x1="740" y1="%d" x2="790" y2="%d" stroke="%s" stroke-width="0.5"/>'%(ty,ty,D))
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">
'%(w,h,w,h)+'
'.join(p)+'
</svg>'

with open(os.path.join(OUT,'continental_distribution.svg'),'w') as f:
    f.write(hm())
print('Generated: continental_distribution.svg')
with open(os.path.join(OUT,'type_lattice.svg'),'w') as f:
    f.write(lattice())
print('Generated: type_lattice.svg')
