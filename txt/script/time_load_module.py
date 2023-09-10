#__all__:goto
r'''[[[
e script/time_load_module.py


script.time_load_module
py -m script.time_load_module
py -m nn_ns.app.debug_cmd   script.time_load_module -x
py -m nn_ns.app.doctest_cmd script.time_load_module:__doc__ -ff -v
py_adhoc_call   script.time_load_module   @f
from script.time_load_module import *
#]]]'''
__all__ = r'''
'''.split()#'''
__all__

from time import monotonic, perf_counter, process_time, thread_time
import sys
mmm = sys.modules

time_ = monotonic
time0 = time_()
prev_time = time0
def show__time():
    global prev_time
    curr_time = time_()
    delta_time = curr_time -prev_time
    total_time = curr_time -time0
    prev_time = curr_time
    print(f'... {delta_time}/{total_time}')

to_show = False
class D(dict):
    def __setitem__(sf, nm, mdl, /):
        if to_show:
            show__time()
            print(f'import {nm}')
        super().__setitem__(nm, mdl)
if 1:
    sys.modules = D(mmm)
    time0 = time_()
    to_show = True
    import seed.tiny
    if to_show:
        show__time()
    to_show = False

if __name__ == "__main__":
    pass
__all__


from script.time_load_module import *
