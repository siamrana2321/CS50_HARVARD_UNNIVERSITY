import emoji

x = input("Input: ")
emj = emoji.emojize(x, language='alias')
print(f"Output: {emj}")
