def recur(x):
    try:
        recur(x)
    except:
        print(1000)

recur(10)