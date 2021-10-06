from string import ascii_letters, digits, punctuation   

class Text_handler:
    def __init__(self, file_name):
        with open(file_name, 'r') as f:
            contents = f.read()
        f.close()
        self.__contents = contents

    def how_many_letters(self):
        counter = 0
        for i in self.__contents:
            if i in ascii_letters:
                counter += 1
        return counter
    
    def how_many_digits(self):
        counter = 0
        for i in self.__contents:
            if i in digits:
                counter += 1
        return counter

    def how_many_words(self):
        counter = 0
        for i in range(0, len(self.__contents) - 1):
            if self.__contents[i] in ascii_letters and self.__contents[i + 1] in punctuation.replace('-', ' '):
                counter += 1
        return counter

    def how_many_sentences(self):
        counter = 0
        flag = False
        for i in range(0, len(self.__contents)):
            if self.__contents[i] in ascii_letters and not flag:
                flag = True
            if self.__contents[i] in '.?!' and flag:
                flag = False
                counter += 1
        return counter
     
    def all_statistic(self):
        return f'\bStatistic:\nletters = {self.how_many_letters()}\nwords = {self.how_many_words()}\ndigits = {self.how_many_digits()}\nsentences = {self.how_many_sentences()}'

    def __str__(self) -> str:
        return self.__contents
    

def main():
    a = Text_handler('text2.txt')
    print(a, '\n\n\n', a.all_statistic())

main()