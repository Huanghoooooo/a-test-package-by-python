'''
文件处理相关工具，内含：
1.函数：print_file_info(file_name)，接收传入文件的路径，打印文件的全部内容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
2.函数：append_to_file(file_name,data)，接收文件路径以及传入数据，将数据追加写入到文件中
'''


def print_file_info(file_name):
    """_summary_\n
    功能是将字符串反转\n
    :param file_name:要打印的文件路径
    """
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        content = f.read()
        print(content)
    except Exception as e:
        print(f"错误", {e})
    finally:
        if f:  # 如果变量是None，表示False，如果有任何内容，则是True
            f.close()


def append_to_file(file_name, data):
    """_summary_\n
    功能是追加\n
    Args:
        file_name (str): 文件路径
        data (str): 数据
        return:None
    """
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()


if __name__ == '__main__':
    # print_file_info("D:/file")
    append_to_file("D:/test.txt", "abcd")
