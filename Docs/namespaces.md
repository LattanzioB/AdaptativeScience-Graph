# Namespaces e IRIs

Este documento fija los prefijos, bases IRI y convenciones de nombres del TP para mantener separadas la T-Box de dominio, la T-Box de ludificacion y los datos.

## Prefijos propios

| Prefijo | IRI base | Uso |
|---|---|---|
| `cipa:` | `https://w3id.org/cipa/ontology#` | Clases y propiedades del dominio de ciencia participativa. |
| `pbl:` | `https://w3id.org/cipa/pbl#` | Clases y propiedades de ludificacion, puntos y medallas. |
| `cipa-data:` | `https://w3id.org/cipa/data/` | Individuos e instancias de prueba o entrega. |

## Prefijos reutilizados

| Prefijo | IRI base | Uso |
|---|---|---|
| `sosa:` | `http://www.w3.org/ns/sosa/` | Observaciones, muestras y sensores cuando aplique. |
| `prov:` | `http://www.w3.org/ns/prov#` | Procedencia de acciones, datos y contribuciones. |
| `skos:` | `http://www.w3.org/2004/02/skos/core#` | Taxonomias y areas de conocimiento. |
| `foaf:` | `http://xmlns.com/foaf/0.1/` | Personas y datos de perfil. |
| `geo:` | `http://www.opengis.net/ont/geosparql#` | Geometrias y relaciones espaciales. |
| `sh:` | `http://www.w3.org/ns/shacl#` | Shapes y reglas de validacion. |

## Patron de IRIs de datos

- Proyectos: `cipa-data:proyecto/arboles-nativos`
- Personas: `cipa-data:persona/ada`
- Protocolos: `cipa-data:protocolo/relevamiento-arboles`
- Muestras: `cipa-data:muestra/ceibo-001`
- Pasos: `cipa-data:paso/registrar-foto`
- Medallas: `cipa-data:medalla/explorador`

En Turtle, estos patrones con `/` en el identificador se escriben como IRIs completas, por ejemplo `<https://w3id.org/cipa/data/persona/ada>`.

## Convencion de nombres

- Clases: `UpperCamelCase`, por ejemplo `cipa:Proyecto`, `pbl:Medalla`.
- Propiedades: `lowerCamelCase`, por ejemplo `cipa:tienePaso`, `pbl:earnedBadge`.
- Individuos: `kebab-case` en el segmento final de la IRI, por ejemplo `cipa-data:persona/ada-lovelace`.
- La T-Box de dominio no importa terminos `pbl:` salvo en documentos de integracion; la ludificacion referencia entidades de dominio desde sus propios axiomas o datos.
