# import random
# print(random.random())
from random import randint, randrange
# print ("Вывод случайного целого числа ", randint(0,10))
# city_list = ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia"]
# print(city_list[random.randint(0,len(city_list)-1)])
# print("Выбор случайного города - ", random.choice(city_list))
# import random
#
# list = [20,30,40,50,60,70,80,90]
# sampling = random.choices(list, k=5)
# print(f"Выборка с методом choices {sampling}, {list}")
# import time
import random
# end_time = time.time()+20
# while time.time < end_time:
#     print(random.randit(0,10))
s_list = ["Пиджак",
          "Рубашка",
          "Платье",
          "Футбока",
          "Шляпа",
          "Брюки",
          "Носки",
          "Шуба",
          "Кепка",
          "Тапки",
          "Платок",
          "Плавки"]
print ("Выбор случайной одежды из списка - ", random.choices(s_list, k=3))