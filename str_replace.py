n = input()
size = len(n) // 2
lst = list(n)
lst[size] = '*'
str1 = '*'
print(str1.join(lst))
