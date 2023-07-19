# https://python3-cookbook.readthedocs.io/zh_CN/latest/c04/p13_create_data_processing_pipelines.html

# 以管道方式处理数据可以用来解决各类其他问题，包括解析，读取实时数据，定时轮询等。
#
# 为了理解代码，重点是要明白 yield 语句作为数据的生产者而 for 循环语句作为数据的消费者。
# 当这些生成器被连在一起后，每个 yield 会将一个单独的数据元素传递给迭代处理管道的下一阶段。
# 在例子最后部分， sum() 函数是最终的程序驱动者，每次从生成器管道中提取出一个元素。
#
# 这种方式一个非常好的特点是每个生成器函数很小并且都是独立的。这样的话就很容易编写和维护它们了。
# 很多时候，这些函数如果比较通用的话可以在其他场景重复使用。 并且最终将这些组件组合起来的代码看上去非常简单，也很容易理解。
#
# 使用这种方式的内存效率也不得不提。上述代码即便是在一个超大型文件目录中也能工作的很好。
# 事实上，由于使用了迭代方式处理，代码运行过程中只需要很小很小的内存。

import os
import fnmatch
import gzip
import bz2
import re
from collections.abc import Iterable


# from collections import Iterable


def gen_find(filepat, top):
    """
    Find all filenames in a directory tree that match a shell wildcard pattern
    """
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    """
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    """
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        # print(isinstance(f, Iterable))
        # 可以看出，f本身就是一个可迭代对象，所以在下面的gen_concatenate函数中，可以直接使用for循环遍历f
        # 遍历f得到的是文件的每一行，类型是str
        yield f
        f.close()


def gen_concatenate(iterators):
    """
    Chain a sequence of iterators together into a single sequence.
    可以这样类比，iterators是一个二维数组，这个函数将其转换为一维数组，就是将多个迭代器链接起来合成一个

    在这里的话，iterators是一个生成器，每个元素是一个文件对象，每个文件对象又是一个可迭代对象，每次迭代得到的是文件的每一行
    """
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    """
    Look for a regex pattern in a sequence of lines
    """
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            # print(line)  # line后面有'\n'，print函数会自动换行，所以打印出的结果之前每次都会有一个空行
            yield line


if __name__ == '__main__':
    # 将这些函数连起来创建一个处理管道。 比如，为了查找包含单词python的所有日志行
    # lognames = gen_find('access-log*', 'www')
    lognames = gen_find('test*.log', './')
    files = gen_opener(lognames)
    lines = gen_concatenate(files)
    pylines = gen_grep('(?i)python', lines)

    # 在生成器表达式中包装数据。 比如，下面这个版本计算出传输的字节数并计算其总和
    bytecolumn = (line.rsplit(None, 1)[1] for line in pylines)
    bytes = (int(x) for x in bytecolumn if x != '-')
    print('Total', sum(bytes))
