# -*- coding: utf-8 -*-
import os, io, shutil
import requests
import zipfile
import json
import shapely.geometry as geo

base_dir = '/Users/ltc/Downloads/EasyVArea/'
os.chdir(base_dir)


def set_location(edu_id, adcode, ratio):
    """
    :param edu_id: 区教育局id
    :param adcode: 区域编码
    :param ratio: 边缘系数，从最大包含区域的正矩形向内压缩的比率
    :return:
    """
    # 地图文件不存在，先下载地图，移动并重命名，压缩成zip文件
    if not os.path.exists(f'{adcode}.json'):
        city_code = adcode // 100 * 100
        res = requests.get(
            f'https://map.easyv.cloud/download_by_folder?list={adcode}%3A{city_code}&province=1&city=1&area=1')
        # 用BytesIO缓存数据，然后直接解压
        with zipfile.ZipFile(io.BytesIO(res.content)) as zf:
            zf.extractall()
        shutil.move(base_dir + f'muti_files/{city_code}.json', f'{adcode}.json')
        os.system(f'zip {adcode}.json.zip {adcode}.json')

    with open(f'{adcode}.json') as f:
        data = json.load(f)
    area = data["features"][0]["geometry"]["coordinates"][0][0]
    print(area)
    poly = geo.Polygon(area)
    print(poly.contains(geo.Point(113, 35)))
    print(poly.contains(geo.Point(113.743742, 34.811443)))


    # return这一行是留着给jupyter显示地图用的
    return poly


if __name__ == '__main__':
    set_location(177, 410105, 0.9)  # 郑州市金水区

