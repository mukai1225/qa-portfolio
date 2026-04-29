from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# 成功テスト
driver.get("file:///C:/Users/sutor/OneDrive/Desktop/qa-selenium/login.html")

driver.find_element(By.ID, "email").send_keys("test@test.com")
driver.find_element(By.ID, "password").send_keys("1234")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(1)

result = driver.find_element(By.ID, "result").text
print("成功テスト:", result)
result = driver.find_element(By.ID, "result").text

if result == "ログイン成功":
    print("成功テスト OK")
else:
    print("成功テスト NG")
# リロード
driver.refresh()

# 失敗テスト
driver.find_element(By.ID, "email").send_keys("test@test.com")
driver.find_element(By.ID, "password").send_keys("9999")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(1)

result = driver.find_element(By.ID, "result").text
print("失敗テスト:", result)
result = driver.find_element(By.ID, "result").text

if result == "ログイン失敗":
    print("失敗テスト OK")
else:
    print("失敗テスト NG")
# リロード
driver.refresh()

# 空欄テスト
driver.find_element(By.ID, "email").send_keys("")
driver.find_element(By.ID, "password").send_keys("")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(1)

result = driver.find_element(By.ID, "result").text
print("空欄テスト:", result)

if result == "ログイン失敗":
    print("空欄テスト OK")
else:
    print("空欄テスト NG")

input("Enter押したら終了")