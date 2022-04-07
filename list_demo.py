"""
Изменения

"""
x = 10.0 + 2
y = 100
z = -10
test_str_value = 'hello'

our_first_list = [x, y, z]
'''print(type(our_first_list))
print(type(our_first_list[0]))
print(help(our_first_list))'''

###изъятие элементов###
'''our_first_list.append(test_str_value)
print(our_first_list)
our_string_back = our_first_list.pop()
print(our_string_back)
print(our_first_list)
our_first_list.pop(0)'''

number_list = []
for i in range(10):
    number_list.append(i)

print(number_list)
print(number_list[1])

'''length_of_list = len(number_list)
print(number_list)
print(number_list[length_of_list-1])
print(number_list[-4])
'''
#срезы
print(number_list[1:5])
print(number_list[2:5:2])
print(number_list[::2])
print(number_list[::-2])
1
for element in number_list[2::2]:
    print(element)