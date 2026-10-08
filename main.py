print ("Приложение «Чудо Обувь» запущено!")
print ("Добро пожаловать!")

login = "admin"
lastname = "Админов"
price = 8990.0
quantity = 5
in_stock = True

print ("Логин:", login)
print ("Фамилия:", lastname)
print ("Цена:", price)
print ("Количество:", quantity)
print ("В наличии:", in_stock)

sizes = [36.0, 37.0, 38.0, 39.0]
print ("\nДоступные размеры:")
for s in sizes:
    print ("- ", s)

print("\nНомера по порядку:")
for i in range(len(sizes)):
    print(i + 1, "-", sizes[i]) 

if quantity <= 3:
    print("\nОсталось мало товара!")
else:
    print("\nТовар в наличии")


users = [{"login": "admin", "lastname": "Админов", "role": "администратор"},
         {"login": "manager", "lastname": "Менеджеров", "role": "менеджер"},
         {"login": "user", "lastname": "Пользователей", "role": "авторизованный"}
         ]

products = [
    {"id": 1, "name": "Air Max", "price": 8999.0, "size": {36.0: 5, 37.0: 2}},
    {"id": 2, "name": "Superstar HellStar", "price": 7999.0, "size": {38.0: 3, 39.0: 4}},
    {"id": 3, "name": "Runfalacon", "price": 6999.0, "size": {39.0: 2}}
]

for p in products: 
    total_qty = sum(p["size"].values())
    print(f"{p['name']} — {p['price']} руб. — Количество: {total_qty} шт.")
    

def find_user(login):
    for u in users:
        if u['login'] == login:
            return u
    return None


result = find_user('admin')
if result:
    print(f"Найден пользователь: {result['lastname']}")
else:
    print("Пользователь не найден")


def total_sum(items):
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total


cart = [
    {'name': 'Air Max',   'price': 8990.0, 'quantity': 2},
    {'name': 'Superstar', 'price': 7490.0, 'quantity': 1},
]

print(f"Итоговая сумма заказа: {total_sum(cart)} руб.")

sorted_by_price = sorted(products, key=lambda p: p['price'])
print("\nТовары по возрастанию цены:")
for p in sorted_by_price:
    print(f"{p['name']} — {p['price']} руб.")


low_stock = [p for p in products if sum(p['size'].values()) <= 3]
print("\nТовары с низким остатком (≤ 3 шт.):")
for p in low_stock:
    print(p['name'])

# Шаг 18. Поиск по названию
def search_products(query):
    query = query.lower()
    return [p for p in products if query in p['name'].lower()]
 
 
found = search_products('max')
print("\nРезультаты поиска 'max':")
for p in found:
    print(p['name'])
 
 
# Шаг 19. Фильтр по цене
def filter_by_price(products, min_price, max_price):
    return [p for p in products if min_price <= p['price'] <= max_price]
 
 
result = filter_by_price(products, 5000, 8000)
print("\nТовары от 5000 до 8000 руб.:")
for p in result:
    print(f"{p['name']} — {p['price']} руб.")
 
 
# ===== Задание 7. Мини-задача «Корзина» =====
 
# Шаг 20
def add_to_cart(cart, product, size, quantity):
    cart.append({
        'product': product['name'],
        'price': product['price'],
        'size': size,
        'quantity': quantity
    })
 
 
def remove_from_cart(cart, name):
    cart[:] = [item for item in cart if item['product'] != name]
 
 
def change_quantity(cart, name, new_qty):
    for item in cart:
        if item['product'] == name:
            item['quantity'] = new_qty
            break
 
 
cart = []
add_to_cart(cart, products[0], 36.0, 2)
add_to_cart(cart, products[1], 37.0, 1)
 
print("\nКорзина:")
for item in cart:
    print(f"{item['product']}, размер {item['size']}, "
          f"{item['quantity']} шт. × {item['price']} = "
          f"{item['quantity'] * item['price']} руб.")
 
print(f"\nИтого: {total_sum(cart)} руб.")
 
change_quantity(cart, 'Air Max', 3)
remove_from_cart(cart, 'Superstar HellStar')
 
print("\nПосле изменений:")
for item in cart:
    print(f"{item['product']}, размер {item['size']}, {item['quantity']} шт.")
print(f"Итого: {total_sum(cart)} руб.")
 