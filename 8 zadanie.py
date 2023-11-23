def a(dist, dengi):
    N = len(dist)
    taxi_n = []
    total_cost = 0

# для каждого сотрудника
    for i in range(N):
        min_cost = float('inf')
        min_taxi = -1
 # проверяем все такси и находим тариф с минимальными затратами для сотрудника
        for j in range(N):
            if dengi[j] < min_cost:
                min_cost = dengi[j]
                min_taxi = j
 # добавляем номер такси в список и увеличиваем суммарные затраты
        taxi_n.append(min_taxi + 1)
        total_cost += min_cost * dist[i]
        dengi[min_taxi] = float('inf')

    return taxi_n, total_cost


# считываем данные
N = int(input("Введите количество сотрудников: "))
dist =  []
dengi = []

print("Введите расстояния до домов сотрудников:")
for i in range(N):
    distance = int(input())
    dist.append(distance)

print("Введите тарифы за проезд в такси:")
for i in range(N):
    rate = int(input())
    dengi.append(rate)
# вызываем функцию для расчета результата
taxi_n, total_cost = a(N, dist, dengi)
print("Номера такси для каждого сотрудника: ", taxi_n)
print("Суммарные затраты на такси: {} рублей".format(total_cost))
