# StockWise API - Gestor de Inventario

## Descripción
API REST para gestionar productos y categorías de un inventario. Permite realizar operaciones CRUD completas y búsqueda por nombre de producto o categoría.

## Tecnologías Usadas
- Python 3.13.3
- Django 5.2.7
- Django REST Framework 3.16.1
- SQLite (base de datos)

## Instrucciones de Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/syderkkk/stockwise_api.git
cd stockwise_api
```

### 2. Crear entorno virtual
```bash
python -m venv venv
venv\Scripts\activate  # Linux/macOS: source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar migraciones
```bash
cd src
python manage.py migrate
```

### 5. Iniciar servidor
```bash
python manage.py runserver
```


El servidor estará disponible en: `http://localhost:8000`´

## Endpoints Disponibles

### **Productos**

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET    |`/api/productos/`| Listar todos los productos|
| POST   |`/api/productos/`| Crear un producto |
| GET    |`/api/productos/{id}/`| Ver detalle de un producto |
| PUT    |`/api/productos/{id}/`| Actualizar un producto completo |
| PATCH  |`/api/productos/{id}/`| Actualizar parcialmente un producto |
| DELETE |`/api/productos/{id}/`| Eliminar un producto |
| GET    |`/api/productos/?search=texto`| Busacr productos por nombre o categoría|

### **Categorías**

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET    |`/api/categorias/`| Listar todos las categorías|
| POST   |`/api/categorias/`| Crear un categoría |
| GET    |`/api/categorias/{id}/`| Ver detalle de una categoría |
| PUT    |`/api/categorias/{id}/`| Actualizar una categoría |
| PATCH  |`/api/categorias/{id}/`| Actualizar parcialmente un categoría |
| DELETE |`/api/categorias/{id}/`| Eliminar un categoría |

## Ejemplo de Uso (curl)

### Crear una categoría
```bash
curl -X POST http://localhost:8000/api/categorias/ \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Electrónica", "descripcion": "Productos electrónicos"}'
```

### Crear un producto
```bash
curl -X POST http://localhost:8000/api/productos/ \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Laptop", "cantidad": 10, "precio": "1500.00", "categoria": 1}'
```

### Listar productos
```bash
curl http://localhost:8000/api/productos/
```

### Buscar productos
```bash
curl http://localhost:8000/api/productos/?search=Laptop
```

### Actualizar producto
```bash
curl -X POST http://localhost:8000/api/productos/1/ \
  -H "Content-Type: application/json" \
  -d '{"cantidad": 15"}'
```

### Eliminar producto
```bash
curl -X DELETE http://localhost:8000/api/productos/1/
```

## Fecha
15 de Octubre del 2025