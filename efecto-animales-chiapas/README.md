# ¿Qué animal de Chiapas eres? — efecto de TikTok (Effect House)

Todo lo necesario para armar el efecto en Effect House y mandarlo a revisión.

| Carpeta / archivo | Qué es |
|---|---|
| `assets/titulo.png` | Tarjeta de título (1024×512) que flota sobre la cabeza |
| `assets/tarjetas/01…50_*.png` | Las 50 tarjetas de resultado (1024×1280), ya terminadas y sin textos provisionales |
| `assets/icono.png` | Ícono del efecto (512×512) para la pantalla de envío |
| `datos/animales_chiapas_50.csv` / `.json` | Los 50 animales (nombre, rasgo, dato, prompt de IA) |
| `herramientas/generar_assets.py` | Regenera título, tarjetas e ícono si cambias el CSV/JSON |
| `1_ARMAR_EN_EFFECT_HOUSE.md` | **Empieza aquí.** Paso a paso con la plantilla Randomizer (sin programar) |
| `2_PROMPT_ASK_AI.md` | Alternativa: que Claude Code lo arme dentro de Effect House con Ask AI |
| `3_ENVIAR_A_APROBACION.md` | Nombre, descripción, video demo y lista de revisión antes de enviar |

## Cambios respecto al kit original

- Las tarjetas decían "AQUÍ VA LA ILUSTRACIÓN DEL ANIMAL (reemplazar PNG)". Así las rechazan por contenido incompleto, así que se rehicieron todas: nombre grande, nombre científico, rasgo, dato real y un motivo por grupo (huella, pisada de ave, hojas).
- En el título se cortaban el "¿" y el "DE". Ya está corregido.
- Se agregó el ícono.

Para cambiar un texto: edita `datos/animales_chiapas_50.json` y corre `pip install pillow && python3 herramientas/generar_assets.py`.
Cuando tengas ilustraciones reales, puedes reemplazar las tarjetas manteniendo el mismo nombre de archivo y el tamaño de 1024×1280.
