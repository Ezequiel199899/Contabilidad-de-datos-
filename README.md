  
spring.datasource.url=jdbc:postgresql://localhost:5432/contable
spring.datasource.username=postgres
spring.datasource.password=postgres
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
server.port=8080
app.owner.name=Ezequiel Samuel Prilusky

# Stripe (reemplazar por tus claves en producción)
stripe.secret.key=sk_test_REPLACE_ME
stripe.webhook.secret=whsec_REPLACE_ME

# Frontend URL (usado para redirect en Stripe)
frontend.url=http://localhost:3000

# Precio único en USD (one-time)
product.price.usd=999 package com.prototipo.contable.controller;

import com.stripe.Stripe;
import com.stripe.exception.StripeException;
import com.stripe.model.checkout.Session;
import com.stripe.param.checkout.SessionCreateParams;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api/pay")
public class PaymentController {

    @Value("${stripe.secret.key:}")
    private String stripeSecret;

    @Value("${frontend.url:http://localhost:3000}")
    private String frontendUrl;

    @Value("${product.price.usd:999}")
    private Long productPriceUsd;

    @PostMapping("/create-session")
    public ResponseEntity<Map<String, String>> createCheckoutSession(@RequestBody Map<String, Object> body)
            throws StripeException {

        Stripe.apiKey = stripeSecret;
        long unitAmountCents = productPriceUsd * 100L;

        SessionCreateParams params = SessionCreateParams.builder()
                .setMode(SessionCreateParams.Mode.PAYMENT)
                .setSuccessUrl(frontendUrl + "/success?session_id={CHECKOUT_SESSION_ID}")
                .setCancelUrl(frontendUrl + "/cancel")
                .addLineItem(
                        SessionCreateParams.LineItem.builder()
                                .setQuantity(1L)
                                .setPriceData(
                                        SessionCreateParams.LineItem.PriceData.builder()
                                                .setCurrency("usd")
                                                .setUnitAmount(unitAmountCents)
                                                .setProductData(
                                                        SessionCreateParams.LineItem.PriceData.ProductData.builder()
                                                                .setName("Licencia Pro — App Contable Bimonetaria")
                                                                .build()
                                                ).build()
                                ).build()
                )
                .build();

        Session session = Session.create(params);
        return ResponseEntity.ok(Map.of("sessionId", session.getId()));
    }
}package com.prototipo.contable.controller;

import org.springframework.web.bind.annotation.*;
import java.util.Map;

@RestController
@RequestMapping("/api/license")
public class LicenseController {

    @GetMapping("/verify")
    public Map<String,Object> verify(@RequestParam String key){
        boolean valid = (key != null && (key.equals("MASTER-LICENSE-KEY") || key.startsWith("LIC-")));
        return Map.of("valid", valid, "owner", "Ezequiel Samuel Prilusky");
    }
}