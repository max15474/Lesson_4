def f():
    pass
print(f())

def add(x, y):
    return x + y
print(add(1, 2))
print(add(1, 2))

car = lambda brend, engine_volume, price: f'Car: {brend.title()}, Engine volume: {engine_volume}, Price: {price}'
print(car('volvo', 1.5, 1300000))