a = '3[a]2[r2[t]]'

z=[]
z.append(0)
def unpack(s):
    rez = ''
    while s[z[0]] !=']':
        if s[z[0]] == '[':
            z[0] += 1
            rez = rez + unpack(s)
            z[0] = min(z[0]+1, len(s)-1)
        else:
            rez += s[z[0]]
            z[0] += 1
    return rez


print(unpack(a))
