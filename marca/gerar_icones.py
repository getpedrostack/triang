"""Gera o ícone mestre (SVG) e os PNGs do Triângulo OCR na paleta Original Coffee Roaster.

Geometria A (viewBox 512):
- triângulo equilátero, raio circunscrito R = 170, traço 26, cantos redondos;
- centroide em y = 256 + R/8 (centro óptico: meio caminho entre caixa e centroide);
- xícaras num triângulo concêntrico; folga g = r/2 igual entre xícaras e até o traço;
- xícara diferente no topo, no eixo de simetria.
Cores (D1 · marca plena): fundo petróleo #104a53 com luz no alto, triângulo pêssego #fad9b8,
xícaras caramelo #da9c5e; a diferente é o "olho" do escudo: anel cobre #ba744d com miolo café #5d3007
(mesma proporção do escudo: miolo 13/22 do anel).
Favicon (32 px) tem geometria própria: triângulo maior, traço 34 e folga 0,9 r, para as xícaras não se fundirem.
Uso (na pasta do app): python marca/gerar_icones.py .
"""
import math, sys, pathlib
from playwright.sync_api import sync_playwright

OUT = pathlib.Path(sys.argv[1])
S3 = math.sqrt(3)
PETROLEO, CAFE, COBRE, CARAMELO, PESSEGO = '#104a53', '#5d3007', '#ba744d', '#da9c5e', '#fad9b8'
FUNDO = ('#17606b', PETROLEO, '#0b363d')  # luz radial: centro, meio, borda


def geo(R=170.0, sw=26.0, k=0.5):
    rc = S3 * (R - sw) / (2 * S3 * (k + 1) + 2 + k)
    g = k * rc
    d = R - 2 * g - sw - 2 * rc
    cx, cy = 256.0, 256.0 + R / 8
    v = [(cx, cy - R), (cx - R * S3 / 2, cy + R / 2), (cx + R * S3 / 2, cy + R / 2)]
    c = [(cx, cy - d), (cx - d * S3 / 2, cy + d / 2), (cx + d * S3 / 2, cy + d / 2)]
    return dict(R=R, sw=sw, rc=rc, g=g, d=d, v=v, c=c, cx=cx, cy=cy)


def n(x):
    return f'{x:.2f}'.rstrip('0').rstrip('.')


def glyph(G):
    v, c, rc = G['v'], G['c'], G['rc']
    p = 'M{} {} L{} {} L{} {} Z'.format(*(n(t) for xy in v for t in xy))
    return (f'<path d="{p}" fill="none" stroke="{PESSEGO}" stroke-width="{n(G["sw"])}" stroke-linejoin="round"/>'
            f'<circle cx="{n(c[0][0])}" cy="{n(c[0][1])}" r="{n(rc)}" fill="{COBRE}"/>'
            f'<circle cx="{n(c[0][0])}" cy="{n(c[0][1])}" r="{n(rc * 13 / 22)}" fill="{CAFE}"/>'
            f'<circle cx="{n(c[1][0])}" cy="{n(c[1][1])}" r="{n(rc)}" fill="{CARAMELO}"/>'
            f'<circle cx="{n(c[2][0])}" cy="{n(c[2][1])}" r="{n(rc)}" fill="{CARAMELO}"/>')


def icon_svg(G):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">'
            '<defs><radialGradient id="g" cx="50%" cy="36%" r="78%">'
            f'<stop offset="0" stop-color="{FUNDO[0]}"/><stop offset=".62" stop-color="{FUNDO[1]}"/>'
            f'<stop offset="1" stop-color="{FUNDO[2]}"/></radialGradient></defs>'
            '<rect width="512" height="512" fill="url(#g)"/>' + glyph(G) + '</svg>\n')


def check(G):
    """Confere folgas e zona segura (círculo de raio 204,8 no centro)."""
    v, c, rc, sw = G['v'], G['c'], G['rc'], G['sw']
    def dist_line(p, a, b):
        return abs((b[0]-a[0])*(a[1]-p[1]) - (a[0]-p[0])*(b[1]-a[1])) / math.dist(a, b)
    edges = [(v[0], v[1]), (v[1], v[2]), (v[2], v[0])]
    gaps_edge = [min(dist_line(p, a, b) for a, b in edges) - sw/2 - rc for p in c]
    gaps_cup = [math.dist(c[i], c[j]) - 2*rc for i, j in ((0, 1), (1, 2), (0, 2))]
    far = max(math.dist(p, (256, 256)) for p in v) + sw/2
    return gaps_edge, gaps_cup, far


G = geo()
ge, gc, far = check(G)
print('r xicara', round(G['rc'], 2), '| folga borda', [round(x, 2) for x in ge],
      '| folga entre', [round(x, 2) for x in gc], '| ponto mais distante', round(far, 1), '(limite 204,8)')
assert max(ge) - min(ge) < .01 and max(gc) - min(gc) < .01 and abs(ge[0] - gc[0]) < .01 and far <= 204.8
svg = icon_svg(G)

F = geo(R=200.0, sw=34.0, k=0.9)
fe, fc, _ = check(F)
print('favicon r', round(F['rc'], 2), '| folga borda', round(fe[0], 2), '| folga entre', round(fc[0], 2))
svg_fav = icon_svg(F)

(OUT / 'icon.svg').write_text(svg, encoding='utf-8', newline='\n')

alvos = [('icon-32.png', 32, svg_fav), ('apple-touch-icon.png', 180, svg), ('icon-192.png', 192, svg), ('icon-512.png', 512, svg)]
with sync_playwright() as pw:
    br = pw.chromium.launch(channel='msedge')
    for nome, px, sv in alvos:
        pg = br.new_page(viewport={'width': px, 'height': px}, device_scale_factor=1)
        pg.set_content(f'<html><body style="margin:0;background:#000">'
                       f'<div style="width:{px}px;height:{px}px">{sv.replace("<svg ", f"<svg width={px} height={px} ")}</div></body></html>')
        pg.screenshot(path=str(OUT / nome), clip={'x': 0, 'y': 0, 'width': px, 'height': px}, omit_background=False)
        pg.close()
    br.close()

from PIL import Image
for nome, px, _ in alvos:
    im = Image.open(OUT / nome).convert('RGB')
    assert im.size == (px, px), (nome, im.size)
    im.save(OUT / nome, optimize=True)
    print(nome, im.size, (OUT / nome).stat().st_size, 'bytes')

# geometria do favicon para a marca da barra superior (#brandMark, escrita à mão no index.html)
print('JS barra', dict(v=[(round(x, 2), round(y, 2)) for x, y in F['v']], c=[(round(x, 2), round(y, 2)) for x, y in F['c']],
                      rc=round(F['rc'], 2), miolo=round(F['rc'] * 13 / 22, 2)))
