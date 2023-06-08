import subprocess

cp = subprocess.run(['ls', '-l'], capture_output=True, universal_newlines=True) # 셸 명령이나 명령줄 소프트웨어 실행

print(cp.stdout)

cp = subprocess.run(['ls', '/doesnotexist'], capture_output=True, universal_newlines=True, check=True)
print(cp)
