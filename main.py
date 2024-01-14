import random

random_list = [random.randint(-10, 10) for i in range(10)]
print("Random list:", random_list)

negative_sum = 0
for x in random_list:
    if x < 0:
        negative_sum += x
print("-------------------------------------------------")
print(f"The sum of numbers is less than 0: {negative_sum}")

even_sum = 0
for x in random_list:
    if x % 2 == 0:
        even_sum += x
print("---------------------------------------")
print(f"The sum of even numbers is: {even_sum}")

odd_sum = 0
for x in random_list:
    if x % 2 != 0:
        odd_sum += x
print("-------------------------------")
print(f"The sum of odd numbers is: {odd_sum}")

product_indices_3 = 1
for i in range(0, len(random_list), 3):
    product_indices_3 *= random_list[i]
print("-----------------------------------------------------")
print(f"Product of elements with indices divisible by 3: {product_indices_3}")

min_value = min(random_list)
max_value = max(random_list)
min_index = random_list.index(min_value)
max_index = random_list.index(max_value)

product_min_max = 1
for i in range(min(min_index, max_index) + 1, max(min_index, max_index)):
    product_min_max *= random_list[i]
print("-------------------------------------------------------------------")
print("The product of elements between the minimum and maximum values:", product_min_max)

print("-------------------------------------------------------------------------")
first_positive_index = -1
i = 0
while i < len(random_list) and first_positive_index == -1:
    if random_list[i] > 0:
        first_positive_index = i
    i += 1

last_positive_index = -1
i = len(random_list) - 1
while i >= 0 and last_positive_index == -1:
    if random_list[i] > 0:
        last_positive_index = i
    i -= 1

if first_positive_index != -1 and last_positive_index != -1:
    sum_between_positives = 0
    i = first_positive_index + 1
    while i < last_positive_index:
        sum_between_positives += random_list[i]
        i += 1
    print("The sum of the elements between the first and last positive elements:", sum_between_positives)
else:
    print("The list contains no positive items or less than two:")