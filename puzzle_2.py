my_int_list = list(map(int, open("data_file.txt").read().split("\n")))
sum_list = []
c = 0
i = 0

while i+2 < len(my_int_list):
    sum_list.append(my_int_list[i] + my_int_list[i+1] + my_int_list[i+2])
    i += 1

k=1
while k < len(sum_list):
    if sum_list[k] > sum_list[k-1]:
        c += 1
    k += 1


print (c)
