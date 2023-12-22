from time import sleep
from behave import given, when, then
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


@given('que estou na página de busca da Amazon')
def go_to_page(context):
    assert context.driver.current_url == "https://www.amazon.com.br/?ref_=nav_ya_signin"

@when('for digitar o nome do "Firestick"')
def search_product(context):
    product_input = context.driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    product_input.send_keys('Firestick')
    assert product_input.get_attribute("value") == "Firestick"


@when('clicar no ícone de Lupa')
def search_icon(context):
    click_search = context.driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")
    click_search.click()


@then('retorna resultado trazendo produtos "Firestick"')
def product_result(context):
    result = context.driver.find_element(By.XPATH, "//span[@class='a-size-medium-plus a-color-base a-text-bold']")
    assert result.is_displayed()


@given('que estou na tela de resultado do Produto')
def screen_result(context):
    result = context.driver.find_element(By.XPATH, "//span[@class='a-size-medium-plus a-color-base a-text-bold']")
    assert result.is_displayed()


@when('clicar no produto escolhido')
def click_product(context):
    product = context.driver.find_element(By.XPATH,
        "//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']").click()
    assert context.driver.find_element(By.XPATH, "//span[@id='productTitle']").is_displayed()


@when('clicar em adicionar ao carrinho')
def add_to_cart(context):
    context.driver.find_element(By.XPATH, "//input[@id='add-to-cart-button']").click()
    sleep(3)

    assert context.driver.find_element(By.XPATH,
        "//*[@class='a-size-medium-plus a-color-base sw-atc-text a-text-bold']").text == "Adicionado ao carrinho"

    try:
        modal = context.driver.find_element(By.XPATH, "//*[@class='a-popover-header-content']")
        if modal.is_displayed():
            # Fechar modal
            context.driver.find_element(By.XPATH, "//span[@class='a-button a-button-base abb-intl-decline']").click()

    except NoSuchElementException:
        print("Modal não exibido")


@then('produto vai para carrinho')
def product_go_to_cart(context):
    context.driver.find_element(By.XPATH, "//a[@href='/cart?ref_=sw_gtc']").click()

    assert context.driver.find_element(By.XPATH, "//h1[contains(text(), 'Carrinho de compras')]").is_displayed()
    sleep(3)

