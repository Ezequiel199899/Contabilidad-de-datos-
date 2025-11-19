bin/bash
# Script de Demostración del Flujo Básico de Git

# 1. Configuración Inicial (Opcional, si ya lo hiciste)
# echo "--- 1. CONFIGURACIÓN INICIAL (Si es la primera vez) ---"
# git config --global user.name "Tu Nombre"
# git config --global user.email "tu@email.com"

# --- CONFIGURACIÓN DEL REPOSITORIO DE PRUEBA ---

# Crear una carpeta de proyecto simulada
echo "--- 2. CREANDO CARPETA DE PRUEBA ---"
mkdir git-test-project
cd git-test-project
echo "Carpeta 'git-test-project' creada y accedida."

# 3. Inicializar Git en la carpeta
echo "--- 3. INICIALIZANDO GIT (git init) ---"
git init
echo "Repositorio Git inicializado."

# --- PRIMER COMMIT ---

# 4. Crear un archivo inicial
echo "--- 4. CREANDO ARCHIVO INICIAL (index.html) ---"
echo "<h1>Bienvenido al Proyecto</h1><p>Versión 1.0</p>" > index.html

# 5. Revisar el estado actual
echo "--- 5. ESTADO (git status) ---"
git status

# 6. Agregar el archivo al Área de Staging
echo "--- 6. AGREGANDO ARCHIVOS (git add .) ---"
git add .

# 7. Crear el primer Commit
echo "--- 7. CREANDO COMMIT (git commit) ---"
git commit -m "feat: Commit inicial con la estructura basica"

# --- SEGUNDO CAMBIO ---

# 8. Modificar el archivo
echo "--- 8. REALIZANDO SEGUNDO CAMBIO ---"
echo "<style>body { font-family: sans-serif; }</style>" >> index.html
echo "Archivo modificado."

# 9. Revisar el estado nuevamente
echo "--- 9. ESTADO después de la modificación ---"
git status

# 10. Agregar solo el archivo modificado
echo "--- 10. AGREGANDO CAMBIOS (git add index.html) ---"
git add index.html

# 11. Crear el segundo Commit
echo "--- 11. CREANDO SEGUNDO COMMIT ---"
git commit -m "style: Agregar fuente sans-serif al CSS"

# --- VERIFICACIÓN Y SIMULACIÓN DE SUBIDA ---

# 12. Ver el historial de commits
echo "--- 12. HISTORIAL DE COMMITS (git log --oneline) ---"
git log --oneline

# 13. Simulación del Push (Subida al remoto)
echo "--- 13. SIMULACIÓN DE SUBIDA (git push) ---"
echo "AVISO: Para subir a un repositorio real (ej. GitHub), faltaría el comando 'git remote add origin <URL>' seguido de 'git push'."
echo "El script ha terminado. Tu repositorio local está listo con 2 commits."
