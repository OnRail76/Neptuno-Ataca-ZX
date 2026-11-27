# NEPTUNO ATACA V1.1 revisada — edición oficial
Tony C. Ware · 2026 · ZX Spectrum 48K · GRIT ENGINE

La base es V1.0, SHA-256 c72b02d640e6aa824dd8e612344355dfa7851140eacfc3d1f62c3cd1499d3ea4. Versión aprobada por el autor. La edición V1.0 se conserva sin modificaciones.

Cinco mapas originales y sus bancos de tiles (comparados sin pérdida), tablas de oleadas, soldados, tanques, jefes y pantallas originales. Nuevos dron circular, pájaro con tres poses y torreta direccional. Corregida la caída accidental desde soldier_anim_dirs hacia air_drone, mediante JP ground_direction. Los aéreos mantienen los cuatro desplazamientos horizontales de DeLuxe; su dibujo se alinea a píxel par, sin cambiar las coordenadas lógicas. Se conserva el título original, sin distintivo DeLuxe.

## Construcción
Desde FUENTES: python3 -m pip install -r requirements.txt; python3 pack.py. Los emisores Python son las fuentes canónicas; generan código máquina, listados ASM, símbolos y TAP. QAOP + SPACE o Kempston. Cargar LOAD "" y pulsar y soltar SPACE/FIRE tras el beep. Truco del título: abajo, soltar, abajo, soltar, FIRE.

## Pruebas
Desde FUENTES: python3 test_v11_sprites.py; python3 test_loader.py; python3 test_009.py; python3 test_campaign011.py; python3 test_audio.py; python3 test_extra.py; python3 test_render.py 1 (repetir 2–5). Registros en PRUEBAS. 480 comprobaciones de dibujo/restauración; 124 apariciones originales, 43 unidades terrestres con disparo; recorrido hasta jefe en cada fase con SPREAD, sin excesos en el modelo (máximo 69.038 T). Modelo Z80/ROM/ULA aproximado; aprobada por el autor en su emulador habitual; sin comprobación en equipo físico. No se certifica 50 imágenes completas por segundo (presentación en dos bandas).
