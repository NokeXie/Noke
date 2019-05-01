import time


# 统计函数运行时间的砖装饰器
def timmer(func):
    def warpper(*args, **kwargs):
        strat_time = time.time()
        func()
        stop_time = time.time()
        print("the func run time is %s" % (stop_time - strat_time))

    return warpper


@timmer
def test1():
    time.sleep(3)
    print("我运行了3秒种")


test1()

