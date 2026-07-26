<div align="center">

# 📋 Decisiones Arquitectónicas Clave (ADRs) — Fictional Entertainment MX

### *Tecnología que conecta historias.*

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

**Documento de Decisiones Arquitectónicas Clave de Referencia**

*Plataforma de Streaming • Microservicios • Cloud Native • Seguridad*

</div>

---

<div align="center">

# 📋 Decisiones Arquitectónicas Clave (ADRs)

</div>

## 🏛️ ADR-001: Microservicios sobre Monolito

**Contexto:** Necesidad de escalar equipos y componentes de forma independiente.  
**Decisión:** Adoptar arquitectura de microservicios con dominios acotados.  
**Consecuencias:** Mayor complejidad operativa, compensada por independencia de despliegue y escalabilidad selectiva.

## 📡 ADR-002: Kafka como Event Bus Central

**Contexto:** Necesidad de comunicación asíncrona confiable y replay de eventos.  
**Decisión:** Apache Kafka como backbone de eventos.  
**Consecuencias:** Tolerancia a fallos, desacoplamiento temporal, capacidad de reconstruir estados desde el log de eventos.

## 🌐 ADR-003: Multi-CDN para Streaming

**Contexto:** Dependencia de un único proveedor de CDN genera riesgo de outage y costos fijos.  
**Decisión:** Enrutamiento inteligente multi-CDN basado en rendimiento y precio.  
**Consecuencias:** Mayor resiliencia y optimización de costos de ancho de banda.

## 🗄️ ADR-004: PostgreSQL + Redis como Stack Primario

**Contexto:** Necesidad de consistencia transaccional y alta velocidad de lectura.  
**Decisión:** PostgreSQL para persistencia, Redis para caché y sesiones.  
**Consecuencias:** Simplicidad operativa, madurez de herramientas, facilidad de contratación de talento.

---

<div align="center">

# 🎬 Fictional Entertainment MX

### *Innovamos tecnología para conectar historias.*

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

**Documento generado con fines académicos**

*Fictional Entertainment MX es una empresa ficticia.*

</div>
