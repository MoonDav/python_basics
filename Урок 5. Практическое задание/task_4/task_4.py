"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
with open('sal.txt', 'r') as fp:
    sal = []
    poor = []
    all_list = fp.read().split('\n')
    for i in all_list:
        i = i.split()
        if int(i[1]) < 20000:
            poor.append(i[0])
        sal.append(i[1])

print(
    f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')
