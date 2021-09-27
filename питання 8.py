list=['one', 'two', 'three', 'four', 'five']
def mysort(mylist = [], numflag = False):
    if numflag == False:
        mylist.sort(key = lambda x: x[0])
    else:
        mylist.sort(key = len)
    return print(mylist)
mysort(list)
mysort(list, True)
print('DONE')
