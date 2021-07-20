# 如何在lxml(xpath)中使用正则表达式re

from lxml import etree
from lxml.etree import HTMLParser
text='''
<div xmlns:pkg="abcdef">
    <pkg:ul>
         <li1 class="item-0"><a href="link1.html">第一个</a></li1>
         <li2 class="item-1"><a href="link2.html">second item</a></li2>
     </pkg:ul>
 </div>
'''
ns = {'pkg': 'abcdef',
      're': 'http://exslt.org/regular-expressions'}

html=etree.XML(text, etree.XMLParser())
# res = html.find('.//pkg:ul', ns)


# result=html.xpath('//a[@href="link2.html"]/../@class')
# result1=html.xpath('//a[@href="link2.html"]/parent::*/@class')
# print(result)
# print(result1)

# 以下前三种方法效果相同，第四种更精确
# res = html.xpath('.//*[starts-with(@class, "item-")]')
# res = html.xpath('.//*[contains(@class, "item-")]')
# res = html.xpath(r".//*[re:match(@class, 'item-')]",
#         namespaces={"re": "http://exslt.org/regular-expressions"})
# res = html.xpath(r".//*[re:match(@class, 'item-\d+')]",
#         namespaces={"re": "http://exslt.org/regular-expressions"})

# res = html.xpath('//node()[starts-with(name(),"li")]')
res = html.xpath(r'//node()[re:match(name(),"li\d")]', namespaces=ns)
res = html.xpath(r'//node()[re:match(name(),"li1|2")]', namespaces=ns)

res = html.xpath('.//li1|.//li2', namespaces=ns)

print(res)

