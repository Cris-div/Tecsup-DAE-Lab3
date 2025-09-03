# 📚 Django Quiz App

Aplicación web desarrollada en **Django** para crear, administrar y responder exámenes tipo cuestionario.  
Incluye **categorías**, **estadísticas** y una **API JSON** para consumir datos desde JavaScript u otros clientes.

---

## ✨ Funcionalidades

- 📖 **Gestión completa de exámenes:**
  - Crear, editar y eliminar exámenes.
  - Agregar preguntas con opciones de respuesta.
  - Validación: **una sola respuesta correcta** por pregunta.

- 🏷️ **Categorías:** Organización de exámenes por tema.

- 📝 **Responder exámenes:** Interfaz simple para que usuarios respondan cuestionarios y vean su puntaje.

- 📊 **Estadísticas:**
  - Número de intentos por examen.
  - Promedio de puntaje.
  - Historial de resultados.

- 🌐 **API JSON:**
  - Endpoints para listar exámenes, preguntas y crear contenido.
  - Frontend con `fetch` para cargar datos dinámicamente.

- 🎨 **Frontend responsivo con Bootstrap 5**.

---

## 📂 Estructura del Proyecto

quiz_app/
├── src/
│ ├── config/ # Configuración principal de Django
│ ├── quiz/ # App principal
│ │ ├── migrations/
│ │ ├── static/quiz/ # Archivos estáticos (JS, CSS)
│ │ │ └── app.js
│ │ ├── templates/quiz/ # Templates HTML
│ │ │ ├── base.html
│ │ │ ├── exam_list.html
│ │ │ ├── exam_detail.html
│ │ │ ├── take_exam.html
│ │ │ └── exam_stats.html
│ │ ├── models.py # Modelos: Exam, Question, Choice, Category, ExamAttempt
│ │ ├── views.py # Vistas tradicionales (HTML)
│ │ ├── views_api.py # Endpoints API JSON
│ │ └── urls.py # Rutas de la app
│ ├── manage.py
│ └── requirements.txt
└── README.md