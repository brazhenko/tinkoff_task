import re
import json
import random


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
        return ' '.join(text) + '.'

    def dump(self):
        with open('pairs.json', "w", encoding="utf-8") as file:
            json.dump(self.Dictionary, file)


if __name__ == '__main__':
    print("Приветствую пользователя моей программы. \n Для начала работы загрузите текст в learn.txt и напишите learn.\n Далее напишите длину последовательности в словах, \n которую вам требуется сгенерировать. \n Для выхода нажмите q")

    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'learn':
            a = TextGenerator()
            a.fit()
            print('Обучение закончено')
        else:
            print('Неверный ввод')
            continue

        while True:
            command = input('Можно ввести длину или вернуться к обучению(написать back) ')
            if command == 'back':
                break
            try:
                number = int(command)
            except Exception:
                print('Неверный ввод')
                continue

            print(a.generate(number))
            # a.dump()
