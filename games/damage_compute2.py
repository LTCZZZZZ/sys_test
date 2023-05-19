def total_simple(atk=1754, cri_r=0.8, cri_d=1.6, ele=0.435):
    """
    :param basis: 攻击力
    :param add: 附加攻击力
    :param per: 比例加成攻击力
    :param cri_r: 暴击率
    :param cri_d: 暴击伤害
    :param ele: 元素伤害加成
    :return:
    """
    print(atk, 1 + cri_r * cri_d, 1 + ele)
    res = atk * (1 + cri_r * cri_d) * (1 + ele)
    print(res)
    return res


# total_simple()
a = total_simple(atk=2319, cri_r=0.814, cri_d=1.744, ele=0.466+0.12+0.3375)
b = total_simple(atk=1754, cri_r=0.814, cri_d=2.347, ele=0.466+0.48+0.3375)  # 神乐之真意80级
c = total_simple(atk=1877, cri_r=0.814, cri_d=2.405, ele=0.466+0.48+0.3375)  # 神乐之真意90级
# total_simple(cri_r=0.05, cri_d=0.5, ele=0)

print(b / a)
print(c / a)
