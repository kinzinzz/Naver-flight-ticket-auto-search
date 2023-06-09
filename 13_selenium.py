from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼
elem = browser.find_element(By.CLASS_NAME, "link_login")
elem.click()

# 3. id, pw 입력
browser.find_element(By.ID, "id").send_keys("asdaddsa")
browser.find_element(By.ID, "pw").send_keys("asdasdasasdas")

# 4. 로그인 버튼 클릭
browser.find_element(By.ID, "log.login").click() 
time.sleep(2)

# 5. 로그인 실패시 id를 새로 입력
browser.find_element(By.ID, "id").clear()
browser.find_element(By.ID, "id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
browser.quit() # browser.close():현재 탭만 종료

time.sleep(10)