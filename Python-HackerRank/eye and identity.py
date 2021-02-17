
import numpy

n, m = map(int, input().split())
print(numpy.eye(n, m, k=0), " ")

# numpy.set_printoptions(sign=' ')
# print(numpy.eye(*map(int, input().split())))