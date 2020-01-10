from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Users\kangs\Downloads\chromedriver_win32\chromedriver.exe")

driver.get('https://1365.go.kr/vols/P9210/partcptn/timeCptn.do')

crawling = 0

while crawling < 56: # 544페이지까지 크롤링 ---------4라면 30페이지까지 크롤링 ------------5라면 40페이지까지 크롤링

    crawling += 1

    for pages in range(3,13): # 1페이지 2페이지 넘어가기

        for page in range(1,11): # 각각의 봉사활동 페이지
            driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[5]/ul/li[%s]/a/dl/dt' %page).click()

            li = driver.find_elements_by_css_selector('#content > div.content_view > div > div.board_view.type2 > h3')

            ol = driver.find_elements_by_css_selector('#content > div.content_view > div > div.board_view.type2 > div.board_data.type2 > div:nth-child(6) > dl:nth-child(2) > dd')

            for title in li:
                print(title.text)

            for person in ol:
                print(person.text)

            driver.back()
            #time.sleep(2)

        driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[6]/div/div/div/a[%s]' %pages ).click()