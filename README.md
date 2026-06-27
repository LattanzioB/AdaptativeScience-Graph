# AdaptativeScience Graph

Repositorio del TP de Ciencia Participativa para modelar una ontologia OWL, poblarla con datos RDF, validar reglas SHACL y ejecutar consultas SPARQL sobre GraphDB.

## Estructura

- `ontology/`: ontologias OWL/Turtle del dominio `cipa:` y de ludificacion `pbl:`.
- `data/`: instancias RDF para proyectos, protocolos, personas, muestras y eventos del juego.
- `shapes/`: shapes SHACL, fixtures de humo y script de validacion local.
- `queries/`: consultas SPARQL para verificacion, inferencias y casos de entrega.
- `Docs/`: backlog, decisiones de modelado, notas operativas y documentacion del TP.
- `graphdb/`: configuracion reproducible de repositorio GraphDB.

## Arranque rapido

1. Crear entorno Python e instalar validadores:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Validar sintaxis RDF y SHACL:

```powershell
python shapes/validate.py --data data/smoke.ttl --shapes shapes/empty.ttl
python shapes/validate.py --data shapes/examples/smoke-valid.ttl --shapes shapes/examples/sparql-person-shape.ttl
python shapes/validate.py --data shapes/examples/smoke-invalid.ttl --shapes shapes/examples/sparql-person-shape.ttl
```

3. Levantar GraphDB local y cargar el TTL de humo:

```powershell
docker compose up -d graphdb
```

Crear el repositorio `cipa-local` con `graphdb/repositories/cipa-local.ttl`, cargar `data/smoke.ttl` y ejecutar `queries/smoke-select.rq`.

## Flujo de ramas y commits

- `main` queda estable y representando entregables validados.
- El trabajo se desarrolla en ramas `codex/<epica-o-historia>` o `feature/<epica-o-historia>`.
- Los commits usan prefijos convencionales: `feat:`, `docs:`, `test:`, `chore:` y `fix:`.
- Cada PR debe indicar historias cubiertas, validaciones ejecutadas y brechas de entorno si las hubiera.
