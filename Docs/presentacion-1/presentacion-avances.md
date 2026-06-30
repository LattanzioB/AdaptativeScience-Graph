# Presentacion de avances - AdaptativeScience Graph

Este documento resume los avances implementados y propone una seguidilla de consultas SPARQL para demostrar el estado actual del proyecto en GraphDB.

## Estado actual

La demo integral cargada en GraphDB incluye:

- Ontologia de dominio `cipa:` en `ontology/cipa-domain.ttl`.
- Ontologia de ludificacion `pbl:` en `ontology/pbl.ttl`.
- Dos proyectos de ciencia participativa:
  - `Arboles nativos`
  - `Observacion de aves`
- Dos protocolos activos:
  - Protocolo con bifurcacion para arboles nativos.
  - Protocolo lineal para observacion de aves.
- Cuatro personas participantes:
  - Ana Perez
  - Matias Cabrera
  - Bruno Lattanzio
  - Lucia Gomez
- Siete muestras geolocalizadas en distintas provincias, incluyendo un caso abandonado para mostrar no obtencion de medallas.
- Veintiuna respuestas de muestra, incluyendo texto libre, opciones de cuestionario y adjuntos multimedia.
- Juego PBL con actividades, reglas de puntos, eventos de puntos, estados de jugador, leaderboard y tres medallas incrementales.

## Que se desarrollo

### Infraestructura

Se dejo una base reproducible para trabajar localmente:

- Estructura de carpetas para ontologias, datos, shapes, consultas, documentacion y configuracion GraphDB.
- `docker-compose.yml` con GraphDB 10.8.8.
- Repositorio GraphDB local `cipa-local` configurado con ruleset `rdfsplus-optimized`.
- Documentacion operativa en `README.md`, `Docs/graphdb.md`, `Docs/validation.md` y `Docs/namespaces.md`.

### Ontologia de dominio

La T-Box de dominio modela proyectos de ciencia participativa:

- `cipa:Proyecto` y `cipa:AreaConocimiento`.
- `cipa:Protocolo`, estados y protocolo activo.
- `cipa:Paso`, con especializaciones `cipa:PasoMultimedia` y `cipa:PasoCuestionario`.
- `cipa:Transicion` reificada, para modelar flujos y bifurcaciones.
- `cipa:Muestra` y `cipa:MuestraRespuesta`, para registrar ejecuciones reales de protocolos.
- `cipa:Persona`, `cipa:Ubicacion` y `cipa:AdjuntoMultimedia`.
- Perfil colaborador con `cipa:personaId`, `cipa:nivelExpertise` y `cipa:areaInteres` derivable.

Tambien se agregaron alineaciones livianas con vocabularios existentes:

- `cipa:Persona` como subclase de `foaf:Person` y `prov:Agent`.
- `cipa:respondidaPor` como subpropiedad de `prov:wasAttributedTo`.
- `cipa:AreaConocimiento` como subclase de `skos:Concept`.
- `cipa:Protocolo` como subclase de `sosa:Procedure`.
- `cipa:Muestra` y `cipa:MuestraRespuesta` alineadas con SOSA.
- `cipa:Ubicacion` alineada con GeoSPARQL.

### Datos de dominio

Se poblo una demo integral con:

- Proyectos en botanica, ambiente y zoologia.
- Protocolos con pasos, enunciados, opciones y transiciones.
- Participantes con identificador estable y nivel de expertise.
- Muestras con ubicacion, fecha, persona responsable y respuestas.
- Casos longitudinales y multi-proyecto: Ana Perez aporta en arboles y aves, y tiene muestras en distintos meses.
- Casos con valores de distinto tipo: texto, opcion seleccionada y multimedia.
- Caso de abandono: Lucia Gomez registra una muestra geolocalizada pero no completa el protocolo ni sube foto.

### Validacion

La validacion local usa `pyshacl` y `rdflib`.

Comandos relevantes:

```powershell
python -c "from rdflib import Graph; Graph().parse('ontology/cipa-domain.ttl', format='turtle'); print('ontology OK')"
python shapes/validate.py --data data/smoke.ttl --shapes shapes/empty.ttl
python shapes/validate.py --data data/smoke.ttl --shapes shapes/domain-smoke.ttl --inference rdfs
python shapes/validate.py --data shapes/examples/smoke-valid.ttl --shapes shapes/examples/sparql-person-shape.ttl
python shapes/validate.py --data shapes/examples/smoke-invalid.ttl --shapes shapes/examples/sparql-person-shape.ttl
```

La carga integral fue validada combinando los TTL de dominio en memoria con `shapes/domain-smoke.ttl` y resultado:

```text
Validation Report
Conforms: True
```

### Ontologia PBL y juego

Se desarrollo una ontologia de ludificacion separada (`pbl:`), sin acoplarla directamente a `cipa:`.

Incluye:

- `pbl:Game`
- `pbl:Activity`
- `pbl:PointRule`
- `pbl:PointAward`
- `pbl:Badge`
- `pbl:Leaderboard`
- `pbl:Player`
- `pbl:PlayerState`
- `pbl:DifficultyLevel`

El juego de demo define:

- Completar un protocolo: 50 puntos, dificultad alta.
- Subir una foto: 20 puntos, dificultad media.
- Geolocalizar una muestra: 10 puntos, dificultad baja.
- Editar perfil: 0 puntos, dificultad baja.
- Eventos `pbl:PointAward` trazables hacia contribuciones de dominio con `pbl:fromContribution`.
- Estados `pbl:PlayerState` con billetera materializada por juego particular.
- Leaderboard que rankea los estados de jugador del juego de relevamiento.
- Tres medallas incrementales:
  - Aficionado: 50 puntos.
  - Explorador: 100 puntos y requiere Aficionado.
  - Naturalista: 200 puntos y requiere Explorador.

Los estados esperados para la demo de medallas son:

- Lucia Gomez: 10 puntos, sin medalla.
- Matias Cabrera: 80 puntos, Aficionado.
- Bruno Lattanzio: 140 puntos, Aficionado + Explorador.
- Ana Perez: 240 puntos, Aficionado + Explorador + Naturalista.

Nota: `pbl:earnedBadge` no se carga a mano. Las medallas son un resultado esperado para E5, donde se determinan via SHACL y luego pueden materializarse.

## Carga integral en GraphDB

La consola web queda en:

```text
http://localhost:7200
```

Repositorio:

```text
cipa-local
```

Para dejar una demo limpia, cargar ontologias y datos integrales, excluyendo `data/smoke.ttl` porque es un fixture minimo de prueba:

```powershell
curl.exe -X DELETE "http://localhost:7200/repositories/cipa-local/statements"

curl.exe -X POST -H "Content-Type: text/turtle" --data-binary "@ontology/cipa-domain.ttl" "http://localhost:7200/repositories/cipa-local/statements"
curl.exe -X POST -H "Content-Type: text/turtle" --data-binary "@ontology/pbl.ttl" "http://localhost:7200/repositories/cipa-local/statements"

curl.exe -X POST -H "Content-Type: text/turtle" --data-binary "@data/proyectos.ttl" "http://localhost:7200/repositories/cipa-local/statements"
curl.exe -X POST -H "Content-Type: text/turtle" --data-binary "@data/personas.ttl" "http://localhost:7200/repositories/cipa-local/statements"
curl.exe -X POST -H "Content-Type: text/turtle" --data-binary "@data/protocolo-arbol.ttl" "http://localhost:7200/repositories/cipa-local/statements"
curl.exe -X POST -H "Content-Type: text/turtle" --data-binary "@data/protocolo-aves.ttl" "http://localhost:7200/repositories/cipa-local/statements"
curl.exe -X POST -H "Content-Type: text/turtle" --data-binary "@data/muestras.ttl" "http://localhost:7200/repositories/cipa-local/statements"
curl.exe -X POST -H "Content-Type: text/turtle" --data-binary "@data/juego.ttl" "http://localhost:7200/repositories/cipa-local/statements"
curl.exe -X POST -H "Content-Type: text/turtle" --data-binary "@data/juego-eventos.ttl" "http://localhost:7200/repositories/cipa-local/statements"
curl.exe -X POST -H "Content-Type: text/turtle" --data-binary "@data/player-state.ttl" "http://localhost:7200/repositories/cipa-local/statements"
```

## Queries para la presentacion

### 1. Resumen de entidades cargadas

Objetivo: mostrar el volumen de la demo integral y que el grafo contiene proyectos, protocolos, pasos, transiciones, muestras, personas y ubicaciones.

```sparql
PREFIX cipa: <https://w3id.org/cipa/ontology#>

SELECT ?tipo (COUNT(DISTINCT ?s) AS ?cantidad)
WHERE {
  VALUES ?tipo {
    cipa:Proyecto
    cipa:Protocolo
    cipa:Paso
    cipa:Transicion
    cipa:Muestra
    cipa:MuestraRespuesta
    cipa:Persona
    cipa:Ubicacion
    cipa:AdjuntoMultimedia
  }
  ?s a ?tipo .
}
GROUP BY ?tipo
ORDER BY ?tipo
```

Resultado esperado:

- 2 proyectos.
- 2 protocolos.
- 8 pasos.
- 6 transiciones.
- 7 muestras.
- 21 respuestas.
- 4 personas.
- 7 ubicaciones.
- 5 adjuntos multimedia.

### 2. Proyectos, areas y protocolos activos

Objetivo: demostrar la clasificacion de proyectos por area de conocimiento y la relacion con su protocolo activo.

```sparql
PREFIX cipa: <https://w3id.org/cipa/ontology#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?proyecto ?nombre ?areaLabel ?protocolo
WHERE {
  ?proyecto a cipa:Proyecto ;
    cipa:tieneNombre ?nombre ;
    cipa:perteneceA ?area ;
    cipa:tieneProtocoloActivo ?protocolo .

  OPTIONAL { ?area skos:prefLabel ?areaLabel . }
}
ORDER BY ?proyecto ?areaLabel
```

Resultado esperado:

- Arboles nativos en Botanica y Ambiente.
- Observacion de aves en Zoologia.
- Cada proyecto apunta a su protocolo activo.

### 3. Flujo de protocolos y bifurcaciones

Objetivo: mostrar que los protocolos no son solo una lista plana de pasos, sino un flujo navegable con transiciones y condiciones.

```sparql
PREFIX cipa: <https://w3id.org/cipa/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?transicion ?desdeLabel ?opcionLabel ?haciaLabel
WHERE {
  ?transicion a cipa:Transicion ;
    cipa:desdePaso ?desde ;
    cipa:haciaPaso ?hacia .

  OPTIONAL { ?desde rdfs:label ?desdeLabel . }
  OPTIONAL { ?hacia rdfs:label ?haciaLabel . }
  OPTIONAL {
    ?transicion cipa:disparadaPor ?opcion .
    OPTIONAL { ?opcion rdfs:label ?opcionLabel . }
  }
}
ORDER BY ?transicion
```

Resultado esperado:

- El protocolo de arboles tiene bifurcacion:
  - "Es nativa?" + "Si" -> "Nombre de la especie".
  - "Es nativa?" + "No" -> "Confirmar especie exotica".
- El protocolo de aves tiene flujo lineal:
  - Foto del ave -> Especie del ave -> Cantidad observada.

### 4. Muestras por persona, proyecto y provincia

Objetivo: mostrar datos reales de participacion, incluyendo geolocalizacion y aportes en mas de un proyecto.

```sparql
PREFIX cipa: <https://w3id.org/cipa/ontology#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?personaNombre ?proyectoNombre ?provincia (COUNT(DISTINCT ?muestra) AS ?muestras)
WHERE {
  ?muestra a cipa:Muestra ;
    cipa:respondidaPor ?persona ;
    cipa:registradaEn ?ubicacion ;
    cipa:ejecutaProtocolo ?protocolo .

  ?persona foaf:name ?personaNombre .
  ?ubicacion rdfs:label ?provincia .
  ?proyecto cipa:tieneProtocoloActivo ?protocolo ;
    cipa:tieneNombre ?proyectoNombre .
}
GROUP BY ?personaNombre ?proyectoNombre ?provincia
ORDER BY ?personaNombre ?proyectoNombre ?provincia
```

Resultado esperado:

- Ana Perez tiene 2 muestras en Arboles nativos, Buenos Aires.
- Ana Perez tiene 1 muestra en Observacion de aves, Santa Fe.
- Bruno Lattanzio participa en Arboles nativos y Observacion de aves.
- Matias Cabrera participa en Arboles nativos, Cordoba.

### 5. Respuestas con texto, opciones y multimedia

Objetivo: mostrar que una muestra puede registrar distintos tipos de respuesta.

```sparql
PREFIX cipa: <https://w3id.org/cipa/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?muestra ?pasoLabel ?valorTexto ?opcionLabel ?adjunto
WHERE {
  ?muestra a cipa:Muestra ;
    cipa:tieneRespuesta ?respuesta .

  ?respuesta cipa:correspondeAPaso ?paso .

  OPTIONAL { ?paso rdfs:label ?pasoLabel . }
  OPTIONAL { ?respuesta cipa:valorTexto ?valorTexto . }
  OPTIONAL {
    ?respuesta cipa:seleccionaOpcion ?opcion .
    OPTIONAL { ?opcion rdfs:label ?opcionLabel . }
  }
  OPTIONAL { ?respuesta cipa:valorMultimedia ?adjunto . }
}
ORDER BY ?muestra ?pasoLabel
LIMIT 30
```

Resultado esperado:

- Respuestas de texto como "Ceibo", "Algarrobo", "Jacaranda", "Hornero" y "Chimango".
- Opciones seleccionadas como "Si", "No", "Flores", "Frutos", "Espinas".
- Adjuntos multimedia como fotos de arboles y aves.

### 6. Inferencia por alineacion con PROV-O

Objetivo: demostrar que la alineacion semantica funciona. La ontologia declara `cipa:respondidaPor` como subpropiedad de `prov:wasAttributedTo`, entonces GraphDB puede responder una consulta PROV-O aunque el dato original use `cipa:respondidaPor`.

```sparql
PREFIX prov: <http://www.w3.org/ns/prov#>

ASK {
  <https://w3id.org/cipa/data/muestra/arboles-001>
    prov:wasAttributedTo
    <https://w3id.org/cipa/data/persona/ana-perez> .
}
```

Resultado esperado:

```text
true
```

### 7. Aportes por persona y area de conocimiento

Objetivo: demostrar una consulta multi-hop que deriva intereses o participacion por area sin cargar una propiedad manual `areaInteres`.

Camino usado:

```text
Persona <- respondidaPor <- Muestra -> ejecutaProtocolo <- tieneProtocoloActivo <- Proyecto -> perteneceA -> Area
```

```sparql
PREFIX cipa: <https://w3id.org/cipa/ontology#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?personaNombre ?areaLabel (COUNT(DISTINCT ?muestra) AS ?aportes)
WHERE {
  ?muestra a cipa:Muestra ;
    cipa:respondidaPor ?persona ;
    cipa:ejecutaProtocolo ?protocolo .

  ?persona foaf:name ?personaNombre .

  ?proyecto cipa:tieneProtocoloActivo ?protocolo ;
    cipa:perteneceA ?area .

  OPTIONAL { ?area skos:prefLabel ?areaLabel . }
}
GROUP BY ?personaNombre ?areaLabel
ORDER BY DESC(?aportes) ?personaNombre ?areaLabel
```

Resultado esperado:

- Ana Perez aparece en Ambiente y Botanica por sus muestras de arboles.
- Ana Perez tambien aparece en Zoologia por su muestra de aves.
- Bruno Lattanzio aparece en Botanica/Ambiente y Zoologia.
- Matias Cabrera aparece en Botanica/Ambiente.

### 8. Resumen de entidades PBL cargadas

Objetivo: mostrar que la capa PBL ya tiene juego, actividades, reglas, jugadores, estados, awards, medallas y leaderboard.

```sparql
PREFIX pbl: <https://w3id.org/cipa/pbl#>

SELECT ?tipo (COUNT(DISTINCT ?s) AS ?cantidad)
WHERE {
  VALUES ?tipo {
    pbl:Game
    pbl:Activity
    pbl:PointRule
    pbl:PointAward
    pbl:Player
    pbl:PlayerState
    pbl:Badge
    pbl:Leaderboard
  }
  ?s a ?tipo .
}
GROUP BY ?tipo
ORDER BY ?tipo
```

Resultado esperado:

- 1 juego.
- 4 actividades.
- 4 reglas de puntos.
- 18 eventos de puntos.
- 4 jugadores.
- 4 estados de jugador.
- 3 medallas.
- 1 leaderboard.

### 9. Reglas de puntos del juego PBL

Objetivo: demostrar la capa de ludificacion separada del dominio.

```sparql
PREFIX pbl: <https://w3id.org/cipa/pbl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?actividadLabel ?puntos ?dificultadLabel
WHERE {
  ?regla a pbl:PointRule ;
    pbl:rewardsActivity ?actividad ;
    pbl:pointValue ?puntos ;
    pbl:hasDifficulty ?dificultad .

  OPTIONAL { ?actividad rdfs:label ?actividadLabel . }
  OPTIONAL { ?dificultad rdfs:label ?dificultadLabel . }
}
ORDER BY DESC(?puntos)
```

Resultado esperado:

- Completar un protocolo: 50 puntos.
- Subir una foto: 20 puntos.
- Geolocalizar una muestra: 10 puntos.
- Editar perfil: 0 puntos.

### 10. Trazabilidad de puntos hacia contribuciones del dominio

Objetivo: demostrar el acople entre dominio y juego sin mezclar las ontologias. Cada `pbl:PointAward` conserva la actividad, la regla aplicada, los puntos y la contribucion de dominio que lo origino.

```sparql
PREFIX pbl: <https://w3id.org/cipa/pbl#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?personaNombre ?actividadLabel ?contribucion ?puntos ?fecha
WHERE {
  ?award a pbl:PointAward ;
    pbl:awardedTo ?estado ;
    pbl:fromActivity ?actividad ;
    pbl:fromContribution ?contribucion ;
    pbl:points ?puntos ;
    pbl:awardedAt ?fecha .

  ?actividad rdfs:label ?actividadLabel .
  ?estado pbl:forPlayer ?player .
  ?player owl:sameAs ?persona .
  ?persona foaf:name ?personaNombre .
}
ORDER BY ?personaNombre ?fecha ?actividadLabel
LIMIT 40
```

Resultado esperado:

- Ana Perez acumula eventos por completar protocolos, subir fotos y geolocalizar muestras.
- Bruno Lattanzio muestra un caso de arbol exotico sin foto y un caso de aves con foto.
- Lucia Gomez solo tiene geolocalizacion, por eso queda en 10 puntos.

### 11. Billetera materializada vs. suma de awards

Objetivo: demostrar que `pbl:pointsBalance` no es un numero arbitrario; coincide con la suma de `pbl:points` de los eventos del jugador.

```sparql
PREFIX pbl: <https://w3id.org/cipa/pbl#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?personaNombre ?balanceMaterializado (SUM(?puntos) AS ?balanceCalculado)
WHERE {
  ?estado a pbl:PlayerState ;
    pbl:forPlayer ?player ;
    pbl:pointsBalance ?balanceMaterializado .

  ?award a pbl:PointAward ;
    pbl:awardedTo ?estado ;
    pbl:points ?puntos .

  ?player owl:sameAs ?persona .
  ?persona foaf:name ?personaNombre .
}
GROUP BY ?personaNombre ?balanceMaterializado
ORDER BY DESC(?balanceMaterializado)
```

Resultado esperado:

- Ana Perez: 240 materializado y 240 calculado.
- Bruno Lattanzio: 140 materializado y 140 calculado.
- Matias Cabrera: 80 materializado y 80 calculado.
- Lucia Gomez: 10 materializado y 10 calculado.

### 12. Leaderboard del juego

Objetivo: mostrar el ranking de jugadores para el juego particular `juego/relevamiento`.

```sparql
PREFIX pbl: <https://w3id.org/cipa/pbl#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?personaNombre ?points
WHERE {
  <https://w3id.org/cipa/data/leaderboard/relevamiento> pbl:ranks ?estado .
  ?estado pbl:forPlayer ?player ;
    pbl:pointsBalance ?points .

  ?player owl:sameAs ?persona .
  ?persona foaf:name ?personaNombre .
}
ORDER BY DESC(?points)
```

Resultado esperado:

1. Ana Perez: 240.
2. Bruno Lattanzio: 140.
3. Matias Cabrera: 80.
4. Lucia Gomez: 10.

### 13. Progreso hacia medallas

Objetivo: anticipar E5 mostrando que los estados actuales ya cubren todos los casos de medalla esperados. Esta consulta no usa `pbl:earnedBadge`; evalua progreso por umbral de puntos.

```sparql
PREFIX pbl: <https://w3id.org/cipa/pbl#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?personaNombre ?medallaLabel ?points ?minPoints ?estadoMedalla
WHERE {
  ?state a pbl:PlayerState ;
    pbl:forPlayer ?player ;
    pbl:pointsBalance ?points .

  ?player owl:sameAs ?persona .
  ?persona foaf:name ?personaNombre .

  ?badge a pbl:Badge ;
    pbl:minPoints ?minPoints ;
    rdfs:label ?medallaLabel .

  BIND(IF(?points >= ?minPoints, "obtenible", "pendiente") AS ?estadoMedalla)
}
ORDER BY ?personaNombre ?minPoints
```

Resultado esperado:

- Lucia Gomez: todas pendientes.
- Matias Cabrera: Aficionado obtenible, Explorador/Naturalista pendientes.
- Bruno Lattanzio: Aficionado y Explorador obtenibles, Naturalista pendiente.
- Ana Perez: las tres obtenibles.

### 14. Medallas incrementales

Objetivo: mostrar el sistema de medallas con precedencia explicita.

```sparql
PREFIX pbl: <https://w3id.org/cipa/pbl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?medallaLabel ?minPoints ?requiereLabel
WHERE {
  ?medalla a pbl:Badge ;
    pbl:minPoints ?minPoints .

  OPTIONAL { ?medalla rdfs:label ?medallaLabel . }
  OPTIONAL {
    ?medalla pbl:requiresBadge ?requiere .
    OPTIONAL { ?requiere rdfs:label ?requiereLabel . }
  }
}
ORDER BY ?minPoints
```

Resultado esperado:

- Aficionado: 50 puntos.
- Explorador: 100 puntos, requiere Aficionado.
- Naturalista: 200 puntos, requiere Explorador.

## Guion sugerido

1. Mostrar que la infraestructura esta lista: GraphDB corriendo, repo `cipa-local`, carga reproducible.
2. Ejecutar la query 1 para mostrar volumen del grafo.
3. Ejecutar la query 2 para explicar proyectos, areas y protocolos activos.
4. Ejecutar la query 3 para mostrar que los protocolos tienen flujo y bifurcaciones.
5. Ejecutar la query 4 para pasar de T-Box a datos reales de participacion.
6. Ejecutar la query 5 para mostrar riqueza de respuestas: texto, opcion y multimedia.
7. Ejecutar la query 6 para mostrar inferencia por alineacion con PROV-O.
8. Ejecutar la query 7 para mostrar consulta multi-hop y participacion por areas.
9. Ejecutar las queries 8 y 9 para mostrar catalogo PBL y reglas de puntos.
10. Ejecutar la query 10 para mostrar trazabilidad entre puntos y contribuciones de dominio.
11. Ejecutar la query 11 para verificar billetera materializada vs. suma de eventos.
12. Ejecutar la query 12 para mostrar el leaderboard.
13. Ejecutar las queries 13 y 14 para cerrar con progreso de medallas y precedencia incremental.

## Cierre

El avance actual ya permite demostrar un ciclo completo:

```text
Ontologia OWL -> datos RDF -> validacion SHACL -> carga GraphDB -> consultas SPARQL -> inferencia -> capa PBL
```

Las proximas historias naturales son:

- Definir shapes de medallas con `sh:sparql`.
- Materializar `pbl:earnedBadge` a partir del resultado SHACL.
- Consultar medallas asignadas y estatus del jugador desde GraphDB.
- Preparar las queries finales de entrega sobre la carga integral.
