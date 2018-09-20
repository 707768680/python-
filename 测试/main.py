import math
def quadratic(a, b, c):
    t = b*b - 4*a*c
    if t > 0 :
        print("有两个不等实根")
        x = (-b + math.sqrt(t))/(2*a)
        y = (-b - math.sqrt(t))/(2*a)
        print(x,y)
    elif t == 0 :
        print("有两个相等实根")
        x = (-b + math.sqrt(t))/(2*a)
        print(x)
    elif t<0 :
        print("没有实根,有两个共轭复根")
quadratic(2,3,1)