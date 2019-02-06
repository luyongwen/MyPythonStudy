# 该脚本适用于Windows，Ubuntu系统，为其他脚本搭建运行环境。
import os
import platform
import sys
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
    result = os.system("apt update && apt upgrade -y && apt install python3.6 python3-dev -y python3-pip")
    if result:
        print("网络错误无法更新系统环境，程序退出，请尝试重新运行程序")
        sys.exit()


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



def main():
    system_name = decide_system()
    print(system_name)
    if system_name == "Windows":
        tool = "pip"
    elif system_name == "Ubuntu":
        system_enviroment()
        tool = "pip3"
    else:
        print("抱歉本程序不适合在该操作系统执行，程序退出")
        sys.exit()
    ls = ["pillow", "jieba", "pyinstaller", "requests", "scipy", "numpy", "matplotlib", "wordcloud"]
    fail = []
    success = []
    for target in ls:
        result = os.system(tool + " install " + target)
        if result:
            fail.append(target)
        else:
            success.append(target)
main()
print_result()
