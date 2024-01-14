import random
random_list = [random.randint(-10, 10) for i in range(10)]
print("Random list:", random_list)

even_number_list = []
for num in random_list:
    if num % 2 == 0:
        even_number_list.append(num)
print(f"List of even numbers: {even_number_list}")

odd_number_list = []
for num in random_list:
    if num % 2 != 0:
        odd_number_list.append(num)
print(f"List of odd numbers: {odd_number_list}")

negative_number_list = []
for num in random_list:
    if num < 0:
        negative_number_list.append(num)
print(f"List of negative numbers: {negative_number_list}")

positive_number_list = []

for num in random_list:
    if num > 0:
        positive_number_list.append(num)
print(f"List of negative numbers: {positive_number_list}")


zero_number_list = []
for num in random_list:
    if num == 0:
        zero_number_list.append(num)
print(f"List of zero numbers: {zero_number_list}")