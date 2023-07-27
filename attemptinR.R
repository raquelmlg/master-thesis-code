calculate_distance_to_colony <- function(x, y, colony) {
  return (sqrt((colony$center_x - x) ^ 2 + (colony$center_y - y) ^ 2))
}

my_method <- function(colonies, l, grid_step = 0.1) {
  area <- 0
  for (i in seq(0, l, grid_step)) {
    for (j in seq(0, l, grid_step)) {
      for (colony in colonies) {
        if (calculate_distance_to_colony(i, j, colony) <= colony$radius) {
          area <- area + grid_step ^ 2
          break
        }
      }
    }
  }
  return (area)
}

montecarlo_method <- function(colonies, l, num_samples = 100000) {
  covered_points <- 0
  for (sample in 1:num_samples) {
    x <- runif(1, 0, l)
    y <- runif(1, 0, l)
    for (colony in colonies) {
      if (calculate_distance_to_colony(x, y, colony) <= colony$radius) {
        covered_points <- covered_points + 1
        break
      }
    }
  }
  return ((covered_points / num_samples) * l ^ 2)
}

colonies <- list(
  list(center_x = 10, center_y = 10, radius = 10)
)

l <- 20
real_area <- pi * 10 ^ 2

time_1 <- Sys.time()
accuracy <- 0
for (i in 1:100) {
  accuracy <- accuracy + abs(my_method(colonies, l, 0.1) - real_area)
}

time_2 <- Sys.time()
print(time_2 - time_1)
print(accuracy / 100)

# check also accuracy
time_1 <- Sys.time()
accuracy <- 0
for (i in 1:100) {
  accuracy <- accuracy + abs(montecarlo_method(colonies, l, 5000) - real_area)
}
time_2 <- Sys.time()
print(time_2 - time_1)
print(accuracy / 100)

