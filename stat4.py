#digits = [1, 2, 3]  # digits: Sample input
def stat4(digits): # stat1(): function for statment 1
    import random
    #digits = (1, 2, 3)  # digits: Sample input in the form of tuple so that it won't change its value.
    s1 = list(digits)  # s1: a variable used to store the value of digits in the form of list so as to make it mutable.
    for i in range(3):
        while True:
            r = random.randint(0, 9)
            if r not in s1 and r not in digits:
                s1[i] = r
                break

    print(s1[0], '', s1[1], '', s1[2], ": Nothing is correct")

