from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By


@given('que estou na tela de login')
def screen_login(context):
    context.driver.find_element(By.XPATH, "//*[@id='nav-link-accountList']").click()
    sleep(2)

@given('informo email correto')
def incorrect_email(context):
    context.driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys("xpto@xpto.com")

@given('clico no botão de continuar')
def continue_button(context):
    context.driver.find_element(By.XPATH, "//input[@id='continue']").click()

@given('informo senha incorreta')
def incorrect_password(context):
    context.driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys("xpto")

@when('clico no botão para logar')
def login_button(context):
    context.driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()
    sleep(5)

@then('retorna mensagem de erro')
def show_error(context):
    assert context.driver.find_element(By.XPATH,
        "//*[@class='a-list-item' and contains(text(), 'Sua senha está incorreta')]").is_displayed()


@given('que retornei para tela de login')
def login_return(context):
    # Altera email
    context.driver.find_element(By.XPATH, "//*[@id='ap_change_login_claim']").click()
    sleep(3)

@given('informo email inexistente')
def non_existent_email(context):
    context.driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys("xpto")

@when('clico no botão continuar')
def continue_button(context):
    context.driver.find_element(By.XPATH, "//input[@id='continue']").click()
    sleep(5)

@then('exibe mensagem de erro')
def show_error(context):
    assert context.driver.find_element(By.XPATH,
        "//*[@class='a-list-item' and contains(text(),'Não encontramos uma conta associada a este endereço de e-mail')]").is_displayed()

    context.driver.find_element(By.XPATH, "//*[@id='ap_email']").clear()

@given('que estou na tela de login Amazon')
def screen_login(context):
    # Confere URL login
    assert context.driver.current_url == "https://www.amazon.com.br/ap/signin"
    sleep(3)

@given('informo credenciais válidas')
def valid_credenciais(context):
    context.driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys("xpto@xpto.com")
    context.driver.find_element(By.XPATH, "//input[@id='continue']").click()
    context.driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys("xpto")
    sleep(2)

@when('clico no botão de login')
def login_button(context):
    context.driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()
    sleep(5)

@then('realiza login com sucesso')
def login_success(context):
    assert context.driver.current_url == "https://www.amazon.com.br/?ref_=nav_ya_signin"