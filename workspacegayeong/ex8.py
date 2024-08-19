from selenium   import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://time.navyism.com/?host=naver.com")
driver.implicitly_wait(0.5)
while True:
    message=driver.find_element(by=By.ID,value="time_area")
    servertime=message.text
    print(servertime)
    # 끝나는 조건을 작성해요, if, break 사용
    if servertime=="2024년 04월 01일 12시 15분 00초":
        break
print("시간 초과")


time.sleep(10)