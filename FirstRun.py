# 该脚本适用于Windows，Ubuntu系统，为其他脚本搭建运行环境。
import os
import platform
# 判断Windows还是Ubuntu，返回系统名称。
def decide_system():
    system = platform.system().lower()
    if system == "Linux".lower():
        release = os.popen("lsb_release -a").read().lower()
        if "ubuntu" in release:
            return "Ubuntu"
        else:
            return "Unknown System"
    elif system == "Windows".lower():
        return "Windows"
    else:
        return "Unkown System"


# 搭建Ubuntu系统环境。
def system_enviroment():
    os.system("apt update && apt upgrade -y && apt install python3.6 python-dev -y python3-pip")


class Setup:
    def __init__(self,  system_name, target_list):
        system_name = system_name
        target_list = target_list
        if system_name == "Windows":
            tools = "pip"
        elif system_name in ["CentOS", "Redhat"]:
            tools = ""

    def setup(system_name, target_list):
        pass

def setup(target):
    result = os.system("pip install " + target)
    if result:
        fail.append(target)
    else:
        success.append(target)


def main(ls):
    for target in ls:
        setup_result(target)


def print_result(fail, success):
    if len(fail) == 0:
        print("All package are installed.")
    else:
        print("Fail to setup these package:", end="")
        for f in fail:
            print(f, end=" ")
        print("\nSuceed to setup these package:", end="")
        for s in success:
            print(s, end=" ")
        print("\n")

ls = ["pillow", "jieba", "pyinstaller", "requests", "scipy", "numpy", "matplotlib", "wordcloud"]
fail = []
success = []
print(decide_system())