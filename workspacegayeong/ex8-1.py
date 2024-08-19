from selenium   import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("https://www.naver.com")
driver.implicitly_wait(0.5)
query_text=f"제주황사지수"
search_box=driver.find_element(by=By.CSS_SELECTOR,value="#query")
search_box.send_keys(query_text)
driver.implicitly_wait(0.5)
search_button=driver.find_element(by=By.CSS_SELECTOR,value="#search-btn")

search_button.click()
temp_div=driver.find_element(by=By.CSS_SELECTOR,value="#main_pack > section.sc_new._atmospheric_environment > div > div.air_environment_wrap > div > div:nth-child(3) > div.main_box > div.map_area > span.ct14.lv1._local > span.value")
print("20602김가영")
print(temp_div.text)
time.sleep(10)