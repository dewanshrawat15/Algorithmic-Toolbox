#Uses python3
import numpy

def lcs2(s1, s2, n1, n2):
    #write your code here
    Matrix = numpy.zeros((n1+1 , n2+1))
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                Matrix[i][j] = Matrix[i-1][j-1] + 1
            if s1[i-1] != s2[j-1]:
                Matrix[i][j] = max(Matrix[i][j-1], Matrix[i-1][j])
    return int(Matrix[n1][n2])

if __name__ == '__main__':
    n1 = int(input())
    s1 = [int(x) for x in input().split()]
    n2 = int(input())
    s2 = [int(x) for x in input().split()]
    LCS_length = lcs2(s1, s2, n1, n2)
    print(LCS_length)