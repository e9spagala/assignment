from typing import Dict
mapper: Dict[str, int] = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20}

for key in mapper.keys():
    print(key)

for val in mapper.values():
    print(val)

for key, val in mapper.items():
    print(f'{key} + two: {str(val + 2)}')