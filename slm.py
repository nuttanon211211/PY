import sys
import numpy
day ,com = [int(e) for e in sys.stdin.readline().split()]
comlist = [int(e) for e in sys.stdin.readline().split()]
comlist = numpy.array(comlist)
time = [int(e) for e in sys.stdin.readline().split()]
time = numpy.array(time)
c = numpy.array(com+1,dtype =int)
c[0] = 0
c[1:] = numpy.sum(time)
print(c)
for i in range(day):
    pa,pb = [int(e) for e in sys.stdin.readlinr().split()]
