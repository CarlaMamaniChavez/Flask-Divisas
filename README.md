# Flask-Divisas
Proyecto de conversion de divas
```text
📂 ProyectoFlaskDomingo
│
├── hola.py              # Archivo principal Flask
├── templates/
│   └── index.html       # Interfaz web principal
├── static/
│   └── style.css        # (Opcional) Estilos para la interfaz
├── .env                 # Variables de entorno (API KEY)
└── requirements.txt     # Dependencias del proyecto
```

# ⚙️ Instalación y configuración
## 1. Clonar el repositorio

git clone https://github.com/tu_usuario/conversor-divisas-flask.git
cd conversor-divisas-flask

## 2. Crear y activar entorno virtual
python -m venv labenv
source labenv/Scripts/activate     # En Windows
source labenv/bin/activate         # En Linux/Mac
## 3. Instalar dependencias
pip install -r requirements.txt

## 4. Crear archivo .env
   KEY=tu_api_key_de_exchangerate_api
   
## 5. Ejecuta el servidor Flask
   python hola.py

## 6. Ejecuta el servidor Flask:
   Abre tu navegador en:
👉 http://127.0.0.1:5000 
