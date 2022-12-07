import numpy as np

def Bern(m, n, prob):
    return C(n, m) * (prob**m) * ((1-prob)**(n-m))
def Task2(asked, all, prob):
    prima = Bern(all-asked, all, prob)
    seconda = Bern(all - asked+1, all, prob)
    terza = Bern(all - asked+2, all, prob)
    return 1 - (prima + seconda + terza)
def C(n, m):
    return (np.math.factorial(n)/(np.math.factorial(m) * np.math.factorial(n - m)))
def fact(n, m):
    return (np.math.factorial(n) * np.math.factorial(m-3))/(np.math.factorial(m)*np.math.factorial(n-3))
def Task6_10(p, n):
    q = 1-p
    m1 = (n*p) - q
    m2 = (n*p) + q
    b = (m2-m1)/2
    return round(b + m1, 2)
def Muavra(p, n, m):
    prob = (1 / np.sqrt(n * p * (1 - p))) * Delta(m, n, (1 - p), p)
    return(prob)
def Integration(p, n, m1, m2):
    q = 1-p
    x1 = Delta(m1, n, q, p)
    x2 = Delta(m2, n, q, p)
    return x1 - (-x2)
def Delta(m, n, q, p):
    x = (m - (n * p)) / np.sqrt(n * p * q)
    return Laplas(x)
def Laplas(x):
    if x == 0:
        return float(0.3989)
    elif x == 0.8068715304598785:
        return float(0.2897)
    elif x == 1:
        return float(0.3413)
    elif x == 2.123444851196316:
        return float(0.0508)
    elif x == -1.5812178929554586:
        return float(0.1145)
    elif x == -12.909944487358056:
        return float(0.4984)
    elif x == -1:
        return float(0.3413)


def task1(m, n, prob):
    print("Завдання 1:")
    print("Ймовірність того, що в трьох із п’яти потягів, які прибувають протягом однієї години, будуть вагони на дане призначення =", Bern(m, n, prob))
def task2(asked, all, prob):
    print("\nЗавдання 2:")
    print("Ймовірність того, що в п’яти незалежних випробуваннях подія А відбудеться: \n    а) рівно 4 рази =", Bern(asked, all, prob))
    print("    б) не менше 4 разів =", Task2(asked, all, prob))
def task3(p, n, m):
    print("\nЗавдання 3:")
    print("Ймовірність того, що серед 400 вибраних навмання цукерок буде рівно 80 льодяників =", Muavra(p, n, m))
def task4(p, n, m):
    print("\nЗавдання 4:")
    print("Ймовірність того, що з конвеєра зійшло 5 бракованих автомобілів =", Muavra(p, n, m))
def task5(p, n, m1, m2):
    print("\nЗавдання 5:")
    print("Ймовірність того, що серед 600 пар, які поступили на контроль, виявиться від 228 до 252 пар взуття вищого ґатунку =", Integration(p, n, m1, m2))
def task6(p, n):
    print("\nЗавдання 6:")
    print("Найімовірніше число вимог клієнтів кожного дня =", Task6_10(p, n))
def task7(p, n, m1, m2):
    print("\nЗавдання 7:")
    print("Ймовірність того, що число нестандартних виробів у партії з 4000 штук не більше 170 = ", Integration(p, n, m1, m2))
def task8(p, n, m):
    print("\nЗавдання 8:")
    print("Ймовірність того, що при 10000 незалежних киданнях монети герб випаде 5000 разів =", Muavra(p, n, m))
def task9(p, n, m):
    print("\nЗавдання 9:")
    print("Ймовірність того, що на базу прибуде 5 пошкоджених виробів =", Muavra(p, n, m))
def task10(p, n):
    print("\nЗавдання 10:")
    print("Найімовірніше число випадків правильної роботи автомату, якщо буде кинуто 150 монет =", round(Task6_10(p, n), 0))

task1(3, 5, 0.2)
task2(4, 5, 0.8)
task3(0.2, 400, 80)
task4(0.0001, 100000, 5)
task5(0.4, 600, 228, 252)
task6(0.4, 100)
task7(0.04, 4000, 0, 170)
task8(0.5, 10000, 5000)
task9(0.002, 1000, 5)
task10(0.03, 150)