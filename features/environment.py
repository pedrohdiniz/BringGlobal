from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from sys import platform



def before_all(context):
    context.url = context.config.userdata['url']
    context.pass_1 = context.config.userdata['passenger_1']
    context.pass_2 = context.config.userdata['passenger_2']
    context.pass_3 = context.config.userdata['passenger_3']
    context.departure = context.config.userdata['departure']
    context.destination = context.config.userdata['to']

def before_scenario(context, scenario):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option("prefs", {
        "intl.accept_languages": "pt-BR",
        "download.default_directory": "resources/",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True,
        "safebrowsing.enabled": True
    })
    # First driver is for windows and the second one is for ubuntu
    if platform == 'win32':
        context.driver = webdriver.Chrome(executable_path='features/resources/chromedriver.exe',
                                          chrome_options=chrome_options)
    else:
        context.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)




