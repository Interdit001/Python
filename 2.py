

n = int(input('Введите время в секундах - '))
hour = n//3600
min = (n//60) - (hour*60)
sec = n%60
print(f'{hour:02}:{min:02}:{sec:02}')

