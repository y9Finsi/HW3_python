chislo_list = list(map(int, input("Введите числа, которые будут входить в список: ").split()))

last_element = chislo_list.pop(-1)
chislo_list.insert(0, last_element)

print(chislo_list)
