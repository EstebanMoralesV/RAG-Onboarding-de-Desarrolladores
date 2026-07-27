# RAG para Onboarding de Desarrolladores

## Descripción

### 1. El problema

El onboarding de desarrolladores consiste en que un nuevo integrante comprenda la documentación, las decisiones técnicas y los procesos de la empresa. Cuando la información es difícil de encontrar o la capacitación no resuelve todas las dudas, el desarrollador invierte más tiempo buscando respuestas, lo que aumenta su carga cognitiva, el estrés y retrasa su productividad. Una documentación clara y accesible facilita la transferencia de conocimiento y reduce el tiempo necesario para incorporarse a un proyecto [1][2].

Estos retrasos afectan tanto a la empresa como al cliente. La empresa pierde tiempo y recursos, reduce su capacidad para atender nuevos proyectos y aumenta el riesgo de incumplimientos. Por su parte, el cliente puede recibir un producto que no cumpla con sus expectativas debido a una mala interpretación de los requisitos. Además, otros miembros del equipo, como analistas de sistemas y arquitectos de software, dedican parte de su tiempo a responder preguntas repetitivas en lugar de enfocarse en tareas de mayor valor.

### 2. Alcance del proyecto

- **Qué hará:** Responder dudas técnicas basadas estrictamente en tres documentos Markdown de prueba (por ejemplo: arquitectura, cultura y despliegue).
- **Qué NO hará:** No se conectará a APIs externas (Jira, Slack), no buscará en internet y se limitará a la documentación provista en la carpeta `data` de este repositorio.
- **Criterios de éxito:** El sistema debe procesar los documentos y responder preguntas con precisión y de forma entendible, indicando cuando no conoce la respuesta para minimizar las alucinaciones.

### 3. Arquitectura y decisiones técnicas (ADRs)

- **Orquestador:** n8n (elegido por su rapidez para prototipar flujos visuales).
- **LLM y Embeddings:** Cohere (elegido por su compatibilidad entre embeddings y modelo de chat y por su rendimiento).
- **Base de datos vectorial:** n8n In-Memory Vector Store.
- **Almacenamiento de mensajes:** n8n In-Memory Almacenamiento de mensajes.
  - **Justificación:** Se prioriza la velocidad de integración y la simplicidad sobre la persistencia a largo plazo.

### X. Ejemplos de preguntas que el agente puede responder.

#### Nivel Trainee

- **1. Sobre herramientas y glosario:** "En la documentación veo mucho las siglas RTO y RPO en la estrategia de respaldo de la Capa de Datos. ¿Me podrías dar un ejemplo sencillo con palabras cotidianas de qué significan si se cae el servidor?"
- **2. Sobre el entorno local:** "Acabo de clonar el repositorio del Backend. Para levantar el proyecto en mi computadora (Local) con Docker Compose, ¿me conecto a la base de datos de 'Dev' o utilizamos datos sintéticos?"
- **3. Sobre la cultura de desarrollo:** "Me asignaron mi primer ticket, pero me acordé de nuestra regla 'Documentar antes de desarrollar'. ¿Dónde se supone que debo escribir esta documentación antes de empezar a programar?"

#### Nivel Junior

- **1. Sobre el patrón BFF:** "Tengo que agregar el campo 'duración_en_minutos' a la pantalla de detalles de la película en Web. ¿Debo modificar el 'Content Metadata Service' directamente o esa agregación se hace en el BFF de Web?"
- **2. Sobre persistencia de datos:** "Voy a crear un servicio pequeño para guardar las configuraciones de la interfaz del usuario en la Smart TV (como tamaño de letra y colores). Revisando nuestras bases de datos, ¿debería pedir una tabla en PostgreSQL o una colección en MongoDB?"
- **3. Sobre asincronía (Kafka):** "Tengo que registrar cuando un usuario le da 'Me gusta' a una serie. En Kafka, ¿debería crear un tópico nuevo exclusivo para los likes, o usamos el tópico general del 'Event Ingestion Service'?"

#### Nivel Senior

- **1. Sobre Disaster Recovery (Multi-Nube):** "Revisando la estrategia Multi-Nube, veo que GCP es primaria y AWS secundaria. Si perdemos la región principal de GCP por completo, ¿cómo está configurado nuestro 'failover automático' para las bases de datos PostgreSQL para garantizar el RPO de 5 minutos sin pérdida de consistencia?"
- **2. Sobre Transacciones Distribuidas:** "El ADR-002 menciona el uso de Kafka y el 'Saga Pattern'. Para el flujo de pagos recurrentes, ¿estamos orquestando las sagas de forma coreográfica pura a través de eventos, o tenemos un servicio orquestador centralizado que maneje las transacciones de compensación si el 'Payment Service' falla?"
- **3. Sobre Machine Learning (MLOps):** "Revisando la plataforma de ML, veo que usamos Feast como Feature Store. Para la inferencia en tiempo real del 'Recommendation Service', ¿cómo estamos mitigando el 'training-serving skew' (desviación) entre lo que entrena Vertex AI y lo que servimos a baja latencia en los contenedores?"

### Ejemplos de respuestas generadas por el agente.

## Referencias

[1] Guru. *Documentación de software: qué es y por qué es importante*. https://www.getguru.com/es/reference/software-documentation

[2] Centro Banamex. *¿Qué es la documentación interna y externa?* https://www.centrobanamex.com.mx/que-es-la-documentacion-interna-y-externa/