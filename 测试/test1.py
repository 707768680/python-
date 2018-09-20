# from test import my_abs

# print(my_abs(-12))
# def product(*x):
#     if(x == ()):
#         print("请输入参数")
#         return
#     sum = 1
#     for k in x:
#         sum *= k
#     print(sum)

# product()

# 汉诺塔移动
# def move(n,a,b,c):
#     if n == 1:
#         print(a,'--->',c)
#     else:
#         move(n-1,a,c,b)
#         move(1,a,b,c)
#         move(n-1,b,a,c)
# move(3,'A','B','C')

# 模拟 trim()

# def trim(s):
#     if s == '':
#         return ''
#     n = 0
#     l = len(s)
#     while s[n] == " ":
#         n += 1
#         if n + 1 == l :
#             return ''
#         print(n)
#     m = -1
#     while s[m] == " ":
#         m -= 1    
#     if m == -1:
#         return s[n:]  
#     m += 1      
#     return s[n:m]
# print(trim(''),'1')

# 返回最大值最小值
# def findMinAndMax(L):
#     if len(L) == 0:
#         return (None,None)
#     m = L[0]
#     n = L[0]
#     for value in L:
#         if value > m :
#             m = value
#         if value < n :
#             n = value
#     return (n,m)
# print(findMinAndMax([7,1,4,3,9,5]))

# 转小写
# L = ['Hello', 'World', 18, 'Apple', None]
# L1 = [s.lower() for se in L if isinstance(s,str)]
# print(L1)

# 杨辉三角
# def triangles():
#     L = [1]   
#     while True:
#         yield L
#         L = [1] + [L[j] + L[j + 1] for j in range(len(L) - 1)] + [1]
# n = 0
# results = []
# for t in triangles():
#     print(t)
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break

# def normalize(name):
#     return name.capitalize()

# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)
# from functools import reduce
# def prod(L):
#     def fn(x,y):
#         return x*y
#     return reduce(fn,L)
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# def str2float(s):
#     L = len(s)
#     domin = s.index('.')
#     def num(x,y):
#         return x*10 + y
#     def char(i):
#         digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#         return digits[i]
#     return reduce(num,map(char,s[:domin] + s[domin+1:]))/pow(10,L-domin-1)

# def is_palindrome(n):
#     if str(n)[:] == str(n)[::-1]:
#         return n
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))

# def createCounter():
#     i = 0
#     def counter(): 
#         nonlocal i
#         i = i + 1
#         return i
#     return counter
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5

# def is_odd(n):
#     return n % 2 == 1

# L = list(filter(lambda n:n % 2 == 1, range(1, 20)))
# print(L)
# import time, functools

# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*arg,**kw):
#         print('%s executed in %s ms' % (fn.__name__, 10.24))
#         return fn(*arg,**kw)
#     return wrapper
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;

# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;7

# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')
# else :
#     print('测试成功')


# plot a sine wave from 0 to 4pi  
# from pylab import *  
# x_values = arange(0.0, math.pi * 4, 0.01)  
# y_values = sin(x_values)  
# plot(x_values, y_values, linewidth=1.0)  
# xlabel('x')  
# ylabel('sin(x)')  
# title('Simple plot')  
# grid(True)  
# savefig("sin.png")  
# show()  