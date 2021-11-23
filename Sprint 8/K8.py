A = input()
B = input()

my_list_1 = [i for i in A if ord(i) % 2 == 0]
my_list_2 = [i for i in B if ord(i) % 2 == 0]

if my_list_1 < my_list_2:
    print(-1)
elif my_list_1 > my_list_2:
    print(1)
else:
    print(0)
