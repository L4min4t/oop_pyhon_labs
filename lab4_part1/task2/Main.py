# Create a class NOTEBOOK, which contains the name, surname, number phone and birthday of person.
# Define methods of access to these fields and overload operations:
# "+" - for adding a new element;
# "-" - for deleting an element;
# "*" - for searching for an element in the Notebook on one of the data fields.
from Person import Person
from Notebook import Notebook

def main():
    x = Person('bebra', 'Barbara', '+380961921937', '01.12.2000')
    x1 = Person('asd', 'dsa', '+380961921945', '02.11.2003')
    x2 = Person('asd123', 'dsa123', '+380961921999', '01.11.1900')
    y = Notebook(x, x1)
    print(y * 'asd')

if __name__ == '__main__':
    main()