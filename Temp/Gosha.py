tmp = [int(i) for i in input().split(' ')]
n = tmp[0]
k = tmp[1]
arr = input()

let_dict = dict()
i = 0
while i < len(arr) - n:
    slice=arr[i:i + n]
    if not slice in let_dict.keys():
        let_dict[slice] = [i, 1]
    else:
        let_dict[slice][1] += 1

    if let_dict[slice][1] == k:
        print(let_dict[slice][0], end=' ')

    i += 1