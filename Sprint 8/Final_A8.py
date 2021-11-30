'''
ID 59444723
1. Распаковываем рекурсией все слова
2. Циклом перебираем их, выделяя общий префикс
'''



def num_let(s):
    i = -1
    if s.isdigit():
        return '', int(s)
    else:
        while s[i].isdigit() and -i <= len(s):
            i -= 1
        i += 1
        return s[:i], int(s[i:])


def unpack(s):
    rez = ''
    while s[z[0]] != ']':
        if s[z[0]] == '[':
            z[0] += 1
            let, nums = num_let(rez)
            rez = let + nums * unpack(s)
            z[0] = min(z[0] + 1, len(s) - 1)
        else:
            rez += s[z[0]]
            z[0] += 1
            if z[0] == len(s): break
    return rez


def det_pref(s1, s2):
    r = 0
    l = min(len(s1), len(s2))
    while s1[r] == s2[r]:
        r += 1
        if r == l: break
    return (s1[:r])


z = []
z.append(0)

n = int(input())
s1 = unpack(input())
for i in range(n - 1):
    z[0] = 0
    s2 = unpack(input())
    s1 = det_pref(s1, s2)

print(s1)
