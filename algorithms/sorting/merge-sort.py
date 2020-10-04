def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        l_array = arr[:mid]
        r_array = arr[mid:]

        mergeSort(l_array)
        mergeSort(r_array)
    
        i = 0
        j = 0
        k = 0

        while i < len(l_array) and j < len(r_array):
            if l_array[i] < r_array[j]:
                arr[k] = l_array[i]
                i = i+1
            else:
                arr[k] = r_array[j]
                j = j+1
            k = k+1
        
        while i < len(l_array):
            arr[k] = l_array[i]
            k = k+1
            i = i+1
        
        while j < len(r_array):
            arr[k] = r_array[j]
            k = k+1
            j = j+1

def main(arr):
    mergeSort(arr)
    return arr
    
print(main([7,4,3,1,3,9,67]))