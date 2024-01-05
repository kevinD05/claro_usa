Feature: Validamos ingresar a la pagina web 

@cyber_security
Scenario: validamos la pestaña Cyber security
    Given ingresmos a la url "claro_url"
    When aceptamos las cookies
    And damos click en el boton solucions y ingresamos a cyber-physical-security
    And damos click en el boton solucions y ingresamos a secure-managed-lan
    And damos click en el boton get started
    And damos click en el boton solucions y ingresamos a cybersoc
    And damos click en el boton get started
    And rellenamos el formulario
    And validaremos mensaje de error
    And damos click en el boton solucions y ingresamos a zero-trust-endpoint-security-solution
    And damos click en el boton view more
    And damos click en el boton solucions y ingresamos a penetration-testing
    And damos click en el boton view all
    