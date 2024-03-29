# CSDN下载的html文件打开时会自动跳转，去掉这个功能，并允许选中、复制
# 跳转节点
# <div style="display:none;">
# 	<img src="" onerror='setTimeout(function(){if(!/(csdn.net|iteye.com|baiducontent.com|googleusercontent.com|360webcache.com|sogoucdn.com|bingj.com|baidu.com)$/.test(window.location.hostname)){window.location.href="\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x63\x73\x64\x6e\x2e\x6e\x65\x74"}},3000);'>
# </div>
# 禁止选中节点
# <style>
#     #content_views{
#         -webkit-touch-callout: none;
#         -webkit-user-select: none;
#         -khtml-user-select: none;
#         -moz-user-select: none;
#         -ms-user-select: none;
#         user-select: none;
#     }
# </style>
import os.path
from lxml import etree


def delete(self, tag):
    node = self.find(tag)
    if node is not None:
        node.getparent().remove(node)


def single_file(path):
    # 指定解析器HTMLParser会根据文件修复HTML文件中缺失的如声明信息
    tree = etree.parse(path, etree.HTMLParser())
    root = tree.getroot()
    # print(root)

    href_div = root.find('.//div[@style="display:none;"]')
    print(href_div)
    # print(href_div.getparent().getparent().getparent())

    style = root.find('head/style')
    # print(style.text)
    style.text = style.text.replace('none', 'true')

    delete(root, './/div[@style="display:none;"]')

    # 注意这个method必不可少，否则默认是xml，会将许多符号(比如引号)都替换掉，
    # 还可能有别的格式问题，总之就是最后用浏览器打开感觉像是丢失了排版格式
    tree.write(path, encoding='utf-8', method='html')


# 这个batch_file整个都是Github Copilot自动生成的，我甚至没打注释，只输入了def batch，就自动生成了下面全部
def batch_file(path):
    """批量处理文件夹下全部文件"""
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.html'):
                single_file(os.path.join(root, file))


if __name__ == '__main__':
    base_dir = '/Users/ltc/Documents/学习资料/Math/机器学习中的数学(全集)'
    # single_file(os.path.join(base_dir, '数学——你与机器学习之间的距离_石 溪的博客-CSDN博客.html'))
    batch_file(base_dir)
