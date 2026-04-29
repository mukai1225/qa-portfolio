from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def run_test(email, password, test_name, expected):
    driver.get("file:///C:/Users/sutor/OneDrive/Desktop/qa-selenium/login.html")

    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(1)

    result = driver.find_element(By.ID, "result").text
    print(test_name + ":", result)

    if result == expected:
        print(test_name + " OK")
    else:
        print(test_name + " NG")

# テスト実行
run_test("test@test.com", "1234", "成功テスト", "ログイン成功")
time.sleep(1)
run_test("test@test.com", "9999", "失敗テスト", "ログイン失敗")
time.sleep(1)
run_test("", "", "空欄テスト", "ログイン失敗")

input("Enter押したら終了")
driver.quit()
