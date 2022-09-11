import train
from train import dictionary
import random
def generate(inputdir='stdin',length = 10, prefix = 1): # создадим функцию денерирующую нужную нам последовательность
    if (prefix == 1):
        prefix = random.choice(train.unique_wordlist(inputdir)) # проверяем введен ли стартовый префикс
    ndic = dictionary(inputdir)
    for i in range(length):  # наконец генерируем последовательность
        print(prefix, end=' ')
        prefix = random.choice(ndic.get(prefix))
