import re

INPUT = "test_input"


def read_input():
    with open(INPUT, "r") as file:
        data = file.read().strip().splitlines()
    sensor_set = set()
    beacon_set = set()
    sensor_set_x_y = set()
    for line in data:
        numbers = re.split(r"\D", line)
        numbers = list(map(int, filter(lambda x: x != "", numbers)))
        s_x = numbers[0]
        s_y = numbers[1]
        b_x = numbers[2]
        b_y = numbers[3]
        d = abs(s_x - b_x) + abs(s_y - b_y)
        sensor_set.add((s_x, s_y, d))
        sensor_set_x_y.add((s_x, s_y))
        beacon_set.add((b_x, b_y))

    return sensor_set, sensor_set_x_y, beacon_set


def print_matrix(sensor_set, sensor_set_x_y, beacon_set):
    N = 20
    matrix = [["." for y in range(N)] for x in range(N)]

    for y in range(N):
        for x in range(N):
            if (x, y) in beacon_set:
                matrix[y][x] = "B"
            elif (x, y) in sensor_set_x_y:
                matrix[y][x] = "S"
            elif is_cannot_possibly_exist(x, y, sensor_set, beacon_set):
                matrix[y][x] = "#"
            else:
                pass

    for y in range(N):
        print("".join(matrix[y]))


def is_cannot_possibly_exist(x, y, sensor_set, beacon_set):
    if (x, y) in beacon_set:
        return False
    else:
        for (s_x, s_y, d) in sensor_set:
            d_x_y = abs(s_x - x) + abs(s_y - y)
            if d_x_y <= d:
                return True
        return False


def is_beacon(x, y, sensor_set, beacon_set):
    result = True
    if (x, y) in beacon_set:
        result = False
    else:
        for (s_x, s_y, d) in sensor_set:
            d_x_y = abs(s_x - x) + abs(s_y - y)
            if d_x_y <= d:
                result = result and False

    return result


def get_answer_1(sensor_set, beacon_set):
    if INPUT == "test_input":
        y = 10
        min_x = -100
        max_x = 100
    else:
        y = 2_000_000
        min_x = -int(1e7)
        max_x = int(1e7)

    counter = 0
    for x in range(min_x, max_x):
        y = y
        if is_cannot_possibly_exist(x, y, sensor_set, beacon_set):
            counter += 1

    return counter


def get_answer_2(sensor_set, beacon_set):
    if INPUT == "test_input":
        min_y = 0
        max_y = 20
        min_x = 0
        max_x = 20
    else:
        min_y = 0
        max_y = 4_000_000
        min_x = 0
        max_x = 4_000_000

    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            if is_beacon(x, y, sensor_set, beacon_set):
                result = x * 4_000_000 + y
                print(x, y)
                break

    return result


def main():
    sensor_set, sensor_set_x_y, beacon_set = read_input()

    print(get_answer_1(sensor_set, beacon_set))
    print_matrix(sensor_set, sensor_set_x_y, beacon_set)
    print(get_answer_2(sensor_set, beacon_set))


if __name__ == "__main__":
    main()
