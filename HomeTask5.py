my_list = [1, 2, 3, 4, 5, 6, 7]
k = 5
a = my_list[k]
my_list.remove(a)
my_list.append(a)
print(my_list.pop())
print(my_list)
