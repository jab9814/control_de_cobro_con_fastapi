# Control de cobro con FastApi

El control de cobro se utiliza en variedades de entornos empresariales y comerciales para gestionar de manera eficiente las cuentas por cobrar y optimizar el flujo en las cajas.

El siguiente proyecto es un sistema de control de cobro y compras para usuarios logrando realizar los siguientes registros:

- Usuarios
- Transacciones
- Facturas
- Planes

Toda la información será almacenada en una base de datos SQLite, pero es posible utilizar otras bases de datos para este proyecto.

## Indice

- [Control de cobro con FastApi](#control-de-cobro-con-fastapi)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación del proyecto y sus requerimientos](#instalación-del-proyecto-y-sus-requerimientos)
- [Comando de Ejecución del proyecto](#comando-de-ejecución-del-proyecto)
- [Usuarios de autorización para los endpoints](#usuarios-de-autorización-para-los-endpoints)
- [Base de datos](#base-de-datos-sqlite)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Como utilizar el proyecto?](#como-utilizar-el-proyecto)

## Tecnologías Utilizadas

- **Python**: Lenguaje principal del proyecto.
- **FastAPI**: Framework para construir APIs rápidas y modernas.
- **Pydantic**: Validación de datos y creación de modelos.
- **SQLite**: Base de datos ligera integrada en el proyecto.

## Instalación del proyecto y sus requerimientos

- Clonar repositorio y ubicarnos dentro del proyecto:

```bash
git clone https://github.com/jab9814/control_de_cobro_con_fastapi.git
cd control_de_cobro_con_fastapi
```

- Crear un entorno virtual (recomendado):

```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

- Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Comando de ejecución del proyecto

Para la ejecución del proyecto es necesario contar con el entorno virtual activo, ubicarnos dentro de la carpeta [src](/src/) y ejecutar el comando el siguiente comando:

   ``` bash
   cd src
   fastapi dev app/main.py 
   ```

Obteniendo una url base para iniciar:

- <http://127.0.0.1:8000>

Para acceder a la documentación interactiva de la API (Swagger UI):

- <http://127.0.0.1:8000/docs>

## Usuarios de autorización para los endpoints

El root del app en general, cuenta con una autorización por defecto:

- **username** = username
- **password** = password

Pero esto es adaptable para los demás endpoints, como también el cambio de usuarios

## Base de datos SQLite

Al iniciar el sistema, dentro de la carpeta [data](data/), se crea automáticamente la base de datos SQLite por nombre [db_project.sqlite3](data/db_project.sqlite3).

En la siguiente ruta [diagramas db](/diagrams_db/README_DB.md), se observa la estructura de las tablas utilizadas en los modelos del proyecto.

## Estructura del Proyecto

``` bash
control_de_cobro_con_fastapi
├──src
│  ├── app
│  │   ├── __init__.py
│  │   ├── main.py
│  │   ├── models
│  │   │   ├── __init__.py
│  │   │   ├── customer_model.py
│  │   │   ├── enums_model.py
│  │   │   ├── invoice_model.py
│  │   │   ├── plans_model.py
│  │   │   └── transaction_model.py
│  │   └── routers
│  │       ├── __init__.py
│  │       ├── customers.py
│  │       ├── invoices.py
│  │       ├── plans.py
│  │       └── transactions.py
├── data
│   ├── __init__.py
│   └── db_project.sqlite3
├── diagrams_db
│   ├── __init__.py
│   ├── control de cobro con fastapi.pgn
│   ├── tables_models.sql
│   └── README_DB.md
├── env/
├── .git/
├── .gitignore
├── README.md
└── requirements.txt

```

## Como utilizar el proyecto?

## Etapas

- [Registrar usuarios](#registrar-usuarios)
- [Transacción realizada por el usuario](#transacción-realizada-por-el-usuario)
- [Creación de factura](#creación-de-factura)
- [Creación de planes para los usuarios](#creación-de-planes-para-los-usuarios)

## Registrar usuarios

## Transacción realizada por el usuario

## Creación de factura

## Creación de planes para los usuarios

## Autor

Proyecto desarrollado por [jab9814](https://github.com/jab9814).
