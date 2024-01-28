def equal_sums(start, end):
    for i in range(start, end + 1, 3):
        even_sum = i + 1
        odd_sum = i + 2
        print(f"{even_sum} {odd_sum}")
start_number = int(input())
end_number = int(input())

# Извикване на функцията
equal_sums(start_number, end_number)
