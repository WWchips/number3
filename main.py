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


def search_products(query):
    query = query.lower()
    return [p for p in products if query in p['name'].lower()]
 
 
found = search_products('max')
print("\nРезультаты поиска 'max':")
for p in found:
    print(p['name'])
 
 

def filter_by_price(products, min_price, max_price):
    return [p for p in products if min_price <= p['price'] <= max_price]
 
 
result = filter_by_price(products, 5000, 8000)
print("\nТовары от 5000 до 8000 руб.:")
for p in result:
    print(f"{p['name']} — {p['price']} руб.")
 
 

 
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




# ===== Задание 8  =====
 

products.append({'id': 4, 'name': 'Gazelle', 'price': 9490.0,
                 'sizes': {40.0: 3, 41.0: 1}})
products.append({'id': 5, 'name': 'Stan Smith', 'price': 5290.0,
                 'sizes': {38.0: 6, 39.0: 4, 40.0: 2}})
 
print("\nКаталог после добавления товаров:")
for p in products:
    print(f"{p['id']}. {p['name']} — {p['price']} руб.")
 
 

def get_sizes(product):
    return [size for size, qty in product['sizes'].items() if qty > 0]
 
 
print("\nДоступные размеры:")
for p in products:
    print(f"{p['name']}: {get_sizes(p)}")
 
 

def get_total_quantity(product):
    return sum(product['sizes'].values())
 
 
print("\nОбщее количество на складе:")
for p in products:
    print(f"{p['name']}: {get_total_quantity(p)} шт.")
 

sorted_by_name = sorted(products, key=lambda p: p['name'])
print("\nТовары по алфавиту:")
for p in sorted_by_name:
    print(p['name'])
 

cheap = [p for p in products if p['price'] < 6000]
print("\nТовары дешевле 6000 руб.:")
for p in cheap:
    print(f"{p['name']} — {p['price']} руб.")
 

print("\nВсе товары (через while):")
i = 0
while i < len(products):
    p = products[i]
    print(f"{p['name']} — {p['price']} руб.")
    i += 1
 