# N=int(input())
# l=[]
# for number in range(N):
#     l.append(number)
# print(l)

if __name__ == '__main__':
    # n = int(input().strip())
    
    # arr = list(map(int, input().rstrip().split()))
    arr=[1,3,5,6]
    joined_numbers=""
    for number in arr:
        new_string=str(number)
        print(new_string)
        joined_numbers=new_string + " " + joined_numbers
    print(joined_numbers)