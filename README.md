#!/bin/bash
# Flujo Completo de Git: Setup, Commits y Verificación Final antes de Push

PROJECT_DIR="git-test-project"

echo "--- 1. INICIANDO EL FLUJO DE TRABAJO DE GIT ---"
echo "Creando y entrando a la carpeta: $PROJECT_DIR"

# Eliminar el directorio si existe para asegurar un inicio limpio
rm -rf $PROJECT_DIR
mkdir $PROJECT_DIR
cd $PROJECT_DIR

# 2. Inicializar el repositorio Git
git init -b main
echo "Repositorio Git inicializado en la rama 'main'."

# --- PASO 1: EL PRIMER COMMIT (feat: Estructura inicial) ---
echo -e "\n--- 3. CREANDO EL CÓDIGO INICIAL Y COMMIT 1 ---"

# Contenido inicial del index.html (primer commit)
cat > index.html <<- 'EOF'
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proyecto Listo para Subir</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="min-h-screen flex items-center justify-center p-4">
    <div class="bg-white p-8 rounded-xl shadow-2xl max-w-lg w-full text-center">
        <h1 class="text-4xl font-bold text-gray-800 mb-4">
            ¡El Código Está Completo!
        </h1>
        <p class="mt-8 text-lg font-medium text-gray-700">
            Esta es la versión inicial de la página.
        </p>
    </div>
</body>
</html>
EOF

# Añadir y commitear el primer cambio
git add index.html
git commit -m "feat: Inicializar estructura básica de la página."
echo "✅ Commit 1 realizado."

# --- PASO 2: EL SEGUNDO COMMIT (style: Añadir fuente) ---
echo -e "\n--- 4. AÑADIENDO ESTILOS Y COMMIT 2 ---"

# Modificar el archivo para añadir el bloque <style> con la fuente sans-serif
cat > index.html <<- 'EOF'
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proyecto Listo para Subir</title>
    <!-- Carga de Tailwind CSS para el estilo -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Aplicamos el tipo de fuente sans-serif a todo el cuerpo, reflejando el segundo commit */
        body {
            font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
            background-color: #f7f7f7;
        }
    </style>
</head>
<body class="min-h-screen flex items-center justify-center p-4">
    <!-- Contenedor principal con esquinas redondeadas y sombra -->
    <div class="bg-white p-8 rounded-xl shadow-2xl max-w-lg w-full text-center">
        <!-- Título principal -->
        <h1 class="text-4xl font-bold text-gray-800 mb-4">
            ¡El Código Está Completo!
        </h1>
        <!-- Mensaje de confirmación de los commits -->
        <p class="text-gray-600 mb-6">
            Esta es la versión final de nuestro archivo. Incluye la estructura básica inicial y la aplicación de la fuente sans-serif.
        </p>

        <!-- Detalle de los cambios -->
        <div class="space-y-4 text-left">
            <div class="p-3 bg-indigo-50 rounded-lg border border-indigo-200">
                <p class="font-semibold text-indigo-700">Commit 1 (feat):</p>
                <p class="text-sm text-indigo-600">Estructura básica de la página (index.html).</p>
            </div>
            <div class="p-3 bg-green-50 rounded-lg border border-green-200">
                <p class="font-semibold text-green-700">Commit 2 (style):</p>
                <p class="text-sm text-green-600">Estilo de fuente sans-serif aplicado a toda la página.</p>
            </div>
        </div>

        <p class="mt-8 text-lg font-medium text-gray-700">
            ¡Listo para hacer git push!
        </p>
    </div>
</body>
</html>
EOF

# Añadir y commitear el segundo cambio
git add index.html
git commit -m "style: Aplicar fuente sans-serif al cuerpo de la página."
echo "✅ Commit 2 realizado."


# --- PASO 3: VERIFICACIÓN FINAL ANTES DEL PUSH ---
echo -e "\n--- 5. REPORTE FINAL: Historial de Commits ---"
git log --oneline --max-count=2
echo "------------------------------------------------"

echo -e "\n--- 6. REPORTE FINAL: Estado del Repositorio (git status) ---"
git status
echo "------------------------------------------------"

echo -e "\n--- RESUMEN ---"
echo "El repositorio tiene 2 commits pendientes de subir (ahead of 'origin/main')."
echo "¡Estás listo para el comando 'git push'!"

# Volver al directorio original
cd ..
