class Product:
    """
    holds products info
    """
    id_generator = 0
    def __init__(self,  price, description, dimensions, quantity_in_stock):
        __slots__ = ['price', 'description', 'dimensions']
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.quantity = quantity_in_stock
        self.id = Product.id_generator
        Product.id_generator += 1

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int):
            raise TypeError("quantity must be int")
        if value < 0:
            raise ValueError("quantity must be >= 0")
        self.__quantity = value
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("ID must be int")
        if value < Product.id_generator:
            raise ValueError("ID generation failure")
        self.__id = value
    
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
        if description == '':
            raise ValueError("description cann't be empty")
        self.__description = description

    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        if not isinstance(dimensions, str):
            raise TypeError("dimensions must be string")
        if dimensions == '':
            raise ValueError("dimensions cann't be empty")
        self.__dimensions = dimensions

    def info_for_order(self):
        return f'ID product: {self.id}\n{self.description}\nprice: {self.price} UAH\ndimension: {self.dimensions}'

    def __str__(self) -> str:
        return f'ID product: {self.id}\n{self.description}\nprice: {self.price} UAH\ndimension: {self.dimensions}\nquantity: {self.quantity}'