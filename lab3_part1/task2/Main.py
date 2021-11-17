# Pizzeria offers pizza-of-the-day for business lunch.
# The type of pizza-of-the-day depends on the day of week.
# Having a pizza-of-the-day simplifies ordering for customers.
# They don't have to be experts on specific types of pizza.
# Also, customers can add extra ingredients to the pizza-of-the-day.
# Write a program that will form orders from customers.

from Pizza import Pizza, Pizza_of_the_day
from Customer import Customer
from Order import Order


def main():
    customer = Customer("Gena")
    pizza1 = Pizza.get_pizza("123")
    pizza2 = Pizza_of_the_day.get_pizza()
    pizza3 = Pizza('No_day', "my_pizza", {"dough": 1, "mutton": 1, "sausages": 1}, 958.3)
    pizza1.add_ingredient("potato", 2)
    pizza3.add_ingredient("ketchup", 1)
    order = Order(customer, pizza2, pizza1, pizza3)
    print(order)
    # Pizza.put_pizza(pizza3)

main()
