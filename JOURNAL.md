# Journal de Desarrollo | RAG Onboarding

## 1. Creación de Documentación Ficticia

* **Fecha:** 25 de julio de 2026
* **Estado:** Completado

---

### Objetivo
Crear un repositorio de documentación estandarizado que sirva como referencia y base de conocimiento para la entrada del RAG.

---

### Decisión
Se optó por generar la documentación mediante IA (Kimi K2.6) para simular el contexto de una empresa ficticia ("Fictional Entertainment MX"), abarcando misión, valores, políticas internas y arquitectura técnica. Esto permite probar el pipeline con datos estructurados sin comprometer información sensible.

---

## 2. Extracción y Limpieza de Documentación (Carpeta `data`)

* **Fecha:** 26 de julio de 2026
* **Estado:** En Proceso

---

### Objetivo
Automatizar la recolección de los documentos de onboarding almacenados en el repositorio de GitHub, descargarlos en texto plano y aplicar un preprocesamiento que elimine ruido antes de la fase de vectorización semántica.

---

### Detalles Técnicos del Nodo de Preprocesamiento
* Eliminación de metadatos irrelevantes y sintaxis innecesaria.
* Normalización de texto (Remoción de espacios/saltos dobles).

---

### Flujo

```mermaid
flowchart TD
    A[API GitHub: Listar archivos] -->|Array de metadatos| B[HTTP GET: download_url]
    B -->|Texto plano| C[Nodo de Preprocesamiento]
    C -->|Texto limpio| D[Siguiente paso: Chunking]