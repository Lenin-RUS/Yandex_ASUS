n = int(input())
my_dict = dict()
max_w = 1
for j in range(n):
    s = input()
    if s in my_dict:
        my_dict[s] += 1
        max_w = max(max_w, my_dict[s])
    else:
        my_dict[s] = 1

rez = []
for i in my_dict:
    if my_dict[i] == max_w:
        rez.append(i)
rez.sort()
print(rez[0])
