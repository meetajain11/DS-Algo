# Time Complexity
# Best Case: O(n2)  Worst Case: O(n2)
# Can be used when we have limited space.

def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

print(selectionSort([6,3,2,8,4]))