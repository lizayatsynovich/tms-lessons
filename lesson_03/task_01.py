# user_seconds = input('Введите секунды: ')
# minute = int(user_seconds) / 60
# seconds_result = int(user_seconds) % int(minute)
# print(str(minute) + ' минут ' + str(seconds_result) + ' секунд')

user_seconds = int(input('Введите секунды: '))
minutes = user_seconds // 60  # количество минут
seconds = user_seconds % 60  # количество секунд
print(str(minutes) + ' минут ' + str(seconds) + ' секунд')


