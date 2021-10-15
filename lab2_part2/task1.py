from Order import Order
from Customer import Customer
from Product import Product

def main():
    try:
        camera = Product(5999.0, 'camera: black, shoots 4k, 32MP', '120x75x45', 1)
        notebook = Product(32500., 'notebook: gray, i9-9999, nvidia3399', '350x220x30', 2)
        cardrider = Product(210.50, 'cardrider: 450mb/s', '25x15x2', 1)

        user = Customer('Vlasiuk', 'Ivan', 'Victorovich', "+380961921937")

        order = Order(user, camera, cardrider)
        print(order)
        
    except Exception as e:
        print(e)


main()