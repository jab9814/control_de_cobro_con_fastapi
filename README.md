# 📦 control_de_cobro_con_fastapi

Sistema de control de cobro y compras para usuarios.  
Permite registrar usuarios, sus transacciones y facturas mediante una API desarrollada con FastAPI.

---

## 🚀 Tecnologías Utilizadas

- **Python**: Lenguaje principal del proyecto.
- **FastAPI**: Framework para construir APIs rápidas y modernas.
- **Pydantic**: Validación de datos y creación de modelos.
- **SQLite**: Base de datos ligera integrada en el proyecto.

---

## 🛠️ Instalación

1. Cloná este repositorio:
   ```bash
   git clone https://github.com/jab9814/control_de_cobro_con_fastapi.git
   cd control_de_cobro_con_fastapi/src

2. Creá un entorno virtual (opcional pero recomendado):
   ```bash
    python -m venv env
    source env/bin/activate  # En Windows: env\Scripts\activate

3. Instalá las dependencias:
   ```bash
    pip install -r requirements.txt

## ▶️ Uso
Navegá a la carpeta src y ejecuta:
   ```bash
   cd src
   fastapi dev app/main.py 

Al iniciar el sistema, se crea una carpeta data/ en la raíz del proyecto (src/) donde se almacena la base de datos SQLite (.sqlite3).
Accedé a la documentación interactiva de la API en:
http://127.0.0.1:8000/docs

🗂️ Estructura del Proyecto

src
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── customer_model.py
│   │   ├── invoice_model.py
│   │   └── transaction_model.py
│   └── routers
│       ├── __init__.py
│       ├── customers.py
│       ├── invoices.py
│       └── transactions.py
├── db_sqlite.py
├── requirements.txt
├── .git/
├── .gitignore
├── README.md
└── env/

Autor
Proyecto desarrollado por [jab9814].
