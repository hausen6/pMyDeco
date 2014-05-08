# coding: sjis
import time
from functools import wraps

def deco_printtime(func):
    """
    関数の実行時間をプリントするデコレータ
    """
    def wrapper(*args, **kwards):
        startTime = time.time()
        func(*args, **kwards)

        # 実行時間を計算する
        finishTime = time.time() - startTime
        hour = int(finishTime / 3600)
        min = int( ( finishTime - hour * 3600 ) / 60 )
        sec = ( finishTime - hour * 3600 - min * 60 )

        # 実行時間のprint
        p = u"func: {0}\ttime: {1}h {2}m {3}s".format(func.__name__, hour, min, sec)
        print(p)
    return wraps(func)(wrapper)

@deco_printtime
def test(a):
    time.sleep(a)

if __name__ == '__main__':
    finishTime = 72
    hour = int(finishTime / 3600)
    min = int( ( finishTime - hour * 3600 ) / 60 )
    sec = ( finishTime - hour * 3600 - min * 60 )

    # 実行時間のprint
    p = u"time: {0}h {1}m {2}s".format( hour, min, sec)
    print(p)
    #test(10)
