#!/usr/bin/env python3
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


# 搭建Windows,Ubuntu系统环境。
def system_enviroment(system_name):
    print("正在搭建系统环境")
    result = os.system("git config --global user.name 'luyongwen' &&\
            git config --global user.email 'luyongwen@hotmail.com'")
    if result:
        print("git设置错误，请手动设置")
    if system_name == "Ubuntu":
        result = os.system("apt update && apt upgrade -y &&\
         apt install python3.6 python3-dev python3-pip -y &&\
          python3 -m pip install --upgrade pip")
        tool = "pip3"
    elif system_name == "Windows":
        result = os.system("python -m pip install --upgrade pip")
        tool = "pip"
    else:
        print("抱歉本程序不适合在该操作系统执行，程序退出")
        sys.exit()
    if result:
        print("网络错误无法更新系统环境，程序退出，请尝试重新运行程序")
        sys.exit()
    return tool

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
    print("本机系统为：" + system_name)
    tool = system_enviroment(system_name)
    ls = ["pillow", "jieba", "pyinstaller", "requests", "scipy", "numpy", "matplotlib", "wordcloud"]
    fail = []
    success = []
    print("程序开始执行，开始安装相关库")
    for target in ls:
        result = os.system(tool + " install " + target)
        if result:
            fail.append(target)
        else:
            success.append(target)
    print_result(fail, success)
    nothing = input("程序执行完毕，按回车键退出")


main()
#print(decide_system())
