import time
from functools import lru_cache

@lru_cache(maxsize=1)
def sleep_(n):
    time.sleep(n)
    return None
if __name__ == '__main__':
    print("1")
    sleep_(5)
    sleep_(4)
    sleep_(3)
    sleep_(2)
    print("terminate ")