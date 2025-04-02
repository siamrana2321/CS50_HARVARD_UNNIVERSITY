x = input("camelCase:")

snake = ""

for i in x:
    if i.isupper() :
        snake+=("_"+i.lower())
    else :
        snake+=i

snake = snake.lstrip("_")

print(snake)

