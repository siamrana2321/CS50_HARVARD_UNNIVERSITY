x = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
y = x.lower().replace(" ","")

if (y == "42") or (y == "forty-two") or (y == "fortytwo") :
    print("Yes")
else :
    print("No")
