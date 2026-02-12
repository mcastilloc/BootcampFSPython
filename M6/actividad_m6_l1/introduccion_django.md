# Introducción a Django

## 1. ¿Qué es Django?
- **Tipo de framework:** Django es un framework de desarrollo web de alto nivel escrito en Python.  
- **Aplicaciones que permite construir:** Facilita la creación de aplicaciones web completas, seguras y escalables, como sistemas de gestión de contenidos, plataformas de comercio electrónico, APIs, aplicaciones empresariales y sitios dinámicos.  
- **Ventajas sobre Python puro:**
  1. Incluye un ORM (Object-Relational Mapping), que simplifica el manejo de bases de datos.  
  2. Ofrece seguridad integrada (protección contra CSRF, XSS, SQL Injection).  
  3. Proporciona un sistema administrativo automático para gestionar datos sin necesidad de programar desde cero.  

---

## 2. Entornos virtuales en Python
- **Definición:** Un entorno virtual es un espacio aislado que permite instalar librerías y dependencias específicas para un proyecto sin afectar el sistema global.  
- **Ventajas en Django:**
  - Evita conflictos entre versiones de librerías.  
  - Permite reproducir fácilmente el entorno de desarrollo en otros equipos.  
  - Facilita la organización y mantenimiento de proyectos independientes.  
- **Comando `python -m venv env`:**  
  Este comando crea un entorno virtual llamado `env`. Dentro de esa carpeta se almacenan los ejecutables de Python y las librerías instaladas, aislando el proyecto del resto del sistema.  

---

## 3. Estructura y diseño de Django
- **Patrón MVC y aplicación en Django (MTV):**

| Concepto tradicional (MVC) | Nombre en Django (MTV) | Función |
|-----------------------------|------------------------|---------|
| Model                      | Model                  | Define la estructura de los datos y cómo se almacenan en la base de datos. |
| View                       | Template               | Se encarga de la presentación y renderización del contenido en HTML. |
| Controller                 | View                   | Contiene la lógica de negocio, recibe las solicitudes y devuelve respuestas. |

- **Enrutador de Django:**  
El enrutador está definido en el archivo `urls.py`. Su función es mapear las URLs solicitadas por el usuario hacia las vistas correspondientes, permitiendo organizar y dirigir el flujo de la aplicación web.  

---

## 4. Principios del desarrollo con Django
- **Principio DRY ("Don't Repeat Yourself"):**  
Significa evitar duplicación de código y lógica. Django lo aplica mediante reutilización de plantillas, herencia de clases y un ORM que reduce la necesidad de escribir consultas SQL repetitivas.  
- **Estructura flexible y minimalista:**  
Django ofrece una arquitectura modular que permite usar solo los componentes necesarios. Aunque incluye muchas funcionalidades, no obliga a utilizarlas todas, lo que lo hace adaptable a distintos proyectos.  
- **Templates en Django:**  
Los *templates* son archivos que definen la presentación de la aplicación (HTML dinámico). Permiten separar la lógica de negocio de la capa visual y facilitan la renderización de contenido dinámico proveniente de las vistas.  

---