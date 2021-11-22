unitnum = int(input('Введите целое положительное число'))
max = unitnum % 10
num = unitnum
while num > 0:
    digit = num % 10
    if digit > max:
            max = digit
    if digit == 9:
        break
    num //= 10
    print(num)

print(f'Наибольшая цифра в числе {unitnum} равна {max}')



