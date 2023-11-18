import random
import logging

# Настройка логгера
logging.basicConfig(filename='barrels.log', filemode='w', level=logging.INFO)

# Функция для вытаскивания бочонка из мешка
def pull_barrel(barrels):
    if barrels:
        barrel = random.choice(barrels)
        barrels.remove(barrel)
        logging.info(f'Вытянут бочонок: {barrel}')
        return barrel
    else:
        logging.warning('Мешок пуст!')
        return None

# Функция для ввода натурального числа N
def input_natural_number():
    while True:
        try:
            n = int(input('Введите натуральное число N: '))
            if n > 0:
                return n
            else:
                print('Число должно быть больше 0!')
        except ValueError:
            print('Ошибка! Введите целое число.')

# Основная программа
def main():
    n = input_natural_number()
    barrels = list(range(1, n+1))

    while barrels:
        input('Нажмите Enter, чтобы вытянуть бочонок...')
        pulled_barrel = pull_barrel(barrels)
        if pulled_barrel:
            print(f'Вытянут бочонок: {pulled_barrel}')

if __name__ == '__main__':
    main()
