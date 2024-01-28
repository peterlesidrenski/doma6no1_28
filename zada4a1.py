current_number = 1
row = 1
target_number = int(input())

while current_number <= target_number:
    for col in range(row):
        print(current_number, end=" ")
        current_number += 1

        if current_number > target_number:
            break

    row += 1
    print()