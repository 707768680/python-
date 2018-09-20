import time 
from collections import Iterable
from collections import Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0
    
    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        return self 

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num  += 1
            return ret
        else:
            raise StopIteration

classmate = Classmate()
classmate.add("盖伦")
classmate.add("赵信")
classmate.add("嘉文")

for name in classmate:
    print(name)


