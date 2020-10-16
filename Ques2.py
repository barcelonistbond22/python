
again='y'
while again=="y" or again=="Y":
    haystack=input("enter a word: ")
    needle=input("enter another word: ")
    if needle in haystack:
        print(haystack.index(needle))
    else:
        print("-1")

    again=input("do you want to continue ? (Y/N): ")
    print()
print("...........THANK YOU..........")

