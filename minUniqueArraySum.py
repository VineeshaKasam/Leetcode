
#Find the minimum unique array sum

def minSum(arr):
    mini = 1
    i = 0
    while i < len(arr):
        mini = arr[i] + 1
        if arr[i] in arr[:i]:
            while mini in arr[:i]:
                mini += 1
            arr[i] = mini
        i += 1
    print sum(arr)

minSum([1,2,3,2,7])
