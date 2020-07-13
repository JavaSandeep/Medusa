#!/bin/python3
from timeit import default_timer as timer

def measure_time(fn):
    def wrapper():
        st_t=timer()
        fn()
        eta=timer()-st_t
        print("Total execution time: {:.6f} seconds".format(eta))
        return
    return wrapper