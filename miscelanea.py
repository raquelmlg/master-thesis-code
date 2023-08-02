# colony = {'center_x': 10, 'center_y':10, 'radius':10}
# print(10**2*math.pi)
# time1 = datetime.now()
# print(calculate_total_covered_area2([colony], 20))
# time2 = datetime.now()
#
# print(time2-time1)
#
# time1 = datetime.now()
# print(calculate_total_covered_area([colony], l=20))
# time2 = datetime.now()
# print(time2-time1)

# MONTE CARLO APPROACH -> SLOWER
# def calculate_total_covered_area(colonies, l, num_samples=100000):
#     covered_points = 0
#     for _ in range(num_samples):
#         x = np.random.uniform(0, l)
#         y = np.random.uniform(0, l)
#         for colony in colonies:
#             if calculate_distance_to_colony(x, y, colony) <= colony['radius']:
#                 covered_points += 1
#                 break
#     return (covered_points / num_samples) * l ** 2


""" NOT USEFUL ANYMORE """


# These functions make no real sense cause the intersection could be of three or more colonies.


## TODO: write mathematically
def calculate_intersection_area(colony1, colony2):
    distance = calculate_distance_between_colonies(colony1, colony2)
    if distance >= colony1['radius'] + colony2['radius']:
        return 0
    elif distance <= abs(colony1['radius'] - colony2['radius']):
        return math.pi * min(colony1['radius'], colony2['radius']) ** 2
    else:
        radius1_sq = colony1['radius'] ** 2
        radius2_sq = colony2['radius'] ** 2
        d = distance
        a = (radius1_sq - radius2_sq + d ** 2) / (2 * d)
        h = math.sqrt(radius1_sq - a ** 2)
        theta1 = math.acos(a / colony1['radius'])
        theta2 = math.acos((d - a) / colony2['radius'])
        intersection_area = (theta1 * radius1_sq - h * a) + (theta2 * radius2_sq - h * (d - a))
        return intersection_area


# makes no real sense cause the intersection could be of three or more colonies.
def calculate_bacterial_density(colonies, l):
    total_concentration = calculate_bacterial_concentration(colonies)
    intersection_area = 0
    for i in range(len(colonies)):
        for j in range(i + 1, len(colonies)):
            intersection_area += calculate_intersection_area(colonies[i], colonies[j])

    density = total_concentration / (l ** 2 + intersection_area)
    return density


def is_colony_inside_square(colony, l):
    # Check if the circle's center is within the boundaries of the square
    radius = colony['radius']
    if (colony['center_x'] - radius >= 0 and colony['center_x'] + radius <= l and
            colony['center_y'] - radius >= 0 and colony['center_y'] + radius <= l):
        return True
    return False

## TODO: IDEA : store the indexes of the points that are already covered by some colony.
## Their state is notgoing to change (at least without the antibiotics) so we don´t need to iterate through them over and over


# second method
def calculate_total_covered_area2(colonies, l, grid_size=5, covered_points = None):
    step_area = 1/grid_size**2
    grid_x = np.arange(1, l*grid_size +1)
    grid_y = np.arange(1, l*grid_size +1)

    if covered_points is None:
        covered_points = set()

    all_points = set((x,y) for x in grid_x for y in grid_y)
    free_points = all_points-covered_points

    for i,j in free_points:
            for colony in colonies:
                squared_distance = calculate_squared_distance_to_colony(i/grid_size, j/grid_size, colony)
                if squared_distance <= colony['radius']**2:
                  #  print(i/grid_size, j/grid_size, squared_distance)
                    covered_points.add((i,j))
                    break # the grid point is already covered by at least one colony, so we can move on to the next grid point.
  #  print(len(covered_points))
  #  print(step_area)
  #  print(len(covered_points)*step_area)
    return len(covered_points)*step_area, covered_points

def calculate_total_covered_area3(colonies, l, grid_size=5, covered_points=None):
    step_area = 1 / (grid_size)**2
    grid_x = np.arange(1, int(l*grid_size) + 1)
    grid_y = np.arange(1, int(l*grid_size) + 1)

    if covered_points is None:
        covered_points = set()

    all_points = set((x, y) for x in grid_x for y in grid_y)
    free_points = all_points - covered_points
    print(len(free_points))

    grid_points = np.meshgrid(grid_x / grid_size, grid_y / grid_size)
    grid_points = np.stack(grid_points, axis=-1).reshape(-1, 2)

    for i, j in grid_points:
        for colony in colonies:
            squared_distance = calculate_squared_distance_to_colony(i, j, colony)
            if squared_distance <= colony['radius']**2:
                covered_points.add((i * grid_size, j * grid_size))
                break  # the grid point is already covered by at least one colony, so we can move on to the next grid point.

    return len(covered_points) * step_area, covered_points