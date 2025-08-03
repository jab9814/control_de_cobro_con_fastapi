# Proyecto de Control de Cobros

🧾 Este proyecto gestiona transacciones, facturas y planes asociados a clientes. Esta información es necesario almacenarla y para ello se hace uso de una base de datos.

## Indice

- [Proyecto de Control de Cobros](#proyecto-de-control-de-cobros)
- [Esquema de la Base de Datos](#esquema-de-la-base-de-datos)
- [Esquema visual](#esquema-visual)
- [Tablas principales y Enums](#tablas-principales-y-enums)
- [Código sql](#código-sql)


## Esquema de la Base de Datos

📊 Puedes ver el diagrama interactivo aquí:  
👉 [Ver en dbdiagram.io](https://dbdiagram.io/e/688f7d1ecca18e685c040d1f/688f9a8ecca18e685c062b89)


## Esquema visual

🖼️ ![Database Schema](/diagrams_db/control_de_cobro_con_fastapi.png)

## Tablas principales y Enums

- **customers**: Información del cliente
- **plans**: Tipos de planes disponibles
- **transactions**: Registro de pagos/transacciones
- **invoices**: Facturas generadas
- **customer_plans**: Relación muchos-a-muchos entre clientes y planes

- **plan_status_type**: Estado del plan (active / inactive)

## Código sql

Al iniciar el proyecto se crea de forma automática la base de datos, utilizando sqlite en el modulo [db_sqlite.py](/src/db_sqlite.py).

Desde el modulo [tables_models.sql](/diagrams_db/tables_models.sql), se puede observar el código sql para la creación de las tablas de forma independiente
