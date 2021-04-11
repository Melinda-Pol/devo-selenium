# devo-selenium
UI automation with python and selenium.

## Installation
[Python Version: 3.8.8]

Use the package manager [pip] to install the following libraries:
* selenium
* html-testRunner


## Previous setup

Before running the project, three essential things needs to be set up:

1. Download ChromeDriver(https://chromedriver.chromium.org/) and add it the PATH at the variable named: **chrome_path** inside file *tests.py*, i.e:
```
chrome_path = 'C:/Users/User/Desktop/webdriver/chromedriver.exe'
```

2. Add your credentials at: *credentials.py* file at the project root and insert credentials, i.e:
   
```
email ='youremail@youremail.com'
password ='yourpassword'
```

## Usage
To run the tests from terminal window:

```
python test_uiexec.py
```

## Future improvements

* Use BDD with behave library.
* Implement a multiple browser tests using pytest framework.
