products = []
def add_product(name, price, quantity):
    product = {'name': name, 'price': price, 'quantity':quantity}
    products.append(product)
def show_product():
    for i, product in enumerate(products, 1):
        print(f"{i}. {product['name']} | {product['quantity']} | {product['price']}")
def find_product(name):
    for product in products:
        if product['name'] == name:
            print(f"{product['name']} | {product['quantity']} | {product['price']}")
            return
    print('такого нету')
def total_price():
    result = 0
    for product in products:
        result += product['price']*product['quantity']
    return result
while True:
    print('=== Магазин ===')
    print('1. Добавить товар')
    print('2. Показать товары')
    print('3. Посчитать общую стоимость')
    print('4. Найти товар')
    print('5. Выход')
    choice = input('Выберите действие: ')
    if choice == '1':
        name = input('Имя: ')
        try:
            price = int(input('Цена: '))
            quantity = int(input('Количество: '))
            add_product(name, price, quantity)
        except ValueError:
            print('Должно быть числами')
    elif choice == '2':
        show_product()
    elif choice == '3':
        print(f'Общая стоимость: {total_price()}')
    elif choice == '4':
        product_1 = input('Введите ваш товар')
        find_product(product_1)
    elif choice == '5':
        break
    else:
        print('Неверный выбор')

#написал программу начальную