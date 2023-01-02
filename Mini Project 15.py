x=int(input("Enter a number x: "))
y=int(input("Enter a number y: "))
prime=0
composite=0
for i in range(x,y+1):
    dc=0
    for y in range(2,x):
        if i%y==0:
            dc=dc+1
        else:
            pass
    if dc==0:
        print(i,"is prime")
        prime+=1
    else:
        print(i,"is composite")
        composite+=1
print("Count:",prime,"prime and",composite,"composite numbers in the given range")