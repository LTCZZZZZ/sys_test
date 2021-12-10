def total(basis=950, add=330, per=1.0, cri_r=0.8, cri_d=1.6, ele=0.435):
    """
    :param basis: 攻击力
    :param add: 附加攻击力
    :param per: 比例加成攻击力
    :param cri_r: 暴击率
    :param cri_d: 暴击伤害
    :param ele: 元素伤害加成
    :return:
    """
    res = (basis * (1 + per) + add) * (1 + cri_r * cri_d) * (1 + ele)
    print(res)
    return res


total()
total(per=1)
total(cri_r=1)
total(cri_d=2)
total(per=2, cri_r=0.05, cri_d=0.5, ele=0)
total(per=1.5, cri_r=0.05, cri_d=0.5)
total(per=0.466 * 3 + 0.25 * 5, add=411, cri_r=0.05, cri_d=0.5)
total(per=0.5, cri_r=1, cri_d=2)

total(per=0.5, cri_r=0.8, cri_d=1.6)
total(per=0.7, cri_r=0.8, cri_d=1.6)
total(per=0.5, cri_r=0.95, cri_d=1.6)
total(per=0.5, cri_r=0.8, cri_d=1.9)

total(per=0.5, cri_r=0.5, cri_d=1)
total(per=0.7, cri_r=0.5, cri_d=1)
total(per=0.5, cri_r=0.65, cri_d=1)
total(per=0.5, cri_r=0.5, cri_d=1.3)

total(per=0.5, cri_r=1, cri_d=2)
total(per=0.7, cri_r=1, cri_d=2)
total(per=0.5, cri_r=1, cri_d=2.3)
# 结论，暴击伤害在200%以上之后，加百分比攻击力收益更高

# res = (basis * (1 + per) + add) * (1 + cri_r * cri_d) * (1 + ele)
# 假设cri_d = 2 * cri_r，
# 则res对cri_r的偏导数为(basis * (1 + per) + add) * (1 + 4 * cri_r) * (1 + ele)
# 则res对per的偏导数为(basis) * (1 + 2 * cri_r**2) * (1 + ele)

def total_r(basis=950, add=330, per=1.0, cri_r=0.8, cri_d=1.6, ele=0.435):
    res = (basis * (1 + per) + add) * (1 + 4 * cri_r) * (1 + ele)
    print(res)
    return res


def total_p(basis=950, add=330, per=1.0, cri_r=0.8, cri_d=1.6, ele=0.435):
    res = (basis) * (1 + 2 * cri_r**2) * (1 + ele)
    print(res)
    return res


# 差别这么大，除了还需要乘以相对系数以外，肯定还有哪里有问题
total_r()
total_p()
total_r(per=0, cri_r=0.05)
total_p(per=0, cri_r=0.05)
total_r(per=0.5, cri_r=0.25)
total_p(per=0.5, cri_r=0.25)
