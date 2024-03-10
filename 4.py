arr = []
def reverse(n):
    global arr
    arr.append(n%10)
    if n>10:
        reverse(n//10)
    return arr
def palindrome(n):
    re = reverse(n)
    re_o = re[::-1]
    if re == re_o:
        return True
    else:
        return False

for i in range(993,99,-1):
    for j in range(914,99,-1):
        if palindrome(i*j):
            count = i*j
            print(i,j)          
        else:           
            j = j-1
    i = i-1



