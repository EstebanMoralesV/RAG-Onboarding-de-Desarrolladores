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
- **LLM y Embeddings:** Cohere (elegido por su compatibilidad y rendimiento).
- **Base de datos vectorial:** n8n In-Memory Vector Store.
  - **Justificación:** Se prioriza la velocidad de integración y la simplicidad sobre la persistencia a largo plazo.

## Referencias

[1] Guru. *Documentación de software: qué es y por qué es importante*. https://www.getguru.com/es/reference/software-documentation

[2] Centro Banamex. *¿Qué es la documentación interna y externa?* https://www.centrobanamex.com.mx/que-es-la-documentacion-interna-y-externa/