# Decisiones de modelado

Este documento registra las decisiones semanticas usadas por la ontologia de dominio `cipa:` y sirve como puente hacia las historias de entrega.

## Ontologia de dominio

- La T-Box principal vive en `ontology/cipa-domain.ttl`.
- `cipa:Proyecto` es la unidad central y se clasifica con `cipa:perteneceA` hacia `cipa:AreaConocimiento`.
- Un proyecto puede tener varios protocolos historicos con `cipa:tieneProtocolo`, pero solo un protocolo activo con `cipa:tieneProtocoloActivo`. La propiedad activa es funcional y ademas se documenta con una restriccion OWL de cardinalidad maxima 1.
- `cipa:Protocolo` se compone con `cipa:tienePaso` y declara su inicio con `cipa:tienePrimerPaso`.

## Pasos, transiciones y bifurcaciones

- `cipa:Paso` separa la definicion del protocolo de la ejecucion concreta.
- `cipa:PasoMultimedia` y `cipa:PasoCuestionario` solo especializan el tipo de enunciado y respuesta esperada.
- Las bifurcaciones se modelan con `cipa:Transicion` reificada, usando `cipa:desdePaso`, `cipa:haciaPaso` y opcionalmente `cipa:disparadaPor`.
- `cipa:siguientePaso` queda como atajo materializable para consultas `cipa:siguientePaso+`; no reemplaza a la transicion reificada porque la condicion necesita vivir en la arista.

## Ejecucion de muestras

- `cipa:Muestra` representa una ejecucion concreta de un protocolo.
- Cada paso recorrido se registra como `cipa:MuestraRespuesta`, enlazada por `cipa:tieneRespuesta` y `cipa:correspondeAPaso`.
- El adjunto subido por una persona cuelga de `cipa:MuestraRespuesta` mediante `cipa:valorMultimedia`; no cuelga de `cipa:EnunciadoMultimedia`, porque el enunciado pertenece a la definicion del protocolo.
- Las reglas de compatibilidad se validan con SHACL en `shapes/domain-smoke.ttl`: respuestas multimedia requieren `cipa:valorMultimedia`; respuestas de cuestionario requieren `cipa:valorTexto` o `cipa:seleccionaOpcion`.

## Alineaciones livianas

Se eligio mapeo liviano en vez de `owl:imports` para evitar depender de resolucion externa durante la carga local en GraphDB.

| Termino CIPA | Alineacion | Justificacion |
|---|---|---|
| `cipa:AreaConocimiento` | `rdfs:subClassOf skos:Concept` | Permite taxonomias controladas de areas y etiquetas multilingues. |
| `cipa:EsquemaAreasConocimiento` | `rdfs:subClassOf skos:ConceptScheme` | Agrupa los conceptos de area del TP. |
| `cipa:Protocolo` | `rdfs:subClassOf sosa:Procedure` | Un protocolo funciona como procedimiento de observacion. |
| `cipa:Muestra` | `rdfs:subClassOf sosa:ObservationCollection` | Una muestra agrupa observaciones/respuestas de una ejecucion. |
| `cipa:MuestraRespuesta` | `rdfs:subClassOf sosa:Observation` | Cada respuesta observa o registra el resultado de un paso. |
| `cipa:respondidaPor` | `rdfs:subPropertyOf prov:wasAttributedTo` | Habilita consultar atribucion con PROV-O. |
| `cipa:Persona` | `rdfs:subClassOf foaf:Person, prov:Agent` | Modela identidad y agente responsable de aportes. |
| `cipa:Ubicacion` | `rdfs:subClassOf geo:Feature` | Deja preparada la evolucion a GeoSPARQL/WKT. |

## Perfil colaborador

- `cipa:personaId` es funcional y se declara como clave OWL de `cipa:Persona`.
- La participacion de una persona en proyectos no se duplica manualmente: se deriva desde `Persona <- respondidaPor <- Muestra -> ejecutaProtocolo <- tieneProtocoloActivo <- Proyecto`.
- `cipa:areaInteres` queda como propiedad derivable para consultas o materializacion posterior.
- `cipa:nivelExpertise` apunta a `cipa:TipoExpertise` (`novato`, `intermedio`, `experto`) y puede asignarse por regla o curacion manual segun frecuencia/calidad de muestras.

## Consistencia

- No se declaran clases disjuntas en esta primera version para evitar inconsistencias accidentales al poblar el grafo.
- Las cardinalidades duras se mantienen al minimo: la regla de unico protocolo activo se expresa como propiedad funcional y como maximo 1, mientras que obligatoriedad de datos de humo se verifica con SHACL.
- El chequeo local cubre parsing RDF/OWL y reglas SHACL; el razonador de Protege y la carga GraphDB completa quedan documentados como validacion manual de entorno.
