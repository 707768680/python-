def set_func1(func):
    print("---开始进行装饰1---")
    def call_func1():
        print("---这是验证1---")
        return func()  
    return call_func1

def set_func2(func):
    print("---开始进行装饰2---")
    def call_func2():
        print("---这是验证2---")
        return func()  
    return call_func2


@set_func1
@set_func2
def test1():
    print("---test1---")


test1()

