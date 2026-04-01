sushi_orders = [
    {"name": "California Roll", "price": 8},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8},
    {"name": "Dragon Roll", "price": 12},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Miso Soup", "price": 4},
    {"name": "Edamame", "price": 5},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8}
]
def reciept(orders):
    the_reciept = {}
    for sushi in orders:
        if sushi['name'] in the_reciept:
            continue
        else:
            the_reciept[sushi['name']] = {
                'price': sushi['price'],
                'qty': 1
            }
    for suhsi, value in the_reciept.items():
        price = value['price'] * value['qty']
        print(sushi, value['qty'], price)
reciept(sushi_orders)