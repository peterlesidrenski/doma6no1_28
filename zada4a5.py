def is_special_number(number, n):
    for digit in str(number):
        if int(digit) == 0 or n % int(digit) != 0:
            return False
    return True
def generate_special_numbers(n):
    special_numbers = []
    for number in range(1111, 10000):
        if is_special_number(number, n):
            special_numbers.append(number)
    return special_numbers
N = int(input("Въведете цяло число N: "))
special_numbers = generate_special_numbers(N)
print(f"Специални числа за N={N}: {special_numbers}")
