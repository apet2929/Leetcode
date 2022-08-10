
import time


def test_timed(func):
    start_time = time.time()
    output = func()
    print("--- %s seconds ---" % (time.time() - start_time))
    return output