def create_num(all_num):
    current_num = 0
    a, b = 0, 1
    while current_num < all_num:
        ret = yield a
        print("====ret====>", ret)
        a, b = b, a+b
        current_num += 1

obj = create_num(10)

ret = next(obj)
print(ret)

# 用生成器对象.send方法可以传参数,用 yeild 返回值来接收,
# 一般不用于第一次执行,如果用于第一次则传 None 参数否则报错 
ret = obj.send("hahaha")
print(ret)
