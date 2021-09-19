def is_sorted(lst):
    if lst == sorted(lst):
        return True
    elif lst == sorted(lst, reverse=True):
        return False
print(is_sorted([1, 2, 3]))
print(is_sorted([3, 2, 1]))
