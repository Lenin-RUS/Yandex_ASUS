n = int(input())
Csent = dict()
CC = []
for j in range(n):
    l = input()
    C_tmp = ''.join(i for i in l if i == i.upper())
    if C_tmp not in Csent:
        Csent[C_tmp] = [l]
    else:
        Csent[C_tmp].append(l)


m = int(input())

# n=10
# m=10
# Csent={'FHRJXN': ['bFHdRdJaXN'], 'ML': ['MhqzvipuzL'], 'DPSVGU': ['DPSVGjUfuy'], 'EAGPR': ['EpayAivGPR'], 'M': ['Mqlmchycpc'], 'JKLDUI': ['JKLDUIbhzh'], 'AHFHMMZQ': ['AHyiFHMMZQ'], 'EJAGPR': ['EJuoAvxGPR'], 'DCNG': ['hDqCNojsGl'], 'DPSVGUA': ['DsPSVGUApr']}
final_rez=[]


for i in range(m):
    l=input()
    tmp_rez = []
    for k in Csent:

        if k.startswith(l):

            for j in Csent[k]:
                if j not in tmp_rez: tmp_rez.append(j)
    tmp_rez.sort()
    final_rez.append(tmp_rez)

for i in final_rez:
    print(*i, sep='\n')


