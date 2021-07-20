class DataSet(object):
    @property
    def method_with_property(self):  ##含有@property
        return 15

    def method_without_property(self):  ##不含@property
        return 15

    def __init__(self):
        self._images = 1
        self._labels = 2  # 定义属性的名称

    @property
    def images(self):  # 方法加入@property后，这个方法相当于一个属性，这个属性可以让用户进行使用，而且用户有没办法随意修改。
        return self._images

    @property
    def labels(self):
        return self._labels


l = DataSet()
print(l.method_with_property) # 加了@property后，可以用调用属性的形式来调用方法,后面不需要加()，如果加会报错(除非此属性返回一个函数)。
print(l.method_without_property())  #没有加@property , 必须使用正常的调用方法的形式，即在后面加()

print(l.images)
l._images = 20
print(l.images)
