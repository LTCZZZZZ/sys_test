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
    set_location(74, (118.350336, 118.440000), (31.203389, 31.312751))  # 芜湖市弋江区


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
