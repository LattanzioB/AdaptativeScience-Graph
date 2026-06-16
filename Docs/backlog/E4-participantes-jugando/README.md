# E4 — Participantes jugando (Req. 4) `[MUST]`

**Requisito de la consigna:** 4 — *Complementar el grafo de 2, en el que los participantes están jugando al juego definido en 3.*
**Objetivo:** conectar el grafo de dominio (E2) con el juego (E3).

## Historias
- [H4.1 — Acciones → eventos de puntos](H4.1-acciones-puntos.md)
- [H4.2 — Estado de jugador](H4.2-estado-jugador.md)
- [H4.3 — Cobertura para demostración](H4.3-cobertura-demo.md)

## Dependencias
- **Depende de:** E2 (datos de dominio) + E3 (reglas y medallas).
- **Habilita:** E5 (shapes evalúan estos puntos/medallas), E6 (consultas de juego).

## Definition of Done (DoD)
El grafo poblado combina dominio + PBL; los puntajes acumulados cierran con las reglas; los datos cubren los tres estados de medalla (gana M1 pero no M2 / hasta M2 / elegible para M3).
