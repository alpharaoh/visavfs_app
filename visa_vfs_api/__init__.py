import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chr_options = Options()
chr_options.add_experimental_option("detach", True)
# chr_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chr_options)
