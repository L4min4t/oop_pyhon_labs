from datetime import date
import json
import os

weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "No_day")


class Pizza:
    def __init__(self, day, name, recipe, price):
        self.day = day
        self.name = name
        self.recipe = dict(recipe)
        self.price = price

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if value.strip() in weekdays:
            self.__day = value.strip()
        else:
            raise ValueError('invalid day')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip() != '':
            self.__name = value
        else:
            raise ValueError('invalid pizza\'s name')

    @property
    def recipe(self):
        return self.__recipe

    @recipe.setter
    def recipe(self, value):
        if isinstance(value, dict):
            for ingredient in value.keys():
                if not isinstance(ingredient, str) and not isinstance(value[ingredient], int):
                    raise ValueError('invalid recipe')
        else:
            raise ValueError('invalid recipe')
        self.__recipe = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if isinstance(value, float) and value > 0:
            self.__price = value
        else:
            raise ValueError('invalid price')

    def add_ingredient(self, ingredient, quantity):
        if isinstance(ingredient, str) and isinstance(quantity, int):
            self.__recipe.update({ingredient: quantity})
            self.__price += 20 * quantity

    @staticmethod
    def get_pizza(name):
        if isinstance(name, str) and name.strip() != '':
            if os.path.exists('pizza.json'):
                with open('pizza.json', 'r') as f:
                    dump = json.load(f)
                    for pizza in dump['menu']:
                        if pizza['name'] == name:
                            return Pizza('No_day', pizza['name'], pizza['recipe'], pizza['price'])
                    else:
                        raise ValueError('pizza doesn\'t exist')
            else:
                raise SystemError('file doesn\'t exists')
        else:
            raise ValueError('invalid pizza\'s name')

    def __to_dict(self):
        dump = {}
        dump['name'] = self.name
        dump['recipe'] = self.recipe
        dump['price'] = self.price
        return dump

    @staticmethod
    def put_pizza(pizza):
        if isinstance(pizza, Pizza):
            if os.path.exists('pizza.json'):
                with open('pizza.json', 'r') as f:
                    data = json.load(f)
                    data['menu'] += [pizza.__to_dict()]
                with open('pizza.json', 'w') as f:
                    json.dump(data, f)
            else:
                raise SystemError('file doesn\'t exists')
        else:
            raise ValueError('isn\'t pizza')

    def __str__(self):
        info = f'Name: {self.name}\nPrice: {self.price}\nThis is the pizza of the {self.day}\nRecipe:\n\t'
        for ingredient in self.recipe.keys():
            info += ingredient + ' : ' + str(self.recipe[ingredient]) + '\n\t'
        return info

class Pizza_of_the_day(Pizza):
    def __init__(self, day, name, recipe, price):
        super.__init__(day, name, recipe, price)

    @staticmethod
    def get_pizza():
        today = date.today().strftime('%A')
        if os.path.exists('pizza.json'):
            with open('pizza.json', 'r') as f:
                dump = json.load(f)
                for pizza_of_the_day in dump['pizza-of-the-day']:
                    if pizza_of_the_day['day'] == today:
                        return Pizza(today, pizza_of_the_day['name'], pizza_of_the_day['recipe'],
                                     pizza_of_the_day['price'])
        else:
            raise SystemError('file doesn\'t exist')