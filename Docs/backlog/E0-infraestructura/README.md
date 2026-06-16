# E0 — Infraestructura y arranque `[MUST]`

**Requisito de la consigna:** habilitador (no es un entregable en sí, pero condiciona todo).
**Objetivo:** dejar el entorno y las convenciones listas antes de modelar.

## Historias
- [H0.1 — Repositorio y estructura](H0.1-repositorio-estructura.md)
- [H0.2 — Instancia GraphDB](H0.2-instancia-graphdb.md)
- [H0.3 — Namespaces y convenciones de IRIs](H0.3-namespaces-iris.md)
- [H0.4 — Toolchain de validación](H0.4-toolchain-validacion.md)

## Dependencias
- **Habilita:** E1 (y por transitividad todo el resto).
- **Depende de:** nada.

## Definition of Done (DoD)
Un TTL de prueba carga en GraphDB con inferencia y pasa una validación SHACL vacía; el repo tiene la estructura de carpetas acordada y un documento de prefijos/IRIs.
