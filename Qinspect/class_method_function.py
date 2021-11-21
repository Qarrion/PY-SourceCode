# https://www.youtube.com/watch?v=myTz-ZDkO6Q

import inspect
import os

# def foo():
#     f = inspect.currentframe()
#     i = inspect.getframeinfo(f)
#     print(i.lineno)
#     print(i.filename)
#     print(i.function)

# foo()


def chek():
    prev_frame = inspect.currentframe().f_back
    if len(prev_frame.f_locals) == 0 :
        # if f_back in function
        def_name = inspect.getframeinfo(prev_frame).function
        print(f"function:{def_name}")

    else:
        the_class = prev_frame.f_locals["self"].__class__.__name__
        the_method = prev_frame.f_code.co_name
        print(f"class:{the_class}, method:{the_method}")


class myc():
    def cfoo(self):
        chek()

# def foo():
#     chek()

dd=myc()
dd.cfoo()
# foo()