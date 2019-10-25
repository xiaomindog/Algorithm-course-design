import datetime

def getBMBC(pattern):
    # 预生成坏字符表
    BMBC = dict()
    for i in range(len(pattern) - 1):
        char = pattern[i]
        # 记录坏字符最右位置（不包括模式串最右侧字符）
        BMBC[char] = i + 1
    return BMBC

def getBMGS(pattern):
    # 预生成好后缀表
    BMGS = dict()

    # 无后缀仅根据坏字移位符规则
    BMGS[''] = 0

    for i in range(len(pattern)):

        # 好后缀
        GS = pattern[len(pattern) - i - 1:]

        for j in range(len(pattern) - i - 1):

            # 匹配部分
            NGS = pattern[j:j + i + 1]

            # 记录模式串中好后缀最靠右位置（除结尾处）
            if GS == NGS:
                BMGS[GS] = len(pattern) - j - i - 1
    return BMGS

def BM(string, pattern):
    """
    Boyer-Moore算法实现字符串查找
    """
    m = len(pattern)#子串
    n = len(string)#父串
    i = 0
    j = m
    indies = []
    BMBC = getBMBC(pattern=pattern)  # 坏字符表
    BMGS = getBMGS(pattern=pattern)  # 好后缀表
    while i < n:
        while (j > 0):
            if i + j -1 >= n: # 当无法继续向下搜索就返回值
                return indies

            # 主串判断匹配部分
            a = string[i + j - 1:i + m]

            # 模式串判断匹配部分
            b = pattern[j - 1:]

            # 当前位匹配成功则继续匹配
            if a == b:
                j = j - 1

            # 当前位匹配失败根据规则移位
            else:
                i = i + max(BMGS.setdefault(b[1:], m), j - BMBC.setdefault(string[i + j - 1], 0))
                j = m

            # 匹配成功返回匹配位置
            if j == 0:
                indies.append(i)
                i += 1
                j = len(pattern)

# https://blog.csdn.net/qq_29423387/article/details/86531392
if __name__ == '__main__':
     starttime = datetime.datetime.now()
     string =[]
     pattern =[]
     file = open("./pai.txt", "r", encoding='gbk')

     for line in file:
        if not line.startswith('>'):
            string.append(line.replace('\n',''))
     string = ''.join(string)#join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串；

     file.close()

     pattern="314159"


     s = BM(string,pattern)

     #print (string)
     print (pattern)
     print (s)
     print('匹配到的个数：',len(s))

     endtime=datetime.datetime.now()
     print ((endtime-starttime))
