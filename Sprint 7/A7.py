days = int(input())
price=[int(i) for i in input().split(' ')]

akc = 0
incom = 0
for i in range(days - 1):
    if akc == 0 and price[i] < price[i + 1]:
        akc = 1
        buy = price[i]
    if akc == 1 and price[i] > price[i + 1]:
        akc = 0
        incom += price[i]-buy

if akc ==1: incom += price[-1]-buy

print(incom)