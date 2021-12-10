import random
import pandas as pd
from connection import connection

# 一般都注释掉，避免误执行
# conn, cursor = connection('api-330-build')
# conn, cursor = connection('api-330-preview', DictCursor=False)

def set_location(edu_id, longitude, latitude):
    # 第一次知道字符串还可以这么结合，网上搜的一般都没有，后来去看官方文档才发现，看来果然还是要看官方文档啊
    # https://docs.python.org/3/tutorial/introduction.html#strings
    cursor.execute('select p.id from institution p left join education_institution q on p.id = q.institution_id ' 
        'where q.education_id = %s and p.type = 2', (edu_id, ))
    id_list = [i[0] for i in cursor.fetchall()]
    print(id_list)

    data = []
    for i in id_list:
        data.append((random.uniform(*longitude), random.uniform(*latitude), i))

    cursor.executemany('update institution set longitude = %s, latitude = %s where id = %s', data)
    conn.commit()


if __name__ == '__main__':
    # set_location(32, (116.395757, 116.430792), (39.867544, 39.955544))  # 北京市崇文区
    # set_location(74, (118.350336, 118.440000), (31.203389, 31.312751))  # 芜湖市弋江区
    # set_location(126, (108.120512, 108.380512), (32.858512, 33.248512))  # 安康市石泉县
    # set_location(108, (113.428117, 113.828117), (31.169888, 31.429888))  # 孝感市安陆市
    # set_location(147, (110.48197, 110.775197), (32.539534, 32.739534))  # 十堰市张湾区
    # set_location(148, (110.637269, 110.937269), (32.448362, 32.608362))  # 十堰市茅箭区(这个区畸形，有点难设置)
    # set_location(152, (104.184704, 104.404704), (30.497396, 30.677396))  # 成都市龙泉驿区
    # set_location(140, (118.236097, 118.356097), (29.679254, 29.799254))  # 黄山市屯溪区
    set_location(168, (98.986097, 99.606097), (23.119254, 23.409254))  # 临沧市沧源县


# api_330_engine = get_engine('api-330-build')
# df1 = pd.read_sql(
#     'SELECT s.id,s.name,s.address,s.longitude,s.latitude from institution s left join education_institution t on s.id = t.institution_id where t.education_id = 1 and s.type = 2;',
#     api_330_engine,
#     index_col=None
# )
# print(df1)
# longitude = []
# latitude = []
# for i in range(2):
#     longitude.append(random.uniform(116.395757, 116.430792))
#     latitude.append(random.uniform(39.867544, 39.955544))
# df1['longitude'] = longitude
# df1['latitude'] = latitude
# print(df1)
# df1.to_sql('institution', api_330_engine, if_exists='update', index=False)
