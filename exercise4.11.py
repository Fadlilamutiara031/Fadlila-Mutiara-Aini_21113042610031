pizza = ['Mozarella', 'Jamur', 'Tuna']

friend_pizzas = pizza[:]

pizza.append('BBQ')
friend_pizzas.append('Original')

print("Pizza favorit saya:")
for jenis in pizza:
    print(jenis)

print("\nPizza favorit teman saya:")
for jenis in friend_pizzas:
    print(jenis)