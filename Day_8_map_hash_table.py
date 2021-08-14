
n=int(input())

phone_book={}

for i in range(n):
    name=str(input())
    phone_number=str(input())
    phone_book[name]=(phone_number)

while True:#indefinite loop
    try:
        queries=str(input("What are you searching for?").lower())
        if queries in phone_book and len(queries)!=0:
            search_result=(str(queries) + "=" + str(phone_book[queries]))
            print(search_result)
        else:
            print("Not found")
    except:
        break

print(phone_book)
