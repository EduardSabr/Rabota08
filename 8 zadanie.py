def a(N, dist, dengi):
    taxi_n = []
    total_cost = 0

    for i in range(N):
        min_cost = float('inf')
        min_taxi = -1
        for j in range(N):
            cost = dist[i] * dengi[j]
            if cost < min_cost:
                min_cost = cost
                min_taxi = j + 1
        taxi_n.append(min_taxi)
        total_cost += min_cost

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
taxi_n, total_cost = a(N, dist, dengi)
print("Номера такси для каждого сотрудника: ", taxi_n)
print("Суммарные затраты на такси: {} рублей".format(total_cost))