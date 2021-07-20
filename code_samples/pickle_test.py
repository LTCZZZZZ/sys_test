# pickle模块主要函数的应用举例
import pickle

if __name__ == '__main__':
    dataList = [[1, 1, 'yes'],
                [1, 1, 'yes'],
                [1, 0, 'no'],
                [0, 1, 'no'],
                [0, 1, 'no']]
    dataDic = {0: [1, 2, 3, 4],
               1: ('a', 'b'),
               2: {'c': 'yes', 'd': 'no'}}

    # 使用dump()将数据序列化到文件中
    fw = open('dataFile.txt', 'wb')
    # Pickle the list using the highest protocol available.
    pickle.dump(dataList, fw, -1)
    # Pickle dictionary using protocol 0.
    pickle.dump(dataDic, fw)
    fw.close()

    # 使用load()将数据从文件中序列化读出
    fr = open('dataFile.txt', 'rb')
    data1 = pickle.load(fr)
    print(data1)
    data2 = pickle.load(fr)
    print(data2)
    # data3 = pickle.load(fr)
    # print(data3)
    fr.close()

    # 注意：dumps(), loads() 和dump(), load()是不同的
    # 使用dumps()和loads()举例
    # p = pickle.dumps(dataList)
    # # print(p)
    # print(pickle.loads(p))
    # p = pickle.dumps(dataDic)
    # print(pickle.loads(p))
