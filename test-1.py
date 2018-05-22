print('hello world!') #输出hello world
10/4
-10/4
10/4.0
-10/4.0
10//4
10%4
0o1,0o20,0o377
1==2<3
1!=2<3
int(10.02323)
float(20)

import math
pow(2,4),2**4
abs(4-16),sum((1,2,3,4))
min(3,1,2,4),max(3,1,2,4)

# 导入随机数模块
import random
# 为'one'赋值=生成一个0到1的随机浮点数
one=random.random()
print(one)

#为‘two’赋值=在qytang、ccie、pass、network中随机选取一个数
two=random.choice(['qytang','ccie','pass','network'])
print(two)

# 随机产生IP地址四个段落的数字
section1=random.randint(1,255)
section2=random.randint(1,255)
section3=random.randint(1,255)
section4=random.randint(1,255)
random_ip=str(section1) +'.' +str(section2)+'.'+str(section3)+'.'+str(section4)

print(random_ip)
