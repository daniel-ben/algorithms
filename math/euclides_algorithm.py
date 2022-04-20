def findGCD(big_num, small_num):

    if big_num < small_num:
        big_num, small_num = small_num, big_num
    
    if small_num == 0:
        return big_num
    elif big_num % small_num == 0:
        return small_num
    else:
        return findGCD(small_num, big_num % small_num)
