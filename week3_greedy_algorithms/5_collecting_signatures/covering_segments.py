# Uses python3
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments = sorted(segments, key=lambda segment: segment.end)
    current = segments[0].end
    points.append(current)
    for s in segments:
        if ((current < s.start) or (current > s.end)):
            current = s.end
            points.append(current)
    return points

if __name__ == '__main__':
    n = int(input())
    segments = []
    for i in range(n):
        start, end = map(int, input().split())
        s = Segment(start, end)
        segments.append(s)
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end = ' ')