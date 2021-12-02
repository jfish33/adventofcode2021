my_int_list = list(map(int, open("data_file.txt").read().split("\n")))
comp_count = 0

i = 1
while i < len(my_int_list):
    if my_int_list[i] > my_int_list[i-1]:
        comp_count += 1
    i += 1

print (comp_count)
