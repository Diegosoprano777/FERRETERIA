# Supermercado API Backend & Automation Testing - Diego Alejandro Sanchez Lopez

Proyecto backend desarrollado con Django REST Framework para la gestión de productos perecederos (`ProductoPerecedero`) en el rubro de Supermercado. Incluye suite de pruebas unitarias, colección de Postman/Newman con validación de JSON Schema y pruebas E2E en modo headless con Cypress.

## 📋 Información del Proyecto
- **Estudiante:** Diego Alejandro Sanchez Lopez
- **Dominio / Rubro:** Supermercado
- **Entidad Principal:** `ProductoPerecedero`
- **Atributos:** `id`, `nombre`, `sku`, `precio_regular`, `dias_vencimiento`, `precio_oferta`
- **Reglas de Negocio:**
  - Validar que `dias_vencimiento` no sea negativo (`< 0`).
  - Calcular automáticamente un **20% de descuento** sobre `precio_regular` si `dias_vencimiento < 5` para determinar `precio_oferta`.

---

## 🚀 Tecnologías Utilizadas

- **Backend:** Python / Django / Django REST Framework (DRF)
- **Base de Datos:** SQLite / PostgreSQL
- **Autenticación:** DRF Token Authentication (`CustomObtainAuthToken`)
- **Testing Unitario:** Django TestCase / APITestCase
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

Ejecutar la suite de pruebas unitarias de Django (modelos y endpoints):

```bash
python manage.py test modulo_inventario
```

---

## 📮 Pruebas de API con Newman CLI

Ejecución de la colección de Postman con entorno local y validaciones (Status code, tiempo de respuesta < 2000 ms y JSON Schema):

```bash
npx newman run Supermercado_API_Testing.postman_collection.json -e Entorno_local.postman_environment.json
```

---

## 🌲 Pruebas de Integración E2E con Cypress

Ejecución headless de la suite E2E de Cypress (POST -> GET -> DELETE):

```bash
npx cypress run --spec "cypress/e2e/supermercado_api_spec.cy.js"
```
