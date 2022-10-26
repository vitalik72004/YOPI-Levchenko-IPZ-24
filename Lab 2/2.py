import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import solve

#==================================================
def task1(num):
    index = num * (lens + 1) - 1
    result = data[int(index)] + (index % int(index)) * (data[int(index) + 1] - data[int(index)])
    return result
#==================================================
def task2():
    sum = 0
    totalsum = 0
    totalSum = 0
    for i in range(lens):
        sum += data[i]

    for i in range(lens):
        totalsum += (data[i] - (sum / lens)) ** 2
        totalSum += abs(data[i] - (sum / lens))

    result = totalsum / lens
    Result = totalSum / lens
    print("Стандартне відхилення = ", str(round(math.sqrt(result))))
    print("Середнє відхилення = ", str(round(Result)))

    f.write("\nСтандартне відхилення = " + str(round(math.sqrt(result))))
    f.write("\nСереднє відхилення = " + str(round(Result)))
#==================================================
def task3():
    sum = 0
    result = []
    for i in data:
        sum += i
    a = np.array([[100, 1, ], [(sum / lens), 1, ]])
    #|100 = 100*a + b
    #|95 = 74.2*a + b
    x = solve(a, np.array([100, 95]))
    for i in range(lens):
        result.append(round(x[0] * data[i] + x[1]))
    print("Старі оцінки: " + str(data))
    f.write("\nСтарі оцінки: " + str(data))

    print("\ny = " + str(x[0]) + "*x + " + str(x[1]))
    f.write("\ny = " + str(x[0]) + "*x + " + str(x[1]))

    print("\nНові оцінки: " + str(result))
    f.write("\nНові оцінки: " + str(result))
#==================================================
def task4():
    print("Діаграма стовбур-листя")
    print("-----------------------")

    f.write("\nДіаграма стовбур-листя")
    f.write("\n-----------------------")

    i = min(data)

    while i <= max(data):
        mas = []
        for j in range(lens):
            if i < data[j] < i + 10:
                mas.append(data[j] % 10)
            elif data[j] == i:
                mas.append(0)
        if len(mas) != 0:
            print(str(i / 10) + " \t| " + str(mas))
            f.write("\n" + str(i / 10) + " \t| " + str(mas))
        i += 10
    print("Ключ = " + str(data[0]))
    f.write("\nКлюч = " + str(data[0]))
# ==================================================
def task5():
    plt.boxplot(data)
    plt.grid()
    plt.show()
#==================================================
f = open("answer.txt", "w")
data = []
for i in open("input_100.txt"):
    data.append(int(i.strip()))
data = np.delete(data, 0)

lens = len(data)
data = sorted(data)

print("Послідовність:", data)
f.write("Послідовність:" + str(data))

print("\nЗавдання 1:")

Q1 = task1(1 / 4)
Q3 = task1(3 / 4)
P90 = task1(0.9)

print("Q1 = ", Q1)
print("\nQ3 = ", Q3)
print("\nP90 = ", P90)

f.write("\nQ1 = ")
f.write(str(Q1))
f.write("\nQ3 = ")
f.write(str(Q3))
f.write("\nP90 = ")
f.write(str(P90))
print("\nЗавдання 2:")
task2()
print("\nЗавдання 3:")
task3()
print("\nЗавдання 4:")
task4()
print("\nЗавдання 5:")
task5()
f.close()
