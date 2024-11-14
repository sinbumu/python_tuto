from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--headless")        # GUI 없이 실행
chrome_options.add_argument("--no-sandbox")      
chrome_options.add_argument("--disable-dev-shm-usage")

# WebDriver 경로 설정 및 드라이버 초기화
chrome_service = Service('/opt/homebrew/bin/chromedriver')  # ChromeDriver 경로
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# 나무위키 페이지로 이동
url = "https://namu.wiki/w/%EC%A0%95%EC%83%81%ED%99%94(%EC%9D%B8%ED%84%B0%EB%84%B7%20%EB%B0%88)"
driver.get(url)

# 페이지가 모두 로드될 때까지 잠시 대기
time.sleep(5)

# 페이지 소스를 BeautifulSoup에 전달하여 파싱
soup = BeautifulSoup(driver.page_source, "html.parser")

# 텍스트만 추출하여 파일에 저장
with open("namuwiki_text.txt", "w", encoding="utf-8") as file:
    for paragraph in soup.find_all("p"):
        text = paragraph.get_text()
        file.write(text + "\n")

# 드라이버 종료
driver.quit()
