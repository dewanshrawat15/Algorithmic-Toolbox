# Uses python3

def binary_search(a, x):
    left, right = 0, len(a)
    while left < right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        else:
            if a[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    a = [int(x) for x in input().split()]
    k = [int(x) for x in input().split()]
    arr = a[1:]
    searchElems = k[1:]
    outputs = []
    for i in searchElems:
        outputs.append(binary_search(arr, i))
    for output in outputs:
        print(output, end=' ')
