x = input("Greeting:")
y = x.lower().replace(" ","")

if (y[:5] == "hello") :
    print("$0")
elif (y[0] == "h") and (y[:5] != "hello") :
    print("$20")
else :
    print("$100")
