from greenlet import greenlet


def func1():
    print(1)
    gr2.switch() # 切换到func2函数
    print(2)
    gr2.switch()


def func2():
    print(3)
    gr1.switch() 
    print(4)


gr1 = greenlet(func1)
gr2 = greenlet(func2)
gr1.switch() # 1 执行func1函数
