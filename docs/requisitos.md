# Análisis de requisitos
## Sistema de Control de Rescate y Adopción Animal

### 1. Introducción
El sistema tiene como finalidad organizar la información de los animales rescatados, los rescatistas y las personas interesadas en adoptar. Permitirá registrar animales, consultar su estado y gestionar solicitudes de adopción.

### 2. Objetivo general
Diseñar un sistema de software que facilite el seguimiento de los animales rescatados y la administración del proceso de adopción mediante una estructura organizada y patrones de diseño.

### 3. Actores del sistema
- **Administrador:** administra los registros y supervisa la información.
- **Rescatista o voluntario:** registra animales rescatados y actualiza su información.
- **Encargado de adopciones:** revisa y gestiona las solicitudes.
- **Adoptante:** consulta animales disponibles y presenta solicitudes de adopción.

### 4. Requisitos funcionales
- RF01: Registrar animales rescatados.
- RF02: Consultar la información de los animales.
- RF03: Actualizar el estado de un animal: rescatado, en recuperación, disponible o adoptado.
- RF04: Registrar los datos de los posibles adoptantes.
- RF05: Crear solicitudes de adopción.
- RF06: Aprobar o rechazar solicitudes.
- RF07: Notificar los cambios importantes en el proceso de adopción.
- RF08: Consultar el historial de adopciones.

### 5. Requisitos no funcionales
- RNF01: La información debe mantenerse organizada y consistente.
- RNF02: El sistema debe ser fácil de utilizar.
- RNF03: El acceso a las funciones administrativas debe controlarse.
- RNF04: El código debe ser modular y facilitar el mantenimiento.
- RNF05: Las operaciones importantes deben generar mensajes claros de confirmación o error.

### 6. Alcance
El proyecto implementará una demostración académica de las funciones principales. No incluye todavía una base de datos real, autenticación completa ni despliegue en producción.

### 7. Patrones de diseño
- **Factory Method (creacional):** permite crear objetos de notificación sin acoplar el código cliente a una clase concreta.
- **Repository (estructural, según la clasificación usada en esta actividad):** centraliza el acceso a los registros de animales. En la clasificación clásica de GoF, Repository no es uno de los 23 patrones originales.
- **Observer (de comportamiento):** comunica cambios de estado a los componentes que están suscritos a las notificaciones.

### 8. Conclusión
El análisis define los usuarios, las funciones y las restricciones principales del sistema. Los patrones de diseño ayudarán a separar responsabilidades, facilitar el mantenimiento y permitir futuras ampliaciones.