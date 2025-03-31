x = input("File name:")
y = x.lower().replace(" ","")

if y.endswith(".gif"):
    print("image/gif")
elif y.endswith(".jpg"):
    print("image/jpeg")
elif y.endswith(".jpeg"):
    print("image/jpeg")
elif y.endswith(".png"):
    print("image/png")
elif y.endswith(".pdf"):
    print("application/pdf")

elif y.endswith(".txt"):
    z = y[:-4]
    print(f"text/{z}")

elif y.endswith(".zip"):
    print("application/zip")
else :
    print("application/octet-stream")
