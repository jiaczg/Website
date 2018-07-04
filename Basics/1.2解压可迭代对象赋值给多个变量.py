# 如果一个可迭代对象的元素个数超过变量个数时，会出现”太多解压值”的异常。
# 那么怎样才能从这个可迭代对象中解压出N个元素出来？
# 迭代解压语法是专门为解压不确定个数或任意个数元素的可迭代对象而设计的

record = ('Jiaczg', 'wujiac', 'chenm', 'jiaczg@gmail.com', '773-555-899', '886-557-433')
name, name2, name3, email, *phone_numbers = record
print(name, name2, name3)
print(email)
print(*phone_numbers)
print('############################################')


# 你有一个公司前8个月销售数据的序列，最近一个月数据和前面7个月的平均值的对比。
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing, current)
trailing_avg = sum(trailing)/len(trailing)
print(trailing_avg)
print('############################################')


# 星号表达式在迭代元素为可变长元组的序列时是很有用的。
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]
def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
print('############################################')


# 星号解压语法在字符串操作的时候也会很有用，比如字符串的分割。
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
name, *number, homedir, sh = line.split(':')
print(name)
print(homedir)
print(number)
print(sh)
print('############################################')


# 你想解压一些元素后丢弃它们，你不能简单就使用*，但是你可以使用一个普通的废弃名称，比如_或者ign。
recorda = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, numbers) = recorda
print(name)
print(numbers)
print('############################################')


# 如果你有一个列表，你可以很容易的将它分割成前后两部分
items = [1, 10, 7, 4, 5, 9, 10, 8, 6]
head, *tail = items
print(head)
print(tail)
print('############################################')

# 如果你够聪明的话，还能用这种分割语法去巧妙的实现递归算法
items = [1, 10, 7, 4, 5, 9, 10, 8, 6]
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
print(sum(tail)) 