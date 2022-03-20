# задание 1
duration = int(input('Ведите количество секунд: '))
day = duration // 86400
hour = duration // 3600 % 24
minute = duration // 60 % 60
second = duration % 60

if day == 0 and hour != 0 and minute != 0 and second != 0:
    print(hour, 'час', minute, 'минут',second, 'сек.')
elif hour == 0 and minute != 0 and second != 0:
    print(minute, 'минут', second, 'сек.')
elif minute == 0 and second != 0:
    print(second, 'сек.')
else:
  print(day, 'дней', hour, 'час', minute, 'минут', second, 'сек.')
