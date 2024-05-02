import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://www.semanticscholar.org/")


search = driver.find_element(By.XPATH, "//input[@type='search']")
search.send_keys('morocco' + Keys.ENTER)


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='link-button--show-visited']")))


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@data-test-id='author-list']")))
search_authors = driver.find_elements(By.XPATH, "//span[@data-test-id='author-list']")
print(len(search_authors))

author_links_list = driver.find_elements(By.XPATH, ".//a[contains(@class,'cl-paper-authors__author-box') and contains(@class, 'notranslate')]")

authors_list = []

for i in range(len(author_links_list)):

    author_links_list = driver.find_elements(By.XPATH,
                                             ".//a[contains(@class,'cl-paper-authors__author-box') and contains(@class, 'notranslate')]")


    author_link = author_links_list[i]

    author_link.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@data-test-id='author-page-tabs__co-authors']")))
    co_authors_link = driver.find_element(By.XPATH, "//a[@data-test-id='author-page-tabs__co-authors']")
    co_authors_link.click()

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='author-influence-page__author-list__item']")))

    author_name = driver.find_element(By.XPATH, "//h1[@data-test-id='author-name']")
    authors_list.append(author_name.text)

    co_authors_list = []

    all_authors = driver.find_elements(By.XPATH, "//h3[@class='author-row__headline__name']")
    for co_author in all_authors:
        co_authors_list.append(co_author.text)

    authors_list.append(co_authors_list)

    print(authors_list)

    driver.back()  

time.sleep(10)
driver.quit()

