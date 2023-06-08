import os

print(os.getcwd()) # 현재 작업 중인 디렉터리 구하기

os.chdir('/tmp') # 디렉터리 이동하기
print(os.getcwd())

os.environ.get('LOGLEVEL') # loglevel 환경변수 갖고오기

os.environ['LOGLEVEL'] = 'DEBUG' # 환경변수 설정.

print(os.environ.get('LOGLEVEL'))

print(os.getlogin()) # 해당 프로세스를 생성한 터미널에 로그인한 사용자
