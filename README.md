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
python -c "from rdflib import Graph; Graph().parse('ontology/cipa-domain.ttl', format='turtle'); print('ontology OK')"
python shapes/validate.py --data data/smoke.ttl --shapes shapes/empty.ttl
python shapes/validate.py --data data/smoke.ttl --shapes shapes/domain-smoke.ttl --inference rdfs
python shapes/validate.py --data shapes/examples/smoke-valid.ttl --shapes shapes/examples/sparql-person-shape.ttl
python shapes/validate.py --data shapes/examples/smoke-invalid.ttl --shapes shapes/examples/sparql-person-shape.ttl
```

3. Levantar GraphDB local:

```powershell
docker compose up -d graphdb
```

La consola web queda en `http://localhost:7200`. Los comandos `curl.exe` de abajo asumen GraphDB ya levantado y se ejecutan desde la raiz del repo.

4. Crear el repositorio `cipa-local` a partir del archivo de configuracion via API REST:

```powershell
curl.exe -X POST http://localhost:7200/rest/repositories -F "config=@graphdb/repositories/cipa-local.ttl"
```

Verificar que aparece en la lista:

```powershell
curl.exe http://localhost:7200/rest/repositories
```

> Nota: `graphdb/repositories/cipa-local.ttl` usa los tipos de GraphDB 10 (`graphdb:SailRepository` / `graphdb:Sail`). En GraphDB 9.x los tipos eran `graphdb:FreeSailRepository` / `graphdb:FreeSail`; si la creacion falla con "Unsupported repository type", revisar que la version del contenedor coincida con el archivo de configuracion.

5. Cargar la ontologia de dominio y los datos de humo via API REST (ambos archivos: el endpoint `statements` sube el contenido desde el host, sin depender de los volumenes montados):

```powershell
curl.exe -X POST -H "Content-Type: text/turtle" --data-binary "@ontology/cipa-domain.ttl" "http://localhost:7200/repositories/cipa-local/statements"
curl.exe -X POST -H "Content-Type: text/turtle" --data-binary "@data/smoke.ttl" "http://localhost:7200/repositories/cipa-local/statements"
```

> Cargar siempre la ontologia junto con los datos: las consultas de inferencia y de dominio necesitan la T-Box (`cipa-domain.ttl`) cargada en el mismo repositorio que la A-Box (`smoke.ttl`).

6. Ejecutar las consultas de humo via API REST (o desde la pestana SPARQL de la consola web):

```powershell
curl.exe -X POST -H "Content-Type: application/sparql-query" -H "Accept: application/sparql-results+json" --data-binary "@queries/smoke-select.rq" "http://localhost:7200/repositories/cipa-local"
curl.exe -X POST -H "Content-Type: application/sparql-query" -H "Accept: application/sparql-results+json" --data-binary "@queries/inference-smoke.rq" "http://localhost:7200/repositories/cipa-local"
curl.exe -X POST -H "Content-Type: application/sparql-query" -H "Accept: application/sparql-results+json" --data-binary "@queries/domain-interests.rq" "http://localhost:7200/repositories/cipa-local"
```

Resultados esperados: `smoke-select` devuelve filas (hay datos), `inference-smoke` devuelve `true` (el ruleset `rdfsplus-optimized` infiere `cipa:ProyectoPiloto rdfs:subClassOf cipa:Proyecto`) y `domain-interests` lista la persona con su area de conocimiento y el conteo de aportes.

## Flujo de ramas y commits

- `main` queda estable y representando entregables validados.
- El trabajo se desarrolla en ramas `codex/<epica-o-historia>` o `feature/<epica-o-historia>`.
- Los commits usan prefijos convencionales: `feat:`, `docs:`, `test:`, `chore:` y `fix:`.
- Cada PR debe indicar historias cubiertas, validaciones ejecutadas y brechas de entorno si las hubiera.
