from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

def funcToBeExecuted(email):
  option = Options()
  option.headless = False

  driver = webdriver.Chrome()
  
  driver.implicitly_wait(30)
  wait = WebDriverWait(driver, 20)

  driver.get('https://www.facebook.com/photo.php?fbid=663700417540504&set=a.105694383341113&type=3&eid=ARC9-IQulTUitAsKt0O8SKQ57ocr9VG-5Lhrxh1ljBvGHcNcPGTTDw-1ZC1wObSn9o7lSsQ_RYxRYi2U')

  # loginButton = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="mobile_login_bar"]/div[2]/a[2]')))
  # loginButton.click()

  # emailInput = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="m_login_email"]')))
  # emailInput.send_keys(f'{email}')

  # passwordInput = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="m_login_password"]')))
  # passwordInput.send_keys('ironman0552')
  # passwordInput.send_keys(Keys.ENTER)

  # count = 0

  # while count<=3750:
  #   sleep(5)

  #   campo_de_comentario = driver.find_element_by_xpath('//*[@id="composerInput"]')
  #   campo_de_comentario.send_keys('a')
  #   sleep(0.5)

  #   submitButton = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="comment_form_100003377617032_2703280489794512"]/div[1]/div[3]/button')))
  #   submitButton.click()

  #   count+=1


