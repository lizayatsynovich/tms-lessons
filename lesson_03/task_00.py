user_name = input('What is your name? Input: ')
user_birth = input('What is your birth year? Input: ')
cur_year = 2023
user_birth = int(user_birth)
user_age = cur_year - user_birth
print('Hello, ' + user_name + ', your age is ' + str(user_age))