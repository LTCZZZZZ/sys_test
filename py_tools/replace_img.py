import os
from PIL import Image

base_dir = '/Users/ltc/Downloads'


def replace(path0, path1, path2):
    with Image.open(os.path.join(base_dir, path0)) as im0:
        # print(im0.mode)
        print(im0.size)
        # data0 = im0.getdata()
        # for item in data0:
        #     print(item)
        #     break
        box = (700, 1420, 1030, 1550)
        im_crop = im0.crop(box)
        # im_crop.show()
        with Image.open(os.path.join(base_dir, path1)) as im1:
            im1.paste(im_crop, box, mask=False)
            # im1.show()
            im1.save(os.path.join(base_dir, path2))


if __name__ == '__main__':
    replace('IMG_0.PNG', 'IMG_1.PNG', 'IMG_2.PNG')
