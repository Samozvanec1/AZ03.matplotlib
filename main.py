import matplotlib.pyplot as plt

# x = [2,6,8,14,19]
# y = [6,4,10,15,16]
#
# plt.plot(x,y)
#
# plt.title("Линейный график")
# plt.xlabel("X-ось")
# plt.ylabel("Y-ось")
#
# plt.show()
# data = [5,6,7,4,6,5,7,4,8,4,9,10,11,8,9,7,10]
#
# plt.hist(data,bins=4) #bins - количество столбиков, по умолчанию 10, но можно указать любое другое.
# plt.xlabel("Часы сна")
# plt.ylabel("Количество людей")
# plt.title("Распределение часов сна")
# plt.show()
x = [1,3,4,5,4,6,9,11,14,14]
y = [1,2,3,4,5,6,7,8,9,10]

plt.scatter(x,y)

plt.title("Диаграмма рассеяния")
plt.xlabel("X-ось")
plt.ylabel("Y-ось")
plt.show()