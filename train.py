import numpy as np
import re
import os
def dictionary(inputdir='stdin'):
    for filename in os.listdir(inputdir): #считываем директорию файлов
       with open(os.path.join(inputdir, filename,), errors = 'replace') as f:
           text = f.read()
    spl_text = re.split(r'\W+', text)  # очистили всё от ненужных символов и разделили на слова
    new_spl_text = [word.lower() for word in spl_text]  # привели все элементы списка к одному регистру
    lnfile = len(new_spl_text)
    np.arr_word = []
    for i in range(lnfile):
        np.arr_word.append(new_spl_text[i])  # делаем из списка слов массив
    unique_arr_word = np.unique(np.arr_word)  # создаем список уникальных слов в тексте, который потребудется нам для словаря
    d2arr = [[] for i in range(len(unique_arr_word))]
    i = 0
    slv = {}
    for word in unique_arr_word:  # сопоставляем каждому слову свой массив
        slv[word] = d2arr[i]
        i += 1
    for i in range(len(np.arr_word) - 1):  # для каждого слова добавляем следующее в его массив
        slv[np.arr_word[i]].append(np.arr_word[i + 1])
    print(len(slv))
    return slv
def unique_wordlist(inputdir): # аналогично создадим функцию, выдающую список уникальных слов для random в блоке generation
    for filename in os.listdir(inputdir):
       with open(os.path.join(inputdir, filename,), errors = 'replace') as f:
           text = f.read()
    spl_text = re.split(r'\W+', text)
    new_spl_text = [word.lower() for word in spl_text]
    lnfile = len(new_spl_text)
    np.arr_word = []
    for i in range(lnfile):
        np.arr_word.append(new_spl_text[i])
    unique_arr_word = np.unique(np.arr_word)
    return unique_arr_word
