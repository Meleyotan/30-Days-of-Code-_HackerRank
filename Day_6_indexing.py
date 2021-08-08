# name="abcdef"
# l=[]
# j=[]
# seperator=','
# for letter in name:
#     if name.index(letter)==0 or name.index(letter)%2:
#         new_letter=letter
#         l.append(new_letter)
#     else:
#         j.append(letter)

# print(l)
# print(seperator.join(l))
# print(j)
# print(seperator.join(j))
# # print(index, letter)

# # T=int(input())
# a="my"
# b="name"
# print(a + b)
S=str(input())
# if len(S)==0:
#     S="Hacker"
N=len(S)
try:
    final_even_word=""
    final_odd_word=""
    for number in range(N):
        if number == 0 or number % 2 == 0:
            new_even_letter=S[number]
            final_even_word = final_even_word + new_even_letter
        else:
            new_odd_letter = S[number]
            final_odd_word= final_odd_word+new_odd_letter
except:
    print("Please try again! You can do better.")

print(final_even_word + " " + final_odd_word)
