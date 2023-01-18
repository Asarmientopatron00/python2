# import this
from package.mod_1 import func_1, func_2
from package.mod_2 import func_3, func_4
import package

a, b, c, d = package.mod_1.func_1(), package.mod_1.func_2(), package.mod_2.func_3(), package.mod_2.func_4()
print(a, b, c, d, package.URL)
