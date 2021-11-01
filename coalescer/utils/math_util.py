import math


def get_average_value(values) -> float:
    return math.floor(sum(values) / len(values))


def get_min_value(values) -> float:
    return min(values)


def get_max_value(values) -> float:
    return max(values)
