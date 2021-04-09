import os, unittest, requests
from credentials import  email, password
from selenium import webdriver
from locators import LoginPage, HomePage, TimeZone
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

chrome_path = '###YOUR CHROMEDRIVER PATH HERE###'

class UIautomation (unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        #chrome_options.add_argument("--kiosk")
        chrome_options.add_argument('headless')
        #chrome_options.add_argument('window-size=1920x1080')
        path_chrome = os.path.normpath(chrome_path)
        self.driver = webdriver.Chrome(options=chrome_options, executable_path= path_chrome)

    def test_TC001_TC002_login(self):
        self.driver.get("https://eu.devo.com/login")
        # Username
        inputusername = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.EMAIL))
        ActionChains(self.driver).move_to_element(inputusername).perform()
        inputusername.send_keys(email)
        # Password
        inputpassword = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.PASSWORD))
        ActionChains(self.driver).move_to_element(inputpassword).perform()
        inputpassword.send_keys(password)
        # Sign-in button
        signin_but = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.SIGIN_BUTTON))
        ActionChains(self.driver).move_to_element(signin_but).perform()
        signin_but.click()
        # Pop-up button
        close_popup = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(HomePage.POPUP))
        ActionChains(self.driver).move_to_element(close_popup).perform()
        close_popup.click()
        # Test1-Log-in
        assert self.driver.current_url == "https://eu.devo.com/welcome"
        # Main-logo
        main_navigation = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePage.MAINLOGO))
        ActionChains(self.driver).move_to_element(main_navigation).perform()
        main_navigation.click()
        # Avatar name
        avatarname = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePage.AVATARNAME))
        ActionChains(self.driver).move_to_element(avatarname).perform()
        assert avatarname.text == email
        print("test_TC001_login: PASS")
        # Test2-Log-out
        logout = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePage.LOGOUT))
        ActionChains(self.driver).move_to_element(logout).perform()
        logout.click()
        self.driver.implicitly_wait(20)
        assert  self.driver.current_url == "https://eu.devo.com/login"
        print("test_TC002_logout: PASS")

    def test_TC003_timezone(self):
        self.driver.get("https://eu.devo.com/login")
        # Username
        inputusername = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.EMAIL))
        ActionChains(self.driver).move_to_element(inputusername).perform()
        inputusername.send_keys(email)
        # Password
        inputpassword = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.PASSWORD))
        ActionChains(self.driver).move_to_element(inputpassword).perform()
        inputpassword.send_keys(password)
        # Sign-in button
        signin_but = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.SIGIN_BUTTON))
        ActionChains(self.driver).move_to_element(signin_but).perform()
        signin_but.click()
        # Pop-up button
        close_popup = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(HomePage.POPUP))
        ActionChains(self.driver).move_to_element(close_popup).perform()
        close_popup.click()
        assert self.driver.current_url == "https://eu.devo.com/welcome"
        # Main-logo
        main_navigation = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePage.MAINLOGO))
        ActionChains(self.driver).move_to_element(main_navigation).perform()
        main_navigation.click()
        #Timezone icon
        drop_tzone = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(TimeZone.DROPTZONE))
        ActionChains(self.driver).move_to_element(drop_tzone).perform()
        drop_tzone.click()
        #Checkbox
        check_tzone = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(TimeZone.CHECKTZONE))
        ActionChains(self.driver).move_to_element(check_tzone).perform()
        check_tzone.click()
        self.driver.implicitly_wait(20)
        #textbox
        drop_textbox = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(TimeZone.TEXTBOX))
        ActionChains(self.driver).move_to_element((drop_textbox)).perform()
        drop_textbox.click()
        #input_tzone
        input_tzone = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(TimeZone.INPUTTZONE))
        ActionChains(self.driver).move_to_element((input_tzone)).perform()
        input_tzone.send_keys('GMT')
        input_tzone.send_keys(Keys.ENTER)
        #checkbox_uzone
        check_uzone =WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(TimeZone.CHECKUZONE))
        ActionChains(self.driver).move_to_element(check_uzone).perform()
        check_uzone.click()
        #save_button
        save_button = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(TimeZone.SAVEBUTTON))
        ActionChains(self.driver).move_to_element(save_button).perform()
        save_button.click()
        # Pop-up button
        close_popup = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(HomePage.POPUP))
        ActionChains(self.driver).move_to_element(close_popup).perform()
        close_popup.click()
        assert self.driver.current_url == "https://eu.devo.com/welcome"
        drop_tzone = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(TimeZone.DROPTZONE))
        ActionChains(self.driver).move_to_element(drop_tzone).perform()
        drop_tzone.click()
        drop_textbox = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(TimeZone.TEXTBOX))
        ActionChains(self.driver).move_to_element((drop_textbox)).perform()
        drop_textbox.click()
        print("test_TC003_timezone:PASS")

    def tearDown(self):
        self.driver.close()