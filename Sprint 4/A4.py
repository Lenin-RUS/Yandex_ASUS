n = int(input())
primary_dict = dict()
for i in range(n):
    for j in input().split(' '):
        if not j in primary_dict.keys():
            primary_dict[j] = [i]
        else:
            primary_dict[j].append(i)

m = int(input())
final_rez = []
for i in range(m):
    secondary_dict = dict()
    for a in input().split(' '):
        if a in primary_dict.keys():
            pr_num = primary_dict[a]
            for j in pr_num:
                if not j in secondary_dict:
                    secondary_dict[j] = 1
                else:
                    secondary_dict[j] += 1
    rez = list(secondary_dict.items())
    rez.sort(key=lambda i: i[1], reverse=True)
    rez = (i[0] + 1 for i in rez[0:5])
    final_rez.append(rez)

for i in final_rez:
    print(*i)
