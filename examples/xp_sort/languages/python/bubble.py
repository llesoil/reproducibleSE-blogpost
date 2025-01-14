
import sys
from load import load_input

# Python3 Optimized implementation
# of Bubble sort
  
# An optimized version of Bubble Sort
def bubbleSort(arr):
    n = len(arr)
   
    # Traverse through all array elements
    for i in range(n):
        swapped = False
  
        # Last i elements are already
        #  in place
        for j in range(0, n-i-1):
   
            # traverse the array from 0 to
            # n-i-1. Swap if the element 
            # found is greater than the
            # next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
  
        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            break

if __name__ == '__main__':
    arr = load_input(sys.argv[1])
    bubbleSort(arr)
  
# This code is contributed by Shreyanshi Arun
