#digits = [1, 2, 3]  # digits: Sample input
def stat3(digits): #stat1(): function for statment 1
    import random
    #digits=(1, 2, 3) #digits: Sample input in the form of tuple so that it won't change its value.
    index_pos_of_wrong_num=random.randint(0, 2)
    s1 = list(digits)  # s1: a variable used to store the value of digits in the form of list so as to make it mutable.
    new_randomnum_is_unique = True
    while new_randomnum_is_unique:
        wrong_num = random.randint(0, 9)
        if wrong_num not in digits:
            s1[index_pos_of_wrong_num] = wrong_num
            new_randomnum_is_unique = False
    all_num_in_diff_pos = False
    t = 0
    s1 = tuple(s1)
    s2 = list(s1)
    while all_num_in_diff_pos==False:
        random.shuffle(s2)
        for i in range(3):
            if s2[i] == s1[i]:
                t = t+1
        if t == 0:
            all_num_in_diff_pos = True
            break
        else:
            t = 0
            continue
    print(s2[0], '', s2[1], '', s2[2], ": Two numbers are correct and wrong placed")
