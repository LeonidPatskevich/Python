from sys import argv

script_name, hours, cost_hour, bonus = argv

sum_ = (int(hours) * int(cost_hour)) + int(bonus)

print("Отработанные часы: ", hours)
print("Стоимость часа: ", cost_hour)
print("Бонус: ", bonus)
print("Итого: ", sum_)