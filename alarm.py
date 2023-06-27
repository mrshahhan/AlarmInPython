from datetime import datetime
from playsound import playsound

def validate_time(alarm_time):
    if len(alarm_time) !=8:
        return 'Неверный формат, попробуите еще раз.'
    else:
        if int(alarm_time[0:2]) > 23:
            return 'Неверный формат часов попробуите еще раз.'
        elif int(alarm_time[3:5]) > 59:
            return 'Неврный формат минут, попробуите еще раз.'
        elif int(alarm_time[6:8]) > 59:
            return 'Неверный формат секунд, попробуте еще раз.'
        else:
            return 'Отлично!'

while True:
    alarm_time = input('Введите время в следующем формате \'HH:MM:SS\' \nВремя будильника: ')
    validate = validate_time(alarm_time)
    if validate != 'Отлично!':
        print(validate)
    else:
        print("Будильник установлен на время ", alarm_time)
        break

alarm_hour = int(alarm_time[0:2])
alarm_min = int(alarm_time[3:5])
alarm_sec = int(alarm_time[6:8])

while True:

    if alarm_hour == current_hour:
        if alarm_min == current_min:    now = datetime.now()

    current_hour = now.hour
    current_min = now.minute
    current_sec = now.second

            if alarm_sec == current_sec:
                print('Вставай!')
                playsound('C:/Users/Shahan/Downloads/doug-maxwell-cast-of-pods.mp3')

