"""Word Finder: finds random words from a dictionary."""


import random
class WordFinder:
    ...
  
    def __init__(self,words):
        self.file = open(words)
        self.word_list = self.file.readlines()
    def __repr__(self):

        return f'{len(self.file.readlines())} words read'
    def random(self): 
        random.shuffle(self.word_list)
        return self.word_list.pop()




    

       

        









words =('/mnt/c/users/zsmit/desktop/python-oo-practice/words.txt')
print(WordFinder(words).random())
