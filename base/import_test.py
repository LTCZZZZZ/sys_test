# 可以看到，此包直接导入test0，且，通过test1又间接导入了test0，
# 但是，test0只被导入了一次，因为python会缓存已经导入的模块，下次再导入时，会直接从缓存中取出，而不会再次执行模块中的代码。
# 结果也可以证明这一点，test0中的print语句只执行了一次，且，a = a1 = 1
from test0 import a
from test1 import a as a1


print(__name__, 'a =', a)
print(__name__, 'a1 = ', a1)
