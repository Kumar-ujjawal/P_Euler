##If we list all the natural numbers below that are multiples of 3 or 5 ,we get 3,5,6,9 and. The sum of these multiples is 23.
##Find the sum of all the multiples of 3 or 5 below 1000

def sum_of_mul_of_three(max_counter):
    sum = 0
    for i in range(max_counter):
        if i%3 ==0:
            sum +=i
    return sum

def sum_of_mul_of_five(max_counter):
    sum = 0
    for i in range(max_counter):
        if i%5 ==0:
            sum +=i
    return sum

def sum_of_mul_of_three_and_five(max_counter):
    sum = 0
    for i in range(max_counter):
        if i%3 ==0 and i%5 ==0:
            sum +=i
    return sum

print("the value of the sum under 1000 will be : ",sum_of_mul_of_five(1000)+sum_of_mul_of_three(1000)-sum_of_mul_of_three_and_five(1000))