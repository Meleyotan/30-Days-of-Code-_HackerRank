n=int(input().strip())
count_consecutive_1=0
max=0

while n >= 2:
    quotient=n//2
    remainder=n%2

    if remainder==1:
        count_consecutive_1+=1
    else:
        count_consecutive_1=0
    if quotient==1:
        count_consecutive_1+=1


    if count_consecutive_1>max:
        max=count_consecutive_1   
    
    
    
    n=quotient

    print("The whole number part:", quotient)
    print("The remainder and the binary:",remainder)
    print("The total number of 1s", count_consecutive_1)
    print("The number of highest consecutive 1s:", max)