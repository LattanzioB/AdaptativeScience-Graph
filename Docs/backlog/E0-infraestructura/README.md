# E0 - Infraestructura y arranque `[MUST]`

**Requisito de la consigna:** habilitador (no es un entregable en si, pero condiciona todo).
**Objetivo:** dejar el entorno y las convenciones listas antes de modelar.
**Estado:** Completado.

## Historias

- [H0.1 - Repositorio y estructura](H0.1-repositorio-estructura.md) - Completado
- [H0.2 - Instancia GraphDB](H0.2-instancia-graphdb.md) - Completado
- [H0.3 - Namespaces y convenciones de IRIs](H0.3-namespaces-iris.md) - Completado
- [H0.4 - Toolchain de validacion](H0.4-toolchain-validacion.md) - Completado

## Dependencias

- **Habilita:** E1 (y por transitividad todo el resto).
- **Depende de:** nada.

## Definition of Done (DoD)

Un TTL de prueba (`data/smoke.ttl`) queda listo para cargar en GraphDB con inferencia, pasa una validacion SHACL vacia (`shapes/empty.ttl`), el repo tiene la estructura de carpetas acordada y el documento de prefijos/IRIs vive en `Docs/namespaces.md`.
