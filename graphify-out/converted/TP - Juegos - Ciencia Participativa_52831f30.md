<!-- converted from TP - Juegos - Ciencia Participativa.docx -->

Modelo de Dominio: Proyectos de Ciencia Participativa
El objetivo es modelar un ecosistema donde múltiples voluntarios recolectan datos científicos bajo una estructura organizada. A continuación, se detallan los componentes principales:
1. El Proyecto de Ciencia Participativa
Cada proyecto es la unidad central de trabajo y cuenta con los siguientes atributos:
Identificación: Nombre y descripción clara del objetivo.
Clasificación: Áreas del conocimiento a las que pertenece (biología, astronomía, ecología, etc.).
Protocolo: Cada proyecto posee un único protocolo activo de recolección de datos.
2. El Protocolo de Recolección
Es la guía que define cómo se deben capturar los datos. Se caracteriza por:
Estado: Puede estar activo o inactivo.
Composición: Está formado por una serie de pasos secuenciales.
Orden: Los pasos deben seguir una lógica cronológica o procedimental.
3. Definición de los Pasos
Cada paso dentro de un protocolo tiene características particulares según el tipo de dato que se desee obtener. Ejemplos de pasos comunes:
Geolocalización: Obtener las coordenadas geográficas del hallazgo.
Temporalidad: Registro automático de fecha y hora.
Multimedia: Captura de una fotografía del espécimen u objeto.
Cuestionario: Preguntas que pueden ser de opción múltiple (Multiple Choice) de selección simple o múltiple. Dependiendo de la selección, se puede realizar una bifurcación en los pasos siguientes, como se muestra en la imagen anterior.


El Proceso de Recolección (Muestreo)
Una vez que el protocolo está definido, el dominio debe ser capaz de modelar las respuestas o recolecciones enviadas por los usuarios.
La Muestra (Respuesta al Protocolo)
Cada vez que una persona realiza un aporte, se genera una instancia de respuesta que vincula los datos específicos con los pasos del protocolo:
Ejemplo de una recolección individual:
Ubicación específica: Latitud/Longitud exacta.
Hora exacta: Momento preciso de la toma.
Archivo: La foto específica tomada en ese instante.
Datos: Las respuestas seleccionadas para las preguntas del cuestionario.
Multiplicidad y Alcance
El sistema está diseñado para gestionar una multiplicidad de proyectos en simultáneo. Estas recolecciones pueden repetirse indefinidamente en diversos puntos geográficos, permitiendo que la recolección de datos sea escalable a nivel local, provincial, nacional o global.

Modelo de Gestión de Participantes y Perfiles
Este módulo se enfoca en el capital humano del proyecto, permitiendo no solo registrar la actividad, sino también entender el comportamiento y fomentar la interacción con los colaboradores.
1. El Participante (Actor Activo)
Es el individuo encargado de ejecutar los protocolos en territorio. Sus características principales son:
Identidad Única: Cada colaborador posee un registro que permite rastrear sus aportes de manera unívoca.
Atribución de Datos: Cada "relevamiento" o muestra enviada queda vinculada permanentemente al usuario que la generó.
2. Dinámica de Participación
El modelo contempla una relación flexible y multívoca entre los usuarios y los proyectos:
Multiplicidad Simultánea: Una persona puede colaborar en diversos proyectos al mismo tiempo (ej. medir calidad del agua y observar aves).
Historial Longitudinal: Se registra la participación a lo largo del tiempo, permitiendo analizar la evolución del compromiso del usuario.
3. El Perfil del Colaborador
A partir de la actividad registrada, el sistema permite la construcción de un Perfil de Usuario dinámico:
Análisis de Intereses: Identificación de las áreas de conocimiento o tipos de protocolos donde el usuario es más activo.
Nivel de Expertise: Capacidad de categorizar a los usuarios según la calidad o frecuencia de sus aportes.
Interacción Personalizada: El perfil sirve como base para crear estrategias de engagement, permitiendo al proyecto interactuar con el colaborador de forma específica y relevante.
Modelo de Ludificación Adaptativa (Framework PBL)
El sistema superpone una capa de ludificación (gamification) sobre las actividades de recolección de datos para incentivar la participación y mejorar la calidad de los aportes.
1. Elementos del Framework PBL
El modelo se basa en la tríada clásica, pero con una estructura semántica flexible:
Points (Puntos): Representan la unidad de medida del esfuerzo y progreso del usuario.
Badges (Insignias/Logros): Representaciones visuales de hitos alcanzados o competencias adquiridas.
Leaderboards (Tablas de posiciones): Herramientas de comparación social para fomentar la competencia sana y el reconocimiento.
2. Lógica de Reglas y Recompensas
El núcleo del modelo es un motor de reglas que determina el flujo de la gamificación:
Configuración de Actividades: Diferenciación entre tareas que otorgan puntos (ej. completar un protocolo complejo) y tareas administrativas o simples que no lo hacen.
Asignación de Puntos: Reglas específicas para calcular la cantidad de puntos según la dificultad de la tarea o la precisión del relevamiento.
Gestión de Insignias:
Criterios de Adjudicación: Reglas de "cuándo" y "cómo" se otorga una insignia.
Precedencia y Dependencia: Lógica de jerarquía donde ganar una insignia puede requerir haber obtenido otras previamente.
3. Estado del Usuario-Jugador
El modelo debe ser capaz de representar y consultar en tiempo real el perfil del "jugador":
Billetera de Puntos: Total acumulado por el usuario.
Colección de Logros: Inventario de insignias obtenidas.
Nivel de Dificultad: Atributo que permite ajustar la recompensa en función de la complejidad del desafío propuesto.

Representación Semántica y Adaptabilidad
Siguiendo los lineamientos de la investigación de Dalponte, este modelo no es estático, sino que busca una descripción semántica profunda para permitir la adaptabilidad:
(A complementar con la documentación de Mara Dalponte Ayastuy)