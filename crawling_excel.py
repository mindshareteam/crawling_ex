from bs4 import BeautifulSoup
import urllib.request
import re
import csv

url2 = "https://www.vms.or.kr/partspace/recruitView.do?seq={}"

with open('volunteerll_list_csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['제목', '활동기간', '활동분야', '봉사지역', '봉사장소', '봉사대상', 'ID'])

    def main():
        global n
        for n in range(312820, 330001):
            parser(url2.format(n))

    def parser(url2):
        source_code_from_URL = urllib.request.urlopen(url2)
        soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')

        title = str(soup.select('div.viewTitle > p.tit')) # 제목
        title = re.sub('<.+?>', '', title, 0).strip()

        obj = str(soup.select('#rightArea > div.con > div.bbs_view > div:nth-child(5) > dl:nth-child(1) > dd')) # 봉사대상
        obj = re.sub('<.+?>', '', obj, 0)

        place = str(soup.select('#rightArea > div.con > div.bbs_view > div:nth-child(4) > dl:nth-child(2) > dd')) # 봉사장소
        place = re.sub('<.+?>', '', place, 0)

        day = str(soup.select('#rightArea > div.con > div.bbs_view > div:nth-child(2) > dl:nth-child(1) > dd')) # 활동기간
        day = re.sub('<.+?>', '', day, 0)

        part = str(soup.select('#rightArea > div.con > div.bbs_view > div:nth-child(2) > dl:nth-child(2) > dd')) # 활동분야
        part = re.sub('<.+?>', '', part, 0)

        address = str(soup.select('#rightArea > div.con > div.bbs_view > div:nth-child(4) > dl:nth-child(1) > dd')) # 봉사지역
        address = re.sub('<.+?>', '', address, 0)

        writer.writerow([title, day, part, address, place, obj, n]) # 나오는 순서

    if __name__ == "__main__":
        main()
