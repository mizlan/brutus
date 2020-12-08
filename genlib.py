import random, io
from typing import Iterable
import copy

class TestCase:
    __slots__ = ['output']

    def __init__(self):
        self.output = io.StringIO()

    def w(self, *args, **kwargs):
        print(*args, **kwargs, file=self.output)

    def p(self):
        print(self.output.getvalue(), end='')

def rng(*args, **kwargs):
    return random.randrange(*args, **kwargs)

def shuf(*args, **kwargs):
    return random.shuffle(*args, **kwargs)

def shuffled(seq: Iterable):
    x = copy.copy(seq)
    shuf(x)
    return x

def rsel(seq):
    return random.choice(seq)

def clump(seq, sz):
    return [seq[k:k+sz] for k in range(0, len(seq), sz)]

def lrange(*args, **kwargs):
    return list(range(*args, **kwargs))

if __name__ == "__main__":
    tc = TestCase()
    n = rng(5, 10)
    tc.w(n)
    ls = shuffled(lrange(1, 2*n+1))
    for c in clump(ls, 2):
        c = sorted(c)
        tc.w(*c)
    tc.p()
