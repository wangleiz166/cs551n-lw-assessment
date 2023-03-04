from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# Use the chrome driver specific to your version of Chrome browser and put it in ./driver directory
CHROME_DRIVER = os.path.join(os.path.join(os.path.dirname(__file__), 'driver'), 'chromedriver')

chrome_options = Options()
# comment out the line below if you want to see the browser launch for tests
# possibly add time.sleep() if required
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-proxy-server')
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")

def before_all(context):
    context.browser = webdriver.Chrome(executable_path=CHROME_DRIVER, options=chrome_options)

def after_all(context):
    context.browser.quit()
