from genericpath import exists
from genericpath import getsize
from string import ascii_letters, digits

class Text_handler:
    """
    parsing of a text file
    """
    def __init__(self, file_name):
        if not isinstance(file_name, str):
            raise TypeError('file name must be a string')
        if file_name == '':
            raise ValueError('file name can\'t be empty')
        if not exists(file_name):
            raise LookupError('file doesn\'t exist')
        if getsize(file_name) >= 6.4e7:
            raise MemoryError('too large file, size of file must be less than 64mb')
        self.__file_name = file_name


    def all_statistic(self):
        file =  open(self.__file_name, 'r')
        number_of_words = 0
        number_of_letters = 0
        number_of_characters = 0
        number_of_sentences = 0  
        number_of_digits = 0
        flag = False    

        for line in file:
            for ch in line: 
                if ch in ascii_letters:
                    number_of_letters += 1
                if ch in digits:
                    number_of_digits += 1
                if ch in ascii_letters and not flag:
                    flag = True
                if ch in '.?!' and flag:
                    flag = False
                    number_of_sentences += 1
            line = line.strip("\n")
            words = line.split()
            number_of_words += len(words)
            number_of_characters += len(line)

        file.close()

        return {'characters' : number_of_characters, 'letters' : number_of_letters, 'digits' : number_of_digits, 'words' : number_of_words, 'sentences' : number_of_sentences}


    def __str__(self) -> str:
        result = 'Statistics:\n'
        for key, value in self.all_statistic().items():
            result = result + key + ': ' + str(value) + '\n'
        return result[0:-1]
    

def main():
    try:
        a = Text_handler('text2.txt')
        print(a)
    except Exception as exc:
        print(exc)

main()