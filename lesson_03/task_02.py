# Пользователь вводит целое трёхзначное число.
# Выведите сумму чисел числа.

# Например: 534 -> 5 + 3 + 4 = 12

user_number = input('Input number: ')
result = int(user_number[0]) + int(user_number[1]) + int(user_number[2])
print(result)