# Before running other programs, please run this script.
import os
ls = ["pillow", "jieba", "pyinstaller", "requests", "scipy", "numpy", "matplotlib", "wordcloud"]
fail = []
success = []
def setup_result(target):
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


main(ls)
print_result(fail, success)