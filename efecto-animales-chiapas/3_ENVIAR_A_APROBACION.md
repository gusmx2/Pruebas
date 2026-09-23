# Enviar el efecto a aprobación

En Effect House: botón **Submit** (arriba a la derecha). Llena la pantalla con lo siguiente.

## Textos para copiar y pegar

**Nombre del efecto** (corto y buscable):
```
Qué animal de Chiapas eres
```

**Descripción / notas para el revisor** (si la pide):
```
Efecto aleatorio: al tocar la pantalla, una ruleta de 50 tarjetas gira sobre la cabeza del usuario y se detiene en un animal nativo de Chiapas, México (jaguar, quetzal, tapir, etc.), con su nombre científico, un rasgo de personalidad divertido y un dato real del animal. Tocar de nuevo reinicia. Sin marcas, música ni personajes de terceros.
```

**Instrucción en pantalla (hint)**: elige la opción **"Tap the screen" / "Toca la pantalla"** de la lista de hints de Effect House.

**Categoría / etiquetas** (si las pide): Divertido / Interactivo / Aleatorio (random, quiz, animales, Chiapas, México).

**Ícono**: `assets/icono.png`.

## Video demo
Grábalo con el mismo efecto ya instalado en tu teléfono (Preview in TikTok), en vertical 9:16:

1. 0–2 s: cara a cámara con el título "¿Qué animal de Chiapas eres?" sobre la cabeza.
2. 2–6 s: tocas la pantalla, gira la ruleta y se detiene.
3. 6–10 s: reacción real al resultado ("¡me salió zanate!").
4. Opcional: una segunda persona repite.

Reglas para que no lo rechacen: que se vea **exactamente lo que hace el efecto** (sin edición, filtros extra, texto encima ni música con derechos), buena luz, cara visible y sin logos de marcas en la ropa o el fondo.

## Revisión final antes de dar "Submit"

Motivos de rechazo comunes y cómo queda este efecto:

- [x] **Contenido provisional o incompleto.** Las tarjetas y el título ya están terminados, sin "reemplazar PNG".
- [x] **Textos cortados o ilegibles.** Revisado en las 50 tarjetas.
- [x] **Marcas, logos o personajes con derechos.** No hay. Las fuentes (DejaVu) son de licencia libre.
- [x] **Contenido engañoso.** Es un juego de azar para divertirse, no un test "científico". No prometas en la descripción que "descubre tu personalidad real".
- [ ] **El efecto no funciona o se ve roto.** Pruébalo en el teléfono (paso 5 de la guía), sin cara, con una cara y con dos.
- [ ] **El ícono no representa el efecto.** El ícono es una huella con signo de pregunta sobre el verde de las tarjetas. Si prefieres, usa una captura del efecto funcionando.
- [ ] **El video demo no coincide con el efecto.** Grábalo con la versión final, sin cambios después.
- [ ] **Assets de ejemplo que sobran.** Borra de Assets todo lo que dejó la plantilla y no uses.
- [ ] **Tamaño del efecto.** Effect House avisa si te pasas del límite. Si pasa, baja las tarjetas a 768×960 (en `generar_assets.py` cambia la última línea de `tarjeta()` para guardar a menor tamaño) y vuelve a importarlas.

## Después de enviar
- La revisión suele tardar entre unas horas y unos días. El estado aparece en Effect House (**My Effects**) y en el sitio de Effect House.
- Si lo rechazan, el aviso dice el motivo: corrige solo eso y vuelve a enviar.
- Cuando se apruebe, graba 5–8 videos con el efecto la primera semana para que empiece a circular.
