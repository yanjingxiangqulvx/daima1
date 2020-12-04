""""
# 查看acill码值
print(ord('a'))

# 取字符串前五位的值
print('hello world'[:5])
# 查看数据的内存地址
a = 1
b = 2
c = a if a > b else b
print(c)
print(id(a))

# 判断字符类型
print(isinstance(a,(int)))
f = ['纵火盛宴','破碎护盾']
print(f[0:2])

for q in ['纵火盛宴','恒温灼烧','电子鱼叉','破碎护盾']:
    print(q)
for index,item in enumerate(['纵火盛宴','恒温灼烧','电子鱼叉','破碎护盾']):
    print(index,item)
x = {1:'A',2:'B',3:'C'}
print(x[2])
for key in x.keys():
    print(x[key])
"""
"""
account = 'admin'
password = '123456'

print('input your username')
account_lg = input();
print('input your password')
password_lg = input();

if(account_lg != account):
    print('用户名输入错误')
elif(password_lg != password):
    print('密码输入错误')
else:
    print('登录成功')
"""

"""
x = 1
while  x <= 10:
    print(x)
    x+=1
else:
    print("else:",x)
"""

a = [1,2,3,4,5,6,7,8,9,10]
for index in range(0,10,2):
    print(a[index] ,end = ' | ')

for x in a:
    if x % 2 == 0:
        continue
    print(x ,end = ' | ')

# 列表的切片
for x in a[::2]:
    print(x, end = ' | ')