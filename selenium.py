from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\kangs\Downloads\chromedriver_win32\chromedriver.exe")

driver.get('https://1365.go.kr/vols/P9210/partcptn/timeCptn.do')

crawling = 0

while crawling < 3:

    crawling = crawling + 1

    for page in range(3,13):
        li = driver.find_elements_by_css_selector('#content > div.content_view > div > div.board_list.data_middle > ul > li > a > dl > dt')

        for title in li:
            print(title.text)

        driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[6]/div/div/div/a[%s]' %page ).click()