# Напишите программу, которая проверяет, является ли введенное пользователем число простым, используя цикл while.

# создаем переменную и присваиваем ей значение, веденное пользователем
n = int(input("Введите число: "))
# создаем переменную и присваиваем ей значение 2
divider = 2
# создаем переменную и присваиваем ей значение f"Число {n} является простым"
answer = f"Число {n} является простым"

# циклом проходим по каждому числу от 2 до n - 1
while (divider < n):
  # проверяем если число n делится с остатком на divider
  if (n % divider != 0): 
    # увеличиваем значение переменной 
    divider += 1
    # продолжаем цикл
    continue
   # проверяем если число n делится без остатком на divider
  elif (n % divider == 0):
    # переприсваиваем значение переменной 
    answer = f"Число {n} не является простым"
    # выходим из цикла
    break;

# выводим значение переменной
print(answer)



  

