from selenium.webdriver.common.by import By

class LoginPage:
    EMAIL = (By.ID,'loginEmail')
    PASSWORD = (By.ID,'loginPass')
    SIGIN_BUTTON = (By.ID,"btSignIn")

class HomePage:
    POPUP=(By.XPATH,'//*[@id="lt-landing"]/div/button')
    MAINLOGO = (By.ID,'lt-main-logo')
    AVATARNAME = (By.XPATH,'//*[@id="avatar-name"]')
    LOGOUT=(By.XPATH,'//*[@id="logout-button"]/a/span')

class TimeZone:
    DROPTZONE = (By.XPATH,'//*[@id="main-navigation-inner"]/ul/li[1]/div/p')
    CHECKTZONE = (By.XPATH,'//*[@id="time-zone-picker"]/div[1]/div/label/input')
    TEXTBOX = (By.XPATH,'//*[@id="time-zone-picker"]/div[1]/span/span[1]/span')
    INPUTTZONE = (By.XPATH,'//*[@id="lt-container"]/span/span/span[1]/input')
    CHECKUZONE = (By.XPATH,'//*[@id="time-zone-picker"]/div[3]/div[2]/label/input')
    SAVEBUTTON = (By.XPATH,'//*[@id="time-zone-picker-modal"]/div[2]/button[2]')
