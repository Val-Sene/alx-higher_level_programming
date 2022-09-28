def uniq_add(my_list=[]):
    unique_list = set(my_list)
    res = 0

    for i in unique_list:
        res += i

    return (res)
