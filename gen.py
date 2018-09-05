'''
Задание только в начальной стадии разработки. Обучался на текстах Войны и Мира.
'''

import re
import json
import random


def get_words(text):
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
