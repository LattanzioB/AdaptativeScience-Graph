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

## Estado de implementación

- H1.1 completada en `ontology/cipa-domain.ttl`: `Proyecto`, `AreaConocimiento`, `perteneceA`, `clasificaProyecto`, `tieneProtocolo` y `tieneProtocoloActivo`.
- H1.2 completada: `Protocolo`, `EstadoProtocolo`, `tienePaso`, `tienePrimerPaso` y estados activo/inactivo.
- H1.3 completada: jerarquia de pasos, enunciados, tipos de respuesta y opciones de cuestionario.
- H1.4 completada: `Transicion` reificada, `desdePaso`, `haciaPaso`, `disparadaPor` y atajo `siguientePaso`.
- H1.5 completada: `Muestra`, `MuestraRespuesta`, `Ubicacion`, `AdjuntoMultimedia` y reglas SHACL de compatibilidad.
- H1.6 completada: `Persona`, `personaId`, clave OWL y participacion derivable.
- H1.7 completada: alineaciones livianas con SOSA, PROV-O, SKOS, FOAF y GeoSPARQL en la ontologia y en `Docs/decisiones-modelado.md`.
- H1.8 completada localmente con validacion RDF/SHACL; el razonador Protege y la carga GraphDB quedan como chequeo manual de entorno.
- H1.9 completada: `nivelExpertise`, escala de expertise y `areaInteres` derivable.
