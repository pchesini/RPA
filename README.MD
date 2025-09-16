# 🤖 RPA con Python

Repositorio de práctica para aprender **Automatización Robótica de Procesos (RPA)** usando **Python**.

---

## 🎯 Objetivo
- Automatizar login en portales web (ejemplo: AFIP).
- Practicar extracción y descarga de datos.
- Procesar información con Python y generar reportes.

---

## 🛠️ Tecnologías
- Python 3.x
- Selenium
- Webdriver Manager
- Python-dotenv

---

## 🚀 Cómo usar
1. Clonar repo:
   ```bash
   git clone https://github.com/pchesini/RPA.git
   cd RPA
2. Crer el entorno virtual 
python -m venv venv
3. Activar entorno
.\venv\Scripts\activate
# si usuas linux 
source venv/bin/activate

4. Instals las dependencias 
pip install -r requirements.txt

5. Crear archivo .env en la raíz del proyecto
AFIP_CUIT=tu_cuit
AFIP_PASS=tu_clave

6. correr los scripts
python entrar_web_afip.py

7. Pra salir del entorno virtual
deactivate



