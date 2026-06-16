# E3 — Ontología PBL + juego sencillo (Req. 3) `[MUST]`

**Requisito de la consigna:** 3 — *Definir una ontología para el modelo de ludificación PBL, y su utilización para un juego sencillo en el que se den diferentes puntos para diferentes acciones, y un sistema de medallas incremental de 3 medallas.*
**Objetivo:** ontología de ludificación **separada** (`pbl:`) y un juego concreto con 3 medallas incrementales.

## Historias
- [H3.1 — Ontología PBL](H3.1-ontologia-pbl.md)
- [H3.2 — Sistema incremental de 3 medallas](H3.2-medallas-incrementales.md)
- [H3.3 — Definición del juego sencillo](H3.3-juego-sencillo.md)
- [H3.4 — Alineación Open Badges](H3.4-open-badges.md) `[COULD]`

## Dependencias
- **Depende de:** E1 (para alinear, no para acoplar: `pbl:` es independiente del dominio).
- **Habilita:** E4 (jugar), E5 (shapes de medallas).

## Definition of Done (DoD)
`ontology/pbl.ttl` consistente e independiente del dominio, con el juego definido: acciones con puntajes diferenciados y 3 medallas encadenadas (M1 → M2 → M3) cuyo grafo de dependencias es acíclico.
