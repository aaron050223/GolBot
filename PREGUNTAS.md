### **1. Ciclo de vida del dato (5b):**  
📌 **¿Cómo maneja los datos el bot?**  
El bot saca la información de los partidos desde la API de `Football-Data` y se la manda a los usuarios por Telegram. No guarda nada por su cuenta, solo actúa como un mensajero.  

📌 **¿Cómo se asegura que los datos sean correctos?**  
Depende totalmente de la API de donde saca los datos.

📌 **¿Cómo se podría mejorar la gestión de datos?**  
Podría guardarse un historial de partidos en una base de datos (tipo SQLite o PostgreSQL) para que el bot pueda responder cosas como "¿Cómo quedó el último clásico?" o "Dime los últimos 5 partidos del Madrid".  

---

### **2. Almacenamiento en la nube (5f):**  
☁️ **¿El bot usa la nube?**  
Por ahora no, solo consulta la API y responde en Telegram, sin guardar nada en servidores propios.  

☁️ **¿Qué opciones hay para almacenar datos?**  
Si se quisiera guardar info, se podría usar algo como Firebase, AWS o MongoDB en la nube. También se podría guardar en un servidor propio, pero la nube tiene la ventaja de que todo está accesible desde cualquier lado.  

☁️ **¿Cómo se podría integrar la nube en futuras versiones?**  
Podría guardarse estadísticas, preferencias de usuarios (por ejemplo, qué ligas les interesan) o incluso un sistema de notificaciones personalizadas para que cada usuario reciba solo lo que le importa.  

---

### **3. Seguridad y regulación (5i):**  
🔒 **¿Qué tan seguro es el bot?**  
Es segura siempre que el código no se comparta, ya que depende de los token de la API y de Telegram.  

🔒 **¿Normativas que podrían afectar?**  
Si maneja datos de usuarios (aunque sea solo sus IDs de Telegram), debería cumplir con el GDPR en la UE, lo que significa que habría que dejarles claro qué datos se guardan y cómo pueden eliminarlos si quieren.  

🔒 **¿Cómo hacerlo más seguro?**  
- Guardar la clave API en variables de entorno en vez de dejarla a la vista en el código.  
- Limitar el número de peticiones por usuario para evitar abusos.  
- Usar cifrado si algún día se almacenan datos sensibles.  

---

### **4. Impacto en negocios o industrias (2e):**  
💼 **¿Para qué podría servir esto en una empresa o en una fábrica?**  
Para el que este metido en el mundo del fútbol está muy bien, como pueden ser:  
- Casas de apuestas podrían usarlo para obtener datos rápidos.  
- Medios deportivos podrían recibir alertas de goles en tiempo real.  
- Equipos de fútbol podrían usarlo para seguir partidos de sus rivales.  

💼 **¿Cómo mejora procesos?**  
Automatiza la búsqueda de resultados y evita que la gente tenga que entrar a varias webs para ver los marcadores.  

💼 **¿Quién más podría beneficiarse?**  
- Periodistas deportivos.  
- Fanáticos que quieran recibir alertas en vivo sin depender de apps oficiales.  
- Plataformas de fantasy fútbol (juego de movil) para dar datos a los jugadores.  

---

### **5. Mejoras en IT y OT (2f):**  
💡 **¿Ayuda a la conexión entre IT y OT?**  
No directamente, porque no es un software industrial. Pero si se amplía con análisis de datos en la nube, podría servir para estudios de rendimiento de jugadores, algo útil en equipos profesionales.  

💡 **¿Qué procesos se pueden mejorar?**  
- Automatización de alertas de goles y resultados.  
- Análisis de estadísticas en tiempo real.  
- Creación de informes sin intervención humana.  

💡 **¿Cómo adaptarlo para mejorar procesos tecnológicos?**  
Se podría integrar con otras plataformas, como Google Sheets, para generar reportes automáticos de los partidos y estadísticas de jugadores.  

---

### **6. Tecnologías Habilitadoras Digitales (THD) (2g):**  
🚀 **¿Qué tecnologías digitales usa?**  
- API Football-Data.org para obtener datos de partidos([Football-Data.org](https://www.football-data.org/)).  
- Telegram Bot API para interactuar con usuarios en tiempo real.  

🚀 **¿Cómo mejoran el bot?**  
- La API REST permite que el bot tenga siempre datos actualizados sin hacer cálculos propios.  
- La integración con Telegram hace que la información llegue directamente al usuario, sin que tenga que entrar a una web.  

🚀 **¿Qué más se podría agregar?**  
- **Inteligencia Artificial** para hacer predicciones de partidos.  
- **Blockchain** para asegurar que los datos sean 100% confiables y no manipulados.  
- **Big Data** para analizar tendencias y patrones en el rendimiento de equipos.  
