# Ferretería El Martillo - API Backend & Automation Testing

Proyecto backend desarrollado con Django REST Framework para la gestión de productos e inventario de Ferretería El Martillo, incluyendo suite de pruebas unitarias, colección de Postman/Newman y pruebas E2E con Cypress.

## 🚀 Tecnologías Utilizadas

- **Backend:** Python 3.13 / Django 6.1 / Django REST Framework (DRF)
- **Base de Datos:** SQLite / PostgreSQL
- **Autenticación:** Django REST Framework Token Authentication
- **Testing Unitario:** Django TestCase
- **Pruebas de API (CLI):** Postman / Newman CLI
- **Pruebas E2E:** Cypress 16

---

## 🛠️ Instalación y Configuración Local

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Diegosoprano777/FERRETERIA.git
   cd FERRETERIA
   ```

2. **Crear y activar entorno virtual:**
   ```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install django djangorestframework drf-spectacular
   npm install
   ```

4. **Ejecutar migraciones y servidor:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

---

## 🧪 Pruebas Unitarias (Django TestCase)

Para ejecutar la suite de pruebas unitarias de Django:

```bash
python manage.py test modulo_inventario
```

---

## 📮 Pruebas de API con Newman CLI

Ejecución de la colección de Postman con entorno local:

```bash
newman run Ferreteria_API_Testing.postman_collection.json -e Entorno_local.postman_environment.json
```

---

## 🌲 Pruebas de Integración E2E con Cypress

Ejecución headless de la suite E2E de Cypress:

```bash
npx cypress run --spec "cypress/e2e/ferreteria_api_spec.cy.js"
```
