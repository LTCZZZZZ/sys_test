# 看dict用**传值后的问题
from copy import copy, deepcopy

def_text_dict = {'algn': 'l', 'fontAlgn': 'auto',
                 'lnSpc': {'type': 'multiple', 'val': 1},
                 'spcBef': {'type': 'constant', 'val': 0},
                 'spcAft': {'type': 'constant', 'val': 0},
                 'item': None,
                 'marL': 0, 'marR': 0, 'indent': 0, 'defTabSz': 914400}

# ap_text_dict = {**def_text_dict}
# ap_text_dict = copy(def_text_dict)
ap_text_dict = deepcopy(def_text_dict)
ap_text_dict['algn'] = 'asdfg'
ap_text_dict['lnSpc']['type'] = 'self'
ap_text_dict['spcBef'] = 3

print(def_text_dict)
print(ap_text_dict)


a = [{'type': 'ole'}]
for content in a:
    content['type'] = 'oMath'
print(a)

para = {'contents': [{'type': 'ole'}]}
for content in para['contents']:
    content['type'] = 'oMath'
print(para)


class Paragraph:

    def keys(self):  # 对象要转换成字典的键的属性
        return ('index', 'type', 'attrs', 'contents')

    def __getitem__(self, item):
        if item == 'contents':
            return [dict(i) for i in getattr(self, item)]
        else:
            return getattr(self, item)

    def __setitem__(self, key, value):
        setattr(self, key, value)


p = Paragraph()
# p.index = 1
# p['index'] = 3
print(p.index)
