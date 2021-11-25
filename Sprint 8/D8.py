def det_pref(s1, s2):
    r = 0
    l = min(len(s1), len(s2))
    while s1[r] == s2[r]:
        r += 1
        if r == l: break
    return (s1[:r])


n = int(input())
s1 = input()
rez = 0
for i in range(n - 1):
    s2 = input()
    if len(s2) == 0 or len(s1) == 0:
        print(0)
        rez = 1
        break
    s1 = det_pref(s1, s2)

if rez == 0: print(len(s1))
