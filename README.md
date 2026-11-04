# ☕ Registra tu vibe

Una app de Python y Streamlit para registrar cómo te sientes y cuánta energía tienes. Cuando guardas un registro, aparece un café gigante con globos durante 2,5 segundos. Después ves una frase motivadora aleatoria y el historial actualizado.

## 1. Crea la carpeta del proyecto

Crea una carpeta llamada `registro-vibe`. En VS Code, abre **Archivo > Abrir carpeta** y selecciónala. Después, abre **Terminal > Nueva terminal**. Los comandos de esta guía son para PowerShell en Windows.

## 2. Crea y activa un entorno virtual

Con Python instalado, ejecuta estos comandos desde la carpeta del proyecto.

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

`venv` crea un entorno aislado para las librerías del proyecto. Cuando se activa, normalmente verás `(.venv)` al principio de la línea de la terminal.

## 3. Crea el archivo requirements.txt

En el explorador de VS Code, haz clic en **Nuevo archivo** y ponle exactamente el nombre `requirements.txt`. Guárdalo en la carpeta principal del proyecto, al mismo nivel que `app.py`. Escribe esta línea y guarda el archivo.

```text
streamlit
```

`requirements.txt` indica qué librerías externas necesita la app. Streamlit es la única dependencia directa. `random`, `time` y `html` vienen con Python.

Para instalar las dependencias que figuran en el archivo, ejecuta este comando con el entorno activado.

```powershell
python -m pip install -r requirements.txt
```

Si ya instalaste Streamlit en un entorno limpio y quieres generar un archivo con las versiones exactas de todos los paquetes instalados, puedes usar `python -m pip freeze > requirements.txt`. Ese comando sobrescribe el archivo e incluye también las dependencias de Streamlit. Para este ejercicio basta con escribir `streamlit` a mano.

## 4. Crea el archivo app.py

En VS Code, crea `app.py` junto a `requirements.txt` y copia el código completo de la app del café. Guarda este documento como `README.md` en la misma carpeta.

```text
registro-vibe/
├── app.py
├── requirements.txt
├── README.md
└── .venv/
```

## 5. Ejecuta la app

En la terminal de VS Code, desde la carpeta del proyecto y con el entorno activado, ejecuta lo siguiente.

```powershell
python -m streamlit run app.py
```

Streamlit suele abrir la app en el navegador. Si no se abre, copia la dirección **Local URL** que aparezca en la terminal. Para detener la app, pulsa **Ctrl + C** en esa terminal.

Si PowerShell bloquea la activación del entorno, puedes instalar y ejecutar con su Python directamente.

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

## 6. Prueba la app

1. Escribe tu nombre.
2. Selecciona tu estado de ánimo y tu nivel de energía del 1 al 10.
3. Pulsa **☕ Registrar mi vibe**.
4. Después del café y los globos, comprueba que aparecen la frase motivadora y el registro en la tabla.

Si pulsas el botón con el nombre vacío, verás un aviso. El historial se guarda en `st.session_state` y se conserva durante la sesión. Al iniciar una sesión nueva, el historial empieza vacío.

## Si ya tienes la carpeta descargada

Ábrela en VS Code y repite los pasos para crear el entorno, instalar las dependencias y arrancar la app. Los archivos `app.py`, `requirements.txt` y `README.md` ya estarán en la carpeta si se incluyeron al compartir el proyecto.
