# 插入头部信息
def insert(name):
    file_name = name
    data = "#!/usr/bin/env python3\n"
    f = open(file_name, "r+", encoding="utf-8")
    old = f.read()
    f.seek(0)
    f.write(data)
    f.write(old)
    f.close()


def get_file():
    import os
    ls = os.popen("ls").read().split("\n")
    new_ls = []
    for name in ls:
        if ".py" in name and name != "insert.py":
            new_ls.append(name)
    return new_ls


file_list = get_file()
for name in file_list:
    print(name)
    insert(name)
