import phonenumbers

class Product:
    """
    holds products info
    """
    def __init__(self,  price, description, dimensions):
        __slots__ = ['price', 'description', 'dimension']
        self.price = price
        self.description = description
        self.dimensions = dimensions

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("price must be float")
        if value <= 0:
            raise ValueError("prise must be > 0")
        self.__price = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError("description must be string")
        self.__description = description

    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        if not isinstance(dimensions, str):
            raise TypeError("dimensions must be string")
        self.__dimensions = dimensions    
            

class Customer:
    """
    holds products info
    """
    def __init__(self, surname, name, patronymic, mobile_phone):
        __slots__ = ['surname', 'name', 'patronymic', 'mobile_phone']
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.mobile_phone = mobile_phone

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("surname must be string")
        self.__surname = surname

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be string")
        self.__name = name

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        if not isinstance(patronymic, str):
            raise TypeError("patronymic must be string")
        self.__patronymic = patronymic

    @property
    def mobile_phone(self):
        return self.__mobile_phone
        
    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        if not phonenumbers.is_possible_number(phonenumbers.parse(mobile_phone)):
            raise ValueError("uncorrect number")
        self.__mobile_phone = mobile_phone

class Order:
    def __init__(self, customer, *products):
        self.customer = customer
        self.products = products
        total_order_value = 0
        for i in products:
           total_order_value += i.price
        self.total_order_value = total_order_value
    
    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, products):
        for i in products: 
            if not isinstance(i, Product):
                raise TypeError("products must be Product type")
        self.__products = products

    @property
    def total_order_value(self):
        return self.__total_order_value

    @total_order_value.setter
    def total_order_value(self, total_order_value):
        self.__total_order_value = total_order_value

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be Customer type")
        self.__customer = customer

       

def main():
    try:
        camera = Product(5999.0, 'camera: black, shoots 4k, 32MP', '120x75x45')
        notebook = Product(32500., 'notebook: gray, i7-9999, nvidia3399', '350x220x30')
        cardrider = Product(210.50, 'cardrider: 450b/s', '25x15x2')
        user = Customer('Vlasiuk', 'Ivan', 'Victorovich', "+380961921937")
        order = Order(user, camera, cardrider)
        print(order.total_order_value, ' total prise')
    except Exception as e:
        print(e)

main()