<div align="center">

# 🏗️ Arquitectura Tecnológica — Fictional Entertainment MX

### *Tecnología que conecta historias.*

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

**Documento de Arquitectura de Referencia**

*Plataforma de Streaming • Microservicios • Cloud Native • Seguridad*

</div>

---

# 📖 Introducción

Este documento define la arquitectura tecnológica de la plataforma de streaming de Fictional Entertainment MX. Su propósito es servir como fuente de verdad para equipos de ingeniería, operaciones y producto, optimizado para ser procesado en sistemas RAG mediante chunking semántico.

Cada sección está diseñada para ser **autocontenida**, con encabezados claros, tablas densas y flujos narrativos completos que facilitan el corte en chunks sin pérdida de contexto.

---

# 🎯 Propósito de la Arquitectura

> **Construir una plataforma de streaming segura, escalable y centrada en el usuario que permita conectar historias a millones de personas en Latinoamérica y el mundo.**

La arquitectura busca equilibrar tres factores fundamentales:

- 😊 **La satisfacción del usuario** — Experiencia fluida, personalizada y confiable.
- 💼 **La sostenibilidad del negocio** — Costos optimizados y modelos de suscripción robustos.
- 🚀 **La innovación tecnológica** — ML, edge computing y arquitectura cloud-native.

---

# ❤️ Principios Arquitectónicos

| Principio | Significado |
|-----------|-------------|
| 💡 **Desacoplamiento** | Cada capacidad de negocio reside en un dominio independiente con su propio ciclo de vida. |
| 🤝 **Resiliencia** | Todos los componentes asumen fallos e implementan degradación elegante. |
| ⭐ **API-First** | Las interfaces se definen por contratos versionados antes de la implementación. |
| 📚 **Datos como producto** | Cada dominio es dueño de sus datos y expone datasets curated para análisis. |
| 🔒 **Seguridad by design** | Zero-trust, cifrado end-to-end y autenticación federada en todo punto de acceso. |
| 🌱 **Sostenibilidad de costos** | Uso de serverless y spot instances donde la latencia lo permita. |
| 🎯 **Observabilidad full-stack** | Métricas, logs y traces en todos los componentes para MTTR mínimo. |

---

# 🧭 Filosofía de Diseño

> **La arquitectura existe para resolver problemas reales, no para demostrar complejidad.**

Antes de diseñar cualquier componente nos preguntamos:

- ¿Genera valor para el usuario?
- ¿Hace más feliz la experiencia de streaming?
- ¿Será fácil de operar y mantener?
- ¿Podrá escalar a millones de usuarios?
- ¿Vale la inversión de ingeniería?

Si la respuesta es **no**, buscamos otra alternativa.

---

# 🏢 Cultura de Arquitectura

Nuestra forma de diseñar sistemas se basa en cinco pilares:

```text
           Innovación
                ▲
                │
 Calidad ◄──────┼──────► Colaboración
                │
                ▼
      Resiliencia
                │
                ▼
   Observabilidad
```

---

# 🧠 Cómo Tomamos Decisiones Tecnológicas

Toda decisión arquitectónica debe cumplir con la mayor cantidad posible de estos criterios:

| Criterio | Pregunta |
|----------|----------|
| 👤 **Usuario** | ¿Mejora la experiencia de streaming? |
| 💰 **Negocio** | ¿Reduce costos o aumenta retención? |
| 🛠 **Ingeniería** | ¿Es técnicamente sostenible a 5 años? |
| 📈 **Escalabilidad** | ¿Funcionará con 10x más usuarios? |
| 🔒 **Seguridad** | ¿Protege datos y contenido? |
| 📊 **Datos** | ¿Tenemos evidencia para justificarla? |

---

<div align="center">

# 🏗️ Arquitectura de Alto Nivel

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

</div>

La plataforma se organiza en cinco capas lógicas desacopladas que operan de forma conjunta:

```text
┌─────────────────────────────────────────────────────────────┐
│  🎨 CAPA DE EXPERIENCIA DE USUARIO (UX Layer)               │
│  Web App · Mobile Apps (iOS/Android) · Smart TV · Consolas  │
├─────────────────────────────────────────────────────────────┤
│  🌐 CAPA DE EDGE Y DISTRIBUCIÓN (Edge Layer)                │
│  CDN Global · API Gateway · WAF · Load Balancers            │
├─────────────────────────────────────────────────────────────┤
│  ⚙️ CAPA DE SERVICIOS (Service Layer)                       │
│  Microservicios de Dominio · BFF · Event Bus                │
├─────────────────────────────────────────────────────────────┤
│  🗄️ CAPA DE DATOS (Data Layer)                              │
│  Bases de Transacción · Cache · Data Lake · ML Platform     │
├─────────────────────────────────────────────────────────────┤
│  ☁️ CAPA DE INFRAESTRUCTURA (Infrastructure Layer)          │
│  Cloud Multi-Region · Kubernetes · Observabilidad · CI/CD   │
└─────────────────────────────────────────────────────────────┘
```

Cada capa se describe en detalle en las secciones siguientes.

---

<div align="center">

# 🎨 Capa de Experiencia de Usuario

</div>

La Capa de Experiencia de Usuario es el punto de contacto entre los suscriptores y la plataforma. Su objetivo es ofrecer una interfaz rápida, accesible y consistente en cualquier dispositivo.

## 📱 Clientes Soportados

| Dispositivo | Tecnología | Descripción |
|-------------|------------|-------------|
| 🖥️ **Aplicación Web** | React + Next.js (SSR) | SPA con Server-Side Rendering para SEO y time-to-first-byte optimizado. |
| 📱 **iOS** | Swift (Nativo) | Experiencia nativa con componentes del design system. |
| 🤖 **Android** | Kotlin (Nativo) | Paridad de features con iOS mediante shared components. |
| 📺 **Smart TVs** | HTML5 / TVML / Tizen / webOS | Clientes ligeros para televisores inteligentes. |
| 🎮 **Consolas** | SDKs Nativos (PS, Xbox) + tvOS | Streaming optimizado para gamepads y controles remotos. |
| 📟 **Set-Top Boxes** | React Native / C++ | Clientes mínimos para hardware de bajo rendimiento. |

## 🎨 Design System y Tokens

Se utiliza un **design system centralizado** que expone tokens de diseño (colores, tipografía, espaciado) mediante una API de configuración. Esto permite actualizar la identidad visual sin despliegues de aplicación.

## 🧠 Estrategia de Estado en el Cliente

| Tipo de Estado | Tecnología | Uso |
|----------------|------------|-----|
| 🌍 **Global** | Redux / Redux Toolkit | Sesión, preferencias, catálogo en caché. |
| 🏠 **Local** | React Context / Compose State | Interacciones efímeras de UI. |
| 📴 **Offline-first** | Background Sync | Catálogo navegable y "Mi Lista" sin conexión. |

---

<div align="center">

# 🌐 Capa de Edge y Distribución

</div>

La Capa de Edge y Distribución gestiona el tráfico de entrada, la terminación TLS, el balanceo de carga y la entrega de contenido estático y de streaming.

## 🚀 CDN Global para Streaming de Video

| Aspecto | Detalle |
|---------|---------|
| 🏢 **Proveedor** | Multi-CDN (Akamai, CloudFront, Cloudflare) con enrutamiento inteligente. |
| 📦 **Contenido** | Video segmentado (HLS/DASH), imágenes de catálogo, subtítulos, metadatos. |
| 💾 **Estrategia de caché** | TTL jerárquico: contenido popular en edge; nicho en origin shield. |
| 🔮 **Prefetching** | Algoritmo de recomendación precarga primeros segundos del siguiente video sugerido. |

## 🚪 API Gateway

| Capacidad | Descripción |
|-----------|-------------|
| 🛡️ **Rate Limiting** | Protección contra abuso y DDoS de aplicación. |
| 🔑 **Autenticación** | Validación JWT/OAuth2 en el borde. |
| 🔄 **Transformación** | Conversión de protocolos y versionado de APIs. |
| 🧭 **Enrutamiento** | Direccionamiento inteligente a microservicios. |
| ⚡ **Circuit Breaker** | Aislamiento de servicios degradados. |
| 🛠️ **Tecnología** | Kong Gateway / AWS API Gateway en modo híbrido. |

## 🧱 Web Application Firewall (WAF)

- Protección contra OWASP Top 10 y bots maliciosos.
- Reglas personalizadas por región geográfica.
- Integración con SIEM para correlación de amenazas.

## ⚖️ Balanceo de Carga

| Capa | Tecnología | Uso |
|------|------------|-----|
| 🌐 **Capa 7 (HTTP/gRPC)** | NGINX / Envoy (Ingress) | Tráfico de APIs y BFFs. |
| 🔌 **Capa 4 (TCP/UDP)** | Network Load Balancers | Streaming en tiempo real y WebRTC. |

---

<div align="center">

# ⚙️ Capa de Servicios

</div>

La Capa de Servicios contiene la lógica de negocio descompuesta en dominios acotados (Bounded Contexts). Cada microservicio es autónomo, posee su propia base de datos y se comunica de forma asíncrona preferentemente.

## 🏛️ Dominios de Negocio y Servicios

| Dominio | Servicios Clave | Responsabilidad |
|---------|-----------------|-----------------|
| 🔐 **Identidad y Acceso** | Auth Service, MFA Service, Session Manager | Autenticación, autorización, tokens y sesiones. |
| 👤 **Usuarios y Perfiles** | User Service, Profile Service, Kids Profile Service | Cuentas, perfiles familiares, controles parentales. |
| 🎬 **Catálogo de Contenido** | Content Metadata Service, Search Service, Genre Service | Metadatos, motor de búsqueda full-text, taxonomías. |
| ▶️ **Streaming y Playback** | Playback Service, License Service, DRM Service | Orquestación de reproducción, licencias DRM. |
| 💳 **Facturación y Pagos** | Subscription Service, Payment Service, Invoice Service | Planes, cobros recurrentes, pasarelas de pago, facturación. |
| 🤖 **Recomendaciones** | Recommendation Service, Personalization Service | Algoritmos de ML para sugerencias y filas personalizadas. |
| 📢 **Notificaciones** | Notification Service, Email Service, Push Service | Comunicaciones transaccionales y de marketing. |
| 📊 **Analítica y Eventos** | Event Ingestion Service, Analytics Service, Feature Flags | Ingesta de eventos, métricas de negocio, A/B testing. |

## 📡 Patrones de Comunicación entre Servicios

| Patrón | Tecnología | Uso |
|--------|------------|-----|
| 🔄 **Síncrona** | gRPC | Comunicación inter-servicio de baja latencia dentro del clúster. |
| 🌐 **Síncrona Pública** | REST (OpenAPI) | APIs externas y BFFs. |
| 📨 **Asíncrona** | Apache Kafka | Event bus central para eventos de dominio. |
| 🎭 **Saga Pattern** | Kafka + Orquestación | Transacciones distribuidas (ej. flujo de suscripción). |

## 🧩 Backend for Frontend (BFF)

Cada familia de clientes (Mobile 📱, Web 🖥️, TV 📺) tiene un **BFF dedicado** que agrega llamadas a múltiples microservicios y reduce el chatter del cliente.

## 🕸️ Service Mesh

- **Istio** gestiona el tráfico entre microservicios.
- Proporciona **mTLS automático**, observabilidad de tráfico (distributed tracing), retries y timeouts.

---

<div align="center">

# 🗄️ Capa de Datos

</div>

La Capa de Datos garantiza la persistencia, disponibilidad y procesamiento de la información en sus distintas formas: transaccional, analítica y de machine learning.

## 🗃️ Bases de Datos Transaccionales

| Tipo | Tecnología | Uso Principal |
|------|------------|---------------|
| 🐘 **Relacional (OLTP)** | PostgreSQL (Cloud SQL / RDS) | Usuarios, suscripciones, facturación, metadatos estructurados. |
| 🍃 **Documental** | MongoDB Atlas | Catálogo flexible, descripciones multilingües, configuraciones UI. |
| ⚡ **Clave-Valor** | Redis (Memorystore / ElastiCache) | Sesiones, rate limiting, caché de catálogo, "Mi Lista". |
| 🔗 **Grafo** | Neo4j (Fase 2) | Relaciones contenido-actores-usuarios para recomendaciones avanzadas. |

## 🏊 Data Lake y Analítica

| Componente | Tecnología | Función |
|------------|------------|---------|
| 🌊 **Data Lake** | Amazon S3 / GCS | Repositorio central en Parquet y Avro. |
| 🌪️ **Ingesta en tiempo real** | Kafka → Spark Streaming / Flink | Procesamiento de eventos de usuario. |
| 🏛️ **Data Warehouse** | BigQuery / Snowflake | Reportes de negocio, cohortes, análisis de churn. |
| 🎼 **Orquestación** | Apache Airflow | Pipelines ETL/ELT programados. |

## 🤖 Plataforma de Machine Learning (MLOps)

| Componente | Tecnología | Función |
|------------|------------|---------|
| 🏪 **Feature Store** | Feast | Compartir features entre entrenamiento y serving. |
| 🧠 **Entrenamiento** | Vertex AI / SageMaker + Kubeflow | Pipelines de entrenamiento de modelos. |
| 🚀 **Serving** | TensorFlow Serving | Despliegue de modelos de baja latencia. |
| 👁️ **Monitoreo** | Drift Detection | Detección de degradación de modelos en producción. |

## 🛡️ Estrategia de Respaldo y Recuperación

| Métrica | Objetivo | Descripción |
|---------|----------|-------------|
| ⏱️ **RPO** | 5 minutos | Máxima pérdida de datos aceptable. |
| ⏱️ **RTO** | 15 minutos | Tiempo máximo de recuperación de servicios core. |
| 🔄 **Replicación** | Multi-region activo-pasivo | Failover automático para bases de datos maestras. |

---

<div align="center">

# ☁️ Capa de Infraestructura y Cloud

</div>

La Capa de Infraestructura provee el cómputo, la red y la orquestación necesarios para operar la plataforma con alta disponibilidad.

## 🌩️ Estrategia Multi-Nube e Híbrida

| Nube | Rol | Servicios Principales |
|------|-----|----------------------|
| ☁️ **GCP (Primaria)** | Datos, ML, Kubernetes | GKE, BigQuery, Vertex AI, Cloud Storage. |
| ☁️ **AWS (Secundaria)** | CDN, Almacenamiento, DR | CloudFront, S3, RDS, EKS para disaster recovery. |
| 🎯 **Estrategia** | Cloud-agnostic | Contenedores y Terraform para evitar vendor lock-in. |

## 🚢 Orquestación de Contenedores

| Componente | Tecnología | Descripción |
|------------|------------|-------------|
| ⚓ **Kubernetes** | GKE / EKS | Clústeres regionales con auto-scaling de nodos. |
| 🏷️ **Namespaces** | K8s Native | Aislamiento por entorno (prod, staging, dev) y dominio. |
| 🔄 **GitOps** | ArgoCD | Despliegues declarativos sincronizados desde Git. |

## 📈 Estrategia de Escalabilidad

| Mecanismo | Tecnología | Descripción |
|-----------|------------|-------------|
| 📊 **HPA** | Kubernetes | Escala pods por CPU, memoria y latencia de requests. |
| 📏 **VPA** | Kubernetes | Ajusta recursos de pods en modo recomendación. |
| ⚡ **KEDA** | Event-driven | Autoscaling de consumidores Kafka (escala a cero). |
| 🏗️ **Cluster Autoscaler** | Kubernetes | Añade/remueve nodos según demanda. |

## 🌐 Red y Conectividad

- **VPCs:** Redes privadas por región con peering entre ellas.
- **Service Discovery:** DNS interno + Istio service registry.
- **Network Policies:** Segmentación de tráfico entre namespaces.

---

<div align="center">

# 🔒 Capa de Seguridad

</div>

La seguridad es una preocupación transversal. La arquitectura implementa **defensa en profundidad** en todas las capas.

## 🛡️ Seguridad en el Edge

- 🔐 **TLS 1.3** en todas las conexiones externas.
- 📌 **Certificate Pinning** en aplicaciones móviles.
- 🌊 **DDoS Protection** integrado en CDN.

## 🔑 Seguridad en la Aplicación

| Capacidad | Tecnología | Descripción |
|-----------|------------|-------------|
| 🔓 **Autenticación** | OAuth 2.0 + OpenID Connect | SSO corporativo y social login. |
| 🛂 **Autorización** | RBAC + ABAC | Control de acceso basado en roles y atributos (controles parentales). |
| 🗝️ **Gestión de Secretos** | HashiCorp Vault | Rotación automática de credenciales, API keys y certificados. |

## 🔐 Seguridad en Datos

| Capa | Medida | Descripción |
|------|--------|-------------|
| 🔄 **Cifrado en tránsito** | mTLS (Istio) | Cifrado bidireccional entre microservicios. |
| 💾 **Cifrado en reposo** | AES-256 | Bases de datos y almacenamiento de objetos. |
| 💳 **Tokenización** | PCI-DSS | Datos de tarjetas tokenizados; nunca se almacenan PANs en crudo. |
| 🎬 **DRM** | Widevine, FairPlay, PlayReady | Protección de contenido audiovisual contra piratería. |

## 📋 Cumplimiento y Gobernanza

- **Estándares:** ISO 27001, SOC 2 Type II, GDPR, LGPD (Brasil).
- **Auditoría:** Trail de auditoría inmutable para todos los accesos a datos sensibles.

---

<div align="center">

# 👁️ Capa de Observabilidad

</div>

La observabilidad permite entender el estado del sistema, detectar anomalías y reducir el MTTR.

## 📊 Pilares de la Observabilidad

| Pilar | Herramienta | Descripción |
|-------|-------------|-------------|
| 📈 **Métricas** | Prometheus + Grafana | Métricas de infraestructura y aplicación. Dashboards de SLO/SLI. |
| 📝 **Logs** | ELK Stack / Loki | Logs centralizados con correlación por trace ID. |
| 🔗 **Traces** | Jaeger / Tempo | Distributed tracing a través de todos los microservicios. |
| 🚨 **Alerting** | PagerDuty + Alertmanager | Alertas basadas en umbrales y anomalías. On-call rotation. |

## 🎯 SLOs y SLIs Críticos

| Indicador | Objetivo | Descripción |
|-----------|----------|-------------|
| ✅ **Disponibilidad** | 99.99% uptime | Servicio de streaming mensual. |
| ⏱️ **TTFF** | P95 < 2 segundos | Time to First Frame (inicio de reproducción). |
| ⚡ **Latencia API** | P99 < 200 ms | APIs de catálogo y usuario. |
| ❌ **Tasa de error** | < 0.1% | Errores HTTP 5xx. |

## 🌍 Rastreo de Negocio

- **Real User Monitoring (RUM):** Métricas de experiencia real (CLS, LCP, FID en web; ANR en móvil).
- **Synthetic Monitoring:** Pruebas programadas de flujos críticos desde múltiples geografías.

---

<div align="center">

# 🎬 Fictional Entertainment MX

### *Innovamos tecnología para conectar historias.*

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

**Documento generado con fines académicos**

*Fictional Entertainment MX es una empresa ficticia.*

</div>
