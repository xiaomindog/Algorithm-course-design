import datetime
import math

# 参考博客： https://blog.csdn.net/every__day/article/details/86644814
# https://blog.csdn.net/OscaronMar/article/details/82877103
# a是否在b中出现  a是模式串

# 设置一个很大的P
P = 20  # 哈希映射表的长度


# MOD = 1000000007

def contain(a, b):
    al = len(a)
    bl = len(b)
    if (al > bl): return -1

    # 计算P的al次方
    t = math.pow(P, al)
    # print(t)

    ah, bh = 0, 0
    # 计算a,b前缀的哈希值
    for i in range(al):
        ah = ah * P + ord(a[i])
        bh = bh * P + ord(b[i])

    # 对 b不断右移一位，更新哈希值并判断
    i = 0
    while i + al <= bl:
        if ah == bh:
            return i
        if i + al < bl:
            bh = bh * P + ord(b[i + al]) - ord(b[i]) * t

        i += 1

    return -1


s = contain('example', 'this is an simple example')
print(s)
