n = int(input())
comands = []
main_dict = dict()


def apply_comand(comand):
    if comand[0] == 'put':
        main_dict[comand[1]] = comand[2]
    if comand[0] == 'get':
        if not comand[1] in main_dict:
            return 'None'
        else:
            return main_dict[comand[1]]
    if comand[0] == 'delete':
        return main_dict.pop(comand[1], 'None')


for i in range(n):
    comands = [i for i in input().split(' ')]
    rez = apply_comand(comands)
    if rez != None: print(rez)
