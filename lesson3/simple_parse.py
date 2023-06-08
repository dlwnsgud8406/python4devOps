#!/usr/bin/env python3

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Echo your input') # 메시지와 함께 파서 객체 생성
    parser.add_argument('message', help='Message to echo') # 도움말 메시지와 위치 기반 명령 추가(--help , -h로 적용되네 이건)
    parser.add_argument('--twice', '-t', help='Do it twice', action = 'store_true') # 옵션 인수 추가, 옵션 인수에 불린 값 저장

    args = parser.parse_args() # 파서를 사용해 인수 파싱
    print(args.message) # 이름을 통해 인숫값에 접근. 옵션 인수의 이름에는 --가 제거되어 있음.
    if args.twice:
        print(args.message)
