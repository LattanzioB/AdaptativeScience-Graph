# E2 — Poblar el grafo de dominio (Req. 2) `[MUST]`

**Requisito de la consigna:** 2 — *Poblar un grafo utilizando la ontología anterior.*
**Objetivo:** instancias reales basadas en el diagrama del TP (protocolo árbol/cazuela).

## Historias
- [H2.1 — Protocolo del diagrama](H2.1-protocolo-diagrama.md)
- [H2.2 — Proyectos y áreas](H2.2-proyectos-areas.md)
- [H2.3 — Participantes](H2.3-participantes.md)
- [H2.4 — Submissions geolocalizadas](H2.4-submissions-geo.md)

## Dependencias
- **Depende de:** E1 (T-Box).
- **Habilita:** E4 (jugar sobre estos datos), E6 (consultas).

## Definition of Done (DoD)
El grafo (A-Box) refleja el diagrama del PDF, incluye multiplicidad simultánea (un participante en ≥2 proyectos) e historial temporal, y las consultas básicas devuelven datos coherentes.
