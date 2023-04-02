kashki = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
num = int(input("число: "))
for i in range(num):
    kashkasegodnya = kashki[i % len(kashki)] #Выбираем кашу на сегодняшний день
    print(kashkasegodnya) #Выводим кашу на день
