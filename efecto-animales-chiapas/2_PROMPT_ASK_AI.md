# Alternativa: que Claude Code lo arme dentro de Effect House (Ask AI)

Úsalo si prefieres una ruleta con número aleatorio real (la plantilla Randomizer decide el resultado por tiempo de giro) o si quieres dos personas con resultados independientes.

## Preparación
1. En Effect House: **proyecto nuevo vacío** → **File → Save As** en una carpeta.
2. Copia dentro de esa carpeta: `assets/titulo.png`, la carpeta `assets/tarjetas/` y `datos/animales_chiapas_50.json`.
3. Botón **Ask AI** → elige **Claude Code** → acepta el aviso.
4. En **More Settings**: apaga *Use Temporary Session* y pon *Share Preview Screenshots* en *Allow for This Project*.
5. Pega el prompt de abajo completo.

## Prompt

```
Construye desde cero un efecto de TikTok 9:16 llamado "¿Qué animal de Chiapas eres?". Es un randomizer tipo "which X are you" con 50 resultados. Usa scripts APJS (TypeScript), no Visual Scripting. El objetivo es que pase la revisión de TikTok a la primera, así que prioriza que funcione sin errores en cualquier teléfono.

ASSETS (ya están en la carpeta del proyecto):
- ./titulo.png → tarjeta de título, 1024x512, con transparencia.
- ./tarjetas/01_*.png … ./tarjetas/50_*.png → 50 tarjetas de resultado, 1024x1280, con transparencia. Impórtalas como texturas en orden numérico.
- ./animales_chiapas_50.json → datos de cada animal (solo como referencia; el texto ya viene dentro de cada tarjeta).

COMPORTAMIENTO:
1. Al abrir: el título flota centrado arriba de la cabeza y la sigue (head tracking). Ancho ≈55% de la pantalla.
2. Al tocar la pantalla o al empezar a grabar (lo primero que pase): el título se desvanece en 0.4 s y empieza la ruleta en el mismo lugar: las tarjetas cambian rápido (~25 por segundo) y frenan con ease-out durante 3.5 s.
3. El resultado se elige con un número aleatorio uniforme 0–49 al iniciar el giro, y la secuencia de frenado termina exactamente en esa tarjeta.
4. Al detenerse: "pop" de escala 1.0 → 1.15 → 1.0 en 0.3 s y la tarjeta se queda fija el resto del video.
5. Un segundo toque reinicia (vuelve el título).
6. Con dos caras, cada una tiene su propia ruleta y resultado.
7. Sin cara en cámara: no debe haber errores; muestra el título centrado en la parte superior del área segura y retoma el seguimiento cuando aparezca una cara.
8. Todo dentro del área segura (nada bajo el botón de grabar ni sobre la barra superior). Que la tarjeta no se corte por arriba cuando la cara está muy cerca.

INSPECTOR: expón spinDuration (3.5), cardWidthPercent (55), titleTexture, cardTextures (arreglo de 50), popEnabled (true).

VERIFICACIÓN: con la cámara de prueba toma capturas del Preview, simula toques y confirma: aparece el título, gira, frena en una tarjeta al azar (prueba 5 veces y dime qué salió), el segundo toque reinicia y no hay errores en la consola con cero, una y dos caras. Corrige los errores de compilación antes de terminar. Al final dame un resumen de los objetos creados y del script.
```

## Ajustes opcionales (uno por mensaje, después de que funcione)
- `Agrega un "tick" corto en cada cambio de tarjeta y un "ding" al detenerse, usando sonidos de la Asset Library (sin música con derechos).`
- `Al detenerse, lanza confeti verde y dorado 1 segundo con un sistema de partículas ligero.`
- `Sube la tarjeta un 10 % para que no tape la frente cuando la persona está cerca.`
