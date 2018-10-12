class Test(object):
    def __init__(self, func):
        self.func = func
    
    def __call__(self):
        print("添加装饰器的功能。。。")
        return self.func()


@Test  # 相当于 get_str = Test(get_str)
def get_str():
    return "haha"

print(get_str())