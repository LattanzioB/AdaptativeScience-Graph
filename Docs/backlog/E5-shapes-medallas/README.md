# E5 — Obtención de medallas con Shapes (Req. 5) `[MUST]`

**Requisito de la consigna:** 5 — *Modelar la obtención de las medallas con Shapes. Es decir, determinar si una persona es ganadora de la medalla a través de Shapes.*
**Objetivo:** determinar al ganador de cada medalla **vía SHACL** usando el patrón `sh:sparql` (conformidad = medalla obtenida).

## Decisión de modelado (16/06)
Patrón elegido: **`sh:sparql` dentro de un `sh:NodeShape` por medalla**, con la convención **conformidad = ganador**.
El `SELECT` de cada shape devuelve filas (violaciones) para las personas que **no** cumplen el criterio; por lo
tanto, una `cipa:Persona` que **conforma** (sin violaciones) es ganadora de esa medalla.

## Historias
- [H5.1 — Patrón `sh:sparql` "conformidad = ganador"](H5.1-patron-sparql.md)
- [H5.2 — Shapes de las 3 medallas con precedencia](H5.2-shapes-medallas.md)
- [H5.3 — Verificación](H5.3-verificacion.md)
- [H5.4 — Materialización](H5.4-materializacion.md) `[SHOULD]`

## Dependencias
- **Depende de:** E4 (puntos/medallas pobladas) + E3 (criterios de medalla).
- **Habilita:** E6 (consultas de medallas, especialmente H6.5/H6.6).

## Definition of Done (DoD)
`shapes/badges.ttl` determina correctamente y de forma reproducible quién gana cada medalla; una persona no elegible **no** conforma; los resultados coinciden con E4.
