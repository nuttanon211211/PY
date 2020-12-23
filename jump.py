import sys
"""def jump0(arr):
    count = 0
    for i in range(len(arr)):
        count+= arr[i]
    return count

def jump(arr,n):
        if(n>=3):
        #L = [0 for i in range(n)]
        #L[0] = arr[0]
        arr[1] = max(arr[1],arr[0]+arr[1])
        arr[2] = max(arr[2],arr[1]+arr[2],arr[0]+arr[2])
        for i in range (3,n):
            arr[i] = max(arr[i-1],arr[i-2],arr[i-3]) + arr[i]
        return arr[-1]
    elif(n==2):
        return max(0,arr[0])+max(0,arr[1])
    else:
        return max(arr[0],0)"""

n = int(input())
arr = [int(e) for e in sys.stdin.readline().strip().split()]
if(n>=3):
        #L = [0 for i in range(n)]
        #L[0] = arr[0]
    arr[1] = max(arr[1],arr[0]+arr[1])
    arr[2] = max(arr[2],arr[1]+arr[2],arr[0]+arr[2])
    for i in range (3,n):
        arr[i] = max(arr[i-1],arr[i-2],arr[i-3]) + arr[i]
    print( arr[-1])
elif(n==2):
    print( max(0,arr[0])+max(0,arr[1]))
else:
    print( max(arr[0],0))
