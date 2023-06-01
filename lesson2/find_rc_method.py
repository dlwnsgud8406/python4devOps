import os

def find_rc(rc_name=".examplerc"):
    # Env 변수 확인
    var_name = "EXAMPLERC_DIR"
    if var_name in os.environ:
        var_path = os.path.join(f"${var_name}", rc_name)
        config_path = os.path.expandvars(var_path)
        print(f"Checking {config_path}")
        if os.path.exists(config_path):
            return config_path

    # 현재 작업 중인 디렉터리 확인
    config_path = os.path.join(os.getcwd(), rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    # 사용자 홈 디렉터리 확인
    home_dir = os.path.expanduser("~/")
    config_path = os.path.join(home_dir, rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    # 이 파일의 디렉터리 확인
    file_path = os.path.abspath(__file__)
    parent_path = os.path.dirname(file_path)
    config_path = os.path.join(parent_path, rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    print(f"File {rc_name} has not been found")
