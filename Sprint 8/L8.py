def prefix_function(s):
    # Функция возвращает массив длины |s|
    p = [None] * len(s)
    p[0] = 0
    for i in range(1, len(s)):
        k = p[i - 1]
        while (k > 0) and (s[k] != s[i]):
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p

s = input()
arr = prefix_function(s)
print(*arr)
