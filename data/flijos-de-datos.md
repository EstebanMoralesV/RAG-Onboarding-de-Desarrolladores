<div align="center">

# 🔄 Flujos de Datos Críticos — Fictional Entertainment MX

### *Tecnología que conecta historias.*

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

**Documento de Flujos de datos de Referencia**

*Plataforma de Streaming • Microservicios • Cloud Native • Seguridad*

</div>

---

<div align="center">

# 🔄 Flujos de Datos Críticos

</div>

Esta sección describe los flujos de datos más importantes de la plataforma, diseñados para ser narrativas completas y autocontenidas.

## 🔐 Flujo de Autenticación y Autorización

1. 📱 El cliente solicita login al **API Gateway**.
2. 🚪 El API Gateway enruta al **Auth Service**.
3. 🔑 El Auth Service valida credenciales contra **PostgreSQL** y emite un **JWT firmado**.
4. 💾 El JWT se devuelve al cliente y se cachea en **Redis** para validaciones rápidas.
5. 🔄 Solicitudes subsecuentes incluyen el JWT; el API Gateway lo valida sin consultar al Auth Service.
6. 👨‍👩‍👧 Para acceso a contenido restringido, el **Playback Service** consulta el **Profile Service** para verificar controles parentales.

## ▶️ Flujo de Reproducción de Video

1. 🎬 El usuario selecciona un título; el client llama al **BFF**.
2. 🧩 El BFF consulta el **Playback Service** para obtener la URL del manifiesto (HLS/DASH).
3. ✅ El Playback Service verifica la suscripción activa y genera una **URL firmada** (pre-signed) con tiempo de expiración.
4. 🌐 El client solicita el manifiesto al **CDN**; si no está en caché, el CDN lo recupera del **Origin** (almacenamiento de objetos).
5. 📦 El client descarga segmentos de video desde el **edge más cercano** al usuario.
6. 📊 Eventos de reproducción (start, pause, buffer, stop) se emiten al **Event Ingestion Service** vía **Kafka**.

## 🤖 Flujo de Recomendación Personalizada

1. 📡 El **Recommendation Service** consume eventos de reproducción y búsqueda desde **Kafka**.
2. 🏪 El **Feature Store** actualiza vectores de usuario y contenido en tiempo cercano a real.
3. 🏠 Cuando el usuario carga la pantalla de inicio, el **BFF** solicita filas personalizadas al Recommendation Service.
4. 🧠 El modelo de ML (collaborative filtering + content-based) genera un **ranking de títulos**.
5. 💾 El resultado se cachea en **Redis** por 5 minutos para reducir carga de inferencia.
6. 🎨 El client renderiza las **filas personalizadas** en la interfaz.

---

<div align="center">

# 🎬 Fictional Entertainment MX

### *Innovamos tecnología para conectar historias.*

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

**Documento generado con fines académicos**

*Fictional Entertainment MX es una empresa ficticia.*

</div>
