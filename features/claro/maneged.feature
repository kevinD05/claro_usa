Feature: Validamos ingresar a la pagina web 

@managed
Scenario: validamos la pestaña maneged network
    Given ingresmos a la url "claro_url"
    When aceptamos las cookies
    And damos click en el boton solucions y ingresamos enterprise-cloud-connect
    And damos click en boton get 
    And damos click en el boton solucions y ingresamos Business internet
    Then  damos click en el boton view solution
