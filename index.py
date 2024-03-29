# 主要记录题目中关于索引的相关知识

# 题号：模拟一简单应用202.py
# 以下为源代码

data = input()  # 姓名 年龄 性别
s=0
n=0
i=0
while data:
    i=i+1
    ls=data.split()
    s=s+int(ls[2])
    if ls[1]=='男':
        n=n+1
    data = input()
s= s/i
print("平均年龄是{:.2f} 男性人数是{}".format(s,n))

'''
第一行 data = input()  # 姓名 年龄 性别 使用 input() 函数从标准输入中读取一行数据，赋值给变量 data，并在右侧用 # 注释说明数据的格式。
第二行 s=0 定义一个变量 s，用来存储年龄的总和，初始值为 0。
第三行 n=0 定义一个变量 n，用来存储男性的人数，初始值为 0。
第四行 i=0 定义一个变量 i，用来存储输入的行数，初始值为 0。
第五行 while data: 使用 while 循环，当 data 不为空时，执行循环体内的语句。
第六行 i=i+1 将 i 的值加 1，表示读取了一行数据。
第七行 ls=data.split() 使用 split() 方法将 data 字符串按空格分割，得到一个列表 ls，其中包含姓名、年龄和性别三个元素。
第八行 s=s+int(ls[2]) 将 ls 列表的第三个元素（年龄）转换为整数，然后加到 s 上，累计年龄的总和。
第九行 if ls[1]=='男': 使用 if 语句判断 ls 列表的第二个元素（性别）是否等于 '男'，如果是，执行下一行语句。
第十行 n=n+1 将 n 的值加 1，表示男性的人数增加了 1。
第十一行 data = input() 再次使用 input() 函数从标准输入中读取一行数据，赋值给变量 data，以便进行下一次循环判断。
第十二行 s= s/i 循环结束后，将 s 的值除以 i，得到平均年龄，赋值给 s。
第十三行 print("平均年龄是{:.2f} 男性人数是{}".format(s,n)) 使用 print() 函数输出结果，使用 format() 方法将 s 和 n 的值插入到字符串中，其中 {:.2f} 表示保留两位小数。
'''
