from selenium import webdriver

my_driver = webdriver.Chrome(executable_path="C:/Users/Noam.Zaidman.NZAIDMAN-T490/Downloads/chromedriver_win32/chromedriver.exe")
my_driver.get("C:/Users/Noam.Zaidman.NZAIDMAN-T490/Downloads/tip_calc/tip_calc/index.html")
my_driver.find_element_by_id("billamt").send_keys("100")
my_driver.find_element_by_xpath("//*[@id=\"serviceQual\"]/option[3]").click()
my_driver.find_element_by_id("peopleamt").send_keys("5")
my_driver.find_element_by_id("calculate").click()
expected = 4.00
actual = my_driver.find_element_by_id("tip").text
assert expected == actual

