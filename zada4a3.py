def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

sum_prime = 0
sum_non_prime = 0

while True:
    input_str = input()
    
    if input_str == "stop":
        break
    
    number = int(input_str)

    if number < 1:
        print("числото е отрицателно")
        continue

    if is_prime(number):
        sum_prime += number
    else:
        sum_non_prime += number

print(f"Сума на простите числа: {sum_prime}")
print(f"Сума на непростите числа: {sum_non_prime}")
