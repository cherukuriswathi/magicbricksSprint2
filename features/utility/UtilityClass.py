from selenium import webdriver
from features.utility.ConfigClass import ConfigClass
class UtilityClass:
    def __init__(self, driver):
        self.driver = driver

    def launch_browser(self):
        self.driver = webdriver.Chrome(ConfigClass.filepath)

    def launch_app(self):
        self.driver.get(ConfigClass.url)

    def close_browser(self):
        self.driver.quit()

    def Maximize_Window(self):
        self.driver.maximize_window()