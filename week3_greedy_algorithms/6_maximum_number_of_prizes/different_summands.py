# Uses python3

def optimal_summands(n):
    summands = []
    #write your code here
    k = int((((1 + 8 * n)**(0.5)) - 1) / 2)
    for i in range(0, k):
        summands.append(i+1)
    reminder = n - ((k * (k + 1)) / 2)
    summands[len(summands) - 1] += int(reminder)
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
