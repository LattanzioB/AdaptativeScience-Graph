# Backlog — TP Ciencia Participativa (OWL + PBL + SHACL + GraphDB)

Índice maestro del backlog en formato **épicas → historias**. El detalle de cada historia vive en
[`backlog/<épica>/<historia>.md`](backlog/). Cada épica está mapeada a un requisito de la **Entrega final**
para que la trazabilidad sea directa en el coloquio.

**Stack:** OWL (Protégé para edición) · SOSA/SSN · PROV-O · SKOS · FOAF · GeoSPARQL · SHACL · GraphDB / RDF4J.
**Convención de historias:** cada una tiene historia de usuario, contexto del PDF, criterios de aceptación (CA) verificables, tareas y artefactos.
**Prioridad:** `[MUST]` para aprobar el 30/06 · `[SHOULD]` pulido · `[COULD]` extensión.

---

## Mapa requisito → épica

| Req. consigna | Épica |
|---|---|
| (habilitador) | [E0 — Infraestructura y arranque](backlog/E0-infraestructura/README.md) |
| 1. Ontología de dominio en OWL | [E1 — Ontología de dominio](backlog/E1-ontologia-dominio/README.md) |
| 2. Poblar el grafo de dominio | [E2 — Poblar el grafo](backlog/E2-poblar-grafo/README.md) |
| 3. Ontología PBL + juego sencillo (3 medallas) | [E3 — Ontología PBL + juego](backlog/E3-ontologia-pbl/README.md) |
| 4. Participantes jugando (integración) | [E4 — Participantes jugando](backlog/E4-participantes-jugando/README.md) |
| 5. Obtención de medallas con Shapes | [E5 — Shapes de medallas](backlog/E5-shapes-medallas/README.md) |
| 6. GraphDB + consultas SPARQL | [E6 — GraphDB + consultas](backlog/E6-graphdb-consultas/README.md) |
| Entrega (GitHub + coloquio) | [E7 — Documentación y defensa](backlog/E7-entrega-defensa/README.md) |

---

## Listado de épicas e historias

### [E0 — Infraestructura y arranque](backlog/E0-infraestructura/README.md) `[MUST]`
- [H0.1 — Repositorio y estructura](backlog/E0-infraestructura/H0.1-repositorio-estructura.md)
- [H0.2 — Instancia GraphDB](backlog/E0-infraestructura/H0.2-instancia-graphdb.md)
- [H0.3 — Namespaces y convenciones de IRIs](backlog/E0-infraestructura/H0.3-namespaces-iris.md)
- [H0.4 — Toolchain de validación](backlog/E0-infraestructura/H0.4-toolchain-validacion.md)

### [E1 — Ontología de dominio en OWL](backlog/E1-ontologia-dominio/README.md) `[MUST]` — Req. 1
- [H1.1 — Proyecto y área de conocimiento](backlog/E1-ontologia-dominio/H1.1-proyecto-clasificacion.md)
- [H1.2 — Protocolo](backlog/E1-ontologia-dominio/H1.2-protocolo.md)
- [H1.3 — Pasos (jerarquía de tipos)](backlog/E1-ontologia-dominio/H1.3-pasos.md)
- [H1.4 — Transiciones (DAG con bifurcación)](backlog/E1-ontologia-dominio/H1.4-transiciones.md)
- [H1.5 — Muestras y respuestas](backlog/E1-ontologia-dominio/H1.5-muestreo.md)
- [H1.6 — Persona participante](backlog/E1-ontologia-dominio/H1.6-participante.md)
- [H1.7 — Reutilización y alineaciones](backlog/E1-ontologia-dominio/H1.7-reutilizacion-alineaciones.md)
- [H1.8 — Consistencia](backlog/E1-ontologia-dominio/H1.8-consistencia.md)
- [H1.9 — Perfil del Colaborador](backlog/E1-ontologia-dominio/H1.9-perfil-colaborador.md) *(nuevo — cubre el módulo de perfiles del PDF)*

### [E2 — Poblar el grafo de dominio](backlog/E2-poblar-grafo/README.md) `[MUST]` — Req. 2
- [H2.1 — Protocolo del diagrama](backlog/E2-poblar-grafo/H2.1-protocolo-diagrama.md)
- [H2.2 — Proyectos y áreas](backlog/E2-poblar-grafo/H2.2-proyectos-areas.md)
- [H2.3 — Personas participantes](backlog/E2-poblar-grafo/H2.3-participantes.md)
- [H2.4 — Muestras geolocalizadas](backlog/E2-poblar-grafo/H2.4-muestras-geolocalizadas.md)

### [E3 — Ontología PBL + juego sencillo](backlog/E3-ontologia-pbl/README.md) `[MUST]` — Req. 3
- [H3.1 — Ontología PBL](backlog/E3-ontologia-pbl/H3.1-ontologia-pbl.md)
- [H3.2 — Sistema incremental de 3 medallas](backlog/E3-ontologia-pbl/H3.2-medallas-incrementales.md)
- [H3.3 — Definición del juego sencillo](backlog/E3-ontologia-pbl/H3.3-juego-sencillo.md)
- [H3.4 — Alineación Open Badges](backlog/E3-ontologia-pbl/H3.4-open-badges.md) `[COULD]`

### [E4 — Participantes jugando](backlog/E4-participantes-jugando/README.md) `[MUST]` — Req. 4
- [H4.1 — Acciones → eventos de puntos](backlog/E4-participantes-jugando/H4.1-acciones-puntos.md)
- [H4.2 — Estado de jugador](backlog/E4-participantes-jugando/H4.2-estado-jugador.md)
- [H4.3 — Cobertura para demostración](backlog/E4-participantes-jugando/H4.3-cobertura-demo.md)

### [E5 — Obtención de medallas con Shapes](backlog/E5-shapes-medallas/README.md) `[MUST]` — Req. 5
- [H5.1 — Patrón `sh:sparql` "conformidad = ganador"](backlog/E5-shapes-medallas/H5.1-patron-sparql.md)
- [H5.2 — Shapes de las 3 medallas con precedencia](backlog/E5-shapes-medallas/H5.2-shapes-medallas.md)
- [H5.3 — Verificación](backlog/E5-shapes-medallas/H5.3-verificacion.md)
- [H5.4 — Materialización](backlog/E5-shapes-medallas/H5.4-materializacion.md) `[SHOULD]`

### [E6 — GraphDB + consultas SPARQL](backlog/E6-graphdb-consultas/README.md) `[MUST]` — Req. 6
- [H6.1 — Carga integral](backlog/E6-graphdb-consultas/H6.1-carga-integral.md)
- [H6.2 — (6.a.i) Dos consultas multi-hop de dominio](backlog/E6-graphdb-consultas/H6.2-consultas-multihop.md)
- [H6.3 — (6.a.ii) Consulta sobre tripletas inferidas](backlog/E6-graphdb-consultas/H6.3-consulta-inferencias.md)
- [H6.4 — (6.b.i) Estatus completo de jugador](backlog/E6-graphdb-consultas/H6.4-estatus-jugador.md)
- [H6.5 — (6.b.ii) Medallas asignadas vs. no asignadas](backlog/E6-graphdb-consultas/H6.5-medallas-asignadas.md)
- [H6.6 — (6.b.iii) Medallas obtenidas por una persona](backlog/E6-graphdb-consultas/H6.6-medallas-persona.md)

### [E7 — Documentación, repositorio y defensa](backlog/E7-entrega-defensa/README.md) `[MUST]` — Entrega
- [H7.1 — README operativo](backlog/E7-entrega-defensa/H7.1-readme-operativo.md)
- [H7.2 — Documento de decisiones de modelado](backlog/E7-entrega-defensa/H7.2-decisiones-modelado.md)
- [H7.3 — Diagramas](backlog/E7-entrega-defensa/H7.3-diagramas.md)
- [H7.4 — Guion de coloquio](backlog/E7-entrega-defensa/H7.4-guion-coloquio.md)
- [H7.5 — Capa de adaptabilidad (Dalponte)](backlog/E7-entrega-defensa/H7.5-capa-dalponte.md) `[COULD]`

---

## Decisiones tomadas (16/06)

1. **Alcance opcional:** se incorpora el **Perfil del Colaborador** (intereses + nivel de expertise) de forma liviana
   en [H1.9](backlog/E1-ontologia-dominio/H1.9-perfil-colaborador.md) y alimenta la consulta multi-hop de
   [H6.2](backlog/E6-graphdb-consultas/H6.2-consultas-multihop.md). **Leaderboards** se modela en la T-Box PBL
   ([H3.1](backlog/E3-ontologia-pbl/H3.1-ontologia-pbl.md)) pero **sin** consulta dedicada. Open Badges (H3.4) y
   Dalponte (H7.5) quedan como `[COULD]`.
2. **Reestructuración de dominio (27/06):** las historias usan la estructura de
   [`Docs/Re-Estructuracion-Dominio`](Re-Estructuracion-Dominio/modelo_dominio_ciencia_participativa.md):
   `cipa:Proyecto`, `cipa:AreaConocimiento`, `cipa:Protocolo`, `cipa:Paso`, `cipa:Transicion`,
   `cipa:Muestra`, `cipa:MuestraRespuesta`, `cipa:Persona`, `cipa:Ubicacion` y `cipa:AdjuntoMultimedia`.
   Se conservan los prefijos e IRIs existentes: T-Box de dominio en `cipa:`, ludificación en `pbl:` y datos en
   `cipa-data:`.
3. **Semántica SHACL de medallas:** patrón **`sh:sparql` dentro del NodeShape**, con la convención
   **conformidad = ganador** (la consulta `SELECT` del shape reporta violación para los *no* ganadores).
   Materialización de `pbl:earnedBadge` vía `CONSTRUCT` como `[SHOULD]`. Ver [E5](backlog/E5-shapes-medallas/README.md).
4. **Estructura de archivos:** una subcarpeta por épica con README de épica + un archivo por historia; este `.md` es el índice maestro.

---

## Hoja de ruta vs. calendario

| Fecha | Hito | Alcance objetivo |
|---|---|---|
| **Mar 16/06** (1ra consulta) | Backlog + arranque | E0 listo, E1 en borrador, dudas para consultar |
| **Mar 30/06** (1ra defensa — *acá se puede aprobar*) | **MVP completo** | **E1–E6 funcionando end-to-end**, repo subido (E7 mínimo). Este es el objetivo real. |
| **Mar 14/07** (última defensa) | Pulido | Refinar consultas, materialización (H5.4), Open Badges (H3.4), capa Dalponte (H7.5), guion de coloquio afinado |

## Dependencias entre épicas
`E0 → E1 → E2`; `E1 → E3`; `E2 + E3 → E4 → E5`; `E1..E5 → E6`; todo `→ E7`.
La ruta crítica para el 30/06 es **E1 → E2 → E3 → E4 → E5 → E6**.

## Riesgos / decisiones abiertas restantes
- **Inversión lógica del `sh:sparql` (H5.1):** la convención conformidad = ganador exige que el `SELECT` devuelva
  filas (violaciones) para quienes **no** cumplen el criterio. Validar este detalle temprano con un caso de prueba.
- **Profundidad del razonador (H6.3):** elegir un ruleset que garantice tripletas inferidas no triviales para la
  consulta de inferencia, sin inflar el store.
- **Doc de Dalponte:** sigue pendiente; sólo afecta `[COULD]` (H7.5), no la aprobación.
