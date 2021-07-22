# 参见：https://www.zhihu.com/question/344805337/answer/1116258929

from os.path import exists
from PyPDF2 import PdfFileReader


def _parse_outline_tree(outline_tree, level=0):
    """Return List[Tuple[level(int), page(int), title(str)]]"""
    ret = []
    for heading in outline_tree:
        if isinstance(heading, list):
            # contains sub-headings
            ret.extend(_parse_outline_tree(heading, level=level+1))
        else:
            print(heading)
            # print(heading[''])
            ret.append((level, heading.page.idnum, heading.title))
    return ret

def extractBookmark(pdf_path, bookmark_txt_path):
    if not exists(pdf_path):
        return "Error: No such file: {}".format(pdf_path)
    if exists(bookmark_txt_path):
        print("Warning: Overwritting {}".format(bookmark_txt_path))

    reader = PdfFileReader(pdf_path)
    # List of ('Destination' objects) or ('Destination' object lists)
    #  [{'/Type': '/Fit', '/Title': u'heading', '/Page': IndirectObject(6, 0)}, ...]
    outlines = reader.outlines
    # List[Tuple[level(int), page(int), title(str)]]
    outlines = _parse_outline_tree(outlines)
    max_length = max(len(item[-1]) + 2 * item[0] for item in outlines) + 1
    # print(outlines)

    # with open(bookmark_txt_path, 'w') as f:
    #     for level, page, title in outlines:
    #         level_space = '  ' * level
    #         title_page_space = ' ' * (max_length - level * 2 - len(title))
    #         f.write("{}{}{}{}\n".format(level_space, title, title_page_space, page))

    return "The bookmarks have been exported to %s" % bookmark_txt_path


if __name__ == "__main__":
    # import sys
    # args = sys.argv
    # print(args) # args[0]是自己的文件名
    # if len(args) != 3:
    #     print("Usage: %s [pdf] [bookmark_txt]" % args[0])
    # else:
    #     print(extractBookmark(args[1], args[2]))
    extractBookmark('Artificial Intelligence 4th-new.pdf', 'd2l-zh_catalog.txt')
    # extractBookmark('Artificial Intelligence 4th.pdf', 'Artificial Intelligence 4th_catalog.txt')
