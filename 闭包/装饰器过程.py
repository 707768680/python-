def set_func(func):
    def call_func():
        print("---验证1---")
        print("---验证1---")
        func()
    return call_func
@set_func   # 等价于 13 行: test1 = set_func(test1)
def test():
    print("---test---")

# 在这里先执行 set_func 函数, 将 test1 传进去, 在调用前增加功能 符合开放封闭原则,
# 相当于在原来的 test1 函数外包裹上一层函数, 不修改函数内的代码添加功能
# test1 = set_func(test1)
test()


print("-----------------------------------")
# 带参数和返回值的装饰器-------------------------
def set_func1(func):
    print("---开始进行装饰---")
    def call_func1(*args, **kwargs):
        print("---这是验证1---")
        print("---这是验证2---")
        # func(args, kwargs)   # 不行, 这样相当于传递了 2 个参数 : 1个元祖, 1个字典
        return func(*args, **kwargs)   # 拆包 然后传递给test1
    return call_func1

@set_func1
def test1(num, *args, **kwargs):
    print("---test1---%d" % num)
    print("---test1---" , args)
    print("---test1---" , kwargs)
    return "ok"

ret = test1(100)
ret = test1(100, 200)
ret = test1(100, 200, 300, mm=100)
print(ret)
