revenue = float(input('Введите значение выручки -'))
costs = float(input('Введите значение издержек -'))
profit = revenue - costs

if profit > 0:
    print(f'Поздравляем, Ваша компания работает с прибылью {profit}!')
    print(f'Рентабельность выручки - {profit/revenue:.3f}')
    employee = int(input('Укажите число сотрудников Вашей компании - '))
    print(f'Прибыль на одного сотрудника Вашей компании - {profit/employee:.2f}')
elif profit < 0:
    print(f'Ваша компания работает с убытком - {-profit}')
else:
    print(f'Прибыль Вашей компании равна нулю')