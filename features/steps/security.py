from behave import step
import os
import time
from helper.services.actions_basic import Basepage
from helper.pages.pages_claro import pageclaro
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

@step(u'ingresmos a la url "claro_url"')
def step_impl(context):
    url = os.getenv('claro_url')
    context.browser.get(url)
    time.sleep(2)

@step(u'aceptamos las cookies')
def step_impl(context):
    Basepage.click_button(context, pageclaro.cookies)
    time.sleep(1)

@step(u'damos click en el boton solucions y ingresamos a cyber-physical-security')
def step_impl(context):
    driver = context.browser
    solucion = driver.find_element(By.XPATH, '//*[@id="w-dropdown-toggle-1"]')
    actions = ActionChains(driver)
    actions.move_to_element(solucion).perform()
    time.sleep(1)
    Basepage.click_button(context, pageclaro.btn_cyber_physical)
    time.sleep(2)


@step(u'damos click en el boton solucions y ingresamos a secure-managed-lan')
def step_impl(context):
    driver = context.browser
    solucion = driver.find_element(By.XPATH, '//*[@id="w-dropdown-toggle-1"]')
    actions = ActionChains(driver)
    actions.move_to_element(solucion).perform()
    time.sleep(1)
    Basepage.click_button(context, pageclaro.btn_secure)
    time.sleep(2)

@step(u'damos click en el boton get started')
def step_impl(context):
    driver = context.browser
    driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight / 1.3);')
    Basepage.click_button(context, pageclaro.btn_get_started)


@step(u'damos click en el boton solucions y ingresamos a cybersoc')
def step_impl(context):
    driver = context.browser
    solucion = driver.find_element(By.XPATH, '//*[@id="w-dropdown-toggle-1"]')
    actions = ActionChains(driver)
    actions.move_to_element(solucion).perform()
    time.sleep(1)
    Basepage.click_button(context, pageclaro.btn_cybersoc)
    time.sleep(2)

@step(u'rellenamos el formulario')
def step_impl(context):
   pass


@step(u'validaremos mensaje de error')
def step_impl(context):
    pass

@step(u'damos click en el boton solucions y ingresamos a zero-trust-endpoint-security-solution')
def step_impl(context):
    driver = context.browser
    solucion = driver.find_element(By.XPATH, '//*[@id="w-dropdown-toggle-1"]')
    actions = ActionChains(driver)
    actions.move_to_element(solucion).perform()
    time.sleep(1)
    Basepage.click_button(context, pageclaro.btn_zero)
    time.sleep(2)

@step(u'damos click en el boton view more')
def step_impl(context):
    driver = context.browser
    driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight / 1.4);')
    time.sleep(2)
    Basepage.click_button(context, pageclaro.btn_more)

@step(u'damos click en el boton solucions y ingresamos a penetration-testing')
def step_impl(context):
    driver = context.browser
    solucion = driver.find_element(By.XPATH, '//*[@id="w-dropdown-toggle-1"]')
    actions = ActionChains(driver)
    actions.move_to_element(solucion).perform()
    time.sleep(1)
    Basepage.click_button(context, pageclaro.btn_testing)
    time.sleep(2)

@step(u'damos click en el boton view all')
def step_impl(context):
    pass