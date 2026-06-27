# GraphDB local

La instancia local usa GraphDB Free con el repositorio `cipa-local` y razonamiento `rdfsplus-optimized`, suficiente para validar inferencias no triviales de `rdfs:subClassOf` y `rdfs:subPropertyOf` durante H6.3.

## Levantar la instancia

```powershell
docker compose up -d graphdb
```

La consola queda disponible en `http://localhost:7200`.

## Crear repositorio

Crear el repositorio desde la consola de GraphDB importando `graphdb/repositories/cipa-local.ttl`.

Configuracion esperada:

- Repository ID: `cipa-local`
- Ruleset: `rdfsplus-optimized`
- SameAs: deshabilitado para evitar expansion innecesaria del grafo
- GeoSPARQL: habilitar desde GraphDB si las historias H1.5/H2.4 usan filtros espaciales en la entrega

## Prueba de humo

1. Cargar `data/smoke.ttl`.
2. Ejecutar `queries/smoke-select.rq` para confirmar que el grafo tiene datos.
3. Ejecutar `queries/inference-smoke.rq`; con el ruleset activo debe responder `true` porque `cipa:ProyectoPiloto rdfs:subClassOf cipa:Proyecto`.
