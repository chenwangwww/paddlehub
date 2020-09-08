from selenium import webdriver
driver = webdriver.PhantomJS(executable_path=r'C:/phantomjs-2.1.1/bin/phantomjs.exe')
driver.get('http://www.baidu.com')
print(driver.page_source)