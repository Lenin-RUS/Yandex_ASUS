i= int(input())
def catalan(n):
    if n >= 2:
        c = ((2 * ((2*n) - 1)) / (n+1)) * catalan(n-1)
        return int(c)
    return 1

print(catalan(i))