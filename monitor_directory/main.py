import os
import time
import re

#담당자 연락처
email = 'defendersunbin98@naver.com'

#1. Directory 내부의 파일 목록을 가져오기
file_path = os.listdir('./monitor_directory')

#2. Directory 폴더가 없을 경우 자동으로 생성
if not os.path.exists('./monitor_directory'):
    os.mkdir('./monitor_directory')

#3. 초기 파일의 목록을 set으로 저장
before = set(os.listdir('./monitor_directory'))
print(f'초기 파일 목록: {before}')

#4. 현재 파일 목록 가져오기 및 directory 1초 단위로 check (while문으로 반복 활용)
while True:
    after = set(os.listdir('./monitor_directory'))

    #새로운 파일을 감지
    new_files = after - before

    #새 파일 감지시 출력 코드 정리
    for file in new_files:
        print(f'새 파일 감지: {file}')
        
        #파일 확장자 리스트로 정리
        name, ext = os.path.splitext(file)
        text_extensions = ['.txt', '.py', '.js', '.class', '.sql', '.html']
        danger_extensions = ['.py', '.js', '.class', '.sql']

        #monitory_directory 폴더에 지정해둔 파일 확장자 파일이 추가되었을 경우, 파일 열어 확인
        if ext in text_extensions:
            with open('./monitor_directory/' + file, 'r') as f:
                content = f.read()

        #정규식으로 민감 정보 탐지하기
        if ext in danger_extensions:
            print(f'(주의 파일) {file}은 보안 위험 파일입니다!')

        #각 파일에 따른 정보 출력    
        if ext in text_extensions:
            with open('./monitor_directory/' + file, 'r') as f:
                content = f.read()
                if re.search(r'(#|//).+', content):
                    print(f"[주석 발견] {file}")
                if re.search(r'\w+@\w+\.\w+', content):
                    print(f"[이메일 발견] {file}")
                if re.search(r'(SELECT|INSERT|UPDATE|DELETE|FROM|WHERE|GROUP BY|HAVING BY|ORDER BY|TRUNCATE)', content):
                    print(f"[SQL 발견] {file}")

    #다음 루프를 위해 before update
    before = after

    #1초 간격으로 상황 업데이트
    time.sleep(1)