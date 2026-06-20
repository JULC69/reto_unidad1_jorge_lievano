==========================================================
## 1. Guía de Instalación de Anaconda en Windows (64 bits)
==========================================================

1. Descargar el Instalador
• Navega al sitio web oficial de Anaconda: anaconda.com/download.
• Regístrate o, si lo prefieres, busca la opción para saltarte el registro (por ejemplo, "Skip Registration") para ir directamente a la descarga.
• Busca la sección de Anaconda Distribution y selecciona el instalador Windows 64-Bit Graphical Installer. El archivo descargado tendrá un nombre similar a Anaconda3-2025.12-2-Windows-x86_64.exe.

2. Verificar la Integridad del Instalador (Opcional pero Recomendado)
Para asegurarte de que el archivo descargado no esté dañado o haya sido alterado, puedes verificar su hash SHA-256:
• Abre una ventana de Símbolo del sistema o PowerShell.
• Navega a la carpeta donde descargaste el instalador (por ejemplo, cd Downloads).
• Ejecuta el siguiente comando para obtener el hash del archivo:
  cmd> certutil -hashfile <NOMBRE_DEL_ARCHIVO> SHA256
(Reemplaza <NOMBRE_DEL_ARCHIVO> con el nombre de tu instalador, por ejemplo, Anaconda3-2025.12-2-Windows-x86_64.exe).
• Compara el hash generado con el hash oficial que encontrarás en el sitio de archivos de Anaconda: repo.anaconda.com/archive . Si coinciden, el archivo es seguro.

3. Ejecutar el Instalador
Ve a tu carpeta de Descargas y haz doble clic en el archivo ejecutable que descargaste para iniciar el instalador.
Nota: No ejecutes el instalador desde la carpeta "Favoritos" para evitar errores de permisos.

4. Paso a Paso del Asistente de Instalación
4.1 Bienvenida: Haz clic en Next > para comenzar.
4.2 Acuerdo de Licencia: Lee el acuerdo de licencia y haz clic en I Agree (Acepto) para continuar.
4.3 Seleccionar Tipo de Instalación: Elige la opción Just Me (Solo para mí) a menos que tengas una razón específica para instalar para todos los usuarios del equipo. Es la opción recomendada para evitar problemas de permisos. Haz clic en Next >.
4.4 Elegir Ubicación de Instalación: Selecciona la carpeta de destino. La ruta por defecto (ej. C:\Users\TuUsuario\anaconda3) es la recomendada . Es importante que la ruta no contenga espacios ni caracteres especiales para evitar problemas de compatibilidad con algunas herramientas . Haz clic en Next.
4.5 Opciones de Instalación Avanzadas: Aquí verás opciones de configuración. Se recomienda marcar la casilla "Register Anaconda3 as my default Python" (Registrar Anaconda3 como mi Python por defecto). Luego, haz clic en Install.
4.6 Instalando: El proceso de instalación comenzará y puede tardar varios minutos . Puedes hacer clic en Show details para ver el progreso de los paquetes que se están instalando.
4.7 Completando la Instalación: Una vez finalizada, aparecerá la pantalla de finalización. Haz clic en Next >.
4.8 Puede aparecer una pantalla promocional de Anaconda Cloud. Puedes hacer clic en Next > para omitirla.
4.9 Finalmente, haz clic en Finish para cerrar el instalador. Puedes dejar marcadas las opciones para abrir tutoriales si lo deseas.

5. Verificar la Instalación
Para confirmar que la instalación fue exitosa, puedes hacer lo siguiente:
• Usando Anaconda Navigator: Busca "Anaconda Navigator" en el menú de inicio de Windows y ábrelo. Si se abre correctamente, la instalación funcionó.
• Usando el Símbolo del sistema (Anaconda Prompt):
  1. Busca y abre el Anaconda Prompt (o el Símbolo del sistema de Windows).
  2. Escribe el comando conda --version y presiona Enter. Deberías ver el número de versión de conda instalado.
  3. Escribe el comando python --version y presiona Enter. Deberías ver la versión de Python que viene con Anaconda.

----------------------------------------------------
Posibles Problemas y Soluciones - Installer Anaconda
----------------------------------------------------
• Problemas de permisos: Si encuentras errores, asegúrate de instalar para "Just Me" y no ejecutes el instalador como Administrador a menos que sea estrictamente necesario.
• Interferencia del antivirus: Si el instalador falla, prueba a desactivar temporalmente tu software antivirus durante la instalación y reactívalo al finalizar.
• Archivo dañado: Si la instalación falla o da errores, descarga de nuevo el instalador y verifica su integridad siguiendo los pasos del Paso 2 de esta guía.

==========================================================
## 2. GUIA CREACION DE AMBIENTE O ÁREA VIRTUAL CON ANACONDA
==========================================================

1. En Windows buscar ANACONDA PROMPT.
2. Clic en Abrir. (base) C:\Usuarios\[NOMBRE_USUARIO]
   ó
   Clic en Ejecutar como Administrador. (base) C:\Windows\System32
3. Verificar versión de conda:
   C:\Usuarios\Jorge\conda --version
4. Verificar versión de python:
   C:\Usuarios\Jorge\python --version
5. Crear un ENTORNO VIRTUAL
   C:\Usuarios\Jorge\conda create -n MasterIA python=3.11
6.1 Activar ENTORNO VIRTUAL
   C:\Usuarios\Jorge\conda activate MasterIA
6.2 Desctivar ENTORNO VIRTUAL
   C:\Usuarios\Jorge\conda desctivate
7. Listar todos los ENTORNOS VIRTUALES disponibles.
   C:\Usuarios\Jorge\conda env list


==========================================================
## 3. Guía de Instalación de VSCode para Windows (64 bits)
==========================================================
Guía de Instalación de Visual Studio Code (VS Code) en Windows (64 bits)

1. Descargar el Instalador
• Abre tu navegador web y ve al sitio oficial de Visual Studio Code: code.visualstudio.com/download.
• La página detectará automáticamente tu sistema operativo y te mostrará el botón "Download for Windows".
• Para asegurarte de obtener la versión de 64 bits, verifica que el nombre del archivo descargado sea similar a VSCodeUserSetup-x64-....exe. Si tu sistema es de 64 bits, esta es la opción correcta .
• Espera a que el archivo .exe termine de descargarse.

2. Ejecutar el Instalador
• Ve a tu carpeta de Descargas y haz doble clic en el archivo ejecutable que descargaste para iniciar el proceso de instalación.
• Nota sobre el tipo de instalador: Se recomienda usar el "User Installer" (Instalador de usuario) para la mayoría de los casos, ya que instala VS Code solo para tu cuenta de usuario y evita posibles problemas de permisos. La otra opción, "System Installer", lo instala para todos los usuarios del equipo.

3. Paso a Paso del Asistente de Instalación
• Acuerdo de Licencia: Lee el acuerdo de licencia, selecciona la opción "I accept the agreement" (Acepto el acuerdo) y haz clic en Next > .
• Seleccionar Ubicación de Instalación: Elige la carpeta de destino. Puedes aceptar la ruta por defecto (normalmente en C:\) o hacer clic en Browse... para seleccionar una ubicación diferente, por ejemplo, en otra unidad como D:\ para ahorrar espacio en el disco del sistema . Haz clic en Next >.
• Seleccionar Carpeta en el Menú Inicio: Puedes elegir si deseas crear una carpeta para VS Code en el menú de inicio o no. Normalmente, puedes dejar la opción por defecto y hacer clic en Next > .
• Tareas Adicionales (Importante): En esta pantalla, verás varias opciones de configuración. Se recomienda marcar todas las casillas para una mejor integración con Windows:
- Create a desktop icon (Crear un icono en el escritorio).
- Add "Open with Code" action to Windows Explorer file context menu (Añadir acción "Abrir con Code" al menú contextual de archivos).
- Add "Open with Code" action to Windows Explorer directory context menu (Añadir acción "Abrir con Code" al menú contextual de directorios).
- Register Code as an editor for supported file types (Registrar Code como editor para tipos de archivo compatibles).
- Add to PATH (Añadir a PATH) - Especialmente importante para poder ejecutar el comando code desde la terminal o el Símbolo del sistema.

• Haz clic en Next >.
• Instalando: Revisa el resumen de tus configuraciones y haz clic en Install (Instalar) para comenzar la instalación. El proceso puede tomar unos minutos .
• Completando la Instalación: Una vez finalizada, aparecerá la pantalla de finalización. Puedes dejar marcada la casilla Launch Visual Studio Code (Iniciar Visual Studio Code) para abrirlo inmediatamente . Haz clic en Finish (Finalizar) para cerrar el instalador .

4. Verificar la Instalación
Para confirmar que la instalación fue exitosa:
• Desde el escritorio: Si marcaste la opción, haz doble clic en el acceso directo de VS Code en tu escritorio.
• Usando el Símbolo del sistema (CMD) o PowerShell: Abre una ventana de terminal y escribe el comando code --version y presiona Enter. Si ves el número de versión de VS Code, significa que la instalación fue exitosa y que la variable PATH se configuró correctamente.

5. Instalación de Extensiones Esenciales y Configuración Adicional

VS Code se potencia con extensiones. Aquí tienes algunos pasos iniciales:
• Instalar el paquete de idioma (opcional):
  1. Haz clic en el icono de Extensiones en la barra lateral izquierda (o presiona Ctrl+Shift+X).
  2. Busca "Spanish Language Pack".
  3. Haz clic en Install.
  4. Una vez instalado, reinicia VS Code cuando se te solicite para que los cambios surtan efecto.

• Instalar extensiones para tu lenguaje de programación:
  - Python - Microsoft
  - Jupyter - Microsoft
  - Pylance - Microsoft
  - Gitlens -- Git supercharged - GitKraken
  - Error Lens - Alexander
  - Indent Rainbow Palettes - Evondev
  - Material Icon Theme - Philipp Kief

• Crear proyecto:
  - Nombre del proyecto: reto_unidad1_jorge_lievano
  - El proyecto realiza actividades de exploración, limpieza, transformación y análisis de un conjunto de datos de ventas de una empresa tecnológica.

• Estructura del proyecto:

reto_unidad1_jorge_lievano/
│
├── data/
│   ├── ventas_techventas.csv
│   └── ventas_techventas_clean.csv
│
├── notebooks/
│   ├── 01_numpy.ipynb
│   ├── 02_sql_discovery.ipynb
│   └── 03_pandas_pipeline.ipynb
│
├── scripts/
│   └── limpiar_csv_completo.py
│
├── sql/
│   └── 02_sql_discovery.sql
│
├── README.md
├── requirements.txt
└── Setup.md

• Configurar INTERPRETE DE PYTHON (ENTORNO DE TRABAJO) para nuestro proyecto en VSCode
  1. CTRL + SHIFT + P
  2. Escibe: Python Select Interpreter
  3. Seleccionar d ela lista: MasterIA (3.11)

• Instalar librerias del proyecto
  1. Abrir una nueva terminal: CTRL + SHIFT + Ñ
  2. Ir al directorio raíz del proyecto
  3. bash> pip install -r requirements.txt 
  4. Escribir: Y

• Personalizar la configuración: Puedes ajustar el tema, la fuente y otras preferencias desde el menú Archivo > Preferencias > Configuración (o Ctrl + ,). También puedes activar el guardado automático de archivos desde la configuración.
   
----------------------------------------------------
## Posibles Problemas y Soluciones con Installer VSCode
----------------------------------------------------
• ¿Necesito permisos de administrador? No necesariamente. Si usas el "User Installer", generalmente no se requieren permisos de administrador, a menos que quieras instalar VS Code en una carpeta protegida del sistema.
• ¿El comando code no funciona en la terminal? Esto suele deberse a que no se marcó la opción "Add to PATH" durante la instalación. Puedes reinstalar VS Code y asegurarte de marcar esa casilla, o añadir manualmente la ruta de instalación a las variables de entorno de Windows.
• Error al iniciar o instalar: Asegúrate de que el instalador se haya descargado completamente y no esté corrupto. Si el problema persiste, intenta ejecutar el instalador como Administrador (clic derecho > "Ejecutar como administrador").

================================================================================
## INSTALAR CONDA PANDAS EN VS CODE
----------------------------------------------------
1. Abre VS Code
Ve a Terminal → New Terminal
Asegúrate de que la terminal esté usando PowerShell o CMD (no Git Bash si tienes problemas)

2. Activar el entorno Conda (si no está activo)
powershell> conda activate MasterIA
Verificarás que el prompt cambie a (MasterIA) al inicio de la línea.

3. Instalar pandas con Conda
powershell> conda install pandas -y

O si prefieres usar pip dentro del entorno conda:
powershell> pip install pandas

4. Verificar la instalación
powershell> python -c "import pandas; print(pandas.__version__)"

=======================================================
## PARA PROCESAR DATOS GUARDADOS EN EXCEL
-------------------------------------------------------
Debe instalar: 
# Opción 1: Instalar una versión más reciente de openpyxl desde conda-forge
# conda install -c conda-forge openpyxl

# Opción 2: Usar pip en lugar de conda (recomendado)
# pip install openpyxl

# Opción 3: Actualizar pandas junto con openpyxl desde conda-forge
# conda install -c conda-forge pandas openpyxl

# Opción 4: Si prefieres mantener los canales actuales, forzar la actualización
# conda update --all
# conda install openpyxl

========================================================
Ing. Jorge Uriel Lievano Cifuentes
Bucaramanga - Colombia
Cel. +57 3209192537

