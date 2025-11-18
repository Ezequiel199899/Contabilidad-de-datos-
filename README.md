  <project xmlns="http://maven.apache.org/POM/4.0.0" 
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
         xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.finanzasai</groupId>
    <artifactId>finanzas-ai</artifactId>
    <version>1.0.0</version>
    
    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <spring.boot.version>3.2.0</spring.boot.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-validation</artifactId>
        </dependency>
        
        <dependency>
            <groupId>com.h2database</groupId>
            <artifactId>h2</artifactId>
            <scope>runtime</scope>
        </dependency>
        
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
    </dependencies>
    
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>${spring.boot.version}</version>
                <executions>
                    <execution>
                        <goals>
                            <goal>repackage</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
    
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>${spring.boot.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
</project>
# H2 Console (Acceso web para ver la DB: http://localhost:8080/h2-console)
spring.h2.console.enabled=true

# Configuración de Conexión
spring.datasource.url=jdbc:h2:mem:finanzasai
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

# Configuración de JPA/Hibernate
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.jpa.hibernate.ddl-auto=update # Crea y actualiza tablas automáticamente
spring.jpa.show-sql=true
package com.finanzasai.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import java.math.BigDecimal;
import javax.validation.constraints.DecimalMin;
import javax.validation.constraints.NotNull;

@Data 
@NoArgsConstructor
@AllArgsConstructor
public class AsientoRequest {
    
    @NotNull(message = "El monto en ARS no puede ser nulo.")
    @DecimalMin(value = "0.01", message = "El monto debe ser positivo.")
    private BigDecimal montoARS;
    
    @NotNull @DecimalMin(value = "0.01", message = "El tipo de cambio USD debe ser positivo.")
    private BigDecimal tipoCambioUSD;
    
    @NotNull @DecimalMin(value = "0.00")
    private BigDecimal tipoCambioEUR;
    
    @NotNull @DecimalMin(value = "0.00")
    private BigDecimal tipoCambioBRL;
    
    @NotNull @DecimalMin(value = "0.00")
    private BigDecimal tipoCambioCLP;

    @NotNull @DecimalMin(value = "0.00")
    private BigDecimal porcentajeIVA;
    
    @NotNull @DecimalMin(value = "0.00")
    private BigDecimal pagoChequeTerceros;
    
    @NotNull @DecimalMin(value = "0.00")
    private BigDecimal pagoPagares;

    @NotNull(message = "La fecha de operación es requerida.")
    private String fechaOperacion;
}
package com.finanzasai.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import java.math.BigDecimal;
import jakarta.persistence.Entity; // Importante
import jakarta.persistence.GeneratedValue; // Importante
import jakarta.persistence.GenerationType; // Importante
import jakarta.persistence.Id; // Importante

@Entity // <-- Es una tabla de DB
@Data
@NoArgsConstructor
@AllArgsConstructor
public class AsientoResponse {
    
    @Id // <-- Clave primaria
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    private String fechaOperacion; // Añadido para guardar la fecha
    
    private BigDecimal montoUSD;
    private BigDecimal montoEUR;
    private BigDecimal montoBRL;
    private BigDecimal montoCLP;

    private BigDecimal ivaCalculado;
    private BigDecimal totalConIVA;
    private BigDecimal patrimonioNeto;

    private BigDecimal simulacionCotizacionIA; 
}
package com.finanzasai.repository;

import com.finanzasai.model.AsientoResponse;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.math.BigDecimal;
import java.util.List;

@Repository
public interface AsientoRepository extends JpaRepository<AsientoResponse, Long> {

    // Consulta automática: Buscar asientos con IVA calculado mayor a un valor
    List<AsientoResponse> findByIvaCalculadoGreaterThan(BigDecimal ivaMinimo);
    
    // Consulta automática: Buscar el asiento con el ID más alto (el último)
    AsientoResponse findTopByOrderByIdDesc();
}
package com.finanzasai.controller;

import com.finanzasai.model.AsientoRequest;
import com.finanzasai.model.AsientoResponse;
import com.finanzasai.service.AsientoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import jakarta.validation.Valid; // Importante: Se usa la versión de jakarta

@RestController
@RequestMapping("/api/asiento")
@CrossOrigin(origins = "*") 
public class AsientoController {

    @Autowired
    private AsientoService asientoService;

    @PostMapping("/generar")
    public AsientoResponse generarAsiento(@Valid @RequestBody AsientoRequest request) { // <-- AQUÍ SE ACTIVA LA VALIDACIÓN
        return asientoService.generarAsiento(request);
    }
}
package com.finanzasai.service;

import com.finanzasai.model.AsientoRequest;
import com.finanzasai.model.AsientoResponse;
import com.finanzasai.repository.AsientoRepository; // Importante
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import java.math.BigDecimal;
import java.math.MathContext;
import java.math.RoundingMode;
import java.util.Map;

@Service
public class AsientoService {
    
    @Autowired
    private AsientoRepository asientoRepository; // <-- Nuevo: Para guardar
    
    // Resto de constantes y RestTemplate
    private static final MathContext MC = new MathContext(10, RoundingMode.HALF_UP);
    private static final BigDecimal CIEN = new BigDecimal("100");
    private static final String PYTHON_API_URL = "http://localhost:5000/predict";
    private final RestTemplate restTemplate = new RestTemplate();


    public AsientoResponse generarAsiento(AsientoRequest request) {
        AsientoResponse response = new AsientoResponse();
        
        // ... (Lógica de cálculo, redondeo, y llamada a Python) ...
        // (Asumimos que todos los campos de 'response' se llenan correctamente aquí)

        // Asignamos la fecha antes de guardar
        response.setFechaOperacion(request.getFechaOperacion()); 

        // ----------------------------------------------------
        // PASO FINAL: Guardar el asiento en la base de datos H2
        // ----------------------------------------------------
        
        AsientoResponse savedResponse = asientoRepository.save(response); 
        
        System.out.println("Asiento guardado con ID: " + savedResponse.getId());

        return savedResponse;
    }
}


