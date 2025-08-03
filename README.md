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
- [Base de datos](#base-de-datos)
- [Comando de Ejecución del proyecto](#comando-de-ejecución-del-proyecto)
- [Usuarios de autorización para los endpoints](#usuarios-de-autorización-para-los-endpoints)
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
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

- Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Base de datos

En el proyecto se utilizara como ejemplo SQLite para la creación de la base de datos. Es necesario crear un archivo .env cpn las variables de entorno a utilizar a la base de datos. Para ello se ejecuta el siguiente comando para copiar el modelo ejemplo .env.example_sqlite para obtener el .env a utilizar:

```bash
cp .env.example_sqlite .env
```

Al ejecutar el proyecto, se crea automáticamente por defecto la base de datos SQLite por nombre [db_project.sqlite3](data/db_project.sqlite3) dentro de la carpeta [data](data/).

En la siguiente ruta [diagramas db](/diagrams_db/README.md), se observa la estructura de las tablas utilizadas en los modelos del proyecto.

### (Opcional):

Es posible utilizar MySQL o Postgres para la creación de la base de datos, para ello se tiene los modelos ejemplos:

```bash
.env.example_mysql
.env.example_postgres
```

Pero es necesario realizar la correcta configuración de las variables de entorno para ejecutar el proyecto con dichas bases de datos.

## Comando de ejecución del proyecto

Para la ejecución del proyecto es necesario contar con el entorno virtual activo y dentro del proyecto. Ejecutar el siguiente comando:

   ``` bash
   fastapi dev src/app/main.py 
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
│   └── README.md
├── venv/
├── .git/
├── .gitignore
├── .env
├── .env.example_sqlite
├── .env.example_mysql
├── .env.example_postgres
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
