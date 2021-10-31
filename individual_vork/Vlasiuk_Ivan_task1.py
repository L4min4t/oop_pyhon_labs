# Розробити клас для роботи з ПРАЙС-ЛИСТОМ комп'ютерної фірми, у якому вказано дані про марку комп'ютера,
# тип процесора, частоту процесора, об'єм оперативної та дискової пам'яті, характеристики відеокарти, ціну комп'ютера.
# Визначити конструктори, методи / властивості додавання, зміни та витирання даних про модель комп'ютера,
# метод пошуку моделі за заданими характеристиками комп'ютера.

class Price_list:
    prise_list = {}
    id_generator = 0
    def __init__(self, brand, cpu, cpu_frequency, ram, rom, gpu, price):
        self.id = Price_list.id_generator
        Price_list.id_generator += 1
        if Price_list.__is_valid_data(brand, cpu, cpu_frequency, ram, rom, gpu, price):
            Price_list.prise_list[self.id] = [brand, cpu, cpu_frequency, ram, rom, gpu, price]
        else:
            raise ValueError('invalid data')

    def __is_valid_data(brand, cpu, cpu_frequency, ram, rom, gpu, price):
        if not isinstance(brand, str) or brand == None:
            return False
        if not isinstance(cpu, str) or brand == None:
            return False
        if not isinstance(cpu_frequency, int) or cpu_frequency < 0 :
            return False
        if not isinstance(ram, int) or ram < 0:
            return False
        if not isinstance(rom, int) or rom < 0:
            return False
        if not isinstance(gpu, str) or gpu == None:
            return False
        if not isinstance(price, float) or price < 0:
            return False
        return True
        
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("ID must be int")
        if value < Price_list.id_generator:
            raise ValueError("ID generation failure")
        self.__id = value
    
    @classmethod
    def find_computer(cls, *args):
        result = {}
        i = 0
        for item in Price_list.prise_list.values():
            for prop in args:
                if prop in item:
                    result[i] = item 
                    i += 1
                    break
        return result

    # не встигаю зробити зміннення і видалення властивостей комп'ютера
    # але це зробивби через ід компютера в списку всіх комп'ютерів
    # викликаєм метод помінятися в інстанса класа (комп'ютера)
    # там ми можемо взнати його ід і вичислити який айтем з словаря за нього відповідає

    @classmethod
    def get_list(cls):
        return str(Price_list.prise_list)

c1 = Price_list('hp', 'i7-999', 4000, 12000, 100000, 'rx580', 45000.)
c2 = Price_list('msi', 'i5-999', 3500, 6000, 50000, '1660', 25000.)
c3 = Price_list('lenovo', 'i5-999', 1600, 7000, 50000, 'mx210', 5000.)
print(Price_list.find_computer('hp', 4000, 6000))
print(Price_list.get_list())
