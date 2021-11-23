passport = input()
base = input()

errors = 0
i = 0
j = 0
rez = 0
if abs(len(passport) - len(base)) > 1:
    print('FAIL')
    rez = 1
else:
    while i < len(passport) and j < len(base):
        try:
            if passport[i] == base[j]:
                i += 1
                j += 1
            elif passport[i] == base[j + 1]:
                j += 2
                i += 1
                errors += 1
            elif passport[i + 1] == base[j]:
                i += 2
                j += 1
                errors += 1
            else:
                errors += 1
                i += 1
                j += 1
        except:
            errors += 1
            i += 1
            j += 1

if j < len(base):
    errors += 1
if i < len(passport):
    errors += 1

if errors < 2:
    print('OK')
elif rez == 0:
    print('FAIL')
