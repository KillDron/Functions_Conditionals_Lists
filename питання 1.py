def mysort(mylist=[], numflag=False)
    L = []
    if numflag == False:
        for i in mylist:
            L.append(str(i))
        print(sorted(L))
    elif numflag == True:
        for i in mylist:
            L.append(int(i))
        print(sorted(L)