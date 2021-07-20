# 注意：此文件只能运行在windows服务器上，此处只为留存副本
from win32com import client as wc
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def doc_pdf(path):
    # print(wc.Dispatch.__doc__)
    word = wc.Dispatch('Word.Application')
    # ppt.DisplayAlerts = 1
    # print(path)
    name = '测试'
    print(BASE_DIR)
    doc = word.Documents.Open(path)
    file_path = os.path.join(BASE_DIR, name)
    print(file_path)

    # doc.SaveAs(file_path, '41')
    # print(doc.Slides(1)._oleobj_.GetIDsOfNames('export'))

    # 如果不加17，导出的文件虽然扩展名为pdf，但实际不可用pdf方式读取
    # 另外，这里SaveAs2和SaveAs都可以
    doc.SaveAs2(f'{file_path}.pdf', 17)
    # 导出为图片时不需要.Close这一环节
    doc.Close()
    # os.system(f'inkscape {file_path}.emf --export-plain-svg={file_path}.svg')


if __name__ == '__main__':
    # pp_code = [8, 40, 19, 11, 23, 64000, 16, 17, 15, 39, 35, 30, 36, 24, 25, 28, 29, 26, 27, 31, 32, 18, 1, 6, 7, 38, 5,
    #            21, 37, 34, 33]
    # pp_code.sort()
    # print(pp_code)
    # svg_code = []
    # for i in range(1, 41):
    #     if i not in pp_code:
    #         svg_code.append(i)
    # print(svg_code)
    # [2, 3, 4, 9, 10, 12, 13, 14, 20, 22]
    doc_pdf(os.path.join(BASE_DIR, '测试.docx'))
