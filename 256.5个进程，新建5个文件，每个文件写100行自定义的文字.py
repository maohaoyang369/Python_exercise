# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 5个进程，新建5个文件，每个文件写100行自定义的文字

# 1 生成子进程，给它指定一个完成的任务（一个函数）
# 2 生成所有的子进程，并start
# 3 join一下所有的子进程，等待所有的子进程执行完毕了，在执行主进程的剩余代码

import multiprocessing


def do(file_path):
    with open(file_path, "w") as fp:
        for i in range(100):
            fp.write("gloryroad"+str(i)+"\n")


if __name__ == '__main__':
    numList = []
    for i in range(5):
        p = multiprocessing.Process(target=do, args=("d:\\python\\pic\\"+str(i)+".txt",))
        numList.append(p)
        p.start()
    # p.join()          # p进程,通过join方法通知主进程死等我结束，再继续执行
    print("Process end.")
for i in numList:
    i.join()            # 每一个进程执行结束后，才会开始下一次循环

# 循环结束了，也就说5个进程全部执行完毕了，然后在执行print语句。
print("done!")
