# Uses python3
from collections import namedtuple

Item = namedtuple("Item", "value weight")
def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    weight_value_pairs = sorted(
        [Item(v, w) for v, w in zip(values, weights)],
        key=lambda i: i.value / i.weight,
        reverse=True
    )
    space_left = int(capacity)
    for item in weight_value_pairs:
        if space_left - item.weight >= 0:
            value += item.value
            space_left -= item.weight
        else:
            value += (item.value / item.weight) * space_left
            space_left = 0
        if not space_left:
            break

    return value


if __name__ == "__main__":
    n, capacity = map(int, input().split())
    values, weights = [], []
    for i in range(n):
        v, w = map(int, input().split())
        values.append(v)
        weights.append(w)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
