from typing import List, Dict

a = {'asdf': 2, 'gdfggg': 2}

print(a['asdf'])

b = ['gdfgmek', '   sdfghjn  ', '天dsgndfg']  # type: List[str]

a['sdfg'] = ' indfjg  nd   '

b[1] = b[1].strip()
a['sdfg'] = a['sdfg'].strip()
