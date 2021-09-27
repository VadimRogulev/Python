"""
1.Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль
ниже среднего.
"""

 
import collections
 
company = collections.namedtuple('company', ['name', 'quarter_first', 'quarter_second',
                                             'quarter_third', 'quarter_fourth', 'profit_for_the_year'])
all_companies = []
a_c = int(input("Введити кол-во компаний: "))
Total_profit = 0

for i in range(a_c):
    name = input(f"Название {i+1}-ого предприятия: ")
    quarter_first = int(input("Прибыль за 1 квартал: "))
    quarter_second = int(input("Прибыль за 2 квартал: "))
    quarter_third = int(input("Прибыль за 3 квартал: "))
    quarter_fourth = int(input("Прибыль за 4 квартал: "))
    profit_for_the_year = quarter_first + quarter_second + quarter_third + quarter_fourth
    Total_profit += profit_for_the_year
    all_companies.append(company(name=name, quarter_first=quarter_first,
                                 quarter_second=quarter_second, quarter_third=quarter_third,
                                 quarter_fourth=quarter_fourth, profit_for_the_year=profit_for_the_year))

average_total_profit = Total_profit / a_c

print(f"Предприятия с прибылью выше средней {average_total_profit}: ")

for company in all_companies:
    if company.profit_for_the_year >= average_total_profit:
        print(company.name)

print(f"Предприятия с прибылью неже средней {average_total_profit}: ")

for company in all_companies:
    if company.profit_for_the_year < average_total_profit:
        print(company.name)
