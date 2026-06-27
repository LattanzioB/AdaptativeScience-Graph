# Toolchain de validacion

La validacion local se apoya en `pyshacl`, que soporta constraints `sh:sparql` y permite iterar sin recargar GraphDB en cada cambio.

## Instalacion

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Comandos de humo

Validacion vacia requerida por E0:

```powershell
python shapes/validate.py --data data/smoke.ttl --shapes shapes/empty.ttl
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
