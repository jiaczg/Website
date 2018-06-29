# 如果一个可迭代对象的元素个数超过变量个数时，会出现”太多解压值”的异常。
# 那么怎样才能从这个可迭代对象中解压出N个元素出来？

record = ('Jiaczg', 'wujiac', 'chenm', 'jiaczg@gmail.com', '773-555-899', '886-557-433')
name, name2, name3, email, *phone_numbers = record
print(name, name2, name3)
print(email)
print(*phone_numbers)
# phone_numbers变量永远都是列表类型，不管解压的电话号码数量是多少(包括0个)。