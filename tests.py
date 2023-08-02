import numpy as np
#import math
#from datetime import datetime

#import common_functions as cf


# def calculate_distance_to_colony(x, y, colony):
#     return math.sqrt((colony['center_x'] - x) ** 2 + (colony['center_y'] - y) ** 2)
#
#
# def calculate_squared_distance_to_colony(x, y, colony):
#     return (colony['center_x'] - x) ** 2 + (colony['center_y'] - y) ** 2
#
#
# def my_method(colonies, l, grid_step=0.1):
#     area = 0
#     for i in np.arange(0, l, grid_step):
#         for j in np.arange(0, l, grid_step):
#             for colony in colonies:
#                 if calculate_distance_to_colony(i, j, colony) <= colony['radius']:
#                     area += grid_step ** 2
#                     break
#     return area


# def my_method2(colonies, l, grid_step=0.1):
#     area = 0
#     for i in np.arange(0, l, grid_step):
#         for j in np.arange(0, l, grid_step):
#             for colony in colonies:
#                 if calculate_squared_distance_to_colony(i, j, colony) <= colony['radius']**2:
#                     area += grid_step ** 2
#                     break
#     return area


# def montecarlo_method(colonies, l, num_samples=10000):
#     covered_points = 0
#     for _ in range(num_samples):
#         x = np.random.uniform(0, l)
#         y = np.random.uniform(0, l)
#         for colony in colonies:
#             if calculate_distance_to_colony(x, y, colony) <= colony['radius']:
#                 covered_points += 1
#                 break
#     return (covered_points / num_samples) * l ** 2
#
#
# colonies = [
#     {'center_x': 10, 'center_y': 10, 'radius': 10}
# ]
#
# l = 20
# real_area = math.pi*10**2
#
# times_method1 = []
# accuracy1 = []
#
# print("METHOD 1")
# time_1 = datetime.now()
# covered_points=set()
# for j in range(0,10):
#     area, covered_points= cf.calculate_total_covered_area2(colonies,l,10,covered_points)
#     accuracy1.append(abs(area-real_area))
# time_2 = datetime.now()
# print(time_2-time_1)
# print(sum(accuracy1)/len(accuracy1))
# print(accuracy1)
#
# print("METHOD 2")
# times_method2 = []
# accuracy2 = []
#
# time_1 = datetime.now()
# for j in range(0,10):
#     area = cf.calculate_total_covered_area(colonies, l,grid_step=0.1)
#     accuracy2.append(abs(real_area-area))
# time_2 = datetime.now()
# print(time_2-time_1)
# print(sum(accuracy2)/len(accuracy2))
# print (accuracy2)


# # check also accuracy
# time_1=datetime.now()
# for i in range(0,100):
#     accuracy += abs(montecarlo_method(colonies, l, 5000)-real_area)
# time_2 = datetime.now()
# print(time_2-time_1)
# print(accuracy/100)


# grid_x = np.arange(1, 1201)
# grid_y = np.arange(1, 1201)
# free_points = set((x, y) for x in grid_x for y in grid_y)
# total_points= len(free_points)
# all_colonies = [{'step': 0, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 1.4519814810320977, 'age': 1}]}, {'step': 1, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 2.1380178790807682, 'age': 2}]}, {'step': 2, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 3.1290268231301335, 'age': 3}]}, {'step': 3, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 4.539460599313097, 'age': 4}]}, {'step': 4, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 6.504942719457268, 'age': 5}]}, {'step': 5, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 9.1649010574303, 'age': 6}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 1, 'age': 0}]}, {'step': 6, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 12.625619439620044, 'age': 7}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 1.4519814810320977, 'age': 1}]}, {'step': 7, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 16.90440571032819, 'age': 8}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 2.1380178790807682, 'age': 2}]}, {'step': 8, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 21.873368961589257, 'age': 9}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 3.1290268231301335, 'age': 3}]}, {'step': 9, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 27.240822612787145, 'age': 10}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 4.539460599313097, 'age': 4}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 1, 'age': 0}]}, {'step': 10, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 32.60375693255841, 'age': 11}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 6.504942719457268, 'age': 5}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 1.4519814810320977, 'age': 1}]}, {'step': 11, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 37.560492430031516, 'age': 12}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 9.1649010574303, 'age': 6}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 2.1380178790807682, 'age': 2}]}, {'step': 12, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 41.82256641812916, 'age': 13}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 12.625619439620044, 'age': 7}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 3.1290268231301335, 'age': 3}]}, {'step': 13, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 45.26559088082431, 'age': 14}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 16.90440571032819, 'age': 8}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 4.539460599313097, 'age': 4}]}, {'step': 14, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 47.90941463748874, 'age': 15}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 21.873368961589257, 'age': 9}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 6.504942719457268, 'age': 5}]}, {'step': 15, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 49.86156104177676, 'age': 16}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 27.240822612787145, 'age': 10}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 9.1649010574303, 'age': 6}]}, {'step': 16, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 51.26168539189691, 'age': 17}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 32.60375693255841, 'age': 11}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 12.625619439620044, 'age': 7}]}, {'step': 17, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 52.24508120146084, 'age': 18}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 37.560492430031516, 'age': 12}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 16.90440571032819, 'age': 8}]}, {'step': 18, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 52.92566880501709, 'age': 19}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 41.82256641812916, 'age': 13}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 21.873368961589257, 'age': 9}]}, {'step': 19, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 53.39189445595736, 'age': 20}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 45.26559088082431, 'age': 14}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 27.240822612787145, 'age': 10}]}]
#
# time_1= datetime.now()
# step_area = 1 / 5 ** 2
# for step in all_colonies:
#     free_points = cf.calculate_free_points(step['colonies'],grid_size=5,free_points=free_points)
#     covered_area = step_area * (total_points - len(free_points))
#     print(covered_area)
# time_2=datetime.now()
# print(time_2-time_1)
#
# time_1 = datetime.now()
# step_area = 1 / 5 ** 2
# for step in all_colonies:
#     covered_area = cf.calculate_total_covered_area(step['colonies'], 240, grid_step=0.2, )
#     print(covered_area)
# time_2 = datetime.now()
# print(time_2 - time_1)


import cProfile
import common_functions as cf

grid_x = np.arange(1, 1201)
grid_y = np.arange(1, 1201)
free_points = set((x, y) for x in grid_x for y in grid_y)
total_points= len(free_points)
all_colonies = [{'step': 0, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 1.4519814810320977, 'age': 1}]}, {'step': 1, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 2.1380178790807682, 'age': 2}]}, {'step': 2, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 3.1290268231301335, 'age': 3}]}, {'step': 3, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 4.539460599313097, 'age': 4}]}, {'step': 4, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 6.504942719457268, 'age': 5}]}, {'step': 5, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 9.1649010574303, 'age': 6}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 1, 'age': 0}]}, {'step': 6, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 12.625619439620044, 'age': 7}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 1.4519814810320977, 'age': 1}]}, {'step': 7, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 16.90440571032819, 'age': 8}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 2.1380178790807682, 'age': 2}]}, {'step': 8, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 21.873368961589257, 'age': 9}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 3.1290268231301335, 'age': 3}]}, {'step': 9, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 27.240822612787145, 'age': 10}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 4.539460599313097, 'age': 4}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 1, 'age': 0}]}, {'step': 10, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 32.60375693255841, 'age': 11}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 6.504942719457268, 'age': 5}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 1.4519814810320977, 'age': 1}]}, {'step': 11, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 37.560492430031516, 'age': 12}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 9.1649010574303, 'age': 6}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 2.1380178790807682, 'age': 2}]}, {'step': 12, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 41.82256641812916, 'age': 13}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 12.625619439620044, 'age': 7}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 3.1290268231301335, 'age': 3}]}, {'step': 13, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 45.26559088082431, 'age': 14}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 16.90440571032819, 'age': 8}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 4.539460599313097, 'age': 4}]}, {'step': 14, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 47.90941463748874, 'age': 15}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 21.873368961589257, 'age': 9}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 6.504942719457268, 'age': 5}]}, {'step': 15, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 49.86156104177676, 'age': 16}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 27.240822612787145, 'age': 10}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 9.1649010574303, 'age': 6}]}, {'step': 16, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 51.26168539189691, 'age': 17}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 32.60375693255841, 'age': 11}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 12.625619439620044, 'age': 7}]}, {'step': 17, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 52.24508120146084, 'age': 18}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 37.560492430031516, 'age': 12}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 16.90440571032819, 'age': 8}]}, {'step': 18, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 52.92566880501709, 'age': 19}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 41.82256641812916, 'age': 13}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 21.873368961589257, 'age': 9}]}, {'step': 19, 'colonies': [{'center_x': 82.02719730538446, 'center_y': 80.46444066461814, 'radius': 53.39189445595736, 'age': 20}, {'center_x': 104.191105926221, 'center_y': 79.47630017581223, 'radius': 45.26559088082431, 'age': 14}, {'center_x': 100.5550727961542, 'center_y': 86.0508656139966, 'radius': 27.240822612787145, 'age': 10}]}]

# Profile the first method
cProfile.runctx("cf.calculate_total_covered_area(all_colonies[0]['colonies'], 240, grid_step=0.2)", None, locals(),sort='cumtime')

# Profile the second method
cProfile.runctx("cf.calculate_free_points(all_colonies[0]['colonies'],grid_size=5,free_points=free_points)", None, locals(), sort='cumtime')