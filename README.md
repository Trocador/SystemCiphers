Markdown
# 🔒 Sistema de Cifrados Criptográficos

Un sistema interactivo de cifrado y descifrado desarrollado en **Python** con una interfaz gráfica moderna utilizando **Tkinter** y **ttkbootstrap**. Este software está diseñado con fines educativos y prácticos, permitiendo visualizar la lógica y los procesos detrás de diversos métodos criptográficos clásicos y contemporáneos.

---

## 🌟 Características Principales

* **Interfaz Moderna e Intuitiva:** Tarjetas interactivas con sombras, desplazamiento fluido (`ScrolledFrame`) y diseño adaptativo (*Flatly theme*).
* **Guías y Esquemas Didácticos:** Muestra la alineación de texto, matrices, trazos e iteraciones paso a paso en algoritmos complejos.
* **Soporte Multi-algoritmo:** Permite cifrar y descifrar textos mediante múltiples técnicas.

---

## 🔐 Algoritmos Implementados

1. **César Normal:** Desplazamiento clásico alfabético fijo.
2. **César por Posición:** Desplazamiento ejecutable con valor $n$ personalizable.
3. **Cifrado por Adición:** Desplazamiento numérico basado en aritmética modular.
4. **Método Fracmasón (Pigpen):** Cifrado gráfico por sustitución de símbolos con mapa visual integrado.
5. **Cifrado Polybius:** Sustitución por coordenadas mediante una matriz $5 \times 5$.
6. **Cifrado Rail Fence:** Transposición en zigzag a través de un número configurable de raíles.
7. **Cifrado por Transposición:** 
   * Por Grupos (clave numérica)
   * Serial
   * Por Columnas / Vertical (palabra clave)
8. **Cifrado Vigenère:** Cifrado polialfabético interactivo con alineación de texto y tabla de cruces.

---

## 🚀 Uso del Ejecutable (`.exe`)

No necesitas instalar Python para ejecutar la aplicación compilada en Windows.

### 📍 Ubicación del Ejecutable
El ejecutable compilado listo para usar se encuentra en la siguiente ruta dentro del proyecto:

```text
SistemaCifrados/
└── dist/
    └── main.exe   <-- ¡Ejecuta este archivo!
Nota: Simplemente haz doble clic sobre dist/main.exe para iniciar la aplicación.

🛠️ Requisitos e Instalación (Entorno de Desarrollo)
Si deseas ejecutar o modificar el código fuente, asegúrate de cumplir con los siguientes requisitos:

Prerrequisitos
Python 3.10+ instalado en el sistema.

Pasos para ejecutar desde la consola:
Clonar o descargar el repositorio:

Bash
git clone [https://github.com/tu-usuario/SistemaCifrados.git](https://github.com/tu-usuario/SistemaCifrados.git)
cd SistemaCifrados
Crear y activar un entorno virtual:

Bash
# En Windows
python -m venv venv
.\venv\Scripts\activate
Instalar dependencias:

Bash
pip install ttkbootstrap pyinstaller
Ejecutar la aplicación:

Bash
python main.py
📦 Compilación y Generación del Ejecutable (.exe)
Si realizaste cambios en el código fuente y deseas volver a empaquetar el ejecutable en un archivo único (.exe) dentro de dist/:

Borra las carpetas build/, dist/ y el archivo main.spec previos (si existen).

Ejecuta el comando de PyInstaller asegurándote de incluir los assets del proyecto y de ttkbootstrap:

DOS
pyinstaller --noconsole --onefile --add-data "assets;assets" --add-data "venv\Lib\site-packages\ttkbootstrap;ttkbootstrap" main.py
El nuevo ejecutable reemplazará al anterior dentro de la carpeta dist/.

📁 Estructura del Proyecto
Plaintext
SistemaCifrados/
│
├── assets/                  # Recursos gráficos (mapas visuales, imágenes, etc.)
│   └── fracmason_mapa.png
│
├── ciphers/                 # Módulos con la lógica criptográfica pura
│   ├── cesar.py
│   ├── adicion.py
│   ├── fracmason.py
│   ├── polybius.py
│   ├── railfence.py
│   ├── transposicion.py
│   └── vigenere.py
│
├── ui/                      # Componentes de la Interfaz Gráfica (Tkinter / ttkbootstrap)
│   ├── main_window.py       # Ventana principal y menú de tarjetas
│   ├── cipher_views.py      # Vistas individuales para cifrado/descifrado
│   └── custom_widgets.py    # Tarjetas personalizadas con sombra
│
├── dist/                    # 🚀 CONTIENE EL EJECUTABLE (.EXE) FINAL
│   └── main.exe
│
├── config.py                # Configuraciones globales y constantes del sistema
├── main.py                  # Punto de entrada de la aplicación
└── README.md                # Documentación del proyecto
🛡️ Licencia
Este proyecto se distribuye bajo la licencia MIT. Siéntete libre de usarlo, modificarlo y compartirlo con fines académicos o personales.
