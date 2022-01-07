# -*- coding: utf-8 -*-
import geopandas as gpd

base_dir = '/Users/ltc/Downloads/EasyVCity/'
gdf = gpd.read_file(base_dir + '110000.json')
print(gdf)
# gdf.to_file(base_dir + 'my_file.shp')  # 这个一下会产生5个文件，醉了

# gdf.to_file(base_dir + "my_file.geojson", driver="GeoJSON")  # 这个可能是我会用的更多的

gdf = gdf.set_index("name")


print(gdf.crs)
gdf.plot()
gdf.to_crs(crs='EPSG:2381').plot()
# 参见 https://www.cnblogs.com/feffery/p/12285828.html

gdf["area"] = gdf.to_crs(crs='EPSG:2381').area / 1e6  # 单位是平方公里
print(gdf["area"])
print(gdf.query("1000 < area < 1500"))

