from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By



class BuyvsRentClass_1:
    def __init__(self,driver):
        self.driver = driver
        self.mbadvice= "(//a[@href ='javascript:void(0)'])[18]"
        self.buyvsrent="//*[@id='commercialIndex']/header/section[2]/div/ul/li[6]/div/div/div[2]/ul/li[6]/a"
        self.taxButton="//*[text()='Tax']"
        self.Dragger="(//*[@class='ui-slider-range ui-widget-header ui-corner-all ui-slider-range-max'])[10]"
        self.MyactivityHover="//*[@class='fo_14px font-type-4 c_white']"
        self.LoginButton="//*[text()='Login']"
        self.propertybutton="//*[text()='Property']"
        self.clickherelink="(//div[@class='ExceedValues'])[2]/a"
        self.AdviceLink="//span[text()='Advice']"
        self.HomeLink="//*[text()='Home']"
        self.explorebutton="//*[@id='exploreSection']/div/div[2]/div[2]/div[2]/input"
    def mouse_hover(self):
        mousehover = self.driver.find_element(By.XPATH, self.mbadvice)
        action = ActionChains(self.driver)
        action.move_to_element(mousehover)
        action.perform()
    def buy_rent_click(self):
        buyrent=self.driver.find_element(By.XPATH,self.buyvsrent)
        buyrent.click()
        print("Parent window title: " + self.driver.title)
        # get current window handle
        p = self.driver.current_window_handle
        # get first child window
        chwd = self.driver.window_handles
        for w in chwd:
        # switch focus to child window
            if (w != p):
                self.driver.switch_to.window(w)
           # continue
    def Tax_Button(self):
        taxbutton= self.driver.find_element(By.XPATH, self.taxButton)
        taxbutton.click()
    def dragger_click(self):
        slider = self.driver.find_element(By.XPATH, self.Dragger)
        action = ActionChains(self.driver)
        #Performing sliding operation by using(X-Y coordinates)
        action.drag_and_drop_by_offset(slider, 2, 0)
        action.perform()
        soapRadioButton =self.driver.find_element(By.XPATH, "(//input[@type='radio'])[7]")
        soapRadioButton.click()
        print(soapRadioButton.is_selected())
        soapRadioButton = self.driver.find_element(By.XPATH, "(//input[@type='radio'])[9]")
        soapRadioButton.click()
        print(soapRadioButton.is_selected())
#---------------------------------------------------------------------------------------------------------------
    def Hover_to_Myactivity(self):
        myactivity = self.driver.find_element(By.XPATH, self.MyactivityHover)
        action = ActionChains(self.driver)
        action.move_to_element(myactivity)
        action.perform()
    def Login_Click(self):
        login=self.driver.find_element(By.XPATH,self.LoginButton)
        login.click()
        print("Parent window title: " + self.driver.title)
        # get current window handle
        p = self.driver.current_window_handle
        # get first child window
        chwd = self.driver.window_handles
        for w in chwd:
            # switch focus to child window
            if (w != p):
                self.driver.switch_to.window(w)
    def Property_Button(self):
        self.driver.refresh()
        propertyButton=self.driver.find_element(By.XPATH, self.propertybutton)
        propertyButton.click()
        link=self.driver.find_element(By.XPATH, self.clickherelink)
        link.click()
#----------------------------------------------------------------------------------------------
    def AdviceLink_click(self):
        Advicelink=self.driver.find_element(By.XPATH, self.AdviceLink)
        Advicelink.click()
        print("Parent window title: " + self.driver.title)
        # get current window handle
        p = self.driver.current_window_handle
        # get first child window
        chwd = self.driver.window_handles
        for w in chwd:
            # switch focus to child window
            if (w != p):
                self.driver.switch_to.window(w)

#---------------------------------------------------------------------------------------------------------------------
    def Home_link(self):
        homelink=self.driver.find_element(By.XPATH, self.HomeLink)
        homelink.click()
        print("Parent window title: " + self.driver.title)
        # get current window handle
        p = self.driver.current_window_handle
        # get first child window
        chwd = self.driver.window_handles
        for w in chwd:
            # switch focus to child window
            if (w != p):
                self.driver.switch_to.window(w)

