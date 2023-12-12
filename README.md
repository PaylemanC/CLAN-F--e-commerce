# CLAN-F--e-commerce

**E-commerce de productos innovadores, tanto de línea personal como del hogar, con Inteligencia Artificial integrada.**

<img src="static/images/logo/banner.png">

Este es un proyecto Open Source desarrollado como proyecto del curso [Full Stack Python](https://agenciadeaprendizaje.bue.edu.ar/curso/fullstack-con-python-cac-4-0/) de [Codo a Codo](https://buenosaires.gob.ar/educacion/codocodo/el-programa).

## Developer Team 💻:

- [Alberto Márquez](https://github.com/YeiAlb)
- [Carina Payleman](https://github.com/PaylemanC)
- [Francisco Javier Zani](https://github.com/Franjazani)

## Tecnologías utilizadas 🛠️:

* HTML y CSS
* Javascript
* Python
* DJANGO
* MYSQL

## Instalación 🔧:

### Requisitos previos

* Instalado [Python y pip](https://www.python.org/downloads/).
* Instalado [MySQL](https://dev.mysql.com/downloads/installer/).
* ⚠ Las instrucciones que inician en "python" pueden variar dependiendo del SO (ej. "python3" con SO Linux).
* Recomendamos tener instalado una herramienta visual de MySQL como PhpMyAdmin (con XAMPP) o MySQL Workbench.

### Instalación y configuración del entorno virtual

1. Crea el entorno virtual en el directorio raíz ejecutando el comando en PowerShell:

```bash {"id":"01HHFKBYW0P2TF03SAKCNQ7FF5"}
python -m venv env

```

*⚠ Nota importante: nótese que el nombre del **entorno virtual debe llamarse sí o sí venv o env**

2. Activa el entorno virtual moviéndote con 'cd' a tu carpeta de entorno y ejecuta el comando:

```bash {"id":"01HHFKBYW0P2TF03SAKE1C0ND6"}
Scripts/activate

```

***Recuerda que debes activar el entorno virtual cada vez que trabajes en el proyecto.**

3. Con el entorno virtual ya activo, dirígete a la carpeta raíz donde se encuentra el archivo **requirements.txt** y ejecuta el comando para instalar todas las dependencias del proyecto:

```bash {"id":"01HHFKBYW0P2TF03SAKHEEA26A"}
pip install -r requirements.txt

```

El proceso puede demorar. Una vez finalizado, tendrás todas las dependencias necesarias para trabajar con el proyecto instaladas.

***EXTRA**: Si en algún momento necesitas desactivar el entorno virtual, puedes hacerlo con el comando:

```bash {"id":"01HHFKBYW0P2TF03SAKHJV53NA"}
deactivate

```

### Base de datos (local)

**Este proyecto fue trabajado sobre MySQL y por eso las instrucciones procederán con este. Si desean utilizar otro motor de base de datos, pueden buscar su configuración en la [documentación oficial](https://docs.djangoproject.com/en/4.2/ref/databases/).*

1. Crea un archivo **local.py** (es importante que sea este y no otro nombre) en la carpeta **settings** a la misma altura que el archivo **"settings.py"**.
2. Copia la siguiente estructura en **local.py**:

```python {"id":"01HHFKBYW0P2TF03SAKKYC23H5"}
from .settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '', # NOMBRE BD
        'USER': 'root', # U OTRO
        'PASSWORD': '', # CONTRASEÑA DE USER
        'HOST': 'localhost',
        'PORT': '3306', # POR DEFECTO, SI TIENEN OTRO CAMBIAR
        'OPTIONS': {
            'sql_mode': 'traditional'
        }
    }
}

```

*Recuerda crear la Base de Datos ('NAME') previamente con MySQL utilizando herramientas como la terminal, PhpMyAdmin o Workbench (SOLO la base de datos, para conectarla):

```sql 
CREATE DATABASE IF NOT EXISTS nombre_bd;

```

## Uso del server y migraciones

Pueden verificar que toda la instalación fue exitosa levantando el servidor a la altura raíz del proyecto con el comando:

```bash {"id":"01HHFKBYW0P2TF03SAKQ2EH5C5"}
python manage.py runserver

```

Aplicar también las migraciones de la base de datos para traer todas las tablas:

```bash {"id":"01HHFKBYW0P2TF03SAKQFAB1EZ"}
python manage.py migrate

```

Si también lo desean, pueden ejecutar:

```bash {"id":"01HHFKBYW0P2TF03SAKQP497G0"}
python manage.py loaddata productos.json

```

...para cargar datos preestablecidos de algunos productos de muestra. Automáticamente figurarán en las url /productos y /administrador.

## Superusuario

Deberán crear un superusuario para acceder al panel administrador, CRUD de productos y otros controles de la base de datos:

```bash {"id":"01HHFKBYW0P2TF03SAKVH3CHKT"}
python manage.py createsuperuser

```

Con este mismo usuario podrán acceder desde la url /login a funcionalidades de CRUD.