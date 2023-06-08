import sys

print(sys.byteorder) # 현재 아키텍처의 바이트 순서

print(sys.getsizeof(1)) # 파이썬 객체의 크기

print(sys.platform) # 기반 OS에 따라 다르게 동작하도록 하고 싶을때

if sys.version_info.major < 3: # 파이썬 정수 버전
    print("You need to update your Python verison")
elif sys.version_info.minor < 7: # 파이썬 소수 버전
    print("You are not running the latest version of Python")
else:
    print("All is good.")

