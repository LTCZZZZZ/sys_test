# -*- coding: utf-8 -*-
import os, io, shutil
import time

import requests
import zipfile
import json
import shapely.geometry as geo
import random
from connection import connection, get_server, get_server2

base_dir = '/Users/ltc/Downloads/EasyVArea/'
os.chdir(base_dir)


def zoom(bound, ratio):
    """
    这个函数大段是由Github Copilot生成的，又一次惊艳了我
    将bound缩放到ratio比例，w代表x方向，h代表y方向，r代表各点向内缩进的比例
    :param bound:
    :param ratio:
    :return:
    """
    w = bound[2] - bound[0]
    h = bound[3] - bound[1]
    r = (1 - ratio) / 2
    return bound[0] + w * r, bound[1] + h * r, bound[2] - w * r, bound[3] - h * r


def generate_point(poly, bounds):
    """在poly内，bounds范围内生成一个随机点"""
    while True:
        x = random.uniform(bounds[0], bounds[2])
        y = random.uniform(bounds[1], bounds[3])
        if poly.contains(geo.Point(x, y)):
            return [x, y]


def generate_location(edu_id, adcode, poly, bounds, n=30):
    """
    根据edu_id，area在rpc的数据库中edu_location表中生成n个随机点数据，满足点在poly中
    """
    # 先看数据表中是否存在edu_id的数据
    cur_rpc.execute(f"SELECT * FROM edu_location WHERE edu_id={edu_id} limit 1")
    if cur_rpc.fetchone() is None:
        loc = []
        for i in range(n):
            loc.append(generate_point(poly, bounds))
        print(f'loc: {loc}')
        cur_rpc.execute(f"insert into edu_location values({edu_id}, '{json.dumps(loc)}', '{adcode}')")
        conn_rpc.commit()


def update_location(edu_id, poly, bounds):
    """
    根据edu_id，area在api的数据库中institution表中更新经纬度数据，使其在poly中
    """
    # 全部更新
    cur_api.execute('select p.id from institution p left join education_institution q on p.id = q.institution_id '
                   'where q.education_id = %s and p.type = 2', (edu_id,))
    # 只更新没有经纬度的
    # cur_api.execute('select p.id from institution p left join education_institution q on p.id = q.institution_id '
    #                 'where q.education_id = %s and p.type = 2 and p.longitude = 0', (edu_id,))
    id_list = [i[0] for i in cur_api.fetchall()]
    print(id_list)

    loc = []
    for i in id_list:
        loc.append(tuple(generate_point(poly, bounds) + [i]))

    cur_api.executemany('update institution set longitude = %s, latitude = %s where id = %s', loc)
    conn_api.commit()


def set_location(edu_id, adcode, ratio):
    """
    主逻辑函数
    :param edu_id: 区教育局id
    :param adcode: 区域编码
    :param ratio: 边缘系数，从最大包含区域的正矩形向内压缩的比率
    :return:
    """
    print(f'edu_id: {edu_id}')
    # 地图文件不存在，先下载地图，移动并重命名，压缩成zip文件
    if not os.path.exists(f'{adcode}.json'):
        city_code = adcode // 100 * 100
        # print(f'https://map.easyv.cloud/api/download_by_folder?list={adcode}%3A{city_code}&province=1&city=1&area=1')
        # res = requests.get(
        #     f'https://map.easyv.cloud/api/download_by_folder?list={adcode}%3A{city_code}&province=1&city=1&area=1')
        res = requests.get(
            f'https://map.easyv.cloud/api/download_by_folder?list={adcode}&province=0&city=1&area=1')
        print(res.text)
        res = requests.get(
            f'https://map.easyv.cloud/api/download_by_url?url={res.text}'
        )
        # print(res)
        # 用BytesIO缓存数据，然后直接解压
        # with zipfile.ZipFile(io.BytesIO(res.content)) as zf:
        #     zf.extractall()
        # shutil.move(base_dir + f'muti_files/{city_code}.json', f'{adcode}.json')

        # 获取地图文件方式又有更改，现在直接是json文件
        with open(f'{adcode}.json', 'wb') as f:
            f.write(res.content)

        os.system(f'zip {adcode}.json.zip {adcode}.json')

    with open(f'{adcode}.json') as f:
        data = json.load(f)
    area = data["features"][0]["geometry"]["coordinates"][0][0]
    # print(f'area: {area}')
    poly = geo.Polygon(area)
    # print(poly.contains(geo.Point(113, 35)))
    # print(poly.contains(geo.Point(113.743742, 34.811443)))
    # print(poly.bounds)
    # print(poly.minimum_rotated_rectangle)
    bounds = zoom(poly.bounds, ratio)
    generate_location(edu_id, adcode, poly, bounds)
    update_location(edu_id, poly, bounds)

    # return这一行是留着给jupyter显示地图用的
    return geo.GeometryCollection([poly, poly.minimum_rotated_rectangle])


def process():
    """主执行进程"""
    # set_location(32, 110101, 0.9)  # 北京市崇文区
    # set_location(74, 340203, 1.2)  # 芜湖市弋江区
    # set_location(126, 610922, 0.9)  # 安康市石泉县
    # set_location(108, 420982, 0.9)  # 孝感市安陆市
    # set_location(147, 420303, 0.9)  # 十堰市张湾区
    # set_location(148, 420302, 0.9)  # 十堰市茅箭区(这个区畸形，有点难设置)
    # set_location(152, 510112, 0.9)  # 成都市龙泉驿区
    # set_location(140, 341002, 0.9)  # 黄山市屯溪区
    # set_location(168, 530927, 0.9)  # 临沧市沧源县
    # set_location(188, 431228, 0.9)  # 怀化市芷江县
    # set_location(185, 130126, 0.9)  # 石家庄灵寿县
    # set_location(212, 650102, 0.9)  # 乌鲁木齐天山区
    # set_location(177, 410105, 0.9)  # 郑州市金水区
    # set_location(169, 341024, 0.9)  # 黄山市祁门县
    # set_location(217, 321311, 0.9)  # 宿迁市宿豫区
    # set_location(101, 340304, 0.9)  # 蚌埠市高新区（禹会区）
    # set_location(290, 110101, 0.9)  # 鸿合三点伴区级教育局端演示平台（东城区地图）
    # set_location(218, 130635, 0.9)  # 河北省保定市蠡县
    # set_location(283, 370902, 0.9)  # 山东省泰安市泰山区
    # set_location(116, 532527, 0.9)  # 云南省红河州泸西县
    # set_location(306, 360702, 0.9)  # 江西省赣州市章贡区
    # set_location(341, 360702, 0.9)  # 江西省赣州市章贡区（兴趣）
    # set_location(342, 360702, 0.9)  # 江西省赣州市章贡区（幼儿园）
    # set_location(297, 522723, 0.9)  # 贵州省黔南州贵定县
    # set_location(286, 520624, 0.9)  # 贵州省铜仁市思南县
    # set_location(330, 220623, 0.9)  # 吉林省白山市长白县
    # set_location(324, 320602, 0.9)  # 江苏省南通市崇川区
    # set_location(385, 320585, 0.9)  # 江苏省苏州市太仓市
    # set_location(393, 320582, 0.9)  # 江苏省苏州市张家港市
    # set_location(397, 321311, 0.9)  # 江苏省宿迁市宿豫区
    # set_location(86, 532528, 0.9)  # 云南省红河州元阳县
    # set_location(403, 320382, 0.9)  # 徐州市邳州市
    # set_location(404, 320303, 0.9)  # 徐州市云龙区
    # set_location(405, 320311, 0.9)  # 徐州市泉山区
    # set_location(194, 320371, 0.9)  # 徐州市经济开发区（无地图，暂未处理）


def main(env):
    """为了区分不同环境抽象出来的函数"""
    global conn_api, cur_api, conn_rpc, cur_rpc
    if env == 'build':
        conn_api, cur_api = connection('api-330-build')
        conn_rpc, cur_rpc = connection('rpc-analysis-build')
        process()
    elif env == 'preview':
        server1, server2 = get_server2('ubuntu', 'rpc-analysis-preview', 'api-330-preview')
        # 注意，如果要加as结构，是在with后的每个变量加，示例：
        # with server1 as s1, server2 as s2:
        with server1, server2:
            # print(server1.local_bind_port)
            conn_rpc, cur_rpc = connection('rpc-analysis-preview', ssh=True, port=server1.local_bind_port)
            conn_api, cur_api = connection('api-330-preview', DictCursor=False, ssh=True, port=server2.local_bind_port)
            process()
            conn_rpc.close()
            conn_api.close()
    elif env == 'production':
        server1, server2 = get_server2('ubuntu', 'rpc-analysis-production', 'api-330-preview')
        with server1, server2:
            conn_rpc, cur_rpc = connection('rpc-analysis-production', ssh=True, port=server1.local_bind_port)
            conn_api, cur_api = connection('api-330-preview', DictCursor=False, ssh=True, port=server2.local_bind_port)
            process()
            conn_rpc.close()
            conn_api.close()


if __name__ == '__main__':
    # 平常注释掉，避免误执行
    # main('build')
    # main('preview')
    # main('production')
    pass
