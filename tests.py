import numpy as np
import math
from datetime import datetime


def calculate_distance_to_colony(x, y, colony):
    return math.sqrt((colony['center_x'] - x) ** 2 + (colony['center_y'] - y) ** 2)


def calculate_squared_distance_to_colony(x, y, colony):
    return (colony['center_x'] - x) ** 2 + (colony['center_y'] - y) ** 2


def my_method(colonies, l, grid_step=0.1):
    area = 0
    for i in np.arange(0, l, grid_step):
        for j in np.arange(0, l, grid_step):
            for colony in colonies:
                if calculate_distance_to_colony(i, j, colony) <= colony['radius']:
                    area += grid_step ** 2
                    break
    return area


def my_method2(colonies, l, grid_step=0.1):
    area = 0
    for i in np.arange(0, l, grid_step):
        for j in np.arange(0, l, grid_step):
            for colony in colonies:
                if calculate_squared_distance_to_colony(i, j, colony) <= colony['radius']**2:
                    area += grid_step ** 2
                    break
    return area


# def montecarlo_method(colonies, l, num_samples=100000):
#     covered_points = 0
#     for _ in range(num_samples):
#         x = np.random.uniform(0, l)
#         y = np.random.uniform(0, l)
#         for colony in colonies:
#             if calculate_distance_to_colony(x, y, colony) <= colony['radius']:
#                 covered_points += 1
#                 break
#     return (covered_points / num_samples) * l ** 2


colonies = [
    {'center_x': 10, 'center_y': 10, 'radius': 10}
]

l = 20
real_area = math.pi*10**2

times_method1 = []
accuracy1 = []
for j in range(0,100):
    time_1 = datetime.now()
    accuracy = 0
    for i in range(0, 100):
        accuracy += abs(my_method(colonies, l, 0.1)-real_area)

    time_2 = datetime.now()
    times_method1.append((time_2-time_1).microseconds)
    accuracy1.append(accuracy)

print(sum(times_method1)/len(times_method1))
print(sum(accuracy1)/len(accuracy1))


times_method2 = []
accuracy2 = []
for j in range(0,100):
    time_1 = datetime.now()
    accuracy = 0
    for i in range(0, 100):
        accuracy += abs(my_method2(colonies, l, 0.1)-real_area)

    time_2 = datetime.now()
    times_method2.append((time_2-time_1).microseconds)
    accuracy2.append(accuracy)

print(sum(times_method2)/len(times_method2))
print(sum(accuracy2)/len(accuracy2))


# # check also accuracy
# time_1=datetime.now()
# for i in range(0,100):
#     accuracy += abs(montecarlo_method(colonies, l, 5000)-real_area)
# time_2 = datetime.now()
# print(time_2-time_1)
# print(accuracy/100)