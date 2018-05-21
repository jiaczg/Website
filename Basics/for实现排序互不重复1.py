#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
#程序分析：可填在百位、十位、个位的数字都是1、}2、3、4。组成所有的排列后再去 掉不满足条件的排列。


# python range() 函数可创建一个整数列表，一般用在 for 循环中。
# 函数语法
# range(start, stop[, step])
# 参数说明：
# start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
# stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
# step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)


# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if(i != j)and(i != k)and(j != k):
#                 print(i,j,k)

                 

# 指出三位数的数量，添加无重复三位数的数量

sun = [1,2,3,4,5,6,7,8,9,10]
i = 0
for a in sun:
    for b in sun:
        for c in sun:
            if (a != b) and (a != c) and (c != b):
                i += 1   # 每次循环i会加1
                print(a,b,c)
print('总数量:', i)


