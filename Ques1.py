list1=[3,6,5,8]
again='Y'
while again=='Y' or again=='y':
    num=int(input("enetr a number: "))

    if num in list1:
        print(list1.index(num))
    else:
        print('-1')
    again=input("do you wnat to continue? (Y/N) ")
    print()

print("..............THANKYOU.................")

