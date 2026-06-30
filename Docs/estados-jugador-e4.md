# E4 — Estados de jugador esperados (juego "relevamiento participativo")

Tabla de referencia para el coloquio (H4.3 / H7.4). Documenta qué representa cada
persona y cómo se compone su billetera de puntos a partir de los `pbl:PointAward`
de `data/juego-eventos.ttl`.

> **Nota (Opción A):** la columna "Medallas" es el **resultado esperado**, no un dato
> cargado a mano. La obtención de medallas se determina con Shapes en E5 (req. 5) y se
> materializa (`pbl:earnedBadge`) en H5.4. Esta tabla sirve de _golden result_ para
> verificar que el shape produce exactamente estas medallas.

## Reglas de puntaje aplicadas

| Actividad | Regla | Puntos | Disparador en el dominio |
|---|---|---|---|
| Completar protocolo | `regla/protocolo` | 50 | La `cipa:Muestra` alcanzó un paso terminal (`foto-arbol`, `confirmar-exotica` o `aves-cantidad`) |
| Subir foto | `regla/foto` | 20 | Una `cipa:MuestraRespuesta` con `cipa:valorMultimedia` |
| Geolocalizar | `regla/geo` | 10 | La `cipa:Muestra` tiene `cipa:registradaEn` una `cipa:Ubicacion` |
| Editar perfil | `regla/perfil` | 0 | Acción administrativa — **no** genera `pbl:PointAward` |

## Medallas (E3)

| Medalla | `minPoints` | Requiere |
|---|---|---|
| Aficionado (M1) | 50 | — |
| Explorador (M2) | 100 | Aficionado |
| Naturalista (M3) | 200 | Explorador |

## Estado por persona

(Medallas = resultado esperado a derivar por E5; ver nota arriba.)

| Persona | Aportes | Cálculo | Billetera | Medallas (esperadas) | Estado demostrado |
|---|---|---|---|---|---|
| **Lucía Gómez** | arboles-005 (abandonada) | 10 | **10** | — | Sin medalla (no-conformidad para E5) |
| **Matías Cabrera** | arboles-002 | 50+20+10 | **80** | Aficionado | Gana M1 pero no M2 |
| **Bruno Lattanzio** | arboles-003 (exótica, sin foto) + aves-002 | (50+10) + (50+20+10) | **140** | Aficionado, Explorador | Llega hasta M2 |
| **Ana Pérez** | arboles-001 + arboles-004 + aves-001 | 3×(50+20+10) | **240** | Aficionado, Explorador, Naturalista | Elegible para M3 |

> La billetera materializada en `data/player-state.ttl` (`pbl:pointsBalance`) debe
> coincidir con `SUM(pbl:points)` de los `pbl:PointAward` de cada jugador.
