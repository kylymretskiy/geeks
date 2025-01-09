data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

for symbol in data_tuple:
    if type(symbol) == str:
        letters.append(symbol)
    else:
        numbers.append(symbol)

del numbers[0:2]
letters.append(True)
numbers.insert(1, 2)
numbers.sort()
letters.reverse()
letters[1] = letters[1].upper()
letters[-2] = letters[-2].lower()
numbers = [number ** 2 for number in numbers]
numbers_tuple = tuple(numbers)
letters_tuple = tuple(letters)


print(numbers_tuple)
print(letters_tuple)