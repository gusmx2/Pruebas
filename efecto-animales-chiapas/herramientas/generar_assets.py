"""Genera los assets del efecto "¿Qué animal de Chiapas eres?".

Salida (en ../assets):
  - titulo.png              1024x512  tarjeta de título que flota sobre la cabeza
  - tarjetas/NN_*.png       1024x1280 una tarjeta de resultado por animal
  - icono.png               512x512   ícono para la publicación en Effect House

Uso:  pip install pillow && python3 generar_assets.py
Edita ../datos/animales_chiapas_50.json y vuelve a correrlo para regenerar todo.
"""
import json
import math
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
DATOS = os.path.join(BASE, "..", "datos", "animales_chiapas_50.json")
SALIDA = os.path.join(BASE, "..", "assets")

VERDE = (31, 113, 71)
VERDE_OSCURO = (20, 78, 49)
BLANCO = (255, 255, 255)
CREMA = (250, 247, 238)
TINTA = (25, 25, 25)
GRIS = (90, 90, 90)

# Color de acento por grupo (pastilla y marco interior)
COLOR_GRUPO = {
    "Mamífero": (176, 108, 40),
    "Ave": (22, 128, 160),
    "Reptil": (104, 128, 36),
    "Anfibio": (206, 60, 50),
    "Pez": (40, 90, 170),
    "Insecto": (120, 70, 170),
}

FUENTES = {
    "bold": ["DejaVuSans-Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
             "/Library/Fonts/Arial Bold.ttf", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"],
    "regular": ["DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                "/Library/Fonts/Arial.ttf", "/System/Library/Fonts/Supplemental/Arial.ttf"],
    "italic": ["DejaVuSans-Oblique.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf",
               "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf",
               "/Library/Fonts/Arial Italic.ttf", "/System/Library/Fonts/Supplemental/Arial Italic.ttf"],
}


def fuente(estilo, tam):
    for ruta in FUENTES[estilo]:
        try:
            return ImageFont.truetype(ruta, tam)
        except OSError:
            continue
    raise SystemExit(f"No encontré una fuente '{estilo}'. Instala DejaVu o ajusta FUENTES.")


def ancho(draw, texto, f):
    x0, _, x1, _ = draw.textbbox((0, 0), texto, font=f)
    return x1 - x0


def ajustar(draw, texto, estilo, tam_max, ancho_max, tam_min=20):
    """Fuente más grande (<= tam_max) con la que el texto cabe en ancho_max."""
    tam = tam_max
    while tam > tam_min and ancho(draw, texto, fuente(estilo, tam)) > ancho_max:
        tam -= 2
    return fuente(estilo, tam)


def partir(draw, texto, f, ancho_max):
    """Divide el texto en líneas que caben en ancho_max."""
    lineas, actual = [], ""
    for palabra in texto.split():
        prueba = f"{actual} {palabra}".strip()
        if ancho(draw, prueba, f) <= ancho_max:
            actual = prueba
        else:
            if actual:
                lineas.append(actual)
            actual = palabra
    if actual:
        lineas.append(actual)
    return lineas


def centrado(draw, y, texto, f, color, W):
    draw.text((W / 2, y), texto, font=f, fill=color, anchor="mt")
    _, y0, _, y1 = draw.textbbox((0, 0), texto, font=f)
    return y + (y1 - y0)


def huella(draw, cx, cy, s, color):
    """Huella de animal: almohadilla + 4 dedos."""
    draw.ellipse([cx - 0.62 * s, cy - 0.15 * s, cx + 0.62 * s, cy + 0.72 * s], fill=color)
    for dx, dy, r in [(-0.78, -0.42, 0.24), (-0.30, -0.80, 0.26), (0.30, -0.80, 0.26), (0.78, -0.42, 0.24)]:
        x, y = cx + dx * s, cy + dy * s
        draw.ellipse([x - r * s, y - r * 1.25 * s, x + r * s, y + r * 1.25 * s], fill=color)


def pisada_ave(draw, cx, cy, s, color):
    """Pisada de ave: tres dedos hacia arriba y uno hacia abajo."""
    w = int(0.16 * s)
    for ang in (-90, -125, -55):
        a = math.radians(ang)
        draw.line([cx, cy, cx + math.cos(a) * s, cy + math.sin(a) * s], fill=color, width=w)
    draw.line([cx, cy, cx, cy + 0.55 * s], fill=color, width=w)
    draw.ellipse([cx - w, cy - w, cx + w, cy + w], fill=color)


def hoja(draw, cx, cy, largo, angulo, color):
    """Hoja simple (polígono lanceolado) para decorar."""
    pts = []
    for i in range(41):
        t = i / 40
        pts.append((t * largo, math.sin(t * math.pi) * largo * 0.22))
    for i in range(40, -1, -1):
        t = i / 40
        pts.append((t * largo, -math.sin(t * math.pi) * largo * 0.22))
    a = math.radians(angulo)
    rot = [(cx + x * math.cos(a) - y * math.sin(a), cy + x * math.sin(a) + y * math.cos(a)) for x, y in pts]
    draw.polygon(rot, fill=color)


def titulo():
    W, H, S = 1024, 512, 2  # se dibuja al doble y se reduce (bordes suaves)
    im = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    m = 16 * S
    d.rounded_rectangle([m, m, W * S - m, H * S - m], radius=70 * S, fill=VERDE, outline=BLANCO, width=10 * S)
    util = W * S - 2 * 90 * S
    f1 = ajustar(d, "¿QUÉ ANIMAL DE", "bold", 96 * S, util)
    f2 = ajustar(d, "CHIAPAS", "bold", 150 * S, util)
    f3 = ajustar(d, "ERES?", "bold", 96 * S, util)
    y = 70 * S
    y = centrado(d, y, "¿QUÉ ANIMAL DE", f1, BLANCO, W * S) + 30 * S
    y = centrado(d, y, "CHIAPAS", f2, (255, 214, 80), W * S) + 30 * S
    centrado(d, y, "ERES?", f3, BLANCO, W * S)
    im.resize((W, H), Image.LANCZOS).save(os.path.join(SALIDA, "titulo.png"))


def texto_inferior(d, a, y, util, W, tam_rasgo, tam_et):
    """Dibuja rasgo y etiqueta desde y; devuelve la y final."""
    f_rasgo = fuente("bold", tam_rasgo)
    for ln in partir(d, a["rasgo"], f_rasgo, util):
        y = centrado(d, y, ln, f_rasgo, TINTA, W) + tam_rasgo // 4
    y += tam_rasgo // 4
    f_et = fuente("regular", tam_et)
    for ln in partir(d, a["etiqueta"], f_et, util):
        y = centrado(d, y, ln, f_et, GRIS, W) + tam_et // 3
    return y


def tarjeta(a, total):
    W, H, S = 1024, 1280, 2
    im = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    acento = COLOR_GRUPO.get(a["grupo"], VERDE)
    m = 16 * S
    # Marco exterior verde y panel crema
    d.rounded_rectangle([m, m, W * S - m, H * S - m], radius=80 * S, fill=VERDE)
    p = 56 * S
    d.rounded_rectangle([p, 190 * S, W * S - p, H * S - 150 * S], radius=50 * S, fill=CREMA)

    # Encabezado
    centrado(d, 58 * S, "¿QUÉ ANIMAL DE CHIAPAS ERES?", ajustar(d, "¿QUÉ ANIMAL DE CHIAPAS ERES?", "bold", 58 * S, W * S - 2 * 80 * S), BLANCO, W * S)
    centrado(d, 128 * S, "TE TOCÓ…", fuente("regular", 40 * S), (210, 235, 220), W * S)

    # Decoración: hojas en las esquinas del panel y huella tenue
    tenue = acento + (40,)
    capa = Image.new("RGBA", im.size, (0, 0, 0, 0))
    dc = ImageDraw.Draw(capa)
    hoja(dc, p + 30 * S, 230 * S, 190 * S, 25, tenue)
    hoja(dc, p + 20 * S, 260 * S, 150 * S, 60, tenue)
    hoja(dc, W * S - p - 30 * S, 230 * S, 190 * S, 155, tenue)
    hoja(dc, W * S - p - 20 * S, 260 * S, 150 * S, 120, tenue)
    if a["grupo"] == "Mamífero":
        huella(dc, W * S / 2, 420 * S, 105 * S, acento + (230,))
    elif a["grupo"] == "Ave":
        pisada_ave(dc, W * S / 2, 430 * S, 120 * S, acento + (230,))
    else:
        for ang in (200, 250, 290, 340):
            hoja(dc, W * S / 2, 470 * S, 150 * S, ang, acento + (200,))
    im.alpha_composite(capa)

    util = W * S - 2 * (p + 50 * S)
    # Nombre (grande, auto-ajustado; si es largo, parte el paréntesis a otra línea)
    nombre = a["nombre"].upper()
    extra = ""
    if "(" in nombre and ancho(d, nombre, fuente("bold", 110 * S)) > util:
        nombre, extra = nombre.split("(", 1)
        nombre, extra = nombre.strip(), "(" + extra.strip()
    y = 580 * S
    y = centrado(d, y, nombre, ajustar(d, nombre, "bold", 130 * S, util, 60 * S), VERDE_OSCURO, W * S) + 18 * S
    if extra:
        y = centrado(d, y, extra, ajustar(d, extra, "bold", 60 * S, util), VERDE_OSCURO, W * S) + 14 * S
    y = centrado(d, y + 6 * S, a["nombre_cientifico"], ajustar(d, a["nombre_cientifico"], "italic", 44 * S, util), GRIS, W * S) + 34 * S

    # Separador
    d.line([W * S / 2 - 120 * S, y, W * S / 2 + 120 * S, y], fill=acento, width=6 * S)
    y += 36 * S

    # Rasgo de personalidad + etiqueta: se reduce la letra hasta que quepa en el panel
    limite = H * S - 170 * S
    for tam_rasgo, tam_et in [(58, 36), (52, 34), (46, 32), (40, 30)]:
        prueba = im.copy()
        fin = texto_inferior(ImageDraw.Draw(prueba), a, y, util, W * S, tam_rasgo * S, tam_et * S)
        if fin <= limite:
            break
    im.paste(prueba)
    d = ImageDraw.Draw(im)

    # Pie: pastilla de grupo + número
    grupo = a["grupo"].upper()
    f_g = fuente("bold", 40 * S)
    gw = ancho(d, grupo, f_g) + 70 * S
    cy = H * S - 83 * S
    d.rounded_rectangle([W * S / 2 - gw / 2, cy - 38 * S, W * S / 2 + gw / 2, cy + 38 * S], radius=38 * S, fill=acento)
    d.text((W * S / 2, cy), grupo, font=f_g, fill=BLANCO, anchor="mm")
    f_n = fuente("regular", 34 * S)
    d.text((p + 20 * S, cy), f"#{a['id']:02d}/{total}", font=f_n, fill=(210, 235, 220), anchor="lm")
    d.text((W * S - p - 20 * S, cy), "CHIAPAS", font=f_n, fill=(210, 235, 220), anchor="rm")

    im.resize((W, H), Image.LANCZOS).save(os.path.join(SALIDA, "tarjetas", a["archivo"]))


def icono():
    W, S = 512, 2
    im = Image.new("RGBA", (W * S, W * S), VERDE + (255,))
    d = ImageDraw.Draw(im)
    capa = Image.new("RGBA", im.size, (0, 0, 0, 0))
    dc = ImageDraw.Draw(capa)
    for cx, cy, l, ang in [(40, 60, 300, 30), (20, 150, 240, 70), (1000, 60, 300, 150), (1010, 150, 240, 110),
                           (60, 990, 280, -30), (970, 990, 280, 210)]:
        hoja(dc, cx, cy, l, ang, (255, 255, 255, 38))
    im.alpha_composite(capa)
    huella(d, W * S / 2, W * S / 2 + 60, 190, BLANCO)
    d.ellipse([W * S - 330, 120, W * S - 110, 340], fill=(255, 214, 80))
    d.text((W * S - 220, 232), "?", font=fuente("bold", 170), fill=VERDE_OSCURO, anchor="mm")
    im.resize((W, W), Image.LANCZOS).convert("RGB").save(os.path.join(SALIDA, "icono.png"))


def main():
    os.makedirs(os.path.join(SALIDA, "tarjetas"), exist_ok=True)
    animales = json.load(open(DATOS, encoding="utf-8"))
    titulo()
    for a in animales:
        tarjeta(a, len(animales))
    icono()
    print(f"Listo: título, {len(animales)} tarjetas e ícono en {os.path.normpath(SALIDA)}")


if __name__ == "__main__":
    main()
