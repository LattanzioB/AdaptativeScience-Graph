# E1 — Ontología de dominio en OWL (Req. 1) `[MUST]`

**Requisito de la consigna:** 1 — *Definir la ontología que modele el dominio de los proyectos de ciencia participativa en OWL.*
**Objetivo:** T-Box del dominio, reutilizando estándares + extensión `cipa:`.

## Historias
- [H1.1 — Proyecto y área de conocimiento](H1.1-proyecto-clasificacion.md)
- [H1.2 — Protocolo](H1.2-protocolo.md)
- [H1.3 — Pasos (jerarquía de tipos)](H1.3-pasos.md)
- [H1.4 — Transiciones (DAG con bifurcación)](H1.4-transiciones.md)
- [H1.5 — Muestras y respuestas](H1.5-muestreo.md)
- [H1.6 — Persona participante](H1.6-participante.md)
- [H1.7 — Reutilización y alineaciones](H1.7-reutilizacion-alineaciones.md)
- [H1.8 — Consistencia](H1.8-consistencia.md)
- [H1.9 — Perfil del Colaborador](H1.9-perfil-colaborador.md) *(cubre el módulo "Gestión de Participantes y Perfiles" del PDF)*

## Dependencias
- **Depende de:** E0 (namespaces, toolchain).
- **Habilita:** E2 (poblar), E3 (alineación con PBL).

## Definition of Done (DoD)
`ontology/cipa-domain.ttl` consistente con la reestructuración de dominio (Proyecto, AreaConocimiento, Protocolo, Paso, Transicion, Muestra, MuestraRespuesta, Persona, Ubicacion y AdjuntoMultimedia), documentado y cargable en GraphDB.
