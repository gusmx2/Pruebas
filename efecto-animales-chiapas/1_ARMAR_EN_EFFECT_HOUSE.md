# Armar el efecto en Effect House (plantilla Randomizer, sin programar)

Es el camino más seguro para un primer efecto: la plantilla ya viene probada por TikTok y solo le cambias las imágenes. Toma unos 30–45 minutos.

> Los nombres de menús pueden variar un poco según tu versión de Effect House. Si algo no aparece igual, busca el equivalente con el mismo nombre en inglés.

## 0. Antes de empezar
1. Descarga esta carpeta completa (`efecto-animales-chiapas`) a tu computadora.
2. Abre Effect House e inicia sesión con **la cuenta de TikTok que va a publicar el efecto** (el crédito "Efecto de @…" sale de esa cuenta).

## 1. Crear el proyecto desde la plantilla
1. En la pantalla de inicio: **Templates** → busca **Randomizer** → elige la versión **2D** (la de "which … are you", con la imagen sobre la cabeza).
2. **File → Save As** → guárdalo como `QueAnimalDeChiapasEres`.
3. Dale **Play** en el Preview para ver cómo funciona la plantilla original antes de tocar nada.

## 2. Importar las imágenes
1. Panel **Assets** → botón **+** → **Import** → **Texture Sequence** (o "Image Sequence") → selecciona las **50** imágenes de `assets/tarjetas/` (todas juntas, se ordenan por el número 01…50).
2. **+** → **Import → From Computer** → `assets/titulo.png`.

## 3. Conectar las imágenes a la plantilla
1. En **Hierarchy**, selecciona el objeto del título (se llama **Title** o similar). En el **Inspector**, en *Texture*, arrastra `titulo.png`.
2. Selecciona el objeto de la ruleta (**RandomAnimationSequence** o similar). En su componente **Animation Sequence**, arrastra la secuencia de 50 tarjetas que importaste.
3. Borra de Assets la secuencia de ejemplo de la plantilla (clic derecho → Delete) para que no quede pesando en el efecto.

## 4. Ajustar tamaño y comportamiento
1. **Tamaño**: con el objeto de la ruleta seleccionado, ajusta la escala hasta que la tarjeta mida más o menos el ancho de la cabeza y medio (≈55 % del ancho de la pantalla). Haz lo mismo con el título.
2. **Posición**: que quede arriba de la cabeza y **no se salga por arriba** de la pantalla cuando la cara está cerca de la cámara (la barra superior de TikTok tapa esa zona).
3. **Tiempo de giro**: abre **Visual Scripting** → subgraph **Randomize** → ajusta:
   - `TapToSpin`: activado (se gira al tocar la pantalla).
   - `TimeToSpin`: **3.5** segundos.
   - `TitleDelay` y `TitleFadeOutTime`: deja los valores por defecto o pon 0.4 s de desvanecido.

## 5. Probar
1. En el Preview, usa las caras de prueba y toca la pantalla: el título desaparece, giran las tarjetas y se detiene en una.
2. Pruébalo **en tu teléfono**: botón **Preview in TikTok** (arriba a la derecha) → escanea el QR desde la app de TikTok.
3. Revisa en el teléfono:
   - [ ] Se lee bien la tarjeta (sin textos cortados).
   - [ ] Funciona con luz baja, con lentes o gorra, y moviéndote.
   - [ ] Si sales de cuadro y vuelves, la tarjeta vuelve a tu cabeza.
   - [ ] Funciona con cámara frontal y trasera (o, si solo es frontal, que no se vea roto con la trasera).
   - [ ] Si la plantilla lo soporta, prueba con dos personas.

## 6. Guardar
**File → Save**. Haz una copia de la carpeta del proyecto antes de cualquier cambio grande.

Luego sigue con `3_ENVIAR_A_APROBACION.md`.
