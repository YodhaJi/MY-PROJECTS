#digits = [1, 2, 3]  # digits: Sample input
def stat1(digits): #stat1(): function for statment 1
    import random
    #digits = (1, 2, 3)  # digits: Sample input in the form of tuple so that it won't change its value.
    index_list = []  # index_list: a list which will hold the value of index postion
    s1 = list(digits)  # s1: a variable used to store the value of digits in the form of list so as to make it mutable.
    two_diff_num=True
    while two_diff_num == True and len(index_list) < 2:
        r = random.randint(0, 2)
        if r not in index_list:
            index_list.append(r)
    for j in index_list:
        new_num_is_unique = True  # new_num_is_unique: a condition which says that the number generated in the form of new_num is unique to digits and s1
        while new_num_is_unique == True:
            new_num = random.randint(0, 9)
            if new_num not in digits and new_num not in s1:
                s1[j] = new_num #new_num is assigned to s1 at index 2
                break
            else:
                continue
    hint="one number is correct and in correct position"
    print(s1[0], '', s1[1], '', s1[2], ": One number is correct and well placed.")
    #print(s1)  # new numbers

