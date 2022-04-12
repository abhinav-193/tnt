import  numpy as np


# #1
b=np.array([int(x in range(5,10)) for x in range(30)])
print(b)

#2
Vector = np.arange(5,20)
print("Original vector:")
print(Vector)
res = Vector[::-1]
print(" new reversed array:",res)
#3
def printOrder(arr,n) :
    # sorting the array
    arr.sort()
    # printing first half in ascending order
    i = 0
    print('printing first half in ascending order')
    while (i< n/ 2 ) :
        print(arr[i])
        i = i + 1
    # printing second half in descending order
    j = n - 1
    print('printing second half in descending order')
    while j >= n / 2 :
        print(arr[j])
        j = j - 1

# Driver code
arr = np.random.randint(0,100,20)
n = len(arr)

printOrder(arr, n)
#4
arr = np.random.randint(0,100,(6,4))
print(arr.argmax())
print(arr.argmin())
#5
arr3 = np.ones((5,5))
print("Original array:")
print(arr3)
print("1 on the border & 0 inside ")
arr3[1:-1,1:-1] = 0
print(arr3)
#6
diag = np.diag(1+np.arange(4) ,-1) + np.diag(1+np.arange(4), 1)
print(diag)
#7
arra1 = np.random.randint(0,5,(10,10))
print("Original arrays:")
print(arra1)
n = 3
i = 1 + (arra1.shape[0]-3)
j = 1 + (arra1.shape[1]-3)
result = np.lib.stride_tricks.as_strided(arra1, shape=(i, j, n, n), strides = arra1.strides + arra1.strides)
print("Contiguous 3x3 blocks:")
print(result)