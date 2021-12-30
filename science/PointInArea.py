# -*- coding: utf-8 -*-
# 判断一个点是否在在区域内

import shapely.geometry as geo

poly = geo.Polygon(([0, 0], [0, 2], [2, 2], [2, 0]))

print(poly)  # 在jupyter中直接输出的是一个多边形图形，这兼容性，我惊了
print(poly.svg())

multi_poly = geo.MultiPolygon([
    (
        ((0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (1.0, 0.0)),
        [((0.1, 0.9), (0.2, 0.9), (0.2, 0.8), (0.1, 0.8)),
         ((0.1, 0.1), (0.2, 0.1), (0.2, 0.2), (0.1, 0.2))]
    )
])
print(multi_poly)
print(multi_poly.area)

p = geo.Point(0.15, 0.15)
print(multi_poly.intersects(p))  # 是否有交点
p = geo.Point(0.3, 0.3)
print(multi_poly.within(p))  # 是否在p内
print(multi_poly.contains(p))  # 是否包含点p

print(poly.within(multi_poly))
print(poly.contains(multi_poly))

geo.GeometryCollection([multi_poly, p])


