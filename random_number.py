def random_number():
    rand_digits = []
    import random
    for i in range(3):
        while True:
            rand_num = random.randint(0, 9)
            if rand_num not in rand_digits:
                rand_digits.append(rand_num)
                break
    rand_digits = tuple(rand_digits)
    return rand_digits
