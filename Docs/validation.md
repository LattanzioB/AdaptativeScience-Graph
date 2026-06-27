# Toolchain de validacion

La validacion local se apoya en `pyshacl`, que soporta constraints `sh:sparql` y permite iterar sin recargar GraphDB en cada cambio.

## Instalacion

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Comandos de humo

Parsing de la T-Box de dominio E1:

```powershell
python -c "from rdflib import Graph; Graph().parse('ontology/cipa-domain.ttl', format='turtle'); print('ontology OK')"
```

Validacion vacia requerida por E0:

```powershell
python shapes/validate.py --data data/smoke.ttl --shapes shapes/empty.ttl
```

Validacion de dominio E1 sobre el grafo de humo:

```powershell
python shapes/validate.py --data data/smoke.ttl --shapes shapes/domain-smoke.ttl --inference rdfs
```

Caso conforme con `sh:sparql`:

```powershell
python shapes/validate.py --data shapes/examples/smoke-valid.ttl --shapes shapes/examples/sparql-person-shape.ttl
```

Caso no conforme esperado:

```powershell
python shapes/validate.py --data shapes/examples/smoke-invalid.ttl --shapes shapes/examples/sparql-person-shape.ttl
```

El tercer comando debe finalizar con codigo distinto de cero y reportar que la persona sin `foaf:name` viola el shape.

## Chequeos manuales de entorno

- Protege/HermiT o Pellet: abrir `ontology/cipa-domain.ttl` y confirmar que no haya clases insatisfacibles.
- GraphDB: crear/cargar el repositorio local, importar `ontology/cipa-domain.ttl` y `data/smoke.ttl`, ejecutar `queries/inference-smoke.rq` con inferencia RDFS/OWL activa y confirmar `true`.
