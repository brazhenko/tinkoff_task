'''
Задание только в начальной стадии разработки. Обучался на текстах Войны и Мира.
'''

import re
import json
import random


'''def get_words(text):
    return re.compile('\w+').findall(text)

res = (open('learn.txt', 'r').read())
res = get_words(res)
Dictionary = {}


for word in res:
    if word not in Dictionary:
        Dictionary.update([(word, [])])


for i in range(len(res)-1):
    Dictionary[res[i]] = Dictionary[res[i]] + [res[i+1]]


def generate(l, start):
    text = [start]
    start = start
    for i in range(l):
        num = random.randint(0, len(Dictionary[start])-1)
        text = text + [Dictionary[start][num]]
        start = Dictionary[start][num]
    return text

test_txt = ' '.join(generate(100, 'охота'))
print(text_txt)
'''


class TextGenerator(object):
    def __init__(self):
        pass

    Dictionary = {}

    def fit(self):
        res = (open('learn.txt', 'r').read()).lower()
        res = re.compile('\w+').findall(res)

        for word in res:
            if word not in self.Dictionary:
                self.Dictionary.update([(word, [])])
        for i in range(len(res) - 1):
            self.Dictionary[res[i]] = self.Dictionary[res[i]] + [res[i + 1]]

    def generate(self, length):
        start = list(self.Dictionary.keys())[random.randint(0,len(self.Dictionary))]
        text = [start]

        for i in range(length):
            num = random.randint(0, len(self.Dictionary[start]) - 1)
            text = text + [self.Dictionary[start][num]]
            start = self.Dictionary[start][num]
        return ' '.join(text)

    def dump(self):
        with open('pairs.json', "w", encoding="utf-8") as file:
            json.dump(self.Dictionary, file)

a = TextGenerator()
a.fit()
print(a.generate(10, ))
a.dump()
