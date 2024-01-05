from behave import step
import os
import time
from helper.services.actions_basic import Basepage
from helper.pages.pages_claro import pageclaro
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

@step(u'damos click en el boton solucions y ingresamos enterprise-cloud-connect')
def step_impl(context):
    driver = context.browser
    solucion = driver.find_element(By.XPATH, '//*[@id="w-dropdown-toggle-1"]')
    actions = ActionChains(driver)
    actions.move_to_element(solucion).perform()
    time.sleep(1)
    Basepage.click_button(context, pageclaro.btn_cloul)
    time.sleep(2)


@step(u'damos click en boton get')
def step_impl(context):
    time.sleep(1)
    Basepage.click_button(context, pageclaro.btn_get)


@step(u'damos click en el boton solucions y ingresamos Business internet')
def step_impl(context):
    driver = context.browser
    solucion = driver.find_element(By.XPATH, '//*[@id="w-dropdown-toggle-1"]')
    actions = ActionChains(driver)
    actions.move_to_element(solucion).perform()
    time.sleep(1)
    Basepage.click_button(context, pageclaro.btn_business)
    time.sleep(2)


@step(u'damos click en el boton view solution')
def step_impl(context):
    driver = context.browser
    driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight / 1.4);')
    Basepage.click_button(context, pageclaro.btn_solutions)
    time.sleep(2)