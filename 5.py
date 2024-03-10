def smallest_number_divisible_by_1_20():
    num = 1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20
    for i in range(num):
        for j in range(21):
            if i%j !=0:
                i = i+1
                break
smallest_number_divisible_by_1_20