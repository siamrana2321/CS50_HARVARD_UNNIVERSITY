a = 50
print(f"Amount Due: {a}")
t = True
while t :
    x = int(input("Insert Coin:"))
    if (x==5) or (x==10) or (x==25) :
        a = a - x
        if a>0 :
            print(f"Amount Due: {a}")
        elif a==0 :
            print(f"Change Owed: {a}")
            t = False
        else :
            print(f"Change Owed: {abs(a)}")
            t = False
    else :
        print(f"Amount Due: {a}")


