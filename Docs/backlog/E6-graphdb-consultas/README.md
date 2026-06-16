# E6 — GraphDB + consultas SPARQL (Req. 6) `[MUST]`

**Requisito de la consigna:** 6 — *Incluir el grafo en una instancia de GraphDB y realizar las consultas necesarias.*
**Objetivo:** cargar todo en GraphDB y resolver las 6 consultas pedidas.

## Las 6 consultas (mapeo a la consigna)
| Sub-req | Historia | Qué pide |
|---|---|---|
| 6.a.i (×2) | [H6.2](H6.2-consultas-multihop.md) | Dos consultas de navegación multi-hop con sentido de dominio |
| 6.a.ii | [H6.3](H6.3-consulta-inferencias.md) | Una consulta que dependa de tripletas inferidas por el razonador |
| 6.b.i | [H6.4](H6.4-estatus-jugador.md) | Estatus completo de una persona jugadora para un juego |
| 6.b.ii | [H6.5](H6.5-medallas-asignadas.md) | Medallas asignadas y aún no asignadas |
| 6.b.iii | [H6.6](H6.6-medallas-persona.md) | Medallas obtenidas por una persona |

## Historias
- [H6.1 — Carga integral](H6.1-carga-integral.md)
- [H6.2 — (6.a.i) Dos consultas multi-hop de dominio](H6.2-consultas-multihop.md)
- [H6.3 — (6.a.ii) Consulta sobre tripletas inferidas](H6.3-consulta-inferencias.md)
- [H6.4 — (6.b.i) Estatus completo de jugador](H6.4-estatus-jugador.md)
- [H6.5 — (6.b.ii) Medallas asignadas vs. no asignadas](H6.5-medallas-asignadas.md)
- [H6.6 — (6.b.iii) Medallas obtenidas por una persona](H6.6-medallas-persona.md)

## Dependencias
- **Depende de:** E1–E5 (todo lo anterior cargado).
- **Habilita:** E7 (demo del coloquio).

## Definition of Done (DoD)
`queries/` con las 6 consultas, cada una corriendo en GraphDB con el ruleset de inferencia activo y con resultado esperado documentado.
