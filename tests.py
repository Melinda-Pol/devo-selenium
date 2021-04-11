import os, unittest
from credentials import  email, password
from selenium import webdriver
from locators import LoginPage, HomePage, TimeZone
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

chrome_path = '###ADD YOUR CHROME DRIVER PATH HERE###'

class UIautomation (unittest.TestCase):

    ##COMMON TESTING ACTIONS
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--kiosk")
        #chrome_options.add_argument('headless')
        #chrome_options.add_argument('window-size=1920x1080')
        path_chrome = os.path.normpath(chrome_path)
        self.driver = webdriver.Chrome(options=chrome_options, executable_path= path_chrome)

    def click_button(self,loc):
        elem = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc))
        ActionChains(self.driver).move_to_element(elem).perform()
        elem.click()

    def send_keys(self,loc,keys):
        elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
        ActionChains(self.driver).move_to_element(elem).perform()
        elem.send_keys(keys)

    def enter_keys(self,loc,keys):
        elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
        ActionChains(self.driver).move_to_element(elem).perform()
        elem.send_keys(keys)
        elem.send_keys(Keys.ENTER)

    def log_in(self):
        self.driver.get("https://eu.devo.com/login")
        # Username
        self.send_keys(LoginPage.EMAIL,email)
        # Password
        self.send_keys(LoginPage.PASSWORD,password)
        # Sign-in button
        self.click_button(LoginPage.SIGIN_BUTTON) #Sign-in button
        # Pop-up button
        self.click_button(HomePage.POPUP)
        assert self.driver.current_url == "https://eu.devo.com/welcome"
        # Main-logo
        self.click_button(HomePage.MAINLOGO)

    ##TEST CASES
    def test_TC001_login(self):
        self.log_in()
        # Test1-Log-in
        avatarname = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePage.AVATARNAME))
        ActionChains(self.driver).move_to_element(avatarname).perform()
        assert avatarname.text == email
        print("test_TC001_login: PASS")

    def test_TC002_logout(self):
        self.log_in()
        # Test2-Log-out
        self.click_button(HomePage.LOGOUT)
        self.driver.implicitly_wait(20)
        assert self.driver.current_url == "https://eu.devo.com/login"
        print("test_TC002_logout: PASS")

    def test_TC003_timezone(self):
        self.log_in()
        #Timezone icon
        self.click_button(TimeZone.DROPTZONE) #Timezone icon
        self.click_button(TimeZone.CHECKTZONE) #Checkbox
        self.click_button(TimeZone.TEXTBOX) #TEXTBOX
        self.driver.implicitly_wait(20)
        self.enter_keys(TimeZone.INPUTTZONE,'GMT') #input_tzone
        self.click_button(TimeZone.CHECKUZONE) #checkbox_uzone
        self.click_button(TimeZone.SAVEBUTTON) #save_button
        self.click_button(HomePage.POPUP) #Pop-up button
        assert self.driver.current_url == "https://eu.devo.com/welcome"
        self.click_button(TimeZone.DROPTZONE) #Timezone
        self.click_button(TimeZone.TEXTBOX) #Textbox
        print("test_TC003_timezone:PASS")

    #Close driver
    def tearDown(self):
        self.driver.close()