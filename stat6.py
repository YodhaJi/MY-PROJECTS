#digits=(4,1,9)
def stat6(digits):
    import random
    index_list = []
    while len(index_list) < len(digits)-1:
        r=random.randint(0, 2)
        if r not in index_list:
            index_list.append(r)
        else:
            pass
    s = digits[index_list[0]]**2 - digits[index_list[1]]**2
    print(abs(s), "     : difference of Square of any two digits ")