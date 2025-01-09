
def is_password_strong(password):
    if len(password) < 6:
        return False

    has_digit = False
    has_letter = False

    for i in range(len(password)):
        if '0' <= password[i] <= '9':
            has_digit = True
        elif ('a' <= password[i] <= 'z') or ('A' <= password[i] <= 'Z'):
            has_letter = True

        if has_digit and has_letter:
            return True

    return False



print(is_password_strong("abc123"))

def nearest_number(numbers, target=0):
    if len(numbers) == 0:
        return None


    closest = numbers[0]

    for num in numbers:
        if abs(num - target) < abs(closest - target):
            closest = num

    return closest


# Пример использования
print(nearest_number([1, 2, 3], 5))
print(nearest_number([10.5, 3.2, -1.7], 2))
print(nearest_number((-10, -5, 0, 5, 10), -3))
print(nearest_number((1, 2, 3)))



