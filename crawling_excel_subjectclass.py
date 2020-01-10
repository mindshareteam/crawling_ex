import django
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import HTTPError
import re
import csv
import pandas
import os
import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

noin = ['어르신', "노인", "치매", "독거", "소외", "노년", "경로", "요양", "할머니", "할아버지"]
handicap = ['장애', '장애인', '장애우', '발달장애', '시각장애', '뇌성마비', '지적장애', '자폐', '정신장애', '병변', '농아인',
            '농아', '지체장애', '지체', '휠체어', '언어장애', '다운증후군', '인지장애', '청각장애', '난청', '정신장애', '중증장애']
kids = ['아동', '영유아', '초등', '초등생', '초등학교', '초등학생', '어린이', '유아', '미취학',
        '저학년', '아이', '유치원', '영아', '육아', '학령기', '아기', '소아', '고학년', '원아']
oldkids = ['고등학생', '중학생', '중등', '중학교', '고등학교', '고교생', '중등생', '고등생', '가출']
sick = ['한부모', '미혼모', '홀몸', '다문화', '외국인', '조손', '입양']

office = ['행정', '사무', '서류', '번역', '통역', '우편물', '영상', '조사', '어린이재단',
          '자선냄비', '월드비전', '기아', '전달', '기부', '모금', '후원', '사업', '운영', '개선', '제작']
study = ['교육', '교실', '학교', '학습', '학습지도', '멘토링', '멘토', '만들기', '지도', '영어', '방과후', '선생님', '어린이', '재능기부', '미술', '어린이날', '재능', '유급', '대학',
         '아카데미', '여름방학', '교사', '고등학생', '특강', '책', '독서', '취업', '그림', '스쿨', '검정고시', '수업', '강사', '수학', '체육', '쓰기', '그리기', '평생교육', '인식', '한글', '육아', '선물']
food = ['식당', '급식', '배식', '도시락', '밑반찬', '김장', '요리', '식품', '김치', '조리', '설거지']
out = ['나눔', '축제', '지역', '대회', '재단', '협회', '홍보', '시립', '박람회', '인솔', '운동', '콘서트', '경로당', '방문', '차량', '여가', '마라톤', '전시회', '설문조사', '여행', '음악회', '주거', '촬영',
       '체육대회', '아트', '영화', '놀이터', '벽화', '인형극', '운동회', '걷기', '공연', '동아리', '수련', '여름캠프', '편지', '스탭', '나눔', '나들이', '문화', '바자회', '배달', '안내', '부스', '미용', '캠프', '동행']
clean = ['정리', '보호', '환경', '청소', '미화', '정화', '세척', '공원']
healing = ['건강', '헌혈', '병원', '재활', '생명', '회복', '정신건강', '검진', '치료', '말벗', '진료', '백혈병', '시각장애', '의료',
           '종합병원', '요양', '목욕', '도우미', '노인', '경로', '장애', '발달장애', '치매', '시각장애인', '상담', '케어', '실버', '독거', '예방']


url2 = "https://www.vms.or.kr/partspace/recruitView.do?seq={}"

with open('volunteerll_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['1', '2', '3', '4', '5', '6',
                     '7', '8', '9', '10', '11', '12', '13'])

    def main():
        global n
        for n in range(333548, 333001, -1):
            parser(url2.format(n))

    def parser(url2):
        source_code_from_URL = urllib.request.urlopen(url2)
        soup = BeautifulSoup(source_code_from_URL, 'lxml',
                             from_encoding='utf-8')

        title = str(soup.select('div.viewTitle > p.tit'))  # 제목
        title = re.sub('<.+?>', '', title, 0).strip()
        title = re.sub(r'[\[\]]', '', title, 0)

        obj = str(soup.select(
            '#rightArea > div.con > div.bbs_view > div:nth-child(5) > dl:nth-child(1) > dd'))  # 봉사대상
        obj = re.sub('<.+?>', '', obj, 0)
        obj = re.sub(r'[\[\]]', '', obj, 0)

        place = str(soup.select(
            '#rightArea > div.con > div.bbs_view > div:nth-child(4) > dl:nth-child(2) > dd'))  # 봉사장소
        place = re.sub('<.+?>', '', place, 0)
        place = re.sub(r'[\[\]]', '', place, 0)

        day = str(soup.select(
            '#rightArea > div.con > div.bbs_view > div:nth-child(2) > dl:nth-child(1) > dd'))  # 활동기간
        day = re.sub('<.+?>', '', day, 0)
        day = re.sub(r'[\[\]]', '', day, 0)
        daylist = day.split(' ~ ')
        try:
            starttime = daylist[0]
            endtime = daylist[1]
        except IndexError:
            starttime = ""
            endtime = ""

        part = str(soup.select(
            '#rightArea > div.con > div.bbs_view > div:nth-child(2) > dl:nth-child(2) > dd'))  # 활동분야
        part = re.sub('<.+?>', '', part, 0)
        part = re.sub(r'[\[\]-]', '', part, 0).strip()

        address = str(soup.select(
            '#rightArea > div.con > div.bbs_view > div:nth-child(4) > dl:nth-child(1) > dd'))  # 봉사지역
        address = re.sub('<.+?>', '', address, 0)
        address = re.sub(r'[\[\]]', '', address, 0)
        address = address.strip()
        address = address[2:]
        address = address.strip()
        addresslist = address.split(' ')
        try:
            city = addresslist[0]
            town = addresslist[1]
        except IndexError:
            town = ""
        print(city+" "+town)
        subjectclass = 0
        if subjectclass == 0:
            for item in noin:
                if obj.find(item) != -1:
                    subjectclass = 1
                    break
                else:
                    subjectclass = 0

        if subjectclass == 0:
            for item in handicap:
                if obj.find(item) != -1:
                    subjectclass = 2
                    break
                else:
                    subjectclass = 0

        if subjectclass == 0:
            for item in kids:
                if obj.find(item) != -1:
                    subjectclass = 3
                    break
                else:
                    subjectclass = 0

        if subjectclass == 0:
            for item in oldkids:
                if obj.find(item) != -1:
                    subjectclass = 4
                    break
                else:
                    subjectclass = 0

        if subjectclass == 0:
            for item in sick:
                if obj.find(item) != -1:
                    subjectclass = 5
                    break
                else:
                    subjectclass = 0

        activityclass = 0
        if activityclass == 0:
            for item2 in office:
                if title.find(item2) != -1:
                    activityclass = 1
                    break
                else:
                    activityclass = 0

        if activityclass == 0:
            for item2 in study:
                if title.find(item2) != -1:
                    activityclass = 2
                    break
                else:
                    activityclass = 0

        if activityclass == 0:
            for item2 in food:
                if title.find(item2) != -1:
                    activityclass = 3
                    break
                else:
                    activityclass = 0

        if activityclass == 0:
            for item2 in out:
                if title.find(item2) != -1:
                    activityclass = 4
                    break
                else:
                    activityclass = 0

        if activityclass == 0:
            for item2 in clean:
                if title.find(item2) != -1:
                    activityclass = 5
                    break
                else:
                    activityclass = 0

        if activityclass == 0:
            for item2 in healing:
                if title.find(item2) != -1:
                    activityclass = 6
                    break
                else:
                    activityclass = 0

        writer.writerow([title, day, starttime, endtime, part, address, city,
                         town, place, obj, subjectclass, activityclass, n])  # 나오는 순서

    if __name__ == "__main__":
        main()