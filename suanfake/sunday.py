import datetime
def sunday_find(src, dst):
    len_src = len(src)
    len_dst = len(dst)
    i = 0
    while i < len_src - len_dst + 1:
        flag = 0
        shift = len_dst
        for j in range(0, len_dst):
            if src[i+j] != dst[j]:
                flag = -1
                break

        if flag == 0:
            return i

        p = dst.rfind(src[i+shift])
        if p == -1:
            shift = len_dst + 1
        else:
            shift = len_dst - p

        i = i + shift

    return -1


if __name__ == "__main__":
    starttime = datetime.datetime.now()
    string = []
    pattern = []
    file = open("./pai.txt", "r", encoding='gbk')

    for line in file:
        if not line.startswith('>'):
            string.append(line.replace('\n', ''))
    string = ''.join(string)  # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串；

    file.close()
    # print(string)
    pattern = "314159"
    fuben_string = string
    temp = []

    pre_chars = 0
    while len(string)>0:
        s=pre_chars+sunday_find(fuben_string,pattern)
        temp.append(s)
        pre_chars=s+len(pattern)

        fuben_string = string[pre_chars:]

        if len(temp)>=100:   #最多匹配个数
             break

    # print (string)
    print(pattern)
    print(temp)
    print('匹配到的个数：', len(temp))

    endtime = datetime.datetime.now()
    print((endtime - starttime))