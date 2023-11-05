import fileinput
from typing import List

chars = list(next(map(str.rstrip, fileinput.input())))

unique_letters = set(map(lambda c: c.lower(), chars))


def react(chars: List[str]) -> int:
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
    return len(chars)


def remove_unit(char: str, chars: List[str]) -> List[str]:
    return list(filter(lambda c: c.lower() != char, chars))


print(min(react(remove_unit(k, chars.copy())) for k in unique_letters))
