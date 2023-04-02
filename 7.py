def find_index_f(word):
 if 'f' in word:
     return word.index('f')
 else:
     return None
word = input()
first_index = find_index_f(word)
last_index = find_index_f(word[::-1])

if first_index == last_index:
 print(first_index)
elif first_index is not None and last_index is not None:
 print(first_index, len(word) - last_index - 1)
else:
 print('Нет ни одного f в слове')
