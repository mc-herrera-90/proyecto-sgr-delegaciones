 ## Configuración del Proyecto

 1. Crear entorno virtual:

```
python -m venv venv
```

 2. Activar entorno virtual:

```
# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

 3. Instalar dependencias:

```
pip install -r requirements.txt
```

 4. Ejecutar migraciones:

```
python manage.py migrate
```

 5. Lanzar servidor:

```
python manage.py runserver
```

 Servidor disponible en `http://127.0.0.1:8000/`.

 ## Comandos útiles

```
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Aplicar migraciones a otra base de datos definida
python manage.py migrate --database=sqlite

# Crear superusuario
python manage.py createsuperuser

# Lanzar servidor
python manage.py runserver
```
