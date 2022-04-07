number_list = []
for i in range(20):
    number_list.append(i)
    if i % 10 == 0:
        number_list[i] = -i
        print(number_list)
        #number_list.clear()
#print(number_list.count('cat'))
#print(number_list)
#number_list.sort()
#print(number_list)
sorted_list = sorted(number_list)
#print(number_list)
#rint(sorted_list)

sorted_list = sorted(number_list, reverse=True)

