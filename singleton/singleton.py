class singleton_base():
    def __init__(self):
        pass
    def foo(self):
        print("foo")

class singleton():
    ref = singleton_base()
    def get_instance():
        return singleton.ref

a = singleton.get_instance()
b = singleton.get_instance()
assert(a == b)

# what is a good way to test singleton
del a
import time
time.sleep(1)
b.foo()
