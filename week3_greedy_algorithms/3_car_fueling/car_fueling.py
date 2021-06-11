# python3


def compute_min_refills(distance, tank, stops):
    # write your code here
    if distance <= tank:
        return 0
    i, numStops, curr_stop, dist_covered = 0, 0, 0, 0
    flag = False
    stops.append(distance)
    while dist_covered < distance:
        while i < len(stops) and stops[i] - curr_stop <= tank:
            i += 1
            flag = True
        if flag:
            if i == len(stops):
                break
            curr_stop = stops[i - 1]
            dist_covered = curr_stop
            numStops += 1
        else:
            return -1
        flag = False
    return numStops

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = [int(x) for x in input().split()]
    print(compute_min_refills(d, m, stops))
