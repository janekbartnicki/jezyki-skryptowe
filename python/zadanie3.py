import random


def monte_carlo_alg(amount_of_points):
    amount_of_points_inside_circle = 0

    for point in range(amount_of_points):
        x_coord = random.uniform(-1, 1)
        y_coord = random.uniform(-1, 1)

        if x_coord ** 2 + y_coord ** 2 <= 1:
            amount_of_points_inside_circle += 1

    return (4 * amount_of_points_inside_circle) / amount_of_points


print(monte_carlo_alg(100_000))
