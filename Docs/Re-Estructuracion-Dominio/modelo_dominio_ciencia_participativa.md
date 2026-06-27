# Modelo de dominio — Ciencia Participativa

## Descripción general

El modelo representa un sistema de **proyectos de ciencia participativa** donde un proyecto tiene protocolos activos, los protocolos contienen pasos, y los pasos pueden ser de tipo multimedia o cuestionario. Al ejecutar un protocolo, se genera una muestra con respuestas asociadas a cada paso.

El dominio parte de un **Área de Conocimiento**, que clasifica o agrupa distintos **Proyectos**. Cada proyecto puede tener uno o más **Protocolos**, aunque se define como regla de negocio que el proyecto debe estar asociado a un **protocolo activo**.

Un **Protocolo** representa una guía o procedimiento que debe seguir el usuario. Está compuesto por pasos y tiene un primer paso definido. Cada paso puede especializarse en:

- `PasoMultimedia`
- `PasoCuestionario`

Ambos son subclases de `Paso`, por lo que en estos casos sí corresponde usar `rdfs:subClassOf`.

---

## Prefijos e IRIs conservados

La reestructuracion cambia los **componentes del dominio**, pero no cambia la separacion de IRIs ya definida para el TP.

```turtle
@prefix cipa:      <BASE_IRI/ontology/cipa#> .
@prefix pbl:       <BASE_IRI/ontology/pbl#> .
@prefix cipa-data: <BASE_IRI/data/> .

@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix geo:  <http://www.opengis.net/ont/geosparql#> .
```

Uso esperado:

- `cipa:` contiene la T-Box del dominio reestructurado: `cipa:Proyecto`, `cipa:AreaConocimiento`, `cipa:Protocolo`, `cipa:Paso`, `cipa:PasoMultimedia`, `cipa:PasoCuestionario`, `cipa:Enunciado`, `cipa:Transicion`, `cipa:Muestra`, `cipa:MuestraRespuesta`, `cipa:Persona`, `cipa:Ubicacion` y `cipa:AdjuntoMultimedia`.
- `cipa:` tambien contiene las propiedades del dominio: `cipa:tieneProtocoloActivo`, `cipa:tienePrimerPaso`, `cipa:desdePaso`, `cipa:haciaPaso`, `cipa:disparadaPor`, `cipa:ejecutaProtocolo`, `cipa:respondidaPor`, `cipa:tieneRespuesta`, `cipa:correspondeAPaso`, `cipa:valorTexto`, `cipa:valorMultimedia`, etc.
- `cipa-data:` contiene individuos y datos de ejemplo: proyectos, protocolos, pasos, opciones, muestras, respuestas, personas, ubicaciones y adjuntos.
- `pbl:` se conserva para la ontologia de ludificacion y no se mezcla con el dominio; el acople se hace en los datos cuando una `cipa:Muestra` o `cipa:MuestraRespuesta` origina eventos de puntos.
- Los prefijos estandar (`skos:`, `prov:`, `foaf:`, `geo:`, `sh:`, etc.) se usan para alineaciones y validacion, no para reemplazar los conceptos centrales del dominio.

Convencion de nombres:

- Clases en `UpperCamelCase`: `cipa:MuestraRespuesta`.
- Propiedades en `lowerCamelCase`: `cipa:tienePrimerPaso`.
- Individuos en `kebab-case` bajo `cipa-data:`: `cipa-data:muestra/ceibo-001`.

---

## Entidades principales

## Área de Conocimiento

Representa una categoría o clasificación temática.

Ejemplos conceptuales:

- Biología
- Ambiente
- Botánica
- Zoología

Relación principal:

```text
ÁreaConocimiento --clasificacion--> Proyecto
```

También podría modelarse como:

```text
Proyecto --perteneceA--> ÁreaConocimiento
```

---

## Proyecto

Un **Proyecto** es la unidad general de trabajo. Agrupa protocolos relacionados con una temática o investigación.

Propiedades y relaciones:

```text
Proyecto
- tieneNombre -> nombre
- tieneDescripcion -> descripcion
- tieneProtocolo -> Protocolo
```

Regla de negocio:

```text
Proyecto -> tieneProtocoloActivo
```

Esto significa que, aunque puedan existir varios protocolos históricos o inactivos, el proyecto debe tener identificado cuál es el protocolo actualmente activo.

---

## Protocolo

Un **Protocolo** define el procedimiento que debe ejecutar el usuario. Está compuesto por pasos y tiene una relación con el primer paso.

Propiedades y relaciones:

```text
Protocolo
- tieneNombre -> nombre
- tieneDescripcion -> descripcion
- tieneEstado -> EstadoProtocolo
- tienePaso -> Paso
- tienePrimerPaso -> Paso
```

La relación `tienePrimerPaso` es importante porque el flujo del protocolo necesita saber dónde comienza.

---

## Paso

`Paso` es la clase base. Representa una unidad dentro de un protocolo.

Relación principal:

```text
Paso
- tieneEnunciado -> Enunciado
```

Además, el paso se especializa en dos subtipos:

```text
PasoMultimedia rdfs:subClassOf Paso
PasoCuestionario rdfs:subClassOf Paso
```

En este caso, el uso de `rdfs:subClassOf` es correcto, porque `PasoMultimedia` y `PasoCuestionario` son tipos específicos de `Paso`.

---

## PasoMultimedia

Un **PasoMultimedia** representa un paso cuyo objetivo es mostrar contenido al usuario o solicitar una interacción relacionada con contenido multimedia.

Relaciones:

```text
PasoMultimedia
- tieneEnunciado -> EnunciadoMultimedia
```

Corrección conceptual importante:

El archivo multimedia subido por el usuario **no debe ser parte del enunciado**. El enunciado pertenece a la definición del protocolo, mientras que el archivo subido por el usuario pertenece a la ejecución concreta del protocolo, es decir, a la muestra.

Por lo tanto:

```text
Incorrecto:
EnunciadoMultimedia -> AdjuntoMultimedia

Correcto:
MuestraRespuesta -> valorMultimedia -> AdjuntoMultimedia
```

---

## PasoCuestionario

Un **PasoCuestionario** representa un paso que espera una respuesta del usuario.

Relaciones:

```text
PasoCuestionario
- tieneEnunciado -> EnunciadoCuestionario
```

El `EnunciadoCuestionario` define el texto o contenido de la pregunta.

Además:

```text
EnunciadoCuestionario
- tieneTipo -> TipoRespuesta
```

Los tipos de respuesta posibles son:

```text
Texto libre
Selector único
Selector múltiple
```

También se relaciona con las posibles opciones de respuesta:

```text
EnunciadoCuestionario -> tienePosibilidades -> OpcionRespuestaCuestionario
```

---

## OpcionRespuestaCuestionario

Representa una opción posible para un cuestionario.

Por ejemplo, si la pregunta es:

```text
¿La especie observada es nativa?
```

Las opciones podrían ser:

```text
Sí
No
No sabe
```

Relaciones:

```text
OpcionRespuestaCuestionario
- rdfs:label -> rdf:langString
```

Esto significa que la opción tiene una etiqueta legible, posiblemente multilenguaje.

Ejemplo:

```text
OpcionRespuestaCuestionario: Sí
rdfs:label: "Sí"@es
```

---

## Transición

La entidad **Transicion** representa el flujo entre pasos del protocolo.

Relaciones:

```text
Transicion
- desdePaso -> Paso
- haciaPaso -> Paso
- disparadaPor -> OpcionRespuestaCuestionario
```

La relación `disparadaPor` es opcional. Esto permite representar dos casos.

### Transición sin condición

```text
Paso A -> Paso B
```

En este caso, siempre que se completa el Paso A, se continúa al Paso B.

### Transición condicionada

```text
Paso A + opción seleccionada X -> Paso B
```

Por ejemplo:

```text
Si responde "Sí" -> ir a Paso 2
Si responde "No" -> ir a Paso 5
```

En el modelo, `Transicion` se conecta con:

```text
desdePaso
haciaPaso
disparadaPor, opcional
```

Esto permite modelar tanto avances lineales como bifurcaciones.

---

## Muestra

Una **Muestra** representa una ejecución concreta de un protocolo por parte de una persona.

Relaciones y propiedades:

```text
Muestra
- ejecutaProtocolo -> Protocolo
- respondidaPor -> Persona
- fechaHora -> timestamp
- registradaEn -> Ubicacion
- tieneRespuesta -> MuestraRespuesta
```

La relación `tieneRespuesta` es de **uno a muchos**:

```text
Muestra -> tieneRespuesta -> MuestraRespuesta
```

Es decir, una muestra puede tener muchas respuestas, una por cada paso recorrido o respondido.

---

## Persona

Representa al usuario o persona que responde o genera la muestra.

Relación:

```text
Muestra --respondidaPor--> Persona
```

---

## Ubicación

Representa la ubicación donde se registró la muestra.

Relaciones:

```text
Ubicacion
- latitud -> decimal
- longitud -> decimal
```

---

## MuestraRespuesta

`MuestraRespuesta` es la entidad que registra lo que ocurrió en cada paso durante la ejecución de una muestra.

Relaciones y propiedades:

```text
MuestraRespuesta
- correspondeAPaso -> Paso
- seleccionaOpcion -> OpcionRespuestaCuestionario
- valorTexto -> texto
- valorMultimedia -> AdjuntoMultimedia
- fechaHoraRespuesta -> timestamp
```

Se define la regla:

```text
MuestraRespuesta
- una por cada paso
```

Esto significa que por cada paso recorrido dentro del protocolo se genera una respuesta asociada a la muestra.

---

## AdjuntoMultimedia

`AdjuntoMultimedia` representa un archivo subido por el usuario como parte de la muestra.

Relaciones:

```text
MuestraRespuesta
- valorMultimedia -> AdjuntoMultimedia

AdjuntoMultimedia
- tieneUrl -> url
```

La corrección conceptual es que `AdjuntoMultimedia` no debe depender de `EnunciadoMultimedia`, sino de `MuestraRespuesta`.

Esto se debe a que el adjunto no es parte de la definición del protocolo, sino del dato recolectado durante la ejecución.

---

# Reglas importantes del modelo

## Proyecto con protocolo activo

```text
Proyecto -> tieneProtocoloActivo
```

El proyecto debe identificar cuál es el protocolo vigente o activo.

---

## Protocolo con primer paso

```text
Protocolo -> tienePrimerPaso
```

Todo protocolo debe tener un paso inicial definido para poder ejecutar el flujo.

---

## Compatibilidad entre MuestraRespuesta y tipo de paso

Regla base:

```text
MuestraRespuesta debe guardar un tipo de valor compatible con el tipo de paso al que responde.
```

Más específicamente:

```text
Si MuestraRespuesta corresponde a PasoMultimedia:
- debe tener valorMultimedia

Si MuestraRespuesta corresponde a PasoCuestionario:
- debe tener valorTexto, seleccionaOpcion, o ambas, según el tipo de cuestionario
```

Para cuestionarios:

```text
Texto libre:
- valorTexto

Selector único:
- seleccionaOpcion

Selector múltiple:
- seleccionaOpcion, posiblemente múltiples opciones
```

---

# Descripción resumida

El modelo define una ontología para proyectos de ciencia participativa. Un proyecto pertenece a un área de conocimiento y tiene protocolos asociados. Cada protocolo define un flujo de pasos, comenzando por un primer paso y avanzando mediante transiciones. Los pasos pueden ser multimedia o cuestionarios.

Los cuestionarios tienen enunciados, tipos de respuesta y opciones posibles. Las transiciones permiten avanzar entre pasos, opcionalmente dependiendo de una opción seleccionada.

Cuando una persona ejecuta un protocolo, se crea una muestra. La muestra registra la persona, fecha, ubicación y un conjunto de respuestas. Cada `MuestraRespuesta` corresponde a un paso recorrido. Si el paso era multimedia, la respuesta puede contener un adjunto multimedia; si era cuestionario, contiene el valor respondido o la opción seleccionada.
