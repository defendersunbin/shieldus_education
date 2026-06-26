#모듈: 외부에 있는 모듈을 사용
# import mod1
# import mod1 as md
# from mod1 import PI, add, sub
from mod1 import *
# from mod.mod2 import *

print('__name__ :', __name__)

print(PI)
print(add(10, 2))
print(sub(5, 2))
print(sub(2, 5))

# print(md.PI)
# print(md.add(6, 3))
# print(md.sub(6, 4))
# print(md.sub(4, 5))

# print(mod1.PI)
# print(mod1.add(5, 2))
# print(mod1.sub(5, 2))
# print(mod1.sub(2, 5))

def start():
    print('start')

if __name__ == '__main__':
    start()