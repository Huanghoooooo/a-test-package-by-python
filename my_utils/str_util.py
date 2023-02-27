'''
字符串相关工具，内含：
1.函数：str_reverse(s)，接受传入字符串，将字符串反转返回
2.函数：substr(s,x,y)，按照下标：x和y，对字符串进行切片
'''


def str_reverse(s):
    new_s = s[::-1]
    return new_s


def substr(s, x, y):
    new_s = s[x:y]
    return new_s

if __name__ == '__main__':
    print(str_reverse("ABCD"))
    print(substr("ABCD",0,4))