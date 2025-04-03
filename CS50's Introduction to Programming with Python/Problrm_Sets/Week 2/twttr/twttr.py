x = input("Input: ")
v = ['A','a','E','e','I','i','O','o','U','u']

s = ""
for i in x:
    if i not in v:
        s+=i
print("Output: "+s)
