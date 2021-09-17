def input_number():
    input_digits = []
    input_num = input("Enter the number: ")
    for i in input_num:
        #a=int(input())
        input_digits.append(int(i))
    input_digits =tuple(input_digits)
    #print(input_digits)

    return input_digits
