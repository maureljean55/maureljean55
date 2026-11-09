"""Generate the profile README SVG assets (light + dark) with embedded, subsetted fonts."""
import base64, os, re, sys, urllib.parse, urllib.request
from collections import defaultdict

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

FONTS = {  # name -> google css2 family spec
    "D": "Archivo:wdth,wght@125,800",
    "T": "Archivo:wdth,wght@112,700",
    "B": "Archivo:wdth,wght@100,400",
    "M": "IBM+Plex+Mono:wght@400",
    "M5": "IBM+Plex+Mono:wght@500",
}
_cache = {}

def font_face(name, text):
    key = (name, text)
    if key in _cache:
        return _cache[key]
    url = f"https://fonts.googleapis.com/css2?family={FONTS[name]}&text={urllib.parse.quote(text)}"
    css = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA})).read().decode()
    furl = re.search(r"url\((https://[^)]+)\)", css).group(1)
    data = urllib.request.urlopen(urllib.request.Request(furl, headers={"User-Agent": UA})).read()
    face = (f"@font-face{{font-family:'{name}';src:url(data:font/woff2;base64,"
            f"{base64.b64encode(data).decode()}) format('woff2');}}")
    _cache[key] = face
    return face

THEMES = {
    "light": dict(paper="#F6F7F9", surface="#FFFFFF", ink="#101828", muted="#5B6474",
                  faint="#98A2B3", line="#E3E7EE", grid="#D5DAE3", signal="#3A5BFF",
                  signal_soft="#3A5BFF", teal="#0E9F6E", teal_soft="#0E9F6E"),
    "dark": dict(paper="#0D1117", surface="#131A24", ink="#E8EDF5", muted="#9AA6B8",
                 faint="#5E6B7E", line="#232C3A", grid="#263040", signal="#8CA2FF",
                 signal_soft="#8CA2FF", teal="#3DD6A3", teal_soft="#3DD6A3"),
}

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class SVG:
    def __init__(self, w, h, theme, title):
        self.w, self.h, self.c, self.title = w, h, THEMES[theme], title
        self.body, self.chars, self.css = [], defaultdict(set), []

    def add(self, s):
        self.body.append(s)

    def text(self, x, y, s, font, size, fill, anchor="start", ls=0, extra=""):
        self.chars[font].update(s)
        self.add(f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" fill="{fill}" '
                 f'text-anchor="{anchor}" letter-spacing="{ls}" {extra}>{esc(s)}</text>')

    def frame(self, bg, radius=18, dots=True):
        c = self.c
        self.add(f'<defs><pattern id="g" width="22" height="22" patternUnits="userSpaceOnUse">'
                 f'<circle cx="1" cy="1" r="1" fill="{c["grid"]}"/></pattern>'
                 f'<clipPath id="r"><rect width="{self.w}" height="{self.h}" rx="{radius}"/></clipPath></defs>')
        self.add(f'<g clip-path="url(#r)"><rect width="{self.w}" height="{self.h}" fill="{bg}"/>')
        if dots:
            self.add(f'<rect width="{self.w}" height="{self.h}" fill="url(#g)" opacity=".55"/>')
        self.add('</g>')
        self.add(f'<rect x=".75" y=".75" width="{self.w-1.5}" height="{self.h-1.5}" rx="{radius}" '
                 f'fill="none" stroke="{c["line"]}" stroke-width="1.5"/>')

    def render(self):
        faces = "".join(font_face(f, "".join(sorted(ch))) for f, ch in self.chars.items())
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
                f'viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{esc(self.title)}">'
                f'<title>{esc(self.title)}</title><style>{faces}{"".join(self.css)}</style>'
                + "".join(self.body) + "</svg>")


def save(name, fn):
    for theme in THEMES:
        svg = fn(theme)
        with open(os.path.join(OUT, f"{name}-{theme}.svg"), "w") as f:
            f.write(svg.render())


# ---------------------------------------------------------------- hero
def hero(theme):
    s = SVG(1200, 440, theme, "N'cho Jean Maurel Monne — futur Data Scientist, ECE Paris")
    c = s.c
    s.frame(c["paper"], dots=True)
    s.css.append("""
    .curve{stroke-dasharray:1;stroke-dashoffset:0;animation:draw 2.4s cubic-bezier(.3,.7,.2,1) .3s backwards}
    .area{animation:fade 1s ease-out 2.2s backwards}
    .late{animation:fade .8s ease-out 2.5s backwards}
    .pulse{transform-origin:center;transform-box:fill-box;animation:pulse 2.4s ease-out infinite}
    @keyframes draw{from{stroke-dashoffset:1}}
    @keyframes fade{from{opacity:0}}
    @keyframes pulse{0%{transform:scale(1);opacity:.55}100%{transform:scale(3.2);opacity:0}}
    @media (prefers-reduced-motion:reduce){.curve{animation:none;stroke-dashoffset:0}
      .area,.late{animation:none;opacity:1}.pulse{animation:none;opacity:0}}
    """)
    x = 64
    s.text(x, 84, "ECE PARIS · INTELLIGENCE ARTIFICIELLE", "M5", 14, c["signal"], ls=2.2)
    s.text(x, 160, "N’cho Jean", "D", 66, c["ink"], ls=-1.5)
    s.text(x, 232, "Maurel Monne", "D", 66, c["ink"], ls=-1.5)
    s.text(x, 284, "Futur Data Scientist. Je maîtrise toute la chaîne :", "B", 21, c["muted"])
    s.text(x, 313, "de la base de données au modèle, jusqu’au produit en ligne.", "B", 21, c["muted"])
    # status chip
    s.add(f'<rect x="{x}" y="345" width="506" height="44" rx="22" fill="{c["surface"]}" stroke="{c["line"]}" stroke-width="1.5"/>')
    s.add(f'<circle class="pulse" cx="{x+24}" cy="367" r="6" fill="{c["teal"]}"/>')
    s.add(f'<circle cx="{x+24}" cy="367" r="6" fill="{c["teal"]}"/>')
    s.text(x + 42, 372, "Recherche un stage ou une alternance · Data Scientist", "M5", 13.5, c["ink"])
    s.text(x, 414, "Île-de-France · mobile partout en France", "M", 13, c["faint"])

    # ROC figure
    X0, Y0, S = 800, 74, 300   # plot origin top-left, size
    bx, by = X0, Y0 + S        # bottom-left
    s.text(X0, Y0 - 22, "fig. 1 — courbe ROC, prédiction du churn", "M", 12.5, c["muted"])
    for t in (0, .25, .5, .75, 1):
        gx, gy = bx + t * S, by - t * S
        s.add(f'<line x1="{gx}" y1="{Y0}" x2="{gx}" y2="{by}" stroke="{c["line"]}" stroke-width="1"/>')
        s.add(f'<line x1="{bx}" y1="{gy}" x2="{bx+S}" y2="{gy}" stroke="{c["line"]}" stroke-width="1"/>')
    for t, lab in ((0, "0"), (.5, "0,5"), (1, "1")):
        s.text(bx + t * S, by + 20, lab, "M", 11.5, c["faint"], anchor="middle")
        s.text(bx - 10, by - t * S + 4, lab, "M", 11.5, c["faint"], anchor="end")
    s.add(f'<line x1="{bx}" y1="{by}" x2="{bx+S}" y2="{Y0}" stroke="{c["faint"]}" stroke-width="1.5" stroke-dasharray="4 5"/>')
    s.add(f'<line x1="{bx}" y1="{by}" x2="{bx+S}" y2="{by}" stroke="{c["muted"]}" stroke-width="1.5"/>')
    s.add(f'<line x1="{bx}" y1="{by}" x2="{bx}" y2="{Y0}" stroke="{c["muted"]}" stroke-width="1.5"/>')
    k = 1 / (1 - 0.835) - 1     # y = 1-(1-x)^k  has AUC = 0.835
    pts = [(i / 60, 1 - (1 - i / 60) ** k) for i in range(61)]
    d = " ".join(f"{'M' if i == 0 else 'L'}{bx+px*S:.1f},{by-py*S:.1f}" for i, (px, py) in enumerate(pts))
    s.add(f'<path class="area" d="{d} L{bx+S},{by} Z" fill="{c["signal_soft"]}" fill-opacity=".10"/>')
    s.add(f'<path class="curve" pathLength="1" d="{d}" fill="none" stroke="{c["signal"]}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>')
    s.add('<g class="late">')
    s.text(bx + S - 14, by - 58, "AUC 0,835", "D", 30, c["signal"], anchor="end", ls=-.5)
    s.text(bx + S - 14, by - 34, "régression logistique", "M", 12, c["muted"], anchor="end")
    s.add('</g>')
    s.text(bx + S, by + 44, "taux de faux positifs →", "M", 12, c["muted"], anchor="end")
    s.text(0, 0, "taux de vrais positifs →", "M", 12, c["muted"], anchor="end",
           extra=f'transform="translate({bx-36},{Y0}) rotate(-90)"')
    return s


# ---------------------------------------------------------------- cards
def card_base(s, eyebrow, title, desc, stack, cta="voir le dépôt →", desc_y=126, eyebrow_color=None):
    c = s.c
    s.frame(c["surface"], radius=16, dots=False)
    s.text(32, 48, eyebrow, "M5", 12.5, eyebrow_color or c["signal"], ls=1.8)
    s.text(32, 88, title, "T", 29, c["ink"], ls=-.4)
    for i, line in enumerate(desc):
        s.text(32, desc_y + i * 25, line, "B", 17, c["muted"])
    s.add(f'<line x1="32" y1="{s.h-58}" x2="{s.w-32}" y2="{s.h-58}" stroke="{c["line"]}" stroke-width="1.2"/>')
    s.text(32, s.h - 28, stack, "M", 12.5, c["muted"])
    s.text(s.w - 32, s.h - 28, cta, "M5", 12.5, c["ink"], anchor="end")


def card_churn(theme):
    s = SVG(600, 340, theme, "Prédiction du churn clients — AUC 0,835, 8 départs sur 10 détectés")
    c = s.c
    card_base(s, "MACHINE LEARNING · CLASSIFICATION", "Prédiction du churn",
              ["Repérer les clients d’un", "opérateur télécom qui vont", "résilier, pour agir avant.",
               "7 043 clients · IBM Telco"],
              "python · pandas · scikit-learn")
    gx, gy = 364, 132
    for i in range(10):
        cx, cy = gx + (i % 5) * 44, gy + (i // 5) * 44
        if i < 8:
            s.add(f'<circle cx="{cx}" cy="{cy}" r="14" fill="{c["teal"]}"/>')
        else:
            s.add(f'<circle cx="{cx}" cy="{cy}" r="13" fill="none" stroke="{c["faint"]}" stroke-width="2" stroke-dasharray="3 3"/>')
    s.text(gx - 14, 238, "8 / 10", "D", 30, c["teal"], ls=-.5)
    s.text(gx - 14, 260, "départs détectés · rappel 80 %", "M", 12, c["muted"])
    return s


def card_sales(theme):
    s = SVG(600, 340, theme, "Analyse des ventes d'un magasin — décembre 13,5 % du CA annuel, samedi 24 % du CA hebdomadaire")
    c = s.c
    card_base(s, "ANALYSE · SQL", "Analyse des ventes",
              ["100 000 transactions de", "3 boutiques : ce qui fait", "vraiment le chiffre", "d’affaires."],
              "python · sql · sqlite · matplotlib")
    gx, w = 344, 224
    for row, (val, frac, lab) in enumerate((("13,5 %", .135, "du CA annuel en décembre"),
                                            ("24 %", .24, "du CA hebdo le samedi"))):
        y = 134 + row * 84
        s.text(gx, y, val, "D", 28, c["signal"], ls=-.5)
        s.add(f'<rect x="{gx}" y="{y+12}" width="{w}" height="8" rx="4" fill="{c["line"]}"/>')
        s.add(f'<rect x="{gx}" y="{y+12}" width="{w*frac:.1f}" height="8" rx="4" fill="{c["signal"]}"/>')
        s.text(gx, y + 40, lab, "M", 12, c["muted"])
    return s


def card_objely(theme):
    s = SVG(1200, 360, theme, "Objely — plateforme de restitution d'objets perdus avec rapprochement automatique calculé en SQL")
    c = s.c
    card_base(s, "PRODUIT EN LIGNE · DONNÉES", "Objely",
              ["Plateforme d’objets perdus et trouvés.", "Les déclarations sont rapprochées",
               "automatiquement par un score calculé", "directement en SQL, puis la restitution",
               "est accompagnée jusqu’au bout."],
              "next.js · typescript · supabase · postgresql · gemini",
              cta="démo : objely.vercel.app →", desc_y=128)
    # matching diagram
    lx, rx, cx = 600, 1080, 840
    top = 52
    crit = ["catégorie", "couleurs", "marque", "lieu", "date"]
    for side, x, lab in (("l", lx, "objet perdu"), ("r", rx, "objet trouvé")):
        s.add(f'<rect x="{x-66}" y="{top}" width="132" height="34" rx="17" fill="none" stroke="{c["muted"]}" stroke-width="1.5"/>')
        s.text(x, top + 22, lab, "M5", 12.5, c["ink"], anchor="middle")
    for i, name in enumerate(crit):
        y = top + 62 + i * 26
        s.add(f'<line x1="{lx+28}" y1="{y-4}" x2="{cx-58}" y2="{y-4}" stroke="{c["line"]}" stroke-width="1.5"/>')
        s.add(f'<line x1="{cx+58}" y1="{y-4}" x2="{rx-28}" y2="{y-4}" stroke="{c["line"]}" stroke-width="1.5"/>')
        s.add(f'<circle cx="{lx+28}" cy="{y-4}" r="3.5" fill="{c["muted"]}"/>')
        s.add(f'<circle cx="{rx-28}" cy="{y-4}" r="3.5" fill="{c["muted"]}"/>')
        s.text(cx, y, name, "M", 12.5, c["muted"], anchor="middle")
    s.add(f'<line x1="{lx}" y1="{top+34}" x2="{lx}" y2="{top+166}" stroke="{c["line"]}" stroke-width="1.5"/>')
    s.add(f'<line x1="{rx}" y1="{top+34}" x2="{rx}" y2="{top+166}" stroke="{c["line"]}" stroke-width="1.5"/>')
    s.add(f'<rect x="{cx-70}" y="{top+176}" width="140" height="36" rx="18" fill="{c["signal"]}"/>')
    s.text(cx, top + 199, "score SQL", "M5", 13, c["surface"], anchor="middle")
    s.add(f'<path d="M{lx},{top+166} Q{lx},{top+194} {cx-70},{top+194}" fill="none" stroke="{c["line"]}" stroke-width="1.5"/>')
    s.add(f'<path d="M{rx},{top+166} Q{rx},{top+194} {cx+70},{top+194}" fill="none" stroke="{c["line"]}" stroke-width="1.5"/>')
    # 80 migrations ticks
    s.text(32, 284, "80 migrations PostgreSQL · sécurité par ligne", "M", 12, c["muted"])
    for i in range(80):
        s.add(f'<rect x="{32+i*6.2:.1f}" y="244" width="2.4" height="{10 if i%10 else 14}" '
              f'y-offset="0" fill="{c["signal"] if i%10==0 else c["faint"]}"/>')
    return s


def card_devis(theme):
    s = SVG(600, 340, theme, "Devis Maker — prospection assistée par IA pour une menuiserie à Abidjan")
    c = s.c
    card_base(s, "CLIENT RÉEL · ABIDJAN", "Devis Maker",
              ["Devis et prospection assistée par IA", "pour une menuiserie, livré et utilisé."],
              "next.js · python · sqlite · groq")
    nodes = ["Google", "SQLite", "Llama 3.3", "CSV · WA"]
    w, gap, y = 118, 16, 196
    for i, n in enumerate(nodes):
        x = 32 + i * (w + gap)
        hi = n == "Llama 3.3"
        s.add(f'<rect x="{x}" y="{y}" width="{w}" height="44" rx="10" fill="{c["signal"] if hi else "none"}" '
              f'stroke="{c["signal"] if hi else c["muted"]}" stroke-width="1.5"/>')
        s.text(x + w / 2, y + 27, n, "M5", 13, c["surface"] if hi else c["ink"], anchor="middle")
        if i < 3:
            ax = x + w
            s.add(f'<path d="M{ax+3},{y+22} H{ax+gap-3} M{ax+gap-7},{y+18} L{ax+gap-3},{y+22} L{ax+gap-7},{y+26}" '
                  f'fill="none" stroke="{c["muted"]}" stroke-width="1.5" stroke-linecap="round"/>')
    s.text(32, y + 66, "collecte → stockage → messages personnalisés → export", "M", 12, c["faint"])
    return s


def card_dg(theme):
    s = SVG(600, 340, theme, "DecisionGuard AI — plateforme d'aide à la décision multi-agents, en cours")
    c = s.c
    card_base(s, "IA MULTI-AGENTS · EN COURS", "DecisionGuard AI",
              ["Des agents analysent une décision", "d’entreprise, évaluent les risques et",
               "produisent un rapport (FR / EN)."],
              "fastapi · next.js · postgres · redis · docker", eyebrow_color=c["teal"])
    agents = ["analyse", "risques", "scénarios", "vérification"]
    y, w = 218, 96
    for i, a in enumerate(agents):
        x = 32 + i * (w + 8)
        s.add(f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="15" fill="none" stroke="{c["muted"]}" stroke-width="1.5"/>')
        s.text(x + w / 2, y + 20, a, "M", 12, c["ink"], anchor="middle")
    rxx = 32 + 4 * (w + 8) + 4
    s.add(f'<path d="M{rxx-6},{y+15} H{rxx+8} M{rxx+4},{y+11} L{rxx+8},{y+15} L{rxx+4},{y+19}" fill="none" stroke="{c["muted"]}" stroke-width="1.5" stroke-linecap="round"/>')
    s.add(f'<rect x="{rxx+14}" y="{y}" width="{s.w-32-rxx-14}" height="30" rx="15" fill="{c["teal"]}"/>')
    s.text((rxx + 14 + s.w - 32) / 2, y + 20, "rapport", "M5", 12, c["surface"], anchor="middle")
    return s


# ---------------------------------------------------------------- stack
def stack(theme):
    s = SVG(1200, 300, theme, "Compétences : data science, données, IA générative, produit")
    c = s.c
    s.frame(c["surface"], radius=16, dots=False)
    cols = [
        ("DATA SCIENCE", ["Python", "pandas · NumPy", "scikit-learn", "Matplotlib", "Jupyter"]),
        ("DONNÉES", ["SQL", "PostgreSQL · SQLite", "MongoDB", "Modélisation", "Pipelines de données"]),
        ("IA GÉNÉRATIVE", ["Gemini", "Llama 3.3 (Groq)", "Ingénierie de prompts", "Systèmes multi-agents", "Assistants"]),
        ("PRODUIT", ["TypeScript · Next.js", "React Native · Expo", "FastAPI · Node.js", "Supabase · RLS", "Docker · Vercel"]),
    ]
    cw = (1200 - 64) / 4
    for i, (h, items) in enumerate(cols):
        x = 32 + i * cw + (0 if i == 0 else 24)
        if i:
            s.add(f'<line x1="{32+i*cw}" y1="36" x2="{32+i*cw}" y2="226" stroke="{c["line"]}" stroke-width="1.2"/>')
        s.text(x, 58, h, "M5", 12.5, c["teal"] if i == 0 else c["signal"], ls=1.8)
        for j, it in enumerate(items):
            s.text(x, 98 + j * 28, it, "B", 17, c["ink"] if j == 0 else c["muted"])
    s.add(f'<line x1="32" y1="246" x2="1168" y2="246" stroke="{c["line"]}" stroke-width="1.2"/>')
    s.text(32, 276, "en cours d’approfondissement : statistiques · Power BI · deep learning", "M", 12.5, c["muted"])
    return s


for name, fn in [("hero", hero), ("churn", card_churn), ("ventes", card_sales), ("objely", card_objely),
                 ("devis", card_devis), ("decisionguard", card_dg), ("stack", stack)]:
    save(name, fn)
    print("ok", name)
