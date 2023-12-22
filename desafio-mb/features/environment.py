from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.amazon.com.br/")

def before_scenario(context, scenario):
    context.driver.maximize_window()

def before_step(context, step):
    context.driver.implicitly_wait(2)