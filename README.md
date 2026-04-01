COMMICOMMITfy index.html to add user interface elements (e.g., selectors or input fields) that allow users to map CSV columns to the required fields for entry generation (Amount, Description, Currency, Type, etc.).

Agregar Interfaz de Mapeo de Columnas
Subtask:
Modificar 'index.html' para añadir elementos de la interfaz de usuario (como selectores o campos de entrada) que permitan al usuario elegir qué columna del CSV corresponde a cada campo necesario para la generación de asientos (Monto, Descripción, Moneda, Tipo, etc.).

Reasoning: The subtask requires modifying the index.html file to include column mapping elements. I will update the html_content variable to insert the new UI elements for column mapping, then write this content to the frontend/index.html file.


[ ]
new_mapping_html = '''
        <section id="column-mapping-section">
            <h2>Mapeo de Columnas</h2>
            <div class="mapping-controls">
                <div>
                    <label for="map-amount">Columna para Monto:</label>
                    <select id="map-amount" class="column-selector">
                        <option value="">Seleccionar columna</option>
                    </select>
                </div>
                <div>
                    <label for="map-description">Columna para Descripción:</label>
                    <select id="map-description" class="column-selector">
                        <option value="">Seleccionar columna</option>
                    </select>
                </div>
                <div>
                    <label for="map-currency">Columna para Moneda:</label>
                    <select id="map-currency" class="column-selector">
                        <option value="">Seleccionar columna</option>
                    </select>
                </div>
                <div>
                    <label for="map-type">Columna para Tipo:</label>
                    <select id="map-type" class="column-selector">
                        <option value="">Seleccionar columna</option>
                    </select>
                </div>
            </div>
        </section>
'''

# Find the position to insert the new mapping section
# It should be after the generate-button inside the upload-section
insert_position = html_content.find('<button id="generate-button">Generar Asientos</button>')
if insert_position != -1:
    # Insert the new HTML after the button and its closing tag
    updated_html_content = html_content[:insert_position + len('<button id="generate-button">Generar Asientos</button>') + len('</button>') + len('\n')] + new_mapping_html + html_content[insert_position + len('<button id="generate-button">Generar Asientos</button>') + len('</button>') + len('\n'):]
    html_content = updated_html_content
else:
    print("Could not find the insertion point for column mapping. Please check html_content.")

# Also update the CSS to add styles for the new mapping section
new_css_for_mapping = '''
.mapping-controls {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 15px;
    margin-top: 20px;
}

.mapping-controls div {
    display: flex;
    flex-direction: column;
}

.mapping-controls label {
    margin-bottom: 5px;
    font-weight: bold;
    color: #555;
}

.column-selector {
    width: 100%;
    padding: 8px 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    background-color: #fff;
    font-size: 1em;
    appearance: none; /* Remove default browser styling */
    background-image: url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%23000000%22%20d%3D%22M287%2C197.915L159.27%2C63.267c-5.83-6.075-15.82-6.075-21.652%2C0L5.42%2C197.915c-5.83%2C6.075-5.83%2C15.82%2C0%2C21.896l10.825%2C11.26c5.83%2C6.075%2C15.82%2C6.075%2C21.652%2C0l113.6-118.06l113.6%2C118.06c5.83%2C6.075%2C15.82%2C6.075%2C21.652%2C0l10.825-11.26C292.83%2C213.735%2C292.83%2C203.99%2C287%2C197.915z%22%2F%3E%3C%2Fsvg%3E'); /* Custom arrow */
    background-repeat: no-repeat;
    background-position: right 10px center;
    background-size: 12px;
}

.column-selector:focus {
    border-color: #3498db;
    outline: none;
    box-shadow: 0 0 0 2px rgba(52, 152, 219, 0.25);
}
'''

# Append new CSS to existing css_content
css_content += new_css_for_mapping

# Write the updated HTML and CSS content to files
with open('frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print("frontend/index.html updated with column mapping interface.")

with open('frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)
print("frontend/style.css updated with mapping styles.")
.   app/m
