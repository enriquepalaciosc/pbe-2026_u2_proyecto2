# u2_proyecto1 — API REST de Pedidos (CRUD Clientes)

Proyecto académico de la **Unidad 2: CRUD** de la asignatura **Programación Backend 2026 (TI3041)** — **INACAP Calama**.

API REST construida con **Django** y **Django REST Framework (DRF)**. Las pruebas de la API se hacen con **Bruno**.

---

## Objetivos de aprendizaje

- Definir modelos y relaciones en Django (1-N y N-M).
- Convertir modelos a JSON con **serializers** de DRF.
- Crear vistas con `@api_view` para las operaciones **CRUD**.
- Mapear rutas en `urls.py`.
- Probar endpoints con **Bruno** y revisar los códigos de estado HTTP.

---

## Tecnologías

| Herramienta | Uso |
|---|---|
| Python 3.12+ | Lenguaje |
| Django | Framework web |
| Django REST Framework | API REST |
| SQLite | Base de datos (por defecto) |
| Bruno | Cliente para probar la API |

---

## Estructura del proyecto

```
u2_proyecto1/
├── manage.py
├── u2_proyecto1/
│   ├── settings.py
│   └── urls.py          # Rutas de la API
└── pedidos_app/
    ├── models.py        # Categoria, Producto, Cliente, Pedido, Item
    ├── serializers.py   # ClienteSerializer
    └── views.py         # Vistas CRUD de Cliente
```

---

## Modelo de datos

```
Categoria  N ──── M  Producto
Cliente    1 ──── N  Pedido
Pedido     1 ──── N  Item
Producto   1 ──── N  Item
```

| Modelo | Campos |
|---|---|
| **Categoria** | `nombre` (único) |
| **Producto** | `nombre`, `descripcion`, `precio`, `stock`, `activo`, `creado`, `codigo`, `categorias` (N-M) |
| **Cliente** | `nombre`, `email` (único) |
| **Pedido** | `fecha`, `pagado`, `cliente` (FK) |
| **Item** | `cantidad`, `precio_unitario`, `pedido` (FK), `producto` (FK, PROTECT) |

> En esta etapa el CRUD está implementado solo para **Cliente**. Los demás modelos quedan para las siguientes clases.

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/<usuario>/u2_proyecto1.git
cd u2_proyecto1
```

### 2. Crear y activar entorno virtual

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install django djangorestframework
```

### 4. Verificar `settings.py`

```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'pedidos_app',
]
```

### 5. Migrar y ejecutar

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

La API queda en: `http://127.0.0.1:8000`

### (Opcional) Usuario administrador

```bash
python manage.py createsuperuser
```

Panel admin: `http://127.0.0.1:8000/admin/`

---

## Endpoints — Cliente

| Acción | Método | URL | Respuesta OK | Error |
|---|---|---|---|---|
| Crear | `POST` / `PUT` | `/cliente/agregar` | `201 Created` | `400 Bad Request` |
| Listar todos | `GET` | `/clientes` | `200 OK` | `400 Bad Request` |
| Ver uno | `GET` | `/cliente/<id>` | `200 OK` | `404 Not Found` |
| Modificar | `PATCH` | `/cliente/modificar/<id>` | `202 Accepted` | `400 Bad Request` |
| Eliminar | `DELETE` | `/cliente/eliminar/<id>` | `204 No Content` | `404 Not Found` |

> Las rutas **no** llevan `/` al final.

### Ejemplos

**Crear cliente** — `POST /cliente/agregar`
```json
{
  "nombre": "Juan Pérez",
  "email": "juan@correo.cl"
}
```

Respuesta `201`:
```json
{
  "id": 1,
  "nombre": "Juan Pérez",
  "email": "juan@correo.cl"
}
```

**Modificar cliente** — `PATCH /cliente/modificar/1`

> Se deben enviar **todos** los campos (`nombre` y `email`), porque el serializer valida el objeto completo.

```json
{
  "nombre": "Juan Pérez Soto",
  "email": "juan@correo.cl"
}
```

**Email repetido** — Respuesta `400`:
```json
{
  "email": ["cliente with this email already exists."]
}
```

---

## Pruebas con Bruno

1. Descargar Bruno: https://www.usebruno.com
2. Crear una colección: **u2_proyecto1**.
3. Crear un environment **local** con la variable:

   | Variable | Valor |
   |---|---|
   | `baseUrl` | `http://127.0.0.1:8000` |

4. Crear un request por endpoint:

   | Request | Método | URL |
   |---|---|---|
   | Crear cliente | POST | `{{baseUrl}}/cliente/agregar` |
   | Listar clientes | GET | `{{baseUrl}}/clientes` |
   | Ver cliente | GET | `{{baseUrl}}/cliente/1` |
   | Modificar cliente | PATCH | `{{baseUrl}}/cliente/modificar/1` |
   | Eliminar cliente | DELETE | `{{baseUrl}}/cliente/eliminar/1` |

5. En **POST** y **PATCH**: pestaña **Body → JSON** y pegar el JSON de ejemplo.
6. Revisar el **código de estado** de cada respuesta.

### Flujo sugerido para practicar

1. Crear 2 o 3 clientes.
2. Listar todos.
3. Ver uno por `id`.
4. Modificar uno.
5. Eliminar uno.
6. Volver a listar y verificar.
7. Probar errores: email repetido, `id` que no existe.

---

## Conceptos clave

| Concepto | Descripción |
|---|---|
| **Serializer** | Convierte objetos Python ↔ JSON y valida datos. |
| `many=True` | Se usa cuando se serializa una lista (QuerySet). |
| `is_valid()` | Valida los datos recibidos antes de guardar. |
| `request.data` | Datos enviados desde el cliente (Bruno / frontend). |
| `@api_view` | Define qué métodos HTTP acepta la vista. |
| `status.HTTP_...` | Códigos de estado HTTP de DRF. |

---

## Próximos pasos

- [ ] `ProductoSerializer` y `CategoriaSerializer`
- [ ] CRUD de Producto y Categoría
- [ ] CRUD de Pedido e Item
- [ ] Uso de `partial=True` para modificaciones parciales

---

## Asignatura

**Programación Backend 2026 — TI3041**
INACAP Calama
Docente: Enrique Palacios Carrasco
