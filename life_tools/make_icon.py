# 制作Mac的App图标文件
# 制作完成后，在文件夹中找到想要替换的APP，右键，显示简介，然后把icns文件拖到简介中
from PIL import Image


def border(im, loc='a', width=3, color=(255, 255, 255, 0)):
    """
    im: 图片Image对象
    loc: (str) 边框添加的位置, 默认是'a'(
        四周: 'a' or 'all'
        上: 't' or 'top'
        右: 'r' or 'rigth'
        下: 'b' or 'bottom'
        左: 'l' or 'left'
    )
    width: (int) 边框宽度 (默认是3)
    color: (int or 4-tuple) 边框颜色 (默认为白色纯透明; 也可以设置为四元组表示RGBA颜色)
    """
    # 读取图片
    img_ori = im
    w = img_ori.size[0]
    h = img_ori.size[1]

    # 添加边框
    if loc in ['a', 'all']:
        w += 2 * width
        h += 2 * width
        img_new = Image.new('RGBA', (w, h), color)
        img_new.paste(img_ori, (width, width))
    elif loc in ['t', 'top']:
        h += width
        img_new = Image.new('RGBA', (w, h), color)
        img_new.paste(img_ori, (0, width, w, h))
    elif loc in ['r', 'right']:
        w += width
        img_new = Image.new('RGBA', (w, h), color)
        img_new.paste(img_ori, (0, 0, w - width, h))
    elif loc in ['b', 'bottom']:
        h += width
        img_new = Image.new('RGBA', (w, h), color)
        img_new.paste(img_ori, (0, 0, w, h - width))
    elif loc in ['l', 'left']:
        w += width
        img_new = Image.new('RGBA', (w, h), color)
        img_new.paste(img_ori, (width, 0, w, h))
    return img_new


def make_icon(im_path):
    """
    制作图标
    :param im_path: 图片路径
    :return:
    """
    im = Image.open(im_path)
    # 增加使图片透明的处理
    im = im.convert('RGBA')
    data = im.getdata()
    newData = list()
    for item in data:
        # if item[0] == 255 and item[1] == 255 and item[2] == 255:
        if item[0] > 242 and item[1] > 242 and item[2] > 242:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    im.putdata(newData)
    # 增加透明边框
    im = border(im, loc='a', width=32, color=(0, 153, 255, 0))
    # im.show()
    im.resize((512, 512), Image.ANTIALIAS).save('icon.icns')


if __name__ == '__main__':
    make_icon('plus.jpg')
