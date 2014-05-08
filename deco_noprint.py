# coding: sjis
import sys
import os
import time
from StringIO import StringIO

def deco_noprint(func):
    """
    関数内のプリントを排除するデコレータ
    """
    def wrapper(*args, **kwards):
        # 標準出力を退避する
        sys.stdout = StringIO()
        func(*args, **kwards)
        # 標準出力を元に戻してファイルを削除する
        sys.stdout = sys.__stdout__
        return func
    return wrapper

@deco_noprint
def test(start, to):
    for i in range(start, to):
        print i
        time.sleep(1)

if __name__ == '__main__':
    test(10, 20)
