import time
from features.utility.UtilityClass import UtilityClass
def before_scenario(context, driver):
    UtilityClass.launch_browser(context)
    time.sleep(5)
    UtilityClass.launch_app(context)
    time.sleep(5)
    UtilityClass.Maximize_Window(context)
    time.sleep(5)
def after_scenario(context, driver):
    time.sleep(5)
    UtilityClass.close_browser(context)
