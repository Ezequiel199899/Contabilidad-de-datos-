
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aplicación sin Rojo</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap" rel="stylesheet">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Configuración de la fuente Inter como se recomienda */
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f4f6f8; /* Fondo claro y suave */
        }
        /* Color principal: un azul vibrante, sustituyendo cualquier posible rojo */
        .primary-color {
            background-color: #3b82f6; /* Tailwind blue-500 */
        }
        .primary-color:hover {
            background-color: #2563eb; /* Tailwind blue-600 */
        }
    </style>
</head>
<body class="min-h-screen flex items-center justify-center p-4">

    <div class="w-full max-w-lg bg-white shadow-2xl rounded-xl p-8 space-y-6">

        <h1 class="text-3xl font-extrabold text-gray-900 text-center">
            Generador de Mensajes
        </h1>

        <p class="text-gray-600 text-center">
            Introduce tu nombre y genera un mensaje amistoso.
        </p>

        <div>
            <label for="nameInput" class="block text-sm font-medium text-gray-700 mb-2">
                Tu Nombre:
            </label>
            <input
                type="text"
                id="nameInput"
                placeholder="Ej. Juan Pérez"
                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 transition duration-150"
                required
                aria-required="true"
            >
        </div>

        <button
            id="generateButton"
            class="w-full primary-color text-white font-semibold py-3 rounded-xl shadow-md transition duration-200 ease-in-out transform hover:scale-[1.01]"
        >
            Generar Mensaje
        </button>

        <div id="outputContainer" role="status" class="hidden bg-blue-50 border border-blue-200 p-4 rounded-lg">
            <p class="font-medium text-blue-700">Mensaje Generado:</p>
            <p id="messageOutput" class="mt-1 text-lg text-blue-800 break-words"></p>
        </div>

        <div id="errorBox" role="alert" class="hidden bg-yellow-50 border border-yellow-300 p-3 rounded-lg">
            <p id="errorMessage" class="text-sm font-medium text-yellow-800"></p>
        </div>
    </div>

    <script>
        // Obtener referencias a los elementos del DOM
        const nameInput = document.getElementById('nameInput');
        const generateButton = document.getElementById('generateButton');
        const outputContainer = document.getElementById('outputContainer');
        const messageOutput = document.getElementById('messageOutput');
        const errorBox = document.getElementById('errorBox');
        const errorMessage = document.getElementById('errorMessage');

        /**
         * Oculta los contenedores de error y salida y limpia los mensajes.
         */
        function resetState() {
             errorBox.classList.add('hidden');
             outputContainer.classList.add('hidden');
             errorMessage.textContent = '';
        }

        /**
         * Maneja la generación del mensaje al hacer clic en el botón.
         */
        function generateMessage() {
            resetState(); // Limpiar el estado
            
            const name = nameInput.value.trim();

            if (name === "") {
                // 1. Mostrar mensaje de advertencia amable
                errorMessage.textContent = "¡Oye! Por favor, introduce tu nombre para generar el mensaje.";
                errorBox.classList.remove('hidden');
                
                // 2. Devolver el foco al campo de entrada (mejora de UX/accesibilidad)
                nameInput.focus();

                console.warn("Input validation failed: Name field is empty."); 
                return;
            }

            // Lógica de generación del mensaje
            const message = `Hola, ${name}. ¡Tu solicitud ha sido procesada con éxito! Esperamos que tengas un día increíble y lleno de energía.`;

            // Mostrar el resultado
            messageOutput.textContent = message;
            outputContainer.classList.remove('hidden');

            console.log(`Mensaje generado para: ${name}`);
        }

        // Asignar el listener al botón
        generateButton.addEventListener('click', generateMessage);
        
        // Habilitar la pulsación de Enter en el campo de texto
        nameInput.addEventListener('keydown', (event) => {
            if (event.key === 'Enter') {
                event.preventDefault(); // Evita el envío de formularios
                generateMessage();
            }
        });

        // Asegurarse de que no haya errores al cargar
        window.onload = () => {
             console.log("Aplicación de Generación de Mensajes cargada correctamente.");
             // Poner el foco en el campo de entrada al cargar para mejor UX
             nameInput.focus();
        }; 
    </script>
</body>
</html>
