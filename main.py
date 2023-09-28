numbers = [1,2,3,4,5]
sum = sum(numbers)
print(sum)


max = 0
index_of_max = -1
s = input().split(' ')
len = 0
for i in s:
    i = int(i)
    if i > max:
        max = i
        index_of_max = len
    len += 1
print(max, index_of_max)


ints_list = [1, 2, 3, 4, 3, 2]
for x in ints_list:
    if ints_list.count(x) > 1:
        ints_list.remove(x)
print(ints_list) # [1, 2, 3, 4]



listik1 = [444,242,259,81]
listik2 = [1,4,3,5,9]
listik3 = listik1 + listik2
print(listik3)



numbers =
print(sum(numbers))
# требуемый вывод:
# 45
long_word = (
    'т', 'т', 'а', 'и', 'и', 'а', 'и',
    'и', 'и', 'т', 'т', 'а', 'и', 'и',
    'и', 'и', 'и', 'т', 'и'
)
print("Количество 'т':", )
print("Количество 'a':", )
print("Количество 'и':", )
# требуемый вывод:
# Колличество 'т': 5
# Колличество 'а': 3
# Колличество 'и': 11
week_temp = (26, 29, 34, 32, 28, 26, 23)
sum_temp =
days =
mean_temp = sum_temp / days
print(int(mean_temp))
# требуемый вывод:
# 28


a= input()
b=input()
print(a)
print(b)
print(a+b)
x=len(a)
x1=len(b)
if x>x1:
    print(a)
if x<x1:
    print(b)
if x==x1:
    print("размер одинаковый")