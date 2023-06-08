#!/usr/bin/env python3

import sys

def say_it(greeting, target):
    message = f'{greeting} {target}'
    print(message)

if __name__ =='__main__': # 현재 명령 실행중인지 확인
    greeting = 'Hello' # 기본값 설정
    target = 'Joe'

    if '--help' in sys.argv: # 입력받는 문자열 중 --help가 있는지 확인
        help_message = f"Usage: {sys.argv[0]} --name <NAME> --greeting <GREETING>"
        print(help_message)
        sys.exit() # 도움말 출력 후 프로그램 종료

    if '--name' in sys.argv:
        name_index = sys.argv.index('--name') + 1 # 플래그 뒤에 이어지는 값의 위치 파악
        if name_index < len(sys.argv): # 인수 리스트의 길이 테스트. 플래그 뒤에 값이 없다면 길이가 부족한것으로 나타남
            name = sys.argv[name_index]

    if '--greeting' in sys.argv:
        greeting_index = sys.argv.index('--greeting') + 1
        if greeting_index < len(sys.argv):
            greeting = sys.argv[greeting_index]

    say_it(greeting, name)
