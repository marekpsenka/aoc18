import fileinput

chars = list(next(map(str.rstrip, fileinput.input())))

index = 0

while index < len(chars) - 1:
    if (chars[index].lower() == chars[index + 1].lower()) and (
        (chars[index].isupper() and chars[index + 1].islower())
        or (chars[index].islower() and chars[index + 1].isupper())
    ):
        del chars[index : (index + 2)]
        index = max(0, index - 1)
    else:
        index += 1

print(len(chars))
