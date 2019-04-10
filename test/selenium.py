import pymysql
from openpyxl import Workbook
from datetime import datetime
from selenium import webdriver

dt = datetime.now()
# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='55555',
                       db='how' , port = 3306)

# Connection 으로부터 Cursor 생성
curs = conn.cursor()
wb = Workbook()
ws = wb.active

ws.append(('dept_no','dept_nm'))
# SQL문 실행
sql = "select * from dept"
curs.execute(sql)

# 데이터 Fetch
rows = curs.fetchall()
print(rows)  # 전체 rows

for row in rows:
    ws.append(row)
#데이터 저장
wb.save('/Users/og/Desktop/test'+dt.strftime("%Y%m%d")+'.xlsx')

# Connection 닫기
conn.close()
wb.close()
"""
# 셀레니움연결
driver = webdriver.Chrome('/Program Files/chromedriver')
driver.implicitly_wait(5)
driver.get('https://ancient-headland-21698.herokuapp.com/login')
driver.find_element_by_name('email').send_keys('admin123@naver.com')
driver.find_element_by_name('password').send_keys('admin123')
driver.find_element_by_xpath('/html/body/main/div/form/input[3]').click()
driver.get('https://ancient-headland-21698.herokuapp.com/videos/upload')

# UPLOAD
driver.find_element_by_xpath('//*[@id="file"]').send_keys('C:/Users/og/Desktop/test.mp4')
driver.find_element_by_name('title').send_keys('자동업로드.')
driver.find_element_by_xpath('/html/body/main/div/form/textarea').send_keys('딘라이브')
driver.find_element_by_xpath('/html/body/main/div/form/input[2]').click()"""