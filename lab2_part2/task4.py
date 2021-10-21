# Create a class BINARY TREE that contains background information of product prices (product code, price of 1 product).
# The tree is sorted by product codes. From the keyboard enter data on the number of products in the format: product code, number of products.
# Using a tree, find the cost of products (cost = quantity * price of one product). 

class Binary_tree:
    """
    binary tree of store's products
    """
    def __init__(self, code, price, quantity):
        self.code = code
        self.price = price
        self.quantity = quantity
        self.left = None
        self.right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, node):
        if not isinstance(node, Binary_tree) and node != None:
            raise TypeError('new node must be Binary_tree type')
        self.__left = node

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, node):
        if not isinstance(node, Binary_tree) and node != None:
            raise TypeError('new node must be Binary_tree type')
        self.__right = node


    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        if not isinstance(code, int):
            raise TypeError('code must be int')
        if code < 0:
            raise ValueError('code must be >= 0')
        self.__code = code

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, int):
            raise TypeError('price must be int')
        if price <= 0:
            raise ValueError('price must be > 0')
        self.__price = price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError('quantity must be int')
        if quantity < 0:
            raise ValueError('quantity must be >= 0')
        self.__quantity = quantity

    def insert(self, code, price, quantity):
        if not isinstance(code, int):
            raise TypeError('code must be int')
        if code < 0:
            raise ValueError('code must be >= 0')
        if code < self.code:
            if not self.left:
               self.left = Binary_tree(code, price, quantity)
            else:
               self.left.insert(code, price, quantity)
        elif code > self.code:
               if not self.right:
                  self.right = Binary_tree(code, price, quantity)
               else:
                  self.right.insert(code, price, quantity)

    def total_cost(self):
        total_sum = int(self.quantity * self.price)
        if self.left != None:
            total_sum += self.left.total_cost()
        if self.right != None:
            total_sum += self.right.total_cost()
        return total_sum

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(f'code: {self.code}, price: {self.price}, quantity: {self.quantity}')
        if self.right:
            self.right.PrintTree()

input_int_array = [ int(x) for x in input('code, price, quantity through a space: ').split()]
if len(input_int_array) % 3 != 0:
    raise AttributeError('enter three arguments for each product')
products = Binary_tree(*input_int_array[:3])
for i in range(3, len(input_int_array), 3):
    products.insert(*input_int_array[i:i+3])
products.PrintTree()
print('total cost = ', products.total_cost())