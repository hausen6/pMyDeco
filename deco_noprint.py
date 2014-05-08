# coding: sjis
import sys
import os
import time
from StringIO import StringIO

def deco_noprint(func):
    """
    �֐����̃v�����g��r������f�R���[�^
    """
    def wrapper(*args, **kwards):
        # �W���o�͂�ޔ�����
        sys.stdout = StringIO()
        func(*args, **kwards)
        # �W���o�͂����ɖ߂��ăt�@�C�����폜����
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
