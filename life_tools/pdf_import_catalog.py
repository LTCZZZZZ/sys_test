# 参见：https://www.zhihu.com/question/344805337/answer/1116258929

# 补充：代码中的 page_offset 一般设成 0 即可，
# 它只会在特殊的情况下使用，即 PDF 自带的目录中页码和实际页码存在偏差（通常是一个固定的偏移）的情况，
# 这时只需要将 page_offset 改成实际相应的偏差页数即可。

# 准备一个 txt 文本文件（假设命名为 toc.txt），在其中手动录入需要添加的目录，或者从文本型 PDF 中直接复制出目录，
# 采用类似下面格式即可：
# 唯一的要求是每一行的最后一项是页码（前面的空白符个数不限），并且相同级别的书签要采用相同的缩进量（空格或 tab 都可以）。

import re
from os.path import exists, splitext
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import NullObject, NameObject, TreeObject


def _get_parent_bookmark(current_indent, history_indent, bookmarks):
    '''The parent of A is the nearest bookmark whose indent is smaller than A's
    '''
    assert len(history_indent) == len(bookmarks)
    if current_indent == 0:
        return None
    for i in range(len(history_indent) - 1, -1, -1):
        # len(history_indent) - 1   ===>   0
        if history_indent[i] < current_indent:
            return bookmarks[i]
    return None

def addBookmark(pdf_path, bookmark_txt_path, page_offset=0):
    if not exists(pdf_path):
        return "Error: No such file: {}".format(pdf_path)
    if not exists(bookmark_txt_path):
        return "Error: No such file: {}".format(bookmark_txt_path)

    with open(bookmark_txt_path, 'r', encoding='utf-8') as f:
        bookmark_lines = f.readlines()
    reader = PdfFileReader(pdf_path)
    # print(type(reader.trailer))
    # print(type(reader.trailer['/Root']['/Outlines']))
    # print(type(reader.trailer['/Root']['/Outlines']['/Last']))
    # print(reader.trailer['/Root']['/Outlines'])
    # print(reader.outlines)
    writer = PdfFileWriter()
    # print(writer._objects)
    # print(writer._root_object)
    writer.cloneDocumentFromReader(reader)
    # print(writer._objects)
    # print(writer._root_object)

    # 重新生成空目录，如果是在原目录基础上加的话，就注释掉这一段
    outline = TreeObject()
    outline.update({})
    outlineRef = writer._addObject(outline)
    writer._root_object[NameObject('/Outlines')] = outlineRef

    # 我所不能理解的是，为什么不运行下面writer.addBookmark的一段代码，得出的pdf就全是空白页
    # 运行此段代码时需注释掉上面重新生成空目录的一段，才有控制变量法的效果
    # out_path = splitext(pdf_path)[0] + '-new.pdf'
    # with open(out_path, 'wb') as f:
    #     writer.write(f)
    # return

    maxPages = reader.getNumPages()
    bookmarks, history_indent = [], []
    # decide the level of each bookmark according to the relative indent size in each line
    #   no indent:          level 1
    #     small indent:     level 2
    #       larger indent:  level 3
    #   ...
    i = 0
    for line in bookmark_lines:
        line2 = re.split(r'\s+', line.strip())  # 先strip()，否则最后的列表中前后可能带有空字符串''
        if len(line2) == 1:  # 表示空行，因为上面用了line.strip()
            continue

        indent_size = len(line) - len(line.lstrip())
        parent = _get_parent_bookmark(indent_size, history_indent, bookmarks)
        history_indent.append(indent_size)

        # 删除title中的......结构
        name_chars = line2[:-2]
        while name_chars[-1][-1] == '.':
            del name_chars[-1]

        # title, page = ' '.join(line2[:-1]), int(line2[-1]) - 1
        title, page, top = ' '.join(name_chars), int(line2[-2]) - 1, float(line2[-1])
        if page + page_offset >= maxPages:
            return "Error: page index out of range: %d >= %d" % (page + page_offset, maxPages)

        # print(title, page, parent)
        # MAC上的预览似乎不识别颜色和/FitH模式，只识别/XYZ
        # 另外这里的纵坐标和一般web页面的坐标不同，它类似于平面直角坐标系，原点在页面左下角，且向上是正，所以这里用800-top
        new_bookmark = writer.addBookmark(title, page + page_offset, parent, (0.0, 0.6, 1.0), False, False, '/XYZ', 0, 720 - top, 0)
        # new_bookmark = writer.addBookmark(title, page + page_offset, parent=parent)
        bookmarks.append(new_bookmark)

        # 这里是另外一个不解之处，为什么只运行一次addBookmark时，书签就不显示(这也有可能是mac预览的问题)，
        # 但运行两次，就显示了。仍使i=1，但上面addBookmark再执行一次，或直接使i=2，都能看到效果
        # i += 1
        # if i == 1:
        #     break

    out_path = splitext(pdf_path)[0] + '-new.pdf'
    with open(out_path,'wb') as f:
        writer.write(f)

    return "The bookmarks have been added to %s" % out_path

if __name__ == "__main__":
    # import sys
    # args = sys.argv
    # if len(args) != 4:
    #     print("Usage: %s [pdf] [bookmark_txt] [page_offset]" % args[0])
    # else:
    #     print(addBookmark(args[1], args[2], int(args[3])))
    res = addBookmark('Artificial Intelligence 4th.pdf', 'Artificial Intelligence 4th_catalog.txt', page_offset=13)
    print(res)
